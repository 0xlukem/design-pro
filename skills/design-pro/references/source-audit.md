# Static pattern audit

The `scripts/audit_ui.py` script uses only Python 3 and the standard library. It reads code and returns JSON on stdout; it does not modify the project, install dependencies, or access the network.

## Run

Resolve `SKILL_DIR` to the folder from which you read this skill. Do not assume a personal path or a directory specific to one assistant.

```sh
python3 "$SKILL_DIR/scripts/audit_ui.py" "/path/to/project" --file src/hero.tsx --file src/styles.css
```

Repeat `--file` to limit review to affected code. Without that argument, the script scans interface files in the project and excludes common dependencies and build outputs; it may report existing issues outside the change. Do not expand the work scope to remove them automatically.

## Rules and results

| Rule | Detects | Treatment |
| --- | --- | --- |
| DP001 | CSS gradient functions, SVG gradients, and common Tailwind utilities | Review the restriction and any explicit exception. |
| DP002 | Common Inter declarations and imports, web fonts, and common utilities | Review the restriction and any explicit exception. |
| DP003 | Common infinite-repeat syntax and pulse, bounce, or spin utilities | Contextual review: it may be decorative activity or a functional indicator. |

The script preserves line numbers and skips common comment syntax. It is not a complete parser: computed names, escaped CSS, variables, raster assets, and other constructions may be missed. Example strings or content can produce false positives. Inspect each finding in context.

- Exit code **0**: no unresolved patterns within scope; this does **not** mean “design approved.”
- Exit code **1**: blocked patterns or contextual reviews remain unresolved.
- Exit code **2**: input, reading, or configuration error; the audit did not complete.

The JSON always declares `scope: "static_source_patterns_only"` and `creative_verdict: "not_assessed"`. Reducing many findings to zero closes only that pattern review. It does not justify declaring that the brief, identity, or animation has been achieved.

It does not semantically detect eyebrows, generic copy, filler cards, competing CTAs, hierarchy, contrast, cropping, behavior, or motion quality. These require inspecting the render and walking through the experience.

Keep its results as source hygiene and use the separate [acceptance](acceptance.md) reviews for completion. Do not average the auditor's count with a visual or temporal assessment or remove an expressly requested effect solely to reduce DP003: review and record the scope of the request.

## Scoped exceptions

When appropriate, pass `--exceptions /path/to/exceptions.json`. Each entry must name the rule, relative file, and line range. This list records decisions; it does not grant permission or establish that a request is authentic. Link it to the actual request in the conversation; do not invent an exception to obtain exit code 0.

Example format for a gradient expressly requested in a specific region:

```json
[
  {
    "rule": "DP001",
    "path": "src/hero.css",
    "start_line": 12,
    "end_line": 12,
    "basis": "user-request",
    "reason": "The user enabled the gradient only in this background.",
    "user_request": "I want a gradient in the hero background."
  }
]
```

For DP003, `basis: "functional"` records a real processing indicator with a `reason` explaining what it represents, when it ends, and how it adapts to reduced motion. It does not enable gradients or Inter.

For a real false positive in an example string or other syntax outside visual use, explain the finding in the delivery. Keep the result pending if the script cannot express it; do not invent a human request or functional purpose.

Recheck ranges after editing: lines may change. The report includes unused exceptions to identify stale configuration. Keep proportionate evidence in temporary work or the existing review system.
