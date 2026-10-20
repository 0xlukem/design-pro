import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


BASE = Path(__file__).resolve().parent.parent
SCRIPT = BASE / 'skills/design-pro/scripts/check_acceptance.py'


class AcceptanceTrial(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def check(self, gate, kind, status='pass'):
        return {
            'id': gate, 'gate': gate, 'request': 'Requisito del caso',
            'expected': 'Resultado observable', 'observed': 'Resultado declarado en el caso de prueba',
            'status': status,
            'evidence': [{'kind': kind, 'ref': 'http://localhost:5173/#' + gate, 'note': 'Evidencia declarada para probar el registro, no una ejecución real del producto'}],
        }

    def record(self):
        return {
            'schema_version': 1, 'scope': 'Hero y navegación', 'motion_required': True,
            'checks': [self.check('functional', 'interaction'), self.check('brief', 'screenshot'), self.check('motion', 'playback')],
        }

    def run_review(self, record):
        report = self.root / 'review.json'
        report.write_text(json.dumps(record), encoding='utf-8')
        result = subprocess.run([sys.executable, str(SCRIPT), str(report)], capture_output=True, text=True, check=False)
        self.assertFalse(result.stderr, result.stderr)
        return result.returncode, json.loads(result.stdout)

    def test_real_failure_shape_cannot_be_offset_by_clean_audit(self):
        record = json.loads((BASE / 'tests/fixtures/expressive_brief_regression.json').read_text())
        code, report = self.run_review(record)
        self.assertEqual(code, 1)
        self.assertEqual(report['gates'], {'functional': 'pass', 'brief': 'fail', 'motion': 'fail'})
        self.assertEqual(report['hygiene_informational_only']['source_audit_unresolved'], 0)

    def test_pixel_difference_does_not_prove_temporal_impact(self):
        record = self.record()
        record['checks'][2]['evidence'][0]['kind'] = 'measurement'
        code, report = self.run_review(record)
        self.assertEqual((code, report['gates']['motion']), (1, 'pending'))

    def test_source_inspection_does_not_prove_visual_fidelity(self):
        record = self.record()
        record['checks'][1]['evidence'][0]['kind'] = 'source'
        code, report = self.run_review(record)
        self.assertEqual((code, report['gates']['brief']), (1, 'pending'))

    def test_contact_sheet_is_not_real_time_playback(self):
        record = self.record()
        record['checks'][2]['evidence'][0]['kind'] = 'contact_sheet'
        code, report = self.run_review(record)
        self.assertEqual((code, report['gates']['motion']), (1, 'pending'))

    def test_requested_motion_cannot_be_marked_not_applicable(self):
        record = self.record()
        record['checks'][2]['status'] = 'not_applicable'
        code, report = self.run_review(record)
        self.assertEqual((code, report['gates']['motion']), (1, 'pending'))

    def test_technical_hygiene_does_not_fill_missing_reviews(self):
        record = self.record()
        record['checks'] = []
        record['hygiene'] = {'source_audit_unresolved': 0, 'build': 'pass'}
        code, report = self.run_review(record)
        self.assertEqual(code, 1)
        self.assertEqual(set(report['gates'].values()), {'pending'})

    def test_all_independent_declared_reviews_are_needed(self):
        code, report = self.run_review(self.record())
        self.assertEqual((code, report['status']), (0, 'ready_for_review'))
        self.assertIn('registro declarado', report['limitation'])

    def test_static_brief_can_skip_motion(self):
        record = self.record()
        record['motion_required'] = False
        record['checks'] = record['checks'][:2]
        code, report = self.run_review(record)
        self.assertEqual((code, report['gates']['motion']), (0, 'not_applicable'))

    def test_missing_local_evidence_keeps_review_pending(self):
        record = self.record()
        record['checks'][1]['evidence'][0]['ref'] = 'missing.png'
        code, report = self.run_review(record)
        self.assertEqual((code, report['gates']['brief']), (1, 'pending'))

    def test_report_cannot_read_evidence_outside_its_root(self):
        record = self.record()
        record['checks'][1]['evidence'][0]['ref'] = '../outside.png'
        code, report = self.run_review(record)
        self.assertEqual((code, report['status']), (2, 'error'))

    def test_ids_cannot_hide_a_second_requirement(self):
        record = self.record()
        record['checks'].append(copy.deepcopy(record['checks'][0]))
        code, report = self.run_review(record)
        self.assertEqual((code, report['status']), (2, 'error'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
