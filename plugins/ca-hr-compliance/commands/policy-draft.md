---
description: Draft a California-compliant HR policy in plain language
argument-hint: <policy topic, e.g. bereavement leave, remote work expense reimbursement> [headcount, locations]
---

Draft an HR policy on: $ARGUMENTS

Use the `ca-employment-rules` skill for legal requirements and the `hr-practice` skill for drafting standards.

If headcount or work locations would change the requirements and weren't given, state your assumption at the top (default: 25-99 employees, California only, no local ordinances) and note what changes otherwise. If the user shared their handbook or a template, match its format and voice.

Return:
1. **The policy** (employee-facing): purpose, who's covered, the rule, how to request or report, documentation, pay, and who to contact. Plain language.
2. **HR notes** (not for employees): the legal requirements the policy satisfies, with citations and effective dates; choices the employer must make (for example, whether bereavement is paid; whether to limit designated persons to one per year); and local ordinance checks.
3. **Rollout checklist**: forms to update, managers to train, acknowledgments to collect, and payroll or HRIS settings.

Flag anything that should get an attorney's review before rollout.
