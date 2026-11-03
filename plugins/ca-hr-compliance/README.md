# California HR Compliance

A Claude plugin for HR professionals, office managers, and business owners with California employees. It drafts policies, reviews handbooks, summarizes new laws, and builds onboarding, leave, and termination checklists, using verified 2026-2027 pay rates and California's newest employment laws.

## Commands

| Command | What it does |
|---|---|
| `/policy-draft <topic>` | Plain-language policy, HR notes with legal citations, and a rollout checklist |
| `/handbook-review <handbook>` | Flags must-fix, should-update, and missing policies against current law |
| `/new-law-summary [year]` | New laws that matter for your size and industry, with a dated action checklist |
| `/onboarding-checklist <role>` | Required notices, forms, training, and deadlines for a new hire |
| `/leave-question <situation>` | Which leave laws apply, how much leave and pay, and HR's next steps |
| `/termination-checklist <situation>` | Risk check, final pay timing, required documents, and a meeting plan |

**Skills** (Claude uses these automatically)

- **ca-employment-rules** - minimum wage and exempt thresholds for 2026 and 2027, overtime, meal and rest breaks, final pay, leave laws, hiring and separation rules, training and notices, and new laws for 2026-2028
- **hr-practice** - staying within HR's role, when to call an employment attorney, employee privacy, documentation, and writing policies

## Install

**Claude app (web or desktop):** Customize → Plugins → Add → Add marketplace → Add from a repository → `LiamBayerSr/my-claude-plugins`, then add California HR Compliance. Requires a paid Claude plan.

**Claude Code:**

```
/plugin marketplace add LiamBayerSr/my-claude-plugins
/plugin install ca-hr-compliance@my-claude-plugins
```

## Examples

```
/new-law-summary 2027, 45 employees, restaurants in San Diego
/policy-draft bereavement leave including designated persons, 30 employees
/handbook-review [attach your handbook] 120 employees, Los Angeles and Sacramento
/leave-question employee pregnant, also caring for a parent, 18 employees, 3 years of service
/termination-checklist attendance termination after two written warnings, non-exempt
```

## Privacy

Use roles and placeholders instead of employee names. Never share Social Security numbers, medical details, or immigration documents with the plugin.

## Disclaimer

Not legal advice. Figures and laws are verified as of the date noted in each reference file; confirm current rules with official sources, and check city and county ordinances for each work location. Consult an employment attorney for terminations with legal risk, severance, layoffs, investigations, and agency or legal claims.

## License

MIT
