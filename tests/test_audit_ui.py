import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


BASE = Path(__file__).resolve().parent.parent
SCRIPT = BASE / 'skills/design-pro/scripts/audit_ui.py'


class AuditTrial(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def write(self, name, value):
        file = self.root / name
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(value, encoding='utf-8')
        return file

    def run_audit(self, *args):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(self.root), *args],
            capture_output=True, text=True, check=False,
        )
        self.assertFalse(result.stderr, result.stderr)
        return result.returncode, json.loads(result.stdout)

    def test_plain_ui_comments_and_read_only(self):
        file = self.write('page.html', '<!-- font-family: Inter; linear-gradient(red, blue) -->\n<h1>Archive</h1><button>Open</button>\n')
        before = hashlib.sha256(file.read_bytes()).digest()
        code, report = self.run_audit()
        self.assertEqual(code, 0)
        self.assertEqual(report['findings'], [])
        self.assertEqual(report['scope'], 'static_source_patterns_only')
        self.assertEqual(report['creative_verdict'], 'not_assessed')
        self.assertEqual(before, hashlib.sha256(file.read_bytes()).digest())

    def test_actual_css_and_motion_patterns(self):
        self.write('view.css', '/* gradient demo: linear-gradient(red,blue) */\n.hero {background: linear-gradient(red,blue);}\nbody { font-family: "Inter", sans-serif;}\n.dot { animation: pulse 2s infinite; }\n')
        code, report = self.run_audit()
        self.assertEqual(code, 1)
        self.assertEqual([(x['rule'], x['line']) for x in report['findings']], [('DP001', 2), ('DP002', 3), ('DP003', 4)])

    def test_web_font_unquoted_url_survives_comment_handling(self):
        self.write('fonts.css', '@import url(https://fonts.googleapis.com/css2?family=Inter:wght@400);\n')
        code, report = self.run_audit()
        self.assertEqual(code, 1)
        self.assertEqual(report['findings'][0]['rule'], 'DP002')

    def test_framework_import_svg_and_tailwind(self):
        self.write('view.tsx', 'import { Inter as UIType } from "next/font/google";\nexport const View = () => <div className="bg-radial animate-pulse">Archive</div>;\n')
        self.write('art.svg', '<svg><defs><linearGradient id="light"/></defs></svg>')
        code, report = self.run_audit()
        self.assertEqual(code, 1)
        self.assertEqual({x['rule'] for x in report['findings']}, {'DP001', 'DP002', 'DP003'})
        self.assertEqual(report['files_scanned'], 2)

    def test_similar_words_are_not_inter_font(self):
        self.write('view.tsx', 'const Interaction = "Inter";\nexport const title = "International";\nconst style = {fontFamily: "Arial"};\n')
        code, report = self.run_audit()
        self.assertEqual(code, 0)
        self.assertEqual(report['unresolved'], 0)

    def test_scope_avoids_unrelated_files_and_dependency_outputs(self):
        self.write('src/changed.css', 'body {color: #222;}')
        self.write('src/old.css', 'body {font-family: Inter;}')
        self.write('node_modules/pkg/view.css', 'body {background: linear-gradient(red,blue);}')
        self.write('dist/out.css', 'body {background: linear-gradient(red,blue);}')
        code, report = self.run_audit('--file', 'src/changed.css')
        self.assertEqual((code, report['files_scanned']), (0, 1))
        code, report = self.run_audit()
        self.assertEqual((code, report['files_scanned']), (1, 2))

    def test_explicit_exception_is_limited_to_its_line(self):
        self.write('hero.css', '.hero { background: linear-gradient(red,blue); }\n.card { background: linear-gradient(black,white); }\n')
        entries = [{'rule':'DP001','path':'hero.css','start_line':1,'end_line':1,'basis':'user-request','reason':'Only in the hero','user_request':'Use a gradient in the hero.'}]
        file = self.write('allow.json', json.dumps(entries))
        code, report = self.run_audit('--exceptions', str(file))
        self.assertEqual((code, report['unresolved'], report['exceptions_applied']), (1, 1, 1))
        self.assertEqual([x['allowed'] for x in report['findings']], [True, False])

    def test_functional_indicator_can_resolve_review(self):
        self.write('loading.css', '.spinner {animation: rotate 1s linear infinite;}\n')
        entries = [{'rule':'DP003','path':'loading.css','start_line':1,'end_line':1,'basis':'functional','reason':'Represents real loading; stops on completion and has a reduced-motion alternative.'}]
        file = self.write('allow.json', json.dumps(entries))
        code, report = self.run_audit('--exceptions', str(file))
        self.assertEqual((code, report['unresolved']), (0, 0))

    def test_functional_basis_does_not_allow_gradients(self):
        self.write('hero.css', '.hero {background: linear-gradient(red,blue);}\n')
        entries = [{'rule':'DP001','path':'hero.css','start_line':1,'end_line':1,'basis':'functional','reason':'Decoration'}]
        file = self.write('allow.json', json.dumps(entries))
        code, report = self.run_audit('--exceptions', str(file))
        self.assertEqual((code, report['status']), (2, 'error'))

    def test_missing_explicit_request_is_error(self):
        self.write('hero.css', '.hero {font-family: Inter;}\n')
        entries = [{'rule':'DP002','path':'hero.css','start_line':1,'end_line':1,'basis':'user-request','reason':'I want to allow it'}]
        file = self.write('allow.json', json.dumps(entries))
        code, report = self.run_audit('--exceptions', str(file))
        self.assertEqual((code, report['status']), (2, 'error'))

    def test_missing_scope_cannot_report_success(self):
        self.write('notes.md', 'No source files')
        code, report = self.run_audit()
        self.assertEqual((code, report['status']), (2, 'error'))
        code, report = self.run_audit('--file', '../outside.css')
        self.assertEqual((code, report['status']), (2, 'error'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
