# My Claude Plugins

Role-based Claude plugins that bring subject-matter expertise to everyday professional work.

## Add this marketplace

**Claude app (web or desktop):** Customize → Plugins → Add → Add marketplace → Add from a repository → `LiamBayerSr/my-claude-plugins`. Requires a paid Claude plan.

**Claude Code:**

```
/plugin marketplace add LiamBayerSr/my-claude-plugins
```

## Plugins

### California teachers (K-5)

Lesson plans, worksheets, rubrics, unit plans, differentiation, and family messages aligned to California standards. Each works with or without the teacher's curriculum (HMH or others) and school lesson plan template.

| Plugin | For | Install (Claude Code) |
|---|---|---|
| [ca-kindergarten-teacher](plugins/ca-kindergarten-teacher) | Kindergarten | `/plugin install ca-kindergarten-teacher@my-claude-plugins` |
| [ca-1st-grade-teacher](plugins/ca-1st-grade-teacher) | 1st grade | `/plugin install ca-1st-grade-teacher@my-claude-plugins` |
| [ca-2nd-grade-teacher](plugins/ca-2nd-grade-teacher) | 2nd grade | `/plugin install ca-2nd-grade-teacher@my-claude-plugins` |
| [ca-3rd-grade-teacher](plugins/ca-3rd-grade-teacher) | 3rd grade | `/plugin install ca-3rd-grade-teacher@my-claude-plugins` |
| [ca-4th-grade-teacher](plugins/ca-4th-grade-teacher) | 4th grade | `/plugin install ca-4th-grade-teacher@my-claude-plugins` |
| [ca-5th-grade-teacher](plugins/ca-5th-grade-teacher) | 5th grade | `/plugin install ca-5th-grade-teacher@my-claude-plugins` |

## For maintainers

The teacher plugins are generated from shared templates. Edit files in `tools/ca-teacher/` (templates, grade standards, and the grade table in `build.py`), then run:

```
python3 tools/ca-teacher/build.py
```

Bump `VERSION` in `build.py` when publishing a change, then validate with `claude plugin validate --strict plugins/<name>`.
