# Part 3: Product and page patterns

## Contents

1. Product classification
2. Product compositions
3. Reusable page patterns
4. Adaptation and review

## 1. Product classification

Start with the task, not a template. A product can combine content/communication, operations, data-heavy work, workflow, documents, engineering/projects, AI assistance, and administration. Do not treat departmental labels as fixed layouts: an Engineering tool can be data-heavy, and Finance can need a document or reading view.

Before designing, state the primary user, task, critical information, action, secondary information, expected density, navigation need, and small-screen implications. Do not repeat the brand interview. Ask only for missing product information that affects the work.

## 2. Product compositions

| Product | Main priority | Suitable candidate composition | Avoid by default |
| --- | --- | --- | --- |
| Intranet | Find, read, navigate, act | Top/hybrid navigation; announcements; editorial news; events; resources | Admin dashboard, four KPIs, every item in colored cards |
| Operational | Act on work needing attention | Useful queue/list; filters; status; actionable exceptions | Totals with no task value or large decorative banners |
| Data-heavy | Compare and inspect records | Wide structured table; search/filter; relevant summary; export when required | Hiding essential data to look minimal |
| Workflow | Understand state and next action | Current status, responsible role, blockers, next step, relevant history | Stepper without real stages |
| Engineering/project | Understand a project and its documents | Project summary; phase/owner; documents/versions; timeline or tabs when justified | Reusing a generic Finance dashboard unchanged |
| Document-heavy | Find and inspect the right document | Searchable list; metadata; preview; version/history when necessary | Mandatory thumbnails for every file |
| AI tool | Complete a task with assistance | Structured input/process/review/result, or conversation only when useful | Chat box, gradients, sparkle, or robot imagery simply because AI is present |
| Admin | Manage content/users/settings reliably | Light navigation, working area, forms/tables, clear permissions | Marketing hero, vanity metrics, ornamental welcome cards |

These are options, not fixed templates. Use approved photography only when content benefits from it. Do not fabricate metrics, project data, or live integration claims.

### Intranet

Give announcements and useful resources a clear hierarchy. News can have images without becoming a dashboard. Reading and discovery may justify more whitespace. Keep important links and updates easy to find. A top navigation is a candidate, not an automatic requirement.

### Operational and data-heavy

Show useful queues and exceptions, not just volume. A request awaiting review can be actionable; a total record count is useful only when it helps the user. Wide tables may be necessary; neither minimal cards nor responsive support permits dropping critical records or actions.

### Engineering/project and documents

A project-centered summary may expose phase, owner, milestone, and status. Show current document versions and relevant review context. Drawing or preview areas may use more space than forms. Specialized map, drawing, or version interactions can be product-specific while reusing the same controls and tokens.

### AI tools

AI is a capability, not a visual theme. Distinguish user inputs, processing state, results, evidence/source references when available, and recommended actions. Do not present generated outputs as already approved. Keep review controls near consequential actions. A conversation UI is appropriate only when the task benefits from iterative dialogue.

## 3. Reusable page patterns

| Page | Default anatomy | Adaptive rule |
| --- | --- | --- |
| Home | Most useful starting task or content | Operational, KPI, navigation home, or no home |
| Index/list | Simple header; search/filter when needed; records; relevant pagination | Table for structured comparison, list for content |
| Detail | Essential summary first; supporting groups after | Single page when small; tabs for large independent groups |
| Create/edit | Permanent labels, logical groups, clear actions | Modal for manageable tasks, dedicated page for complex work |
| Content/article | Title, relevant metadata, readable text column, related files | Do not stretch paragraphs edge-to-edge |
| Settings | Named sections, appropriate controls, explicit application behavior | Prefer headings/dividers to unnecessary cards |
| Search results | Query, real result count if known, filters, relevant context | Content list versus structured record table |
| Empty/first use | Clear reason and relevant next action | No illustration-heavy onboarding by default |
| Error | Human-readable problem and realistic recovery | Distinguish failed loading from no data |
| Access denied | Understandable permission state and valid next step | Never imply unavailable records do not exist merely by showing empty data |

Breadcrumbs are optional aids for hierarchy. A dashboard is optional. One primary action per local task group is preferred; a page can contain independent contexts without forcing every action to compete.

## 4. Adaptation and review

Use limited width for forms and reading, wider space for data and drawings, and section-specific widths for mixed pages. Use shared spacing tokens with comfortable/balanced/compact applications, not arbitrary new spacing scales. Balanced remains the default.

Responsive design may reorganize secondary panels, navigation, and columns. Preserve the main task and important information. Do not turn every table into mobile cards automatically.

The three-product test must demonstrate a content-led Intranet, an operational data workspace, and a project/document-led Engineering view. They should share fonts, controls, states, rounding, and spacing logic, but not identical screen structures.

Ask: Where am I? What matters? What can I do? What can be removed without losing understanding or functionality? Do not remove a necessary label, focus state, error explanation, or data column in the name of simplicity.
