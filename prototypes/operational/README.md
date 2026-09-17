# Pilot B: Operational workspace

Status: NOT IMPLEMENTED. Candidate domain: Supply Chain requests or supplier administration. This pilot is not the blueprint for all KUDU products.

## Task

Find a record needing attention, review it, edit a small set of fields, and understand the outcome.

## Composition candidate

Light sidebar when justified; simple page header; visible search and Filters button; active-filter summary; structured table; meaningful row action plus overflow menu; restrained pagination. Optional bulk actions only when real bulk work exists.

## Required interactions

Search; apply and clear filters; sort; pagination; open a medium edit modal; cancel without data loss; validate missing fields; save feedback; recover from a failed request. Distinguish a destructive confirmation from ordinary saving.

## Test fixtures

Few/many rows, long names, missing values, large amounts where relevant, unknown totals, empty filtered results, errors, and loading. Use clearly fictional data. Define whether bulk selection covers visible rows or all filtered records before implementing it.

## Acceptance

Primary blue outline action remains more prominent than neutral filled secondary action. No hidden critical data on mobile; no accidental bulk actions; working keyboard and RTL navigation; no side strips; no decorative metrics. Record untested areas honestly.
