# Brief acceptance and evidence

Read this document when reviewing or completing a visual implementation. Keep depth proportional to scope: a small adjustment can report results in a few lines; a redesign or expressive hero needs traceable requirements and evidence.

## Three independent reviews

| Review | What must hold | Relevant evidence |
| --- | --- | --- |
| Functionality | The affected primary task, states, recovery, accessibility, and adaptation work. | Interaction walkthrough, test results, and relevant measurements. |
| Brief fidelity | Composition, visual language, typography, material, prominence, and concrete requests appear in the result. | Observed rendering in the target frame; comparison with agreed decisions or references. |
| Temporal impact | When motion is requested, its transformation, amplitude, sequence, rhythm, and resolution fulfill the requested role. | Full playback observed at normal speed, a recording or playback reference; key frames as supporting material. |

One passed review cannot compensate for another failed review. Do not use an average or a single “quality score.” If necessary evidence is missing, the outcome is pending. Temporal review may be inapplicable to a static request; it cannot be marked inapplicable when the brief asks for animation.

The pattern auditor checks source hygiene. A build, no overflow, a frame counter, a Pause button, or images with different pixels provide limited information. They do not establish whether the piece has the requested language or impact.

## Turn the brief into criteria

Before implementing, record each decisive requirement as **request → expected observable outcome → verification method**. During review, add the observation and status: pass, fail, or pending.

Include expressive requirements as well as buttons and functions. Distinguish preserving branding from resolving direction. When a brand includes a landing page and an editor, review each surface for its function; a stable working UI does not require a static promotional hero.

For a prominent hero, check first:

1. The selected material matches the brief and corrections; a rejected asset does not reappear in derivatives.
2. The media has the promised weight in the actual frame, including a narrow window.
3. The language emerges from combined composition, typography, material, and behavior, beyond the palette or claim.
4. There is a recognizable transformation and sequence with appropriate rhythm and resolution.
5. The primary action and reading remain usable throughout the piece.

If one of these foundations fails, revise that piece before propagating its treatment across the rest of the surface. This is work evaluation, not a mandatory additional human approval.

## Regression case

A visual-tool landing page calls for a strong hero with hacker character, a prominent animated example, access to the editor, and sample cards. The result has correct navigation, a dark background, thematic text, and a fixed portrait with minimal interference. The cards repeat the portrait and the auditor reaches zero findings.

Functionality may have improved and hygiene may be resolved while fidelity and temporal impact fail. Changing a few frames does not turn that result into the requested scene. Correction requires revisiting material, direction, and sequence; removing more patterns does not resolve the problem by itself.

This regression evaluates the procedure. It does not require a hacker aesthetic or a particular animation in other projects.

## Optional JSON report

For broad changes or repeatable validation, you can record the review and run:

```sh
python3 "$SKILL_DIR/scripts/check_acceptance.py" /path/to/review.json --root /path/to/project
```

The script uses standard Python 3, reads the report, and checks consistency and local evidence references. It does not watch a video, measure aesthetic quality, or convert declarations into creative approval. It can only validate the record of a review you actually performed.

Minimal format:

```json
{
  "schema_version": 1,
  "scope": "Hero and editor access",
  "motion_required": true,
  "hygiene": {"source_audit_unresolved": 0, "build": "pass"},
  "checks": [
    {
      "id": "B1",
      "gate": "brief",
      "request": "A prominent animated demonstration",
      "expected": "The scene is the hero's focal point in the initial frame",
      "observed": "Render review is still pending",
      "status": "pending",
      "evidence": []
    }
  ]
}
```

Add the functionality and motion checks required by the scope. Values for `gate` are `functional`, `brief`, and `motion`; values for `status` are `pass`, `fail`, `pending`, and `not_applicable`. The last is valid only for motion when movement was not requested, with a reason in `observed`.

Each evidence item has `kind`, `ref`, and `note`. Types are `interaction`, `test_run`, `measurement`, `source`, `screenshot`, `contact_sheet`, `video`, and `playback`. `ref` can be a path relative to `--root` or an HTTP(S) URL; local paths must exist. URLs are not automatically downloaded or verified. `note` explains what was observed or what the file establishes.

A functionality check declared passed needs interaction, test, measurement, or playback evidence. A visual check needs rendering: screenshot, video, or playback. A temporal check needs `video` or `playback`; a pixel measurement or contact sheet alone leaves the review pending. The existence of files or URLs does not establish that their contents are correct or were reviewed.

- **0 / `ready_for_review`:** the record declares all applicable requirements fulfilled with relevant evidence types. Visual judgment remains the responsibility of the actual review.
- **1 / `needs_revision`:** a review failed, is pending or missing, or lacks suitable evidence. Technical hygiene does not change this result.
- **2 / `error`:** the report or its paths are invalid; the check could not be completed.

Do not change statuses, invent playback observations, or mark motion optional to obtain exit code 0. Delivery must preserve failures and pending checks with their evidence and explain what remains unresolved.
