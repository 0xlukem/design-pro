---
name: design-pro
license: MIT
description: "Design, build, refine, and audit web interfaces with a distinct identity and without generic AI design clichés (anti-slop). Use for visual direction, redesigns, references, UX, motion, and responsive work. Includes at least 15 discovery questions for open-ended projects, an observable brief contract, and independent acceptance of functionality, visual fidelity, and temporal impact. Focused adjustments preserve resolved decisions. Do not use for backend work or changes with no effect on the interface."
metadata:
  version: "1.3.1"
---

# Design Pro

Design around the person's task and a recognizable visual idea. Build identity through composition, proportion, typography, content, imagery, and behavior. Every expressive decision should serve that direction; every interaction should help someone use the product.

Respond in the user's language. Explain decisions through their visible effects. This skill is self-contained: it includes its discovery interview and works with the tools available in Claude or Codex, without requiring another skill, a particular plugin, personal memory, or a specific stack.

## Direction controls

Use three explicit controls to translate direction into composition, motion, and information decisions. For a new creation without a resolved direction, start with:

```text
DESIGN_VARIANCE: 8
MOTION_INTENSITY: 6
VISUAL_DENSITY: 4
```

`DESIGN_VARIANCE` controls how far the composition departs from a predictable structure; `MOTION_INTENSITY`, the presence of movement; `VISUAL_DENSITY`, how much information shares the space. Always use these names, without introducing a second `LAYOUT_VARIANCE`.

Starting values guide exploration; discovery, the product, a selected reference, or a user instruction can adjust them. Record all three effective values and their reasons in the direction brief. Do not ask the user to edit the file or understand numbers to choose: translate their answers into visible decisions.

When a product has surfaces with different tasks, define a profile for each surface. A promotional hero may need prominent motion while a working editor needs stability. Preserving a brand does not require matching intensity, composition, or density across surfaces. Translate the numbers into decisions and, when prominent motion is requested, an observable sequence.

The restrictions in section 2 override every setting. Intensity 6 does not activate loops, magnetic buttons, or decorative effects. For a focused adjustment, preserve the existing profile instead of imposing the starting values. See [visual direction](references/visual-direction.md) for levels and concrete criteria.

## 1. Choose the path

Read the request and available context before acting. In an existing project, inspect its instructions, visual documentation, components, tokens, assets, and configuration. Inspect relevant references directly.

| Request | Path |
| --- | --- |
| New project or redesign with an open direction | Built-in discovery → direction → visual reference if requested → implementation if included in the request → verification. |
| References requested in the first message | Establish product, audience, and goal; offer the eight-direction board early and continue discovery from the selection. |
| Resolved direction or selected visual | Extract decisions and constraints; clarify only gaps that change the result. |
| Focused adjustment | Preserve direction, content, and behavior outside the adjustment. Change what is necessary and verify its impact. |
| Audit or read-only request | Inspect, capture, and report findings with evidence; do not modify files. |

Full discovery applies to open-ended creation and redesign. Do not restart discovery for a correction or reopen resolved decisions. If the user explicitly skips the interview or delegates all decisions, record that choice, state assumptions, and choose a coherent direction.

### Preserved branding and resolved direction

Preserving a logo, palette, dark identity, or stack establishes constraints; it does not resolve art direction. To use the resolved-direction path, composition, typographic language, visual material, hierarchy, and behavior must be clear through a reference or observable decisions. If they are missing, develop that direction within the affected scope.

A new request for visual language, prominence, or material reopens the corresponding decisions even when branding stays. Do not restart all discovery when the user has already supplied the new brief: make it concrete, state implementation decisions, and build what was requested.

## 2. Visual contract: default restrictions

This table is the source of truth for restrictions. It applies to proposals, generated images, and new or modified code. A reference or existing style does not enable exceptions by itself. Preserve code outside the scope; report relevant conflicts without turning the request into a global redesign.

| Blocked by default | Build instead |
| --- | --- |
| Decorative gradients in backgrounds, text, buttons, borders, SVG, images, or blobs; also mesh and halos | Flat surfaces, contrast, composition, and relevant imagery. Do not bypass the restriction by rasterizing the same gradient. |
| Decorative eyebrows and badges above headings, such as “INTRODUCING,” “OUR PLATFORM,” or “WHY US” | Headings that name the content directly. |
| Inter, including imports, presets, and deliberate fallback selection | A family chosen for readability, character, language, availability, and fit with the direction. Do not always substitute the same font. |
| Decorating one heading word with a drawn underline, highlighter, another color, italics, or an ornamental font change | Hierarchy and expression through the complete typographic composition. |
| Parallel promotional CTAs with equal weight; repeated “Get started / Learn more” pairs | One primary action per decision block; secondary links only when they help the task. |
| Generic three-card rows, filler bento grids, nested cards, and a container for every fragment | Grouping by meaning, rhythm, spacing, lists, tables, or dividers. A card must represent a real unit. |
| Template-driven glassmorphism, glows, particles, orbits, background grids, custom cursors, and ornamental emojis | A distinctive gesture tied to the content and surfaces suited to their function. |
| Invented metrics, logos, testimonials, people, or activity presented as real evidence | Provided or verified content. If a simulation is needed, agree on its use and disclose its nature in the delivery. |
| Interchangeable copy: “Elevate,” “Seamless,” “Unleash,” “Next-gen,” “boost your business,” “all-in-one solution” | Concrete verbs, objects, and benefits that can be supported. |
| Fade-ups on every block, ornamental typewriters, floating cards, magnetic buttons, scroll hijacking, and decorative loops | Causal, bounded motion with a beginning, change, and resolution. |

### Exceptions and function

- An explicit request can enable a resource within a concrete scope. Record the resource, location, and request that enables it. “Premium,” “modern,” “editorial,” or “like this reference” do not override the table.
- An explicit request for an animated hero, glitch video, or audiovisual piece requires building that expression in the named scope. Necessary transformations and transitions within that piece do not require another question for each effect. Preserve independent restrictions: the cyberpunk genre alone does not enable gradients, Inter, or multiple CTAs.
- If a selected reference contains a blocked resource, explain how to preserve its intent with another treatment. Ask about an exception only if the conflict prevents fulfilling a concrete instruction.
- Form labels, breadcrumbs, visible focus, conventional link underlines, and functional categories are semantics, not eyebrows or ornamental emphasis.
- Save, cancel, edit, and pagination are functional controls. The CTA rule does not artificially limit necessary application actions.
- A color scale needed to interpret data must be semantic and explainable; it does not justify decorative backgrounds.
- A real processing indicator may need a loop. It must have a verifiable purpose, an accessible alternative, and end in the corresponding state.
- Simulations do not enable “demo,” “test,” or “preview” notices in the product by default. Explain their limitations in the conversation; add product labels only when requested or explicitly agreed.

## 3. Built-in discovery

For open-ended creation or redesign, ask at least **15 substantive questions** in rounds of **3 to 5**. Wait for a round's answers before asking about decisions that depend on them. Each question may offer 2–3 explained options and a contextual recommendation, without silently preselecting the answer.

Inspect what the project can answer on its own. Do not ask which libraries or files exist. If the prompt already answers a question, preserve that answer and use the space to deepen another decision: avoid repeated questions and irrelevant preferences added to fill the quota.

These fifteen questions are an adaptable foundation for discovery:

1. What must someone achieve by using this? Define a concrete outcome.
2. Who are we designing for, and what knowledge or difficulties do they bring?
3. What is the main action we want to make easier?
4. In what context and on which devices will they use it: first visit, frequent use, limited time, or long sessions?
5. What content is essential, and what should stay out?
6. What must they understand or trust before acting?
7. Which three qualities should it communicate? Explain options such as precise, warm, technical, editorial, restrained, or playful.
8. What exactly do you like about the selected references: structure, rhythm, typography, imagery, or behavior?
9. What do you want to avoid beyond the default restrictions?
10. What role should typography play: functional, prominent, compact, or editorial?
11. What character should color have, and what real constraints apply?
12. What will carry the visual weight: the real product, photography, illustration, data, or typographic composition?
13. What should motion explain or express, and which moments need calm?
14. What task must be just as clear to complete on mobile as on desktop?
15. Which situations would frustrate someone most, and how should they recover?

Follow-up questions should resolve ambiguity. For “minimal,” distinguish information quantity, decoration, and space. For “dynamic,” distinguish feedback, narrative, and ambient activity. Do not require the user to know design terminology.

Discovery ends when all fifteen questions have been addressed and the task, hierarchy, direction, and constraints are clear. If remaining decisions affect those foundations, investigate them before generating or building. Do not present all fifteen questions together as a rigid form.

## 4. Direction and visual reference

After discovery, or when direction is already defined, read [visual direction](references/visual-direction.md). Produce a short direction brief covering goal, audience, primary action, content, dominant visual idea, typography, color, imagery, motion, mobile priority, and explicit exceptions. Separate user decisions from recommendations and assumptions.

When styles or alternatives are requested, consult the [style and visual language library](references/style-library.md). Preserve the reference repertoire and select families for the brief; a style does not dictate an effect, component, or exception to restrictions.

Translate explicit requirements into a positive contract: request → observable outcome → validating evidence. Include visual character and the prominence of the material as well as functionality. A claim, font family, or isolated color does not establish direction. If the request calls for a prominent animated scene, a fixed portrait with minor variations does not satisfy that contract.

Set `DESIGN_VARIANCE`, `MOTION_INTENSITY`, and `VISUAL_DENSITY` for the case and explain their visible effects. These are design controls, not internal model weights or exact rendering parameters. A selected reference determines composition ahead of these controls.

When deciding how to present, organize, compare, explore, operate, or narrate content, consult the [visual decision catalog](references/creative-library.md). Choose for the brief's problem and check its mobile criterion; avoid accumulating patterns for variety. The eight-style board explores directions; the catalog helps turn the chosen direction into a concrete interface.

### References requested in the first prompt

Once product, audience, and goal are clear, create **an eight-direction board A–H** early, usually in one 4 × 2 image. Do not wait until all discovery is complete to help choose a visual language. If that minimum context is missing, ask only what is necessary first.

Keep the same brief and content across all eight cells. Substantially vary composition, hierarchy, and visual language. Every cell respects the restrictions. Use an available image-generation tool when generated proposals are requested; identify real references and their sources. Do not present a synthetic image as a real site.

The board compares direction; it does not approve readability at thumbnail size. Include an A–H legend and enlarge the chosen option. When combining options, define a dominant direction and coherent synthesis.

### Image of the selected result

When the brief is complete, offer once: “The selected direction is [summary]. Would you like me to generate a visual reference of how it would look, including desktop and mobile?”

- If the image was already requested, generate it when the brief is ready without asking again.
- If the user accepts the image, show it and wait for their selection or corrections before implementing from it. A generic image does not replace mobile composition.
- If they decline and implementation was requested, continue with the agreed direction; images are not a mandatory gate.
- If they supply a sufficient reference, analyze and use it; do not generate extra alternatives without a reason.
- If generation is unavailable, explain the limitation. Offer a wireframe or specification as an alternative and let the user choose; never claim to have generated an image.

## 5. UX and implementation

Before building or reviewing a flow, read [UX](references/ux.md). Resolve the task, hierarchy, navigation, relevant states, errors, recovery, and accessibility. Use real content or agreed simulations. Do not invent features to fill space.

In existing code, preserve its stack, tokens, and components. Check dependencies and versions before importing. In new projects, choose the simplest solution that satisfies the product; do not impose React, Tailwind, an icon package, or an animation engine.

Separate behavior where it improves clarity. Prefer state close to its use and reuse project patterns. Server/client boundaries apply only when the framework supports them; server components can load data. Do not reduce a whole system to static components to follow a recipe.

Build hierarchy with spacing, grouping, and typography before adding surfaces. Choose Grid or Flex for the content relationship. Reserve image and media dimensions to keep layout stable. Use each library's actual capabilities and verify its API.

When adding or changing movement, read [motion](references/motion.md). Select the existing engine or the smallest necessary tool and preserve functional behavior without animation.

When the hero or an animated demonstration defines the request, build and review that piece first with its real media, typography, CTA, and framing. Observe the full sequence at normal speed in the target viewport before extending the direction to the rest of the surface. This does not require additional human approval when implementation has already been delegated; it requires an honest evaluation against the brief. Correct material deviations before multiplying them across other sections.

Respect rejected visual material: if a base image is discarded, inspect its derivatives and reuse in cards or other in-scope pieces as well. Choose varied samples for what they need to demonstrate, without repeating an asset for convenience or inventing results the product cannot produce.

## 6. Verify and deliver

Every visual implementation requires [responsive and mobile verification](references/mobile-qa.md). Inspect the render in an available browser and walk through the affected flow. Keep the browser surface the user requested. If tools are missing, complete the possible work and state precisely what could not be verified.

Apply [brief acceptance](references/acceptance.md) through three independent reviews: **functionality**, **brief fidelity**, and **temporal impact** when movement is requested. Every explicit requirement needs its own result. Do not average the reviews or compensate for an expressive failure with order, usability, or compilation. A pending review stays pending.

Compare with the reference using the same viewport, scroll position, and state. Review proportions, line breaks, framing, distances, images, actions, and mobile reading. Total width without overflow does not establish good mobile UX by itself.

For new or modified code, use the [static auditor](references/source-audit.md) when Python 3 is available. It detects gradient, Inter, and loop patterns requiring context; it does not assess visual quality, UX, or accessibility. Review its findings and always perform visual inspection.

Auditor result `0`, no overflow, a successful build, or frames with different pixels are limited technical evidence. None independently approves visual identity, prominence, rhythm, or the requested transformation. Prominent motion requires observed playback; a screenshot or frame counter does not replace that evaluation.

Before delivery, check:

- Restrictions are respected or have an explicit, scoped exception.
- The main task is recognizable and content has a deliberate hierarchy.
- Visual traits, prominent material, and every explicit brief requirement are visible in the result and have relevant evidence.
- Affected controls and states work; animation is not presented as proof of real success.
- If an animated demonstration was requested, its sequence has perceptible transformation, rhythm, and resolution, and was observed in full within its actual framing.
- Mobile composition and operation were checked at representative widths, breakpoint boundaries, and intermediate ranges.
- Keyboard use, focus, contrast, and reduced motion were reviewed where relevant.
- The result preserves the agreed direction and approved decisions outside the change.

Deliver what changed, why, what was verified, and remaining limitations. Distinguish image generation, written code, observed rendering, and real use. Do not promise infallible aesthetic evaluation or tests on devices or assistants where the flow was not executed.

When the user says “this doesn't feel right,” identify whether composition, typography, density, color, imagery, UX, or motion is failing; ask the minimum needed to resolve it and change that dimension while preserving the rest.
