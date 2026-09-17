# Part 2: Component specifications

## Contents

1. Shared contract
2. Actions and controls
3. Forms and selection
4. Tables, search, and filtering
5. Containers and overlays
6. Feedback, files, and workflow
7. Navigation and contextual help

## 1. Shared contract

These are specifications, not completed components. Implement them in the actual product stack after reviewing existing code. Desired API examples are illustrative and do not imply `@kudu/ui` exists.

Every relevant component must define default, hover, active/pressed, keyboard focus, disabled, loading, empty, error, permission, responsive, and directionality behavior. Not every state applies to every component; mark irrelevant checks rather than fabricating them. Semantic status HEX values and final overlay shadows are still unresolved.

Use semantic CSS variables. Geometry defaults are draft: control sizes 32/40/44 px; normal control radius 10 px; panel 12 px; modal 14 px; icon sizes 16/20/24 px. A visible icon's size is not its whole clickable target.

## 2. Actions and controls

### Button

| Variant | Appearance | Intended use |
| --- | --- | --- |
| Primary | Blue outline, blue text/icon, light/transparent surface, no shadow | Main task in a local action group |
| Secondary | Very light neutral fill, dark text, no dominant border/shadow | Cancel, back, or supporting action |
| Destructive | Red filled, readable contrasting text | Actual destructive/negative high-impact action |
| Ghost | Text and optional outline icon; quiet background only on interaction | Low-emphasis contextual action |

Default button height is 40 px with 10 px radius, 14 px Medium text, and approximately 12-16 px inline padding. Use min-height and wrapping behavior where localization/zoom requires growth.

Primary states: default blue outline; hover pale blue; pressed a distinguishable stronger state; visible focus; disabled neutral. Do not silently turn the normal primary button into filled blue. The stronger pressed token is not finalized. Secondary hover darkens only slightly. Verify secondary fill does not outrank primary. Red is reserved; not every negative-sounding label automatically means data destruction.

During an operation, prevent duplicate activation and preserve the accessible label. An icon-only button needs a meaningful name and adequate target. Do not make every row action a prominent primary button. No yellow default CTA, gradient, large pill, shadowed action, or per-product custom button language.

Proposed API:

```tsx
<Button variant="primary">Save</Button>
<Button variant="secondary">Cancel</Button>
<Button variant="destructive">Delete</Button>
<Button variant="ghost">View details</Button>
```

### Input, textarea, select, date control, and search

Use soft neutral fill, a quiet border, 10 px radius, and a visible blue focus state. Inputs/selects normally use the shared control height; multiline textareas grow appropriately. Placeholder text cannot replace the permanent label. Do not use inset shadows.

The subtle border and fill choices are not automatically sufficient for control identification; validate non-text contrast. Error state combines a visible state change with a relevant text message. Read-only and disabled are different states: do not disable content users still need to select or read.

Select uses the same visual language and a simple chevron. Search within choices only when the options justify it. Preserve native semantics or use a tested accessible interaction primitive; do not build an inaccessible custom list merely to match a screenshot.

### Checkbox, radio, switch

Use restrained blue selected states and consistent keyboard focus. Checkbox supports independent selection and genuine indeterminate state. Radio supports mutually exclusive choices. Switch is for a true on/off setting, not a substitute for agreement checkboxes. Explain whether a switch applies immediately or requires Save; avoid silent inconsistencies.

## 3. Forms and selection

Use permanent minimal labels above fields. Mark required fields with an asterisk and programmatically required state. Add helper text only when a format, constraint, or non-obvious requirement is important. Show upload limits before selection, even in a minimal form.

Use one column by default. Two columns are appropriate for short, logically related fields; collapse to one when space or readable labels demand it. Do not add columns merely to reduce height. Short/medium tasks normally use a modal; complex or multi-stage work may require a page.

Long forms use headings/sections by default. Accordions are justified for optional or independently large areas; tabs require meaningful independent groups. Validation must not leave an error hidden in an unopened group.

Validation: inline messages under affected fields; summary for long or multi-error forms. Preserve entered values. Focus the first invalid field or the linked summary according to the implemented accessible flow. Do not send a disappearing toast as the only validation report. Timing beyond the discussed submit behavior remains an implementation decision, not a new approved rule.

## 4. Tables, search, and filtering

### Structured table

Use a clear, softly distinguished header; light row dividers; restrained hover; consistent alignment; and no default border around every cell. Essential text must be readable. Do not put the entire table in a card without a grouping reason.

Align numeric columns for comparison and isolate mixed-direction identifiers when needed. Keep statuses textual with soft badges. Use semantic column headers; if sorting is implemented, expose its state and keyboard operation. Select columns for the task, not decorative uniformity.

### Search and filters

On searchable data indexes, show search and a Filters button. Do not force search onto every page. Applied filters show a count and concise removable selections with Clear all. Distinguish unfiltered empty state from no matches. Specific filter-popover placement, URL persistence, and pagination reset behavior must be decided in implementation; they were not all approved in the interview.

### Row actions and selection

Show the most useful labeled action plus an overflow menu. Keep secondary/destructive actions in overflow when not the main task. Avoid a row of unexplained icons. Confirmation destructive buttons use the red-filled convention; do not turn every overflow menu item into a filled button.

Bulk selection is opt-in per real workflow. Once selected, show a contextual bar with count, meaningful actions, and Clear selection. Define whether selection includes this page or all filtered results. Never imply a larger selection than the user actually made. Hide the bar when selection clears.

### Pagination

Keep pagination legible but quiet. Show a range and total only when known. Do not invent totals. Infinite scroll is not the default for operational records; justify it by task. Keyboard and RTL behavior must be tested.

## 5. Containers and overlays

### Card and panel

Use only for a coherent independent item, such as an event or project summary. Prefer plain sections and dividers elsewhere. No card around every heading/filter/table. No nested card shells. No colored side accent lines or substitutes.

### Modal

Modal First is a default for manageable tasks, not permission to put every workflow in a small box. Use white surface, shared radius, clear title and close action, and minimal justified depth. Standard Small/Medium/Large width roles are approved; their exact pixel widths remain unresolved. Height adapts to content, capped by the viewport; scrolling should not hide critical actions.

Use a named dialog, deliberate initial focus, keyboard containment, Escape behavior appropriate to the task, and focus return after dismissal. Keep background content inactive while a modal is active. See the external APG reference in [accessibility](accessibility.md). Avoid nested modals.

Footer order follows locale/direction. Proposed implementation is primary at the logical inline end: right in LTR and left in RTL. This makes the earlier choice executable but still needs visual and keyboard-order validation.

### Confirmation

Request confirmation only for destructive or meaningful high-impact actions. State the object, effect, and action precisely; use a specific action label instead of a generic Yes. Routine Save/Edit should not trigger unnecessary confirmation. An unsaved-changes warning may be appropriate where dismissing would actually lose meaningful work; it is not a reason for constant prompts.

## 6. Feedback, files, and workflow

### Soft status badge

Use a very light surface with readable darker text, compact geometry, and optional purposeful icon. Map status meaning to success/warning/error/info/neutral; do not assign every domain state a new color. Semantic HEX values are not finalized. Color alone is insufficient.

### Toast and inline alert

Toast first for short-lived confirmations such as saved/updated/uploaded. Persistent blocking or actionable issues stay inline with text and a recovery action. Toasts do not steal focus or become the only location of an important result. Alert styling uses soft surface, icon/text, and optional action, never a colored side strip. Timeout and live-region details are implementation proposals to test, not fixed approved numbers.

### File upload

Use drag-and-drop plus an accessible file-picker control when uploading is central; a simple upload button when secondary. Show actual allowed formats/size before choosing, then filename, size/type, state, and relevant remove/replace controls. Keep failure details inline. Do not inherit the illustrative PDF/XLSX and 10 MB example as a global business restriction. Product/backend requirements determine limits; UI restrictions alone do not enforce upload safety.

### Empty state

Use a simple outline icon when helpful, descriptive title, one short explanatory sentence, and one relevant action. No large illustration or mandatory pattern. Differentiate first use, filtered no-results, failure, and lack of permission rather than representing all as no data.

### Loading/progress

Use skeletons for known page/list/table structure and a small spinner for short actions. For longer work, show meaningful stage text and actual progress only when available. Do not invent percentage completion, keep an endless silent spinner, or make an asynchronous task an unnecessary wizard step.

### Tabs, accordion, stepper

Tabs represent independent groups; do not use them merely to shorten a page. Use quiet blue active treatment and accessible state. Accordions disclose genuinely separable content. A stepper shows real sequential progress: horizontal for roughly 3-5 clear stages; vertical for a justified longer/complex flow; compact stage text for tight space. Do not fabricate steps for a one-screen operation.

## 7. Navigation and contextual help

Use a simple page header: title, optional short description, main action, and optional helpful divider. Breadcrumbs are for meaningful hierarchy, not mandatory decoration. Do not wrap the header in a card.

Choose sidebar, top, hybrid, minimal, or no navigation by product. When a sidebar is used, it is light with restrained blue details. Active state must not use a colored side strip. Collapse/reflow navigation rather than obscuring the main mobile task.

Tooltips can clarify an icon or secondary detail but cannot hide required instructions. Design keyboard and pointer behavior, and ensure the underlying control already has an accessible name.
