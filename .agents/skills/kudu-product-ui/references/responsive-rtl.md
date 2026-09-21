# Responsive and RTL/LTR behavior

## Fixed direction

Responsive behavior is required from the beginning (D42), across Intranet, Engineering, operational systems, Finance, Supply Chain, and other internal products. Navigation and content widths are adaptive (D40-D41), not a single template.

Set the actual document language and direction, for example `lang="en" dir="ltr"` or `lang="ar" dir="rtl"`. English documentation does not imply English-only products. Use logical layout properties and preserve a sensible DOM/keyboard order. Do not reverse layout twice through both `dir` and arbitrary row reversal.

## Component behavior

| Component | Small-screen behavior | Direction considerations |
| --- | --- | --- |
| Header/actions | Wrap/reorder without hiding the main task | Primary action at agreed logical location |
| Navigation | Appropriate collapse, drawer, or simpler structure | Directional chevrons/arrows follow meaning |
| Form | Single column when needed; labels remain visible | Arabic metrics and mixed-value fields tested |
| Modal | Fit viewport; controlled internal overflow; reachable actions | Footer mirrors logically, not arbitrary tab order |
| Table | Preserve key columns; purposeful horizontal scroll where necessary | Isolate IDs/numbers; align columns for comparison |
| Filters | Remain accessible behind Filters; active count/clear actions visible | Chips and dismissal controls remain understandable |
| Detail page | Essential summary first; secondary panels relocate | Reading order remains meaningful |
| Stepper | Compact progress when the full layout does not fit | Stage sequence follows language and actual task |
| Toast/alert | Do not cover task controls or vanish as sole error evidence | Readable text and correct announcement behavior |

The draft breakpoint boundaries are 640, 1024, and 1440 CSS px. Content can require adaptation between these boundaries. Do not treat devices as exact pixel categories or infer that four screenshot sizes prove responsiveness.

## Content direction is not always UI direction

Do not blindly mirror every icon or every input value. Search, calendar, delete, and logos normally retain their orientation. Back/forward and directional chevrons follow their actual function. Email addresses, paths, invoice IDs, and many technical values may need explicit LTR/isolation inside an RTL screen. Format dates/numbers/currencies according to the product's locale requirements; do not invent a universal Arabic numeral policy.

Use `bdi`, `dir="auto"`, or explicit direction where the content requires it. Test real mixed strings with punctuation and long values. Table numeric alignment should aid comparison rather than reversing every column mechanically.

## Time display

Display all user-facing times in the `Asia/Riyadh` time zone. Use a 12-hour clock with lowercase `am`/`pm`; the required format is `YYYY-MM-DD h:mm am`, for example `2026-09-20 11:41 am`. Convert timestamps for display rather than changing stored source values. Preserve the original timestamp and time-zone data when the product needs traceability, exports, or audit history.

## Modal footer proposal

The approved decision is language-aware ordering. A concrete proposed convention is primary at logical inline-end: right in LTR and left in RTL, with secondary adjacent toward inline-start. Validate the actual DOM/focus order and translated labels before freezing this as an implementation convention.

## Validation

Test actual desktop/tablet/mobile compositions in both languages, long text, zoom/reflow, keyboard navigation, and all relevant states. A screenshot or setting `dir="rtl"` alone is not proof of correct behavior. Keep unknowns recorded as NOT TESTED.
