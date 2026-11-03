# Tax Preparer

A Claude plugin for CPAs, enrolled agents, and tax preparers. It speeds up federal tax research, client communication, and tax-season workflows, with current-year figures and citations to primary authority.

## Commands

| Command | What it does |
|---|---|
| `/tax-research <question>` | Short research memo with conclusion, analysis, confidence, and citations |
| `/client-checklist <client situation>` | Tailored document request list, including new-law items and due diligence questions |
| `/client-letter <purpose>` | Plain-English client letter or email |
| `/notice-response <notice type>` | Explains an IRS notice, lays out options and deadlines, and drafts a response |
| `/year-end-planning <client profile>` | Prioritized planning opportunities with deadlines and watch-outs |
| `/engagement-letter <service>` | Draft engagement letter, or fills your firm's own template |

**Skills** (Claude uses these automatically)

- **federal-tax-figures** - verified tax year 2026 figures (brackets, standard deduction, retirement, HSA, estate and gift, Social Security wage base), 2025 One Big Beautiful Bill Act provisions, and a deadline calendar. Looks up official IRS releases for any year not on file.
- **tax-practice-standards** - Circular 230, preparer penalties, §7216 confidentiality, data security, refundable-credit due diligence, and client writing.

## Install

**Claude app (web or desktop):** Customize → Plugins → Add → Add marketplace → Add from a repository → `LiamBayerSr/my-claude-plugins`, then add Tax Preparer. Requires a paid Claude plan.

**Claude Code:**

```
/plugin marketplace add LiamBayerSr/my-claude-plugins
/plugin install tax-preparer@my-claude-plugins
```

## Examples

```
/tax-research Can a 2026 Roth conversion push a 64-year-old into a higher IRMAA tier two years later?
/client-checklist married couple, both W-2, one gets tips, bought a new US-assembled car in 2026
/client-letter explain the new $6,000 senior deduction to retired clients
/notice-response CP2000 [attach redacted notice]
/year-end-planning age 66 retiree, $140k income, large IRA, gives to charity
```

## Privacy

Never share full SSNs, ITINs, account numbers, or birth dates with the plugin; it works from placeholders and redacted documents. Remember IRC §7216 consent requirements before sharing return information outside return preparation.

## Disclaimer

For use by tax professionals, who remain responsible for all advice and filings. Figures are verified as of the date noted in each reference file; confirm against current IRS guidance. Federal only.

## License

MIT
