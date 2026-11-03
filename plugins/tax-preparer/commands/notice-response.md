---
description: Analyze an IRS notice and draft a response plan and letter
argument-hint: <notice type, e.g. CP2000> + paste or attach the redacted notice
---

Help respond to this IRS notice: $ARGUMENTS

Use the `tax-practice-standards` skill. Ask the practitioner to redact SSNs and account numbers if they appear in what was shared.

If no notice text or image was provided, ask for it (redacted), plus the client's position.

Return:
1. **What the notice is** - notice type, what the IRS is proposing or asking, and the tax year.
2. **Deadline** - the response date shown on the notice, and what happens if it's missed (for example, a statutory notice of deficiency). If the date isn't visible, say so.
3. **Options** - agree, partially agree, or disagree, with what each requires.
4. **Documents needed** - specific records to support the response.
5. **Draft response letter** - addressed per the notice's instructions, referencing the notice number and tax year, using placeholders for identifying information. Factual, concise, with an enclosure list.
6. **Representation note** - if the practitioner isn't already authorized, remind them a Form 2848 (or Form 8821 for information only) may be needed.

Flag for escalation anything suggesting fraud, multiple unfiled years, or a matter heading to Tax Court.
