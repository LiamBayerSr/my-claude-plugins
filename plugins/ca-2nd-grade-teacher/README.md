# California 2nd Grade Teacher

A Claude plugin for California 2nd-grade teachers. It drafts lesson plans, worksheets, rubrics, unit plans, differentiated activities, and family messages, aligned to California state standards and built around how 7- and 8-year-olds learn.

## What's inside

**Commands**

| Command | What it does |
|---|---|
| `/plan-from-curriculum <lesson or week>` | Turns HMH (or other adopted curriculum) pages into a ready-to-teach lesson or week plan |
| `/lesson-plan <topic or standard>` | Standards-aligned lesson with ELD supports and differentiation |
| `/worksheet <skill or standard>` | Printable practice in three levels, with answer keys |
| `/rubric <assignment>` | Four-level rubric plus a kid-friendly "I can" checklist |
| `/differentiate <lesson>` | Adapts an activity for English learners, struggling readers, and advanced students |
| `/unit-plan <topic>` | Multi-week unit map with assessment and family letter |
| `/parent-email <purpose>` | Warm family message, with optional translation |

**Skills** (Claude uses these automatically)

- **ca-grade2-standards** - paraphrased California grade 2 standards for Math, ELA, CA NGSS science, History-Social Science, and ELD, by code
- **second-grade-teaching** - child development, lesson design, English learner support, student privacy, and family communication

## Install

In Claude Code:

```
/plugin marketplace add LiamBayerSr/my-claude-plugins
/plugin install ca-2nd-grade-teacher@my-claude-plugins
```

## Examples

```
/lesson-plan 2.NBT.5 adding within 100 using place value, 50 min
/plan-from-curriculum HMH Into Math Module 3 Lesson 2 [attach photos]
/worksheet telling time to the nearest five minutes
/differentiate [paste a reading activity]
/parent-email great progress in reading fluency, Spanish
```

## Privacy

The plugin is designed so teachers never need to share student names or records. It uses placeholders like "[Student]" and describes needs instead of children.

## Disclaimer

Standards are paraphrased summaries for planning. For official wording, see the California Department of Education: https://www.cde.ca.gov/be/st/ss/. Always follow your district's curriculum, policies, and each student's IEP or 504 plan.

## License

MIT
