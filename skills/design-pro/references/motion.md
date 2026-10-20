# Motion with purpose

Read this document when a request includes movement or animations are modified. Restrictions and exceptions are in `SKILL.md`; a high intensity level does not disable them.

## Design the change

Describe each important animation through this contract:

| Field | Question |
| --- | --- |
| Trigger | Which action or real change starts it? |
| Purpose | Does it explain relationship, state, focus, or identity? |
| Transformation | What changes and what remains an anchor? |
| Resolution | In which usable state does it end, and when? |
| Alternatives | How does it work with touch, keyboard, and reduced motion? |

If you cannot describe the purpose, keep the interface still. Motion should end where it leaves the person ready to continue.

Expressive prominence is a valid purpose when it is part of the brief. Do not reduce that request to hover or control feedback because every animation is presumed to be utilitarian. Distinguish a conceptual demonstration from a real product output, and do not attribute unsupported transformations to the product.

## Prominent piece and sequence

When an audiovisual hero, fully animated scene, or powerful demonstration is requested, define these before extending the design:

- **Material:** what exists in the scene and which assets were accepted or rejected.
- **Transformation:** the structural, material, shape, or relationship change the person must perceive.
- **Sequence:** initial state → development → main change → resolution; design the return as well if the piece repeats.
- **Framing and reading:** how much space the piece occupies, what is visible on entry, and how it coexists with the CTA and heading on each surface.
- **Rhythm and amplitude:** action and reading time, enough variation to fulfill the brief, and stability where action is needed.

As an example structure, a signal can appear, reconstruct, interrupt, and resolve in a different composition. Choose phases and durations for the content; do not impose this sequence on every piece.

Implement and observe the full cycle with the actual medium first. If the brief requires prominent transformation, varying noise or tracking over the same image is insufficient merely because it produces different frames. The same applies to a generic crossfade between states when a specific transformation was requested.

An expressly requested loop can have narrative and purpose. Record its scope and make its progression legible; preserve pause controls, accessibility, and device adaptation. The restriction on ornamental loops must not neutralize an explicitly requested audiovisual piece.

Cards or samples must demonstrate what they claim. If they promise animated behavior, a capture at a fixed time does not establish it. If the task only requires comparing static appearance, a fixed sample can be correct: record the distinction without making every card animate by obligation.

## Coherent character

Choose concrete qualities for the product: precise, mechanical, heavy, elastic, delicate, or energetic. Define a small family of durations, distances, and curves. Perceived mass and distance inform timing; no spring curve is universally “premium.”

Use one dominant distinctive gesture per flow or prominent section, supported by discreet transitions. Expression can be intense where it helps the narrative; frequently used working content needs stability and immediate response.

As an adjustable starting point, direct feedback often needs tens of milliseconds and local transitions a few hundred. Observe the result: duration must not delay the task or prevent reading. Do not add artificial waits to complete choreography.

### Numerical timing and settling references

Keep concrete parameters as revisable starting points, never as a guarantee of aesthetics or performance:

| Situation | Starting reference | Adjustment |
| --- | --- | --- |
| Press or hover response | 80–150 ms | The action is recognized immediately and remains accessible without hover. |
| Local change or brief exit | 150–250 ms | Preserve continuity without delaying the next action. |
| Expansion, detail, or context change | 250–400 ms | Relate origin and destination through a legible resolution. |
| Justified cascade | 30–70 ms separation, brief total budget | Avoid making the last useful element wait before it can be used. |
| Precise resolution | Settling without perceptible bounce | Suitable when final position matters for reading, comparison, or action. Adjust the curve to distance. |
| Elastic resolution | At most one brief overshoot if justified by the direction | Adjust mass and damping in the installed API until that behavior is achieved; check interruption and repetition. |

Record chosen values for the dominant gesture and its variants when direction depends on motion. If the engine does not use these physical parameters, preserve the observable character through its own controls. The table is a design reference; verify implementation in the render.

## Causal examples

| Situation | Relationship to preserve |
| --- | --- |
| Reordering | The piece retains continuity, makes origin and destination visible, and settles in place. |
| Filtering | The set makes it understandable what remains, leaves, and appears. |
| Opening detail | The selected element connects to expanded context and allows returning to its origin. |
| Changing view | The person retains a reference to position or selection. |
| Confirming an action | The response accompanies the actual result in the relevant location. |
| Revealing an editorial sequence | Change helps read a relationship or story specific to the content. |

These examples explain decisions; they are not recipes to add to every product. Avoid simulating reordering data or activity that does not happen.

## Implementation and cost

Reuse the installed engine and check its version and API. CSS may be enough for small transitions; an additional engine needs a concrete reason. Different engines can coexist in independent parts, but must not compete for the same property on the same element.

For continuous changes, avoid state updates that rerender the tree every frame. Use suitable engine mechanisms, mutable values, or native animation. Prioritize transform and opacity when they fulfill the effect; do not promise GPU acceleration or smoothness without observing cost.

Geometry transitions need a conscious layout, transform, or native-API strategy; repeatedly measuring and writing layout can be expensive. Do not use `transition: all`: declare the necessary properties.

Clean up listeners, observers, timelines, and timers on exit. Pause continuous work when it is out of view or the tab is inactive. Use `will-change` only when useful and remove it when appropriate.

`memo` does not guarantee performance. Isolate work by responsibility and measure the actual problem before adding optimizations. Keep a usable version if the script is slow, fails, or never runs its entrance.

## Touch and accessibility

Hover effects enrich capable pointers. Every essential action and datum must remain available through touch and keyboard. An element following the cursor must not make the control harder to hit.

With `prefers-reduced-motion`, simplify or remove nonessential movement while preserving outcome, focus, and feedback. Keep content visible; an element at opacity 0 waiting for a disabled animation is a failure.

If functional automatic movement exists, offer control when appropriate and avoid interfering with reading. A processing indicator must end when the operation resolves; the app cannot pretend to be perpetually active.

## Verify rhythm and behavior

Observe the full sequence: entrance, interruption, repetition, exit, and return. Test fast actions, state changes before completion, and reduced-motion preference.

An image does not validate rhythm. When movement defines the proposal, offer a short interactive demonstration with pause and replay; add scrubbing or slower speed if useful for review. Do not generate a costly video or study by default for a simple hover.

Report what was observed and under which conditions. If claiming a frame-rate target, include a measurement of the walkthrough and the device or environment used.

### Independent temporal impact

Evaluate the main change's readability, amplitude, progression, pauses, and resolution at normal speed. Also review the first frame, ending, return, and change of example. A working Pause control verifies playback, not choreography quality.

Keep a recording or reference to observed playback, with key-phase frames if useful for comparison. A contact sheet communicates structure but does not replace watching the sequence in real time. If playback cannot be observed, impact remains pending; do not approve it from code.

A programmed update limit is a decision, not an FPS measurement. If the performance budget requires changing language or fluidity, explain and resolve the conflict; do not silently reduce the expression that defines the request. A deliberately low-frame-rate treatment can be valid when it is the selected direction, not an automatic excuse.

Record the outcome in the temporal [acceptance](acceptance.md) review. Pixel differences between two images establish only change; they must accompany evaluation of the brief and full cycle.

## Technical references

Verify the installed library's API against its official documentation when needed. For accessibility and memoization limits:

- [W3C: Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)
- [W3C: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
- [React: memo](https://react.dev/reference/react/memo)
