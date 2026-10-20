# Visual direction and references

Read this document to define a direction, produce references, or evaluate whether a proposal has an identity. Restrictions and exceptions live exclusively in section 2 of `SKILL.md` and remain active throughout exploration.

## Direction brief

Return a brief that supports decisions throughout the work. Adapt its length to the project:

| Field | What it must resolve |
| --- | --- |
| Product, audience, and task | What the person uses, for what purpose, and in which context. |
| Surface | Promotional landing page, editor, catalog, or component; each one's function within the same brand. |
| Preserved constraints | Logo, palette, content, or integrations that stay; do not confuse them with a resolved direction. |
| Action and hierarchy | What is recognized first, what needs to be understood, and what happens next. |
| Content | What actually exists, what is missing, and which simulations were agreed. |
| Visual idea | A concrete sentence describing the relationship between content and composition. |
| System | Available type families, scale, flat palette, spacing, surfaces, and imagery. |
| Behavior | What motion explains and where the interface stays still. |
| Mobile | Reading, navigation, and action priorities on a small screen. |
| Controls | Effective `DESIGN_VARIANCE`, `MOTION_INTENSITY`, and `VISUAL_DENSITY` values, with their visible effects. |
| Provenance | User decisions, recommendations, assumptions, origins of values, and explicit exceptions. |

An idea such as “a collection archive with a side index and prominent photography” guides decisions. Adjectives such as “premium, modern, and clean” need to become concrete before guiding implementation.

## Positive contract and observable outcomes

For each requirement that determines the result, record:

| Request | Observable decision | Evidence of fulfillment |
| --- | --- | --- |
| Composition or prominence | Which element dominates, its relationship to text, and how it enters the initial frame. | Rendering in the viewport where the surface will be used. |
| Typographic language | Letter construction, width, weight, rhythm, and relationship to content. | Real text in the composition, not the name of a font. |
| Visual material | Which image, scene, medium, or geometry appears and why it represents the product or direction. | Actual asset or rendered scene; clear provenance and function. |
| Palette and materiality | Contrast, surfaces, texture, and depth compatible with restrictions. | Integrated result, not an isolated color swatch. |
| Requested motion | What changes, in which order, with what amplitude, and where it resolves. | Full playback; key frames as supporting material. |
| UX and primary action | What can be done and how its result is recognized. | Action walkthrough and relevant recovery. |

“Keep it dark” resolves only part of the palette. “Cyberpunk” or “hacker” requires a coherent combination of composition, typography, material, and behavior. Black, green, uppercase letters, and a thematic claim do not establish that language.

When the user requests an ethereal, unusual, or audiovisual piece, propose and specify how it will be perceived: for example, geometry losing and regaining structure, material changes, layers with depth, or visible reconstruction. These are possibilities according to the brief, not a recipe for every brand or implicit permission for blocked decoration.

Make the hypothesis refutable: describe what will be visible and which result would fall short. If prominent animation was requested, a fixed image with minor interference can fail even when rendering changes some pixels. If an image was rejected, reusing it in a card does not satisfy the correction either.

## Surfaces within one brand

A landing page needs to express value and may use a central audiovisual piece. An editor needs to support repeated work with stable controls. A catalog needs comparable samples. Keep brand coherence and adapt composition, density, and motion to those functions.

Define the prominent piece and check it before extending the language to other sections. If the hero does not communicate the direction, repeating its font, palette, and asset across the site amplifies the problem.

The brief may live in the conversation. Save it in the project if that is part of the request or the work needs a persistent document; do not create auxiliary documentation for every adjustment.

## Direction controls and levels

Starting values are defined in `SKILL.md`; that is the only place that configures the starting point. Keep all three explicit controls in the brief even when the user answers in natural language. Adjust effective values to the product and record whether they come from the brief, a reference, a user choice, or the starting profile.

| Control | 1–3 | 4–7 | 8–10 |
| --- | --- | --- | --- |
| `DESIGN_VARIANCE` | Stable grids, consistent alignments, and repeated proportions. | Controlled offsets, changes in proportion, and rhythm between text and images. | Expressive composition: differently sized masses, marked asymmetry, and a distinct visual sequence. |
| `MOTION_INTENSITY` | Immediate feedback and discreet transitions, usually without automatic entrances. | Spatial continuity, perceptible state changes, and a bounded expressive gesture. | Prominent choreography, spatial transitions, or sequences tied to content and justified by the product. |
| `VISUAL_DENSITY` | Few units, controlled reading width, and generous separation. | Balanced everyday reading and grouping by task. | Frequent, compact information, precise rows or columns, and controls that remain legible. |

High variance does not require masonry, overlap, or huge empty spaces. High intensity does not enable blocked decoration or loops. High density does not justify tiny controls. Record the reason for each choice rather than fictitious numerical precision.

Intensity and impact are different. A minimal effect can score highly because it runs constantly while still failing to deliver a prominent transformation. Justify values through observable outcomes and distinguish the hero profile from a working surface's profile.

In the A–H board, each direction can explore a different profile; record differences when they help selection. In the chosen direction, keep a coherent profile and adapt its expression to each device: mobile does not inherit overlaps that prevent operation.

## Type scale and weights

Define a scale and concrete roles instead of relying on “premium typography.” Adjustable starting references include body text at 16 px relative to root size, long text at roughly 45–65 characters per line, and headings at 32–40 px on mobile and 48–64 px on desktop when content allows. These are composition references, not mandatory sizes for every product.

| Role | Weight reference | Criterion |
| --- | --- | --- |
| Reading text | 400 | Preserve comfortable reading and sufficient contrast. |
| Labels and actions | 500–600 | Distinguish function without making every control prominent. |
| Headings | 500–700 | Build hierarchy together with size, space, and proportion. |
| Data | Consistent weight and tabular figures when useful | Support comparison; use monospace only if it serves the direction. |

Check which weights and characters the actual family provides. An editorial family may resolve hierarchy with other weights; do not force synthetic bold or an ornamental mixture of styles within a word. Preserve the core typography restrictions.

## Eight-direction board

Use it when references or an eight-style exploration are requested. Keep product, audience, content, and primary action consistent so comparison is meaningful.

These eight families remain available as a starting point. To broaden or deepen styles for the brief, consult the [style and visual language library](style-library.md):

| Direction | Decision to explore |
| --- | --- |
| Editorial typography | Reading rhythm and typography as structure. |
| Technical utility | Density, precision, and repeated operation. |
| Warm modernism | Proportion, space, and approachability. |
| Industrial | Structure, signage, contrast, and materials. |
| Restrained brutalism | Direct hierarchy and deliberately raw composition. |
| Cultural archive | Classification, indexes, and relationships between pieces. |
| Photography | Framing, image sequencing, and dialogue with text. |
| Playful geometry | Shape, flat color, and expressive behavior. |

Adapt or replace these families for the product; this is not a mandatory list for every board. Differences must extend beyond palette and font. Each proposal should change at least one relevant structural decision: hierarchy, composition, imagery, or how content is explored.

For a 4 × 2 image, reserve a consistent cell per direction and accompany it with an A–H legend. Check the generated board: eight distinct cells, clear correspondence with the legend, and compliance with restrictions. If a cell violates the brief, correct it before offering it as an option. Image generation can produce imperfect text; do not present it as approved copy.

For real references, inspect screens before citing them and link their sources. Explain what is adopted and what is discarded. Do not attribute a generated proposal to a real product.

Then select resources from the [visual decision catalog](creative-library.md) for the task they solve. A family such as “industrial” can use a product record, comparison, or narrative scene; it does not require a particular component. If combining references, record which visual relationship each contributes and preserve a dominant direction.

## Adaptable generation prompt

Attach the real images available to you; do not claim they were attached when only a description was provided. Build the prompt with:

1. Agreed product, audience, task, and content.
2. Output type: A–H board or detailed screen of a selected direction.
3. Dimensions and aspect ratio. For a detailed screen, define desktop and mobile separately or in two clearly separated frames.
4. Agreed composition, typography, color, imagery, and density.
5. All applicable restrictions from section 2 of `SKILL.md` and explicit exceptions.
6. Readable content, clear hierarchy, and one primary action; no invented feature inventory to fill space.

Request interface content without a device frame or browser chrome unless expressly requested. Do not stretch a desktop composition to fill a mobile frame. Recompose for its priorities.

If product imagery is missing, ask about its use when decisive or propose a direction supported by actual material. Do not automatically substitute random photographs or decorative illustrations for relevant imagery.

## Visual evaluation and feedback

Compare the selected reference with the render, not with a description of how it should look. Review relationships between elements and the full frame alongside isolated details.

Use these acceptance criteria:

- The screen communicates product, task, and next step without an external explanation.
- The visual idea is recognizable through connected typography, composition, imagery, and behavior decisions.
- The piece works with its specific content; it does not depend on filler metrics or decoration.
- Hierarchy keeps working with real text and on mobile.
- Spaces, alignments, line breaks, crops, and states show intent and coherence.
- The result respects the reference and agreed corrections.

Check every explicit request through the independent [acceptance](acceptance.md) review. Respected restrictions and an orderly screen cannot compensate for the wrong visual language.

When someone says “this doesn't feel right,” locate the affected dimension before regenerating everything. In a reference mix, choose a dominant direction and explain how the secondary gesture will fit.
