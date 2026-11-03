---
description: Generate a year-end tax planning checklist of opportunities for a client profile
argument-hint: <client profile, e.g. age 66 retiree with IRA and taxable brokerage, $140k income>
---

Generate year-end planning ideas for: $ARGUMENTS

Use the `federal-tax-figures` skill (current-year limits and the 2025-2028 deductions) and the `tax-practice-standards` skill. This is for the practitioner to evaluate, not advice sent directly to the client.

Return a prioritized list. For each opportunity:
- **What** - the move (for example, bunching charitable gifts, Roth conversion, maximizing HSA, harvesting losses, timing income to stay under a phase-out).
- **Why it may fit** - tied to the profile's facts and the specific threshold or limit, with the tax year.
- **Deadline** - December 31, the filing deadline, or another date.
- **Watch-outs** - phase-outs, wash-sale rules, IRMAA or ACA premium effects, state tax, and anything that needs more facts.

Group into "Act before December 31" and "Can wait until filing." End with the facts you'd want to confirm before recommending any of these.
