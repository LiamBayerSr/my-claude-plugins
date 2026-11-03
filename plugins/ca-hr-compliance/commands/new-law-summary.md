---
description: Summarize new California employment laws for a year, with an employer action checklist
argument-hint: [year, default the coming year] [headcount, industry]
---

Summarize new California employment laws for: $ARGUMENTS

Use `references/new-laws-2026-2027.md` and `references/pay-rates.md` in the `ca-employment-rules` skill. If the year asked about isn't covered there, or more than a few months have passed since the file's verification date, search official and reputable employer-side sources (leginfo.legislature.ca.gov, dir.ca.gov, calcivilrights.ca.gov) for laws signed since, and cite them.

Return:
1. **Top changes for this employer** - the 3-5 that matter most given their headcount and industry, in plain language.
2. **Full table** - bill, topic, effective date, who it applies to, action needed.
3. **Action checklist by date** - grouped "before January 1," "by mid-year," and "later," with owners left as blanks.
4. **Manager talking points** - a short paragraph HR can share with supervisors.

Skip laws that clearly don't apply to this employer's size or industry, and say so in one line.
