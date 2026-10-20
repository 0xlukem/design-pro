#!/usr/bin/env python3
"""Check evidence-record coherence; never grade aesthetic or temporal quality."""

import argparse
import json
from pathlib import Path
import sys
from urllib.parse import urlsplit


GATES = ('functional', 'brief', 'motion')
STATUSES = {'pass', 'fail', 'pending', 'not_applicable'}
KINDS = {'interaction', 'test_run', 'measurement', 'source', 'screenshot', 'contact_sheet', 'video', 'playback'}
SUFFICIENT_KINDS = {
    'functional': {'interaction', 'test_run', 'measurement', 'video', 'playback'},
    'brief': {'screenshot', 'video', 'playback'},
    'motion': {'video', 'playback'},
}


def nonempty(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Campo de texto requerido: ' + field)
    return value.strip()


def evidence_exists(item, root):
    if not isinstance(item, dict) or item.get('kind') not in KINDS:
        raise ValueError('Evidencia con tipo inválido.')
    ref = nonempty(item.get('ref'), 'evidence.ref')
    nonempty(item.get('note'), 'evidence.note')
    url = urlsplit(ref)
    if url.scheme:
        if url.scheme not in {'http', 'https'} or not url.netloc:
            raise ValueError('Solo se aceptan referencias URL HTTP(S).')
        return True  # Existence and playback are declarations, not verified here.
    relative = Path(ref)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('La evidencia local debe ser relativa a root y sin ..')
    target = (root / relative).resolve()
    if not target.is_relative_to(root):
        raise ValueError('Evidencia fuera de root.')
    return target.is_file()


def evaluate(record, root):
    if not isinstance(record, dict) or type(record.get('schema_version')) is not int or record['schema_version'] != 1:
        raise ValueError('schema_version debe ser 1.')
    nonempty(record.get('scope'), 'scope')
    if type(record.get('motion_required')) is not bool:
        raise ValueError('motion_required debe ser booleano.')
    checks = record.get('checks')
    if not isinstance(checks, list):
        raise ValueError('checks debe ser una lista.')
    if not isinstance(record.get('hygiene', {}), dict):
        raise ValueError('hygiene debe ser un objeto informativo.')
    seen = set()
    results = []
    issues = []
    for check in checks:
        if not isinstance(check, dict):
            raise ValueError('Cada check debe ser un objeto.')
        check_id = nonempty(check.get('id'), 'id')
        if check_id in seen:
            raise ValueError('ID de check duplicado: ' + check_id)
        seen.add(check_id)
        gate, status = check.get('gate'), check.get('status')
        if gate not in GATES or status not in STATUSES:
            raise ValueError('Gate o status inválido en ' + check_id)
        for field in ('request', 'expected', 'observed'):
            nonempty(check.get(field), field)
        evidence = check.get('evidence', [])
        if not isinstance(evidence, list):
            raise ValueError('evidence debe ser una lista.')
        available = set()
        missing = False
        for item in evidence:
            if evidence_exists(item, root):
                available.add(item['kind'])
            else:
                missing = True
                issues.append(check_id + ': falta el archivo de evidencia ' + item['ref'])
        effective = status
        if status == 'not_applicable' and (gate != 'motion' or record['motion_required']):
            effective = 'pending'
            issues.append(check_id + ': no puede omitirse esta revisión requerida')
        if status == 'pass' and (missing or not available.intersection(SUFFICIENT_KINDS[gate])):
            effective = 'pending'
            issues.append(check_id + ': la evidencia no sostiene la revisión ' + gate)
        results.append({'id': check_id, 'gate': gate, 'declared_status': status, 'effective_status': effective})
    gates = {}
    for gate in GATES:
        states = [item['effective_status'] for item in results if item['gate'] == gate]
        if gate == 'motion' and not record['motion_required'] and (not states or all(s == 'not_applicable' for s in states)):
            gates[gate] = 'not_applicable'
        elif 'fail' in states:
            gates[gate] = 'fail'
        elif not states or any(s != 'pass' for s in states):
            gates[gate] = 'pending'
            if not states:
                issues.append('Falta la revisión ' + gate)
        else:
            gates[gate] = 'pass'
    ready = all(status in {'pass', 'not_applicable'} for status in gates.values())
    return {
        'status': 'ready_for_review' if ready else 'needs_revision',
        'gates': gates,
        'checks': results,
        'issues': issues,
        'hygiene_informational_only': record.get('hygiene', {}),
        'limitation': 'Valida un registro declarado y referencias de evidencia; no observa reproducción ni certifica fidelidad estética o impacto.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', help='Informe JSON de aceptación.')
    parser.add_argument('--root', help='Raíz de los archivos de evidencia; por defecto, carpeta del informe.')
    args = parser.parse_args()
    try:
        report = Path(args.report).resolve()
        root = Path(args.root).resolve() if args.root else report.parent
        if not root.is_dir():
            raise ValueError('root debe ser un directorio existente.')
        record = json.loads(report.read_text(encoding='utf-8'))
        result = evaluate(record, root)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result['status'] == 'ready_for_review' else 1
    except (OSError, ValueError, UnicodeError, TypeError) as error:
        print(json.dumps({'status': 'error', 'error': str(error)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    sys.exit(main())
