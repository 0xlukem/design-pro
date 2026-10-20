# Responsive and mobile verification with evidence

Read this document before delivering a visual implementation or audit. Apply the walkthrough to affected screens and behavior; expand it when the change affects a shared component.

## Mobile composition

Decide reading, action, navigation, cropping, density, and fixed-element priorities. A small screen needs its own composition, consistent with the chosen direction. Avoid solving it solely by shrinking the font or stacking everything without hierarchy.

Preserve the task and essential information. If a table needs two dimensions, it can use a recognizable scroll container; this does not justify horizontal overflow across the whole page. Check that controls remain reachable.

When producing a visual reference, show desktop and mobile versions of the same direction. The style board does not replace this decision.

## Choose widths and breakpoints

Inspect the actual breakpoints of affected components. Adjust composition where content stops working, without assuming standard classes cover every range.

| Group | Starting verification points |
| --- | --- |
| Mobile | 320, 360, 390, and 430 CSS px. |
| Tablet | 768 or 820, and 1024 if structure or orientation changes. |
| Desktop | 1280 or 1440; 1920 or wider when the surface requires it. |
| Boundaries | For every relevant breakpoint B, check B−1, B, and B+1. |
| Ranges | Resize between points to find broken intermediate widths. |

These widths are verification points, not a requirement to create media queries for each one. For a focused adjustment, check deeply where behavior changes and perform a proportionate regression check in other ranges.

Example: if the menu changes at 768 px, review 767, 768, and 769. If text breaks at 910, correct that range even though it is not a common device size.

## Review content and space

- Horizontal page and component overflow; do not hide it globally to make the check pass.
- Heading breaks, reading width, readable sizes, and spacing between sections.
- Full framing: how much content, imagery, and the next action fit in the available height.
- Promised prominence: check that requested media or demonstrations dominate where intended and are not pushed below the initial frame by text or controls.
- Images with reserved dimensions, meaningful crops, and suitable resolution.
- Long names and titles, accented characters, large quantities, empty states, extensive lists, and missing data.
- Font changes or media loading that alter composition.

## Review operation

Walk through primary actions with emulated or real touch and with the keyboard. Check menus, search, filters, forms, dialogs, and error recovery as relevant to the product.

Use 44 × 44 CSS px as a practical touch-area target, with sufficient spacing. This is a quality choice in this skill, not a claim that every AA criterion requires 44 px. Icons can be small within a suitable interactive area.

Review focus order, visibility of the focused control, zoom, and reduced motion. Check that sticky or floating bars do not cover text, results, or actions.

Check short heights and landscape orientation when they affect operation. For forms, consider the virtual keyboard, scrolling to the active field, and submission controls. If the environment supports observing a real device, also check browser bars and safe areas.

Do not choose `100dvh` universally: use content-based height, stable `svh`, or adaptive `dvh` according to expected behavior. The virtual keyboard and browser bars require specific observation; a narrow desktop screenshot does not establish their behavior.

## Captures and walkthrough

Use the same viewport, scroll position, and state when comparing the reference, before, and after. Scroll through the actual page before capturing sections whose appearance depends on scrolling. Wait for media to load and reach its final size.

Include the actual panel or window viewport where the work is being evaluated when known; do not check only wide presets. Record width, height, and the position of prominent media. A hero that works at 1440 px may relegate its demonstration in a narrower window despite having no overflow.

If an animated scene was requested, observe the same cycle in mobile and primary framing. Adapting cost or layout must not silently turn it into the fixed image the brief rejected. The accessible reduced-motion alternative preserves meaning and is assessed separately.

Screenshots establish composition. Executing actions establishes behavior. Combine both when the request includes interaction.

Record brief fidelity and temporal impact alongside responsive results in [acceptance](acceptance.md). No overflow cannot compensate for invisible prominent media or a visual language different from the request.

For broad work, keep a proportionate evidence record:

| Screen or flow | Viewport and state | Composition | Operation | Evidence or pending check |
| --- | --- | --- | --- | --- |
| Reviewed element | Width × height, orientation, state | Observed result | Action and result | Screenshot, trace, or concrete limitation |

Do not fill this table with assumed approvals. Record only what was executed. Screenshots and logs may remain temporary working material; they should not automatically become product deliverables.

## What verified means

- “Responsive reviewed” requires observed rendering across affected ranges and a walkthrough of relevant states.
- “Emulated mobile” identifies a test using an emulated viewport, touch, or device profile.
- “Real device” describes only a test performed on that device.
- “Accessibility reviewed” lists what was checked; it does not imply complete certification.
- If the browser or a surface is unavailable, state the limitation and the reviews actually performed. Do not replace evidence with a promise.

## Technical references

- [web.dev: content-based breakpoints](https://web.dev/learn/design/media-queries)
- [web.dev: accessible responsive design](https://web.dev/articles/accessible-responsive-design)
- [web.dev: small, large, and dynamic viewports](https://web.dev/blog/viewport-units)
- [W3C: Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- [W3C: Target Size (Enhanced)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html)
