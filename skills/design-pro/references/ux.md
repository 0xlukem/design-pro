# UX: from task to behavior

Read this document when designing, implementing, or auditing a flow. Match the depth to the task; a spacing adjustment does not require redesigning navigation.

## Task and hierarchy

Describe who arrives, what they need, what information they require before acting, and how they recognize the result. Choose one priority per screen or decision block. Supporting actions have less visual weight while remaining accessible.

Organize by frequency, sequence, and meaning. Use progressive disclosure when complexity can wait. Avoid hiding essential information behind exploratory interaction. Preserve recognizable terms and patterns in navigation, filtering, search, and editing.

Test a quick reading of the render: what am I looking at, what is it for, and what can I do? If the screen needs a verbal explanation, revise content and hierarchy.

## States relevant to the product

For each affected interaction, consider only states that exist:

| State | Criterion |
| --- | --- |
| Initial | Helps recognize the task and start. |
| Loading | Explains a real wait; reserves space and preserves useful context. |
| Initial empty state | Shows what is missing and how to begin. |
| No results | Preserves filters or the query and allows correction. |
| Error | Identifies the problem and offers concrete recovery. |
| Success | Confirms an outcome that happened, in the relevant location. |
| Disabled | Explains the prerequisite when it is not evident. |
| Selection or editing | Makes the affected content recognizable and shows how to finish or undo. |

Do not introduce loaders for instant operations or artificial delays to display animations. A skeleton is useful only when it represents an expected structure; a brief, accessible indicator may be better for an indeterminate wait.

In prototypes, disclose which states are simulated and which actions are not connected. A visual response does not establish persistence or real execution.

## Forms and recovery

- Use visible, associated labels; placeholders do not replace them.
- Group related fields, identify required information, and explain requirements before an error.
- Use input types, autocomplete, and inputmode suited to the data.
- Validate at a useful moment, preserve values, and place errors next to the field.
- Associate messages and fields for assistive technologies; avoid relying only on color.
- Prevent duplicate submissions during a real operation and allow retry when it fails.
- Keep the person in context when completing or correcting. Consider undo for reversible actions and proportionate protection for destructive ones.

Do not add fields the product does not need. In stepped flows, make progress recognizable and allow returning without losing data when feasible.

## Accessibility and predictability

Use semantic HTML before recreating controls. Review accessible names, tab order, keyboard activation, visible focus, and text/control contrast. Check contrast with a tool or calculation; looking at the color does not verify it.

Informative images need alternative text based on their observed content. Reserve `alt=""` for actual decoration. If an image is still missing, record that integration as pending; do not present empty alt text on a prominent photograph as resolved accessibility.

Reading and focus order must remain meaningful in every composition. Do not change visual order alone so keyboard and screen-reader users encounter a different story.

In dialogs, move focus to the appropriate context, contain it within a real modal, and restore it on close. Provide keyboard dismissal and a visible control. Prevent banners, fixed bars, or the keyboard from hiding the active element.

Important state changes must be perceivable without watching one point or interpreting an animation. Use proportionate accessible announcements when the change is not otherwise communicated.

## Content and complexity

Use concrete verbs for actions and consistent names for the same entities. Error messages should explain what happened and what can be done. Avoid spatial language such as “on the left” when the mobile composition changes.

Test long titles and names, accented characters, different quantities, large lists, empty lists, and missing content. Translation or real text should not dismantle a composition prepared only for short phrases.

Do not add search, tabs, filters, notifications, dark mode, or sections merely because they look typical of an application. Each element needs a task or requirement that justifies it.

## Completion evidence

Walk through the main task and at least its relevant recovery. Report observed states, simulated states, and what could not be executed. A screenshot establishes appearance; the walkthrough provides behavioral evidence.
