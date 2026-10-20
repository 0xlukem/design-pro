# Design Pro

An agent skill for designing, building, and reviewing web interfaces with a distinct visual direction, clear UX, purposeful motion, and verified mobile behavior.

Design Pro turns a brief into observable design decisions. It combines creative discovery, visual references, adjustable direction controls, and separate acceptance checks for functionality, brief fidelity, and motion. Version 1.3 includes **20 visual style families** and a **36-resource decision catalog** organized around seven design problems.

The same skill works with **Claude Code and Codex**. It supports existing stacks and uses the tools available in the current environment. The instructions, reference guides, and examples are written in English; the agent responds in the user's language.

## Install

With Node.js and npm available, run this from the project where you want to use the skill:

```sh
npx skills add 0xlukem/design-pro --skill design-pro -a claude-code -a codex
```

For a user-wide installation in both agents, add `-g`:

```sh
npx skills add 0xlukem/design-pro --skill design-pro -a claude-code -a codex -g
```

The command uses the [Agent Skills CLI](https://github.com/vercel-labs/skills). You can also copy the complete [`skills/design-pro`](skills/design-pro) folder into `.claude/skills/` for Claude Code or `.agents/skills/` for Codex. Include its references, scripts, metadata, and license.

## Use

Invoke `/design-pro` in Claude Code or mention `$design-pro` in Codex.

```text
Use design-pro to create a personal reading app.
I haven't chosen a visual direction yet. Start with discovery.
```

```text
Use design-pro to explore eight visual directions for a photography archive.
Show them in one 4-by-2 image, labeled A–H, before we choose a direction.
```

```text
Use design-pro to audit this screen, read only.
Review hierarchy, interaction states, keyboard access, and actual breakpoints.
```

```text
Use design-pro to adjust only the mobile heading.
Preserve the approved composition and spacing.
```

## Workflow

1. **Identify the scope.** Choose the appropriate path for a new interface, open redesign, selected direction, focused adjustment, or read-only audit.
2. **Discover the brief.** Open-ended projects use at least 15 substantive questions in rounds of 3–5. Follow-up questions respond to the answers; focused fixes preserve decisions already made.
3. **Define observable direction.** Translate the brief into composition, typography, imagery, material, hierarchy, and behavior. Record what the result must show and how it will be checked. Shared branding can support different profiles for a promotional landing page and a working editor.
4. **Explore references.** When references are requested at the start, produce an early eight-direction board once the product, audience, and goal are clear. A detailed desktop and mobile reference can follow the selected direction.
5. **Build in context.** Use the project's stack, tokens, components, and real content. When an animated scene defines the request, build and observe that scene before extending its direction to other sections.
6. **Verify each outcome.** Evaluate functionality, brief fidelity, and temporal impact separately. Report evidence, failures, and unresolved checks without averaging the results.

Users can explicitly skip discovery or delegate design decisions. Image generation uses an available image tool; the skill does not bundle an image service or API key. If generation is unavailable, the agent explains the limitation and offers an alternative.

## Visual styles and references

The [style library](skills/design-pro/references/style-library.md) covers 20 families: editorial typography, Swiss/international, functional minimalism, warm modernism, industrial, technical utility, restrained brutalism, neobrutalism, cultural archives, photography, playful geometry, retro digital, retrofuturism, cyberpunk/hacker, organic/ethereal, handcrafted/tactile, collage, Art Deco, spatial/3D, and controlled maximalism.

These families provide a vocabulary for exploration. Each direction still needs specific composition, typography, material, and behavior. The A–H board selects eight relevant proposals for the brief; its options can come from this library or other suitable references.

The [visual decision catalog](skills/design-pro/references/creative-library.md) contains 36 resources grouped by the problem they address:

- Communicating a proposition.
- Organizing information and density.
- Comparing options and establishing trust.
- Exploring collections.
- Operating, editing, and recovering.
- Telling a story through motion.
- Establishing character through typography and material.

Each resource describes the relationship that should be visible and what to check on mobile. Styles, composition resources, and techniques such as masonry, modular grids, glass, or scroll narratives remain distinct choices. A style name does not automatically enable a blocked effect.

Reference exploration can use inspected real sources or generated proposals. Real references retain source links; generated proposals are identified as generated. The [direction guide](skills/design-pro/references/visual-direction.md) covers the A–H board, reference analysis, and detailed desktop/mobile compositions.

## Direction controls and type weights

| Control | Starting value | What it changes |
| --- | --- | --- |
| `DESIGN_VARIANCE` | **8** | Composition, proportions, asymmetry, and visual rhythm. |
| `MOTION_INTENSITY` | **6** | Presence of motion, spatial continuity, and expressive sequencing. |
| `VISUAL_DENSITY` | **4** | How much information shares the space and how it is grouped. |

Discovery and selected references adjust these values. They are design controls, not internal model weights or exact rendering parameters. Record effective profiles for different surfaces when their tasks require different behavior. Explicit visual restrictions apply at every setting.

The [direction guide](skills/design-pro/references/visual-direction.md) also retains practical type-scale and weight references: body text around **400**, labels and actions around **500–600**, and headings around **500–700**, adjusted to the actual typeface and content. The [motion guide](skills/design-pro/references/motion.md) covers timing, settling behavior, interruption, and full-sequence observation.

## Default visual restrictions

Design Pro blocks common generated-interface shortcuts by default:

- Decorative gradients, mesh backgrounds, glows, and halos.
- Decorative eyebrows and badges above headings.
- Inter and automatic substitution with the same font across unrelated projects.
- A single heading word decorated with an underline, another color, italics, or a different font.
- Competing promotional CTAs with equal visual weight.
- Filler bento grids, generic three-card rows, and unnecessary containers.
- Interchangeable marketing copy and invented social proof.
- Repeated fade-ups, ornamental typewriters, floating cards, magnetic buttons, scroll hijacking, and decorative loops.

An explicit request can enable a resource within the named scope. Functional labels, visible keyboard focus, recognizable links, and necessary application actions remain usable. An expressly requested animated hero receives a real expressive sequence; each independent restriction still applies.

[`SKILL.md`](skills/design-pro/SKILL.md) is the source of truth for restrictions and exceptions.

## UX, mobile, and acceptance

The [UX guide](skills/design-pro/references/ux.md) covers tasks, navigation, forms, relevant states, accessibility, and recovery. The [mobile guide](skills/design-pro/references/mobile-qa.md) requires a composed mobile layout, representative widths, intermediate ranges, and checks at **B−1 / B / B+1** for relevant breakpoints.

Verification distinguishes browser rendering, emulation, and actual device use. It includes content and interaction checks; a narrow screenshot or the absence of horizontal overflow establishes only a limited part of the result.

The [acceptance guide](skills/design-pro/references/acceptance.md) keeps three outcomes independent:

| Review | Evidence it needs |
| --- | --- |
| Functionality | Relevant interactions, states, results, and recovery. |
| Brief fidelity | The requested composition, material, hierarchy, and visual identity in the actual render. |
| Motion, when required | Observed normal-speed playback of a complete sequence, including transformation, rhythm, amplitude, and resolution. |

A successful build, clean static audit, changing pixels, or working Pause control cannot compensate for a failed visual or motion requirement. Unobserved outcomes remain pending.

## Review tools

Both scripts use Python 3 and the standard library. They read inputs and return JSON without modifying the project.

### Static source audit

```sh
python3 skills/design-pro/scripts/audit_ui.py /path/to/project --file src/hero.tsx --file src/styles.css
```

The auditor flags common gradient syntax (`DP001`), Inter usage (`DP002`), and loops requiring contextual review (`DP003`). Scoped exceptions can be recorded by file and line. It does not assess composition, semantic clichés, UX, contrast, or creative quality.

See [scope, exit codes, and exceptions](skills/design-pro/references/source-audit.md).

### Acceptance record check

```sh
python3 skills/design-pro/scripts/check_acceptance.py /path/to/review.json --root /path/to/project
```

This checks record consistency and evidence types. Failed, missing, or unsupported outcomes stay open; static-audit results remain informational. The script does not watch videos or judge aesthetics. A coherent record can become `ready_for_review`, which is a request for review rather than automatic creative approval.

## Development

Run the test suite without installing dependencies:

```sh
python3 -m unittest discover -s tests -v
```

The suite covers static auditing and acceptance-record consistency, including a regression where technical checks pass while an expressive brief fails. Structural checks and instruction trials complement these tests; they do not establish creative quality or a complete native workflow in both agents.

```text
design-pro/
├── README.md
├── LICENSE
├── .gitignore
├── skills/
│   └── design-pro/
│       ├── SKILL.md
│       ├── LICENSE
│       ├── agents/openai.yaml
│       ├── references/
│       │   ├── style-library.md
│       │   ├── visual-direction.md
│       │   ├── creative-library.md
│       │   ├── ux.md
│       │   ├── motion.md
│       │   ├── acceptance.md
│       │   ├── mobile-qa.md
│       │   └── source-audit.md
│       └── scripts/
│           ├── audit_ui.py
│           └── check_acceptance.py
└── tests/
    ├── fixtures/expressive_brief_regression.json
    ├── test_audit_ui.py
    └── test_acceptance.py
```

## License

[MIT](LICENSE). The installable skill includes a copy of the license so it can be distributed as a complete package.
