# California 4th Grade Teacher

A Claude plugin for California 4th-grade teachers. It drafts lesson plans, worksheets, rubrics, unit plans, differentiated activities, and family messages, aligned to California state standards and built around how 9- and 10-year-olds learn.

## Works with or without your materials

Every command works on its own. Add more and the output gets more specific:

- **Your curriculum** (optional) - attach photos or a PDF of the pages, paste the text, or just describe the lesson. Works with HMH or any program. Without it, plans are built from the standards.
- **Your template** (optional) - attach your school's lesson plan template and the plan comes back in that exact layout, as a Word file if your template is one. Without it, a clean default format is used.

Tip: keep your template in a Claude Project so it's there every time.

## Commands

| Command | What it does |
|---|---|
| `/lesson-plan <topic, standard, or lesson>` | A lesson or a whole week, with timing, ELD supports, and differentiation |
| `/worksheet <skill or standard>` | Printable practice in three levels, with answer keys |
| `/rubric <assignment>` | Four-level rubric plus a kid-friendly "I can" checklist |
| `/differentiate <lesson>` | Adapts an activity for English learners, struggling readers, and advanced students |
| `/unit-plan <topic>` | Multi-week unit map with assessment and family letter |
| `/parent-email <purpose>` | Warm family message, with optional translation |

**Skills** (Claude uses these automatically)

- **ca-grade4-standards** - paraphrased California grade 4 standards for Math, ELA, CA NGSS science, History-Social Science, and ELD, by code
- **fourth-grade-teaching** - child development, lesson design, working from adopted curriculum, using your template, English learner support, student privacy, and family communication

## Install

**Claude app (web or desktop):** Customize → Plugins → Add → Add marketplace → Add from a repository → `LiamBayerSr/my-claude-plugins`, then add California 4th Grade Teacher. Requires a paid Claude plan.

**Claude Code:**

```
/plugin marketplace add LiamBayerSr/my-claude-plugins
/plugin install ca-4th-grade-teacher@my-claude-plugins
```

## Examples

```
/lesson-plan 4.NF.1 equivalent fractions with area models, 50 min
/lesson-plan HMH math Module 7 Lesson 3 [attach page photos and your template]
/unit-plan California Gold Rush, 3 weeks
/differentiate [paste an activity]
/parent-email great progress in reading, Spanish
```

## Privacy

The plugin is designed so teachers never need to share student names or records. It uses placeholders like "[Student]" and describes needs instead of children. Curriculum pages you attach are used only in your conversation; they are never part of this plugin.

## Disclaimer

Standards are paraphrased summaries for planning. For official wording, see the California Department of Education: https://www.cde.ca.gov/be/st/ss/. Always follow your district's curriculum, policies, and each student's IEP or 504 plan.

## License

MIT
