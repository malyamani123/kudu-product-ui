# Part 7: Governance and daily workflow

## Contents

1. Authority and changes
2. Daily product workflow
3. Releases and migration

## 1. Authority and changes

Maintain one source of truth. Brand rules come from the supplied brand guide; product decisions come from D01-D45 and X01; project composition follows the actual task. A project may compose components but must not silently redesign their language.

The request owner is the proposed initial maintainer, not a claim of formally delegated corporate authority. Seek the appropriate brand owner for changes to official brand assets. Keep component extensions lightweight rather than requiring a committee for ordinary layout work.

Before adding a component, check for an existing one, then compatible composition. Keep truly specialized product capabilities local. Promote a component when reusable need is demonstrated, not because a new card style looks attractive.

Use `assets/templates/component-proposal.md` for a missing pattern or exception. Explain the problem, existing options, smallest extension, reuse, responsive/RTL/accessibility impact, and approval. No silent new colors, fonts, icon family, button variant, or colored side strips.

## 2. Daily product workflow

1. Inspect requirements, accessible repository, current behavior, stack, components, tests, assets, and actual users.
2. Classify the product and identify the task, essential information, primary action, navigation need, and data density.
3. Propose a representative screen using existing foundations and relevant patterns. Expose genuine gaps before coding.
4. Implement only the approved scope, preserving business behavior, access controls, contracts, and unrelated changes.
5. Review actual screens and run available tests. Report what is implemented, tested, unresolved, or blocked.
6. Continue other screens after the representative design is accepted.

Do not repeat the completed 45-question interview. A design-system choice should not become a new preference question in every project. Ask only for product-specific unknowns that affect the work.

For AI-assisted review, distinguish exact evidence from interpretation. Check tokens, typography, controls, icons, radius, states, responsive behavior, bidirectionality, accessibility, and prohibited motifs. Do not claim tests that were not run.

## 3. Releases and migration

Keep the release status honest. The current bundle is `0.1.0-draft.1`; no production package or validated v1.0 is implied. Use a change log and decision register. After establishing public package APIs, use patch for compatible fixes, minor for compatible additions, and major for incompatible API changes; brand/process changes also require documented impact review.

Record what changed, why, affected products, compatibility, adoption instructions, and evidence. Deprecate an existing public component before removing it. Do not assume a changed central file updates deployed products automatically. Each product must intentionally adopt a tested revision.

Migration is incremental: audit actual code, align fonts/tokens, controls, icons, radius and containers, then navigation/tables/page composition, while protecting functionality. Remove prohibited side strips. Do not rewrite a working application solely to change appearance.

Automated linting, visual regression, and package splitting are later enhancements, not prerequisites to this draft. A text search for CSS cannot establish complete visual compliance. Keep all scripts' claims within their tested scope.

Definition of done: reused language, justified composition, no prohibited patterns, correct relevant states, responsive layouts, RTL/LTR behavior, keyboard/focus/label behavior, tested contrast, documented limitations, and updated docs for any accepted change.
