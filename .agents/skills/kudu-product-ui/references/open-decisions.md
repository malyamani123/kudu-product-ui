# Open decisions and known limitations

These are explicit gaps, not permission to silently replace user-approved material.

| ID | Item | Status / next action |
| --- | --- | --- |
| O01 | Draft muted text `#8A9099` | Known contrast risk on light surfaces; compute evidence and propose a readable role replacement |
| O02 | Quiet borders/soft input fills | Do not assume adequate essential control contrast; test and propose boundary treatment |
| O03 | Success/warning/error/info HEX values | Deferred in planning; not invented in the bundle |
| O04 | Destructive button foreground/background | Red Filled is approved; exact accessible red pair is not selected |
| O05 | Exact icon library | Simple Outline approved; compare candidates with actual typefaces before choosing |
| O06 | Font assets and provisioning | Baloo Bhaijaan 2 is required for English and Arabic; font files and the approved delivery path are absent |
| O07 | Approved logo/vector assets | Horizontal and vertical PNG variants are bundled; vector files and additional background variants are not supplied |
| O08 | Arabic size/line-height tuning | Draft roles need actual-font rendering; prevent clipped glyphs |
| O09 | Pressed surfaces, scrim, floating/modal shadows | Draft behavior approved; exact values unresolved |
| O10 | Small/Medium/Large modal widths | Hybrid sizing approved; exact widths unresolved |
| O11 | Breakpoints, control sizes, content widths | Preserved proposed values; validate before freezing |
| O12 | Accessibility version | User chose WCAG AA; WCAG 2.2 AA proposed for implementation |
| O13 | Modal footer exact order | Language-aware approved; inline-end primary is a proposed concrete mapping |
| O14 | Brand RGB/HEX discrepancies | Printed page 18 blue/grey representations differ; preserve HEX and request brand-owner resolution |
| O15 | Frontend framework and dependency stack | Not fixed by the design system; inspect each project |
| O16 | Core component implementation | Specifications only; no published `@kudu/ui` |
| O17 | Three product prototypes | Briefs only; not built or visually tested |
| O18 | Automated/live accessibility evidence | Token diagnostics are limited; browser/keyboard/screen-reader review still required |
| O19 | Package version/release status | `0.1.0-draft.1`; not production v1.0 |
| O20 | Distribution/brand permissions | Repository is public; no corporate licensing or approval is inferred |
| O21 | Secondary text on subtle surface | Measured 4.40:1 for `#667085` on `#F2F1ED`, below the 4.5:1 normal-text target; propose a role or surface adjustment before production |

Do not respond to these gaps by restarting the completed design interview. Resolve them with actual prototype evidence, accessible project input, and specific approval when a decision changes. Record recommendations as proposals, not new official KUDU rules.
