---
description: Build a tax-season document request checklist tailored to a client's situation
argument-hint: <client situation, e.g. married W-2 couple, new rental property, sold stock, two kids in daycare>
---

Build a document request checklist for a client whose situation is: $ARGUMENTS

Use the `federal-tax-figures` skill to include items tied to current-year rules (including 2025-2028 deductions such as tips, overtime, car loan interest, and the senior deduction where they might apply) and the `tax-practice-standards` skill for due diligence and data security.

Produce a client-facing checklist:
- Grouped by category (income, deductions and credits, life changes, health coverage, prior-year items, business or rental if relevant).
- Each item in plain English with the form name in parentheses ("Your W-2 from each employer (Form W-2)").
- "If this applies to you" items worded as questions, so the client can skip what doesn't apply.
- Due diligence questions for refundable credits and head of household status where relevant.
- A short note at the top: the deadline to send documents, and to upload through the firm's secure portal rather than email.

Then, separately, a short **preparer notes** section: items likely to need follow-up, and new-law items to ask about.
