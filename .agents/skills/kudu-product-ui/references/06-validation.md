# Part 6: Validation and prototyping

## Contents

1. Purpose and prototypes
2. Validation matrix
3. Evidence and acceptance

## 1. Purpose and prototypes

Test the design language before calling it v1.0. This repository contains prototype briefs, not rendered prototypes or a browser-tested component library.

| Pilot | Representative screen | What it tests |
| --- | --- | --- |
| Intranet | Existing home or content-discovery page, after actual source is available | Warmth, typography, editorial hierarchy, top/hybrid navigation, images and reading |
| Operational | Representative queue/list plus create/edit modal | Structured data, filters, row/bulk actions, inputs, feedback, density |
| Engineering | Project detail with files/versions and meaningful groups | Project context, document states, tabs/sections, complex detail composition |

Use synthetic, clearly labeled data for public examples. Do not publish production screenshots or records. An existing Intranet pilot requires access to its actual code or supplied screen; do not pretend the brand PDF is that implementation.

Put the three compositions beside each other. They must share language without sharing an identical layout. A repeated sidebar/four-KPIs/chart/table skeleton fails the flexibility test. A visual review remains a judgment, not a measurable guarantee of uniqueness.

## 2. Validation matrix

| Area | Required checks |
| --- | --- |
| Brand/surfaces | Quiet warm surfaces; restrained yellow; meaningful blue; approved assets |
| Typography | Actual Config Rounded/DIN Next Arabic; long English/Arabic text; figures, dates, currency; no clipping |
| Primary action | Outline primary remains identifiable beside neutral secondary; destructive hierarchy is intentional |
| Tables | Short/long lists, long names/IDs, large values, missing values, many/few columns, actual overflow |
| Forms | Short, medium, and long examples; related columns; errors; summary; preserved values |
| Dialogs | Small/medium/large content; capped height; mobile viewport; keyboard focus; dismissal/return |
| States | Loading, empty, filtered no-results, errors, access denied, disabled, success, long-running progress |
| Responsive | Desktop, tablet, mobile; small-width and zoom/reflow checks where applicable |
| RTL/LTR | Navigation, action order, icons, mixed identifiers/numbers, labels, tables, breadcrumbs |
| Accessibility | Text/non-text contrast, keyboard, focus, labels, programmatic states, status announcements |
| Motion | Calm transitions, stable layout, reduced-motion preference |
| X01 | No colored side strip, including pseudo-elements, inset shadows, alerts, and navigation |

Test controls with the actual licensed fonts. A system-font preview can test layout provisionally but cannot validate final KUDU typography. Evaluate candidate outline libraries alongside the fonts before approving one.

The token checker computes selected opaque sRGB color pairs and verifies variable references. It does not inspect a browser, evaluate screen-reader behavior, or certify WCAG conformance. `--strict` reports unresolved contrast risks as failure. Default diagnostic mode still prints warnings; absence of a nonzero exit in that mode does not mean accessibility passed.

## 3. Evidence and acceptance

Record each check as PASS, NEEDS REVISION, NOT TESTED, or NOT APPLICABLE. Attach the tested revision, environment, screen/state, viewport, locale, method, and outcome. Use `assets/templates/screen-review.md` and the screen brief rather than reporting an unsupported score.

Apply a brief recognition test: can the user understand location, essential information, and next action? Apply a removal test, but never remove information needed for use or accessibility. Check family consistency without relying solely on the logo.

Exact values may be refined through evidence; approved principles and variants cannot be silently changed. Keep current known issues in `open-decisions.md`. v1.0 requires actual core implementation, three validated pilots, licensed asset provisioning, approved resolved tokens, and documented responsive/RTL/accessibility evidence. Until then, use the draft version label.
