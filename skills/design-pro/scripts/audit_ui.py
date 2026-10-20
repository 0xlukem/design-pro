#!/usr/bin/env python3
"""Read-only, dependency-free checks for a small subset of Design Pro rules."""

import argparse
import json
import os
from pathlib import Path
import re
import sys


EXTENSIONS = {
    '.html', '.htm', '.css', '.scss', '.sass', '.less', '.js', '.jsx',
    '.mjs', '.cjs', '.ts', '.tsx', '.vue', '.svelte', '.astro', '.svg',
}
EXCLUDED = {
    '.git', 'node_modules', 'dist', 'build', 'coverage', '.next', '.nuxt',
    '.output', '.turbo', '.venv', 'venv', '__pycache__', 'vendor',
}
# Preserve strings and line numbers; remove common source comments.
COMMENT_TOKENS = re.compile(
    r'''("(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|`(?:\\.|[^`\\])*`)|'''
    r'''(/\*[\s\S]*?\*/|<!--[\s\S]*?-->|(?<!:)//[^\r\n]*)'''
)
RULES = {
    'DP001': (
        'blocked', 'Gradient detected: review restriction and exception scope.',
        re.compile(
            r'\b(?:repeating-)?(?:linear|radial|conic)-gradient\s*\('
            r'|<\s*(?:linearGradient|radialGradient)\b'
            r'|(?<![\w-])bg-(?:gradient-to-[\w-]+|linear(?:-[\w\[\]%-]+)?'
            r'|radial(?:-[\w\[\]%-]+)?|conic(?:-[\w\[\]%-]+)?)(?![\w-])',
            re.IGNORECASE,
        ),
    ),
    'DP002': (
        'blocked', 'Inter usage or loading detected.',
        re.compile(
            r'\b(?:font-family|fontFamily)\s*[:=][^;\n}]*?\bInter\b'
            r'|\bimport\s*\{[^}]*\bInter\b[^}]*\}\s*from\s*[\'"]next/font/(?:google|local)[\'"]'
            r'|\bInter\s*\('
            r'|@fontsource/(?:variable-)?inter(?:/|[\'"])'
            r'|family=Inter(?=[:&+\'"\s]|%3[Aa]|$)'
            r'|(?<![\w-])font-inter(?![\w-])'
            r'|font-\[[^\]\n]*\bInter\b[^\]\n]*\]',
            re.IGNORECASE,
        ),
    ),
    'DP003': (
        'review', 'Loop detected: check purpose, completion, and accessibility.',
        re.compile(
            r'\banimation(?:-iteration-count)?\s*:[^;\n}]*\binfinite\b'
            r'|\brepeat\s*:\s*(?:Infinity\b|-1\b)'
            r'|\brepeatCount\s*=\s*[\'"]indefinite[\'"]'
            r'|(?<![\w-])animate-(?:pulse|bounce|spin)(?![\w-])',
            re.IGNORECASE,
        ),
    ),
}


def remove_comments(source):
    def replace(match):
        if match.group(1) is not None:
            return match.group(0)
        return ''.join('\n' if char == '\n' else ' ' for char in match.group(0))
    return COMMENT_TOKENS.sub(replace, source)


def relative_source(root, relative):
    path = Path(relative)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError('Paths must be project-relative and contain no ..')
    candidate = root / path
    if candidate.is_symlink():
        raise ValueError('Symlinks are not audited: ' + str(relative))
    resolved = candidate.resolve()
    try:
        resolved.relative_to(root)
    except ValueError as error:
        raise ValueError('Path outside the project: ' + str(relative)) from error
    if not resolved.is_file() or resolved.suffix.lower() not in EXTENSIONS:
        raise ValueError('Not a supported source file: ' + str(relative))
    if any(part in EXCLUDED for part in resolved.relative_to(root).parts):
        raise ValueError('File inside an excluded directory: ' + str(relative))
    return resolved


def load_exceptions(path, root):
    if path is None:
        return []
    entries = json.loads(Path(path).read_text(encoding='utf-8'))
    if not isinstance(entries, list):
        raise ValueError('The exceptions file must contain a JSON list.')
    allowed_keys = {
        'rule', 'path', 'start_line', 'end_line', 'basis', 'reason', 'user_request',
    }
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) - allowed_keys:
            raise ValueError('Exception has unknown fields or an invalid format.')
        if entry.get('rule') not in RULES or entry.get('basis') not in {'user-request', 'functional'}:
            raise ValueError('Invalid exception rule or basis.')
        for key in ('path', 'reason'):
            if not isinstance(entry.get(key), str) or not entry[key].strip():
                raise ValueError('Each exception requires ' + key)
        for key in ('start_line', 'end_line'):
            if type(entry.get(key)) is not int or entry[key] < 1:
                raise ValueError('Each exception requires positive line numbers.')
        if entry['end_line'] < entry['start_line']:
            raise ValueError('Reversed line range.')
        if entry['basis'] == 'functional' and entry['rule'] != 'DP003':
            raise ValueError('The functional basis only resolves DP003 findings.')
        if entry['basis'] == 'user-request':
            if not isinstance(entry.get('user_request'), str) or not entry['user_request'].strip():
                raise ValueError('An explicit exception requires the user request.')
        file = relative_source(root, entry['path'])
        if entry['end_line'] > len(file.read_text(encoding='utf-8').splitlines()):
            raise ValueError('Exception outside the file line range.')
        entry['path'] = file.relative_to(root).as_posix()
    return entries


def audit(root, files, exceptions):
    findings = []
    applied = set()
    for file in files:
        source = remove_comments(file.read_text(encoding='utf-8'))
        relative = file.relative_to(root).as_posix()
        seen = set()
        for rule, (severity, message, pattern) in RULES.items():
            for match in pattern.finditer(source):
                line = source.count('\n', 0, match.start()) + 1
                if (rule, line) in seen:
                    continue
                seen.add((rule, line))
                item = {
                    'rule': rule, 'severity': severity, 'path': relative,
                    'line': line, 'message': message, 'allowed': False,
                }
                for index, entry in enumerate(exceptions):
                    if (entry['rule'] == rule and entry['path'] == relative
                            and entry['start_line'] <= line <= entry['end_line']):
                        item['allowed'] = True
                        item['exception_basis'] = entry['basis']
                        applied.add(index)
                        break
                findings.append(item)
    unresolved = sum(not item['allowed'] for item in findings)
    return {
        'status': 'needs_review' if unresolved else 'no_unresolved_patterns',
        'scope': 'static_source_patterns_only',
        'creative_verdict': 'not_assessed',
        'files_scanned': len(files),
        'unresolved': unresolved,
        'exceptions_applied': len(applied),
        'unused_exceptions': [i for i in range(len(exceptions)) if i not in applied],
        'findings': sorted(findings, key=lambda item: (item['path'], item['line'], item['rule'])),
        'limitation': 'Static pattern review; does not certify aesthetics, UX, or accessibility.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', help='Project directory to review.')
    parser.add_argument('--file', action='append', default=[], help='Relative file; repeat to limit scope.')
    parser.add_argument('--exceptions', help='JSON list of justified exceptions by file and line range.')
    args = parser.parse_args()
    try:
        root = Path(args.root).resolve()
        if not root.is_dir():
            raise ValueError('The project must be an existing directory.')
        if args.file:
            files = sorted({relative_source(root, path) for path in args.file})
        else:
            files = []
            for directory, dirs, names in os.walk(root, followlinks=False):
                dirs[:] = sorted(d for d in dirs if d not in EXCLUDED and not (Path(directory) / d).is_symlink())
                for name in sorted(names):
                    file = Path(directory) / name
                    if not file.is_symlink() and file.suffix.lower() in EXTENSIONS:
                        files.append(file)
        if not files:
            raise ValueError('No supported source files within scope.')
        exceptions = load_exceptions(args.exceptions, root)
        report = audit(root, files, exceptions)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1 if report['unresolved'] else 0
    except (OSError, ValueError, UnicodeError, TypeError) as error:
        print(json.dumps({'status': 'error', 'error': str(error)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    sys.exit(main())
