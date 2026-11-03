#!/usr/bin/env python3
"""Generate the California K-5 teacher plugins from shared templates.

Usage (from the repo root):  python3 tools/ca-teacher/build.py

Edit templates/ for anything shared across grades, grades/<g>/references/ for a
grade's standards, and the GRADES table below for grade-specific guidance. Then
re-run this script. Bump VERSION when you publish a change.
"""
import json
import shutil
from pathlib import Path

VERSION = "0.4.0"
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
TEMPLATES = HERE / "templates"

K2_SCREENING = (
    "- California requires universal screening of K-2 students for risk of reading difficulties, "
    "including dyslexia, starting in the 2025-26 school year. Follow the district's screener and "
    "referral process."
)

GRADES = {
    "K": dict(
        slug="ca-kindergarten-teacher",
        display="California Kindergarten Teacher",
        adj="kindergarten",
        noun="kindergartner",
        noun_pl="kindergartners",
        label="kindergarten",
        grade_std_label="kindergarten",
        std="ca-kindergarten-standards",
        teach="kindergarten-teaching",
        ages="5- and 6-year-olds",
        age_self="a 5-year-old (use pictures and read it aloud)",
        minutes=30,
        example_code="K.CC.4",
        code_examples="K.CC.4 or RF.K.2",
        math_domains="Counting & Cardinality, Operations & Algebraic Thinking, Number & Operations in Base Ten, Measurement & Data, Geometry",
        hss_theme="Learning and Working Now and Long Ago",
        test_rule="Kindergarten has no state testing. Favor observation, conversation, and hands-on checks over paper assessments.",
        who="""- Ages 5-6. Direct instruction works in short bursts of about 5-10 minutes; alternate with movement, songs, and hands-on centers.
- Most are learning to read: concepts of print, letter names and sounds, rhyming, blending and segmenting sounds. Many are not yet reading independently.
- Learning through play and talk is central. Oral language, routines, and social-emotional skills (sharing, turn-taking, naming feelings) are part of every lesson.
- Thinking is concrete: counting real objects, building, sorting, acting things out.
- Fine motor skills are still developing; cutting, tracing, and pencil grip are active work.""",
        materials="""- Students can't read most directions: write directions for the teacher to read aloud and add a simple picture icon for each task (crayon, scissors, pencil).
- Default 3-6 items. Large print, big spaces, one task per section.
- Prefer circling, coloring, matching, tracing, and cut-and-paste over writing. Tracing lines and primary-ruled lines for any writing.
- Use pictures of familiar objects; avoid clutter and decorative clip art that distracts.""",
        math_item="use real-world pictures to count, compare, or show addition and subtraction within 10; include one \"show me with a drawing\" item.",
        reading_item="focus on letters, sounds, rhyming, and a few high-frequency words; use pictures for every word students must read.",
        reading_assess=K2_SCREENING
        + "\n- There is no state academic testing in kindergarten. Districts often use kindergarten readiness or early literacy assessments; follow the teacher's district tools."
        + "\n- For struggling early readers, emphasize phonological awareness, letter-sound knowledge, and daily small-group practice.",
        examples=[
            "/lesson-plan K.CC.4 counting objects to 10, 30 min",
            "/lesson-plan HMH reading week 6 [attach page photos and your template]",
            "/worksheet beginning sounds with pictures",
        ],
    ),
    "1": dict(
        slug="ca-1st-grade-teacher",
        display="California 1st Grade Teacher",
        adj="1st-grade",
        noun="1st grader",
        noun_pl="1st graders",
        label="1st grade",
        grade_std_label="grade 1",
        std="ca-grade1-standards",
        teach="first-grade-teaching",
        ages="6- and 7-year-olds",
        age_self="a 6-year-old (use icons and keep words simple)",
        minutes=40,
        example_code="1.OA.6",
        code_examples="1.OA.6 or RF.1.3",
        math_domains="Operations & Algebraic Thinking, Number & Operations in Base Ten, Measurement & Data, Geometry",
        hss_theme="A Child's Place in Time and Space",
        test_rule="Grade 1 has no state testing. Favor classroom formative assessment over test-prep framing.",
        who="""- Ages 6-7. Direct instruction works in chunks of about 10 minutes; plan movement and a change of activity after that.
- The big year for learning to decode: short and long vowels, digraphs, blends, final -e, and building fluency with decodable text.
- Concrete before abstract: counters, ten-frames, number lines, and connecting cubes before symbols.
- Eager to please and to show what they know; respond well to routines, clear modeling, and specific praise.
- Handwriting and stamina for writing are still growing.""",
        materials="""- Short, simple directions with a picture icon; the teacher may read them aloud.
- Default 5-8 items. Large print, primary-ruled writing lines, plenty of white space.
- Use decodable words that match phonics taught so far, plus common high-frequency words.
- Mix response types: circling, matching, drawing, short written answers.""",
        math_item="include at least one picture-supported word problem and one \"show your thinking\" item with room to draw.",
        reading_item="use decodable words that match the phonics pattern; keep any passage to a few short sentences.",
        reading_assess=K2_SCREENING
        + "\n- There is no state academic testing in grade 1. Districts often use benchmark reading assessments; follow the teacher's tools."
        + "\n- For struggling readers, emphasize explicit phonics, blending, decodable text, and repeated reading in small groups.",
        examples=[
            "/lesson-plan 1.OA.6 adding within 20 using make-a-ten, 40 min",
            "/lesson-plan HMH math Module 2 Lesson 4 [attach page photos and your template]",
            "/worksheet short a and short i words",
        ],
    ),
    "2": dict(
        slug="ca-2nd-grade-teacher",
        display="California 2nd Grade Teacher",
        adj="2nd-grade",
        noun="2nd grader",
        noun_pl="2nd graders",
        label="2nd grade",
        grade_std_label="grade 2",
        std="ca-grade2-standards",
        teach="second-grade-teaching",
        ages="7- and 8-year-olds",
        age_self="a 7-year-old",
        minutes=45,
        example_code="2.NBT.5",
        code_examples="2.NBT.5 or RL.2.3",
        math_domains="Operations & Algebraic Thinking, Number & Operations in Base Ten, Measurement & Data, Geometry",
        hss_theme="People Who Make a Difference",
        test_rule="Grade 2 is not a CAASPP testing year (testing begins in grade 3), so favor classroom formative assessment over test-prep framing.",
        who="""- Ages 7-8. Attention for direct instruction is roughly 10-15 minutes; plan for movement and a change of activity after that.
- Moving from learning to read toward reading to learn. Decoding of multisyllable words, vowel teams, and fluency are still active work.
- Concrete before abstract: manipulatives (base-ten blocks, number lines, coins) before symbols.
- Strong sense of fairness and rules; respond well to routines, choice within limits, and specific praise.
- Fine motor skills vary widely.""",
        materials="""- One-sentence, kid-friendly directions per section that most students can read on their own.
- Default 8-10 items. Large writing lines and uncluttered layouts.
- Use decodable, grade-appropriate words; keep passages short.
- Leave room for drawings and showing work.""",
        math_item="include at least one word problem and one \"explain your thinking\" item; leave room for drawings.",
        reading_item="use decodable, grade-appropriate words; keep passages short.",
        reading_assess=K2_SCREENING
        + "\n- Grade 2 has no state academic testing; CAASPP begins in grade 3."
        + "\n- For struggling readers, emphasize explicit phonics (vowel teams, multisyllable words), decodable text, and fluency practice.",
        examples=[
            "/lesson-plan 2.NBT.5 adding within 100 using place value, 50 min",
            "/lesson-plan HMH math Module 3 Lesson 2 [attach page photos and your template]",
            "/worksheet telling time to the nearest five minutes",
        ],
    ),
    "3": dict(
        slug="ca-3rd-grade-teacher",
        display="California 3rd Grade Teacher",
        adj="3rd-grade",
        noun="3rd grader",
        noun_pl="3rd graders",
        label="3rd grade",
        grade_std_label="grade 3",
        std="ca-grade3-standards",
        teach="third-grade-teaching",
        ages="8- and 9-year-olds",
        age_self="an 8-year-old",
        minutes=50,
        example_code="3.OA.7",
        code_examples="3.OA.7 or RI.3.2",
        math_domains="Operations & Algebraic Thinking, Number & Operations in Base Ten, Number & Operations - Fractions, Measurement & Data, Geometry",
        hss_theme="Continuity and Change",
        test_rule="Grade 3 is the first CAASPP year (ELA and math, in spring). Build real understanding first; use test-like item types only as occasional practice, not the default.",
        who="""- Ages 8-9. Direct instruction of about 15 minutes, then active practice.
- The shift to reading to learn: longer chapter books, informational text in science and social studies, and building stamina.
- Multiplication, division, and fractions are new and big. Use arrays, equal groups, area models, and fraction strips before abstract procedures.
- Growing independence and peer focus; partner and small-group work becomes more productive.
- Ready for multi-paragraph writing with support.""",
        materials="""- Short directions students can read independently.
- Default 8-12 items. Clean layout with room to show work.
- Include at least one item asking students to explain or justify.
- Passages can be longer (a page or so) with text features.""",
        math_item="include at least two word problems, one \"explain your thinking\" item, and room for drawings or models.",
        reading_item="use grade-level text; include at least one question that requires citing details from the text.",
        reading_assess="""- Grade 3 is the first year of CAASPP Smarter Balanced testing in ELA and math, typically in spring. Teachers may want occasional practice with similar item types (multi-select, short constructed response), but strong instruction is the best preparation.
- Students who still struggle to decode in grade 3 need explicit, systematic phonics and fluency intervention, not just more comprehension practice. Universal K-2 screening data may be available to the teacher.""",
        examples=[
            "/lesson-plan 3.OA.7 multiplying with arrays, 50 min",
            "/lesson-plan HMH reading Module 4 week 2 [attach page photos and your template]",
            "/worksheet unit fractions on a number line",
        ],
    ),
    "4": dict(
        slug="ca-4th-grade-teacher",
        display="California 4th Grade Teacher",
        adj="4th-grade",
        noun="4th grader",
        noun_pl="4th graders",
        label="4th grade",
        grade_std_label="grade 4",
        std="ca-grade4-standards",
        teach="fourth-grade-teaching",
        ages="9- and 10-year-olds",
        age_self="a 9-year-old",
        minutes=50,
        example_code="4.NF.1",
        code_examples="4.NF.1 or W.4.1",
        math_domains="Operations & Algebraic Thinking, Number & Operations in Base Ten, Number & Operations - Fractions, Measurement & Data, Geometry",
        hss_theme="California: A Changing State",
        test_rule="Grade 4 includes CAASPP testing in ELA and math. Build real understanding first; use test-like item types only as occasional practice.",
        who="""- Ages 9-10. Direct instruction of about 15-20 minutes, then extended practice and discussion.
- Reading to learn across subjects; increasingly complex informational and literary texts.
- Multi-digit operations, equivalent fractions, and decimals. Models still matter, but students can connect them to written methods.
- Strong interest in fairness, debate, and peer opinion; good age for structured argument and collaborative projects.
- Writing grows to organized multi-paragraph pieces with evidence.""",
        materials="""- Directions students read on their own; multi-step tasks are fine if each step is clear.
- Default 10-15 items. Layout can be denser but stays clean.
- Include items requiring written explanation and evidence.
- Passages can be one to two pages, with text features and visuals.""",
        math_item="include multi-step word problems, at least one \"explain your reasoning\" item, and space for models or work.",
        reading_item="use grade-level text; include questions that require evidence from the text and at least one short written response.",
        reading_assess="""- Grade 4 includes CAASPP Smarter Balanced testing in ELA and math, typically in spring. Occasional practice with similar item types is fine; strong instruction is the best preparation.
- Students who still struggle with decoding or fluency need targeted intervention (multisyllable word strategies, fluency practice) alongside access to grade-level content through read-alouds and discussion.""",
        examples=[
            "/lesson-plan 4.NF.1 equivalent fractions with area models, 50 min",
            "/lesson-plan HMH math Module 7 Lesson 3 [attach page photos and your template]",
            "/unit-plan California Gold Rush, 3 weeks",
        ],
    ),
    "5": dict(
        slug="ca-5th-grade-teacher",
        display="California 5th Grade Teacher",
        adj="5th-grade",
        noun="5th grader",
        noun_pl="5th graders",
        label="5th grade",
        grade_std_label="grade 5",
        std="ca-grade5-standards",
        teach="fifth-grade-teaching",
        ages="10- and 11-year-olds",
        age_self="a 10-year-old",
        minutes=50,
        example_code="5.NF.1",
        code_examples="5.NF.1 or RI.5.8",
        math_domains="Operations & Algebraic Thinking, Number & Operations in Base Ten, Number & Operations - Fractions, Measurement & Data, Geometry",
        hss_theme="United States History and Geography: Making a New Nation",
        test_rule="Grade 5 includes CAASPP testing in ELA and math plus the California Science Test (CAST). Build real understanding first; use test-like items only as occasional practice.",
        who="""- Ages 10-11. Direct instruction of about 15-20 minutes, then extended practice, discussion, and projects.
- Ready for complex texts, multiple sources, and analyzing how authors support claims.
- Fractions with unlike denominators, decimal operations, and volume; increasingly abstract reasoning, still grounded in models.
- Preparing for middle school: more independence, organization skills, and ownership of learning. Peer relationships matter a lot.
- Writing includes researched, multi-paragraph opinion and informative pieces.""",
        materials="""- Directions students read on their own; multi-step tasks and short projects are fine.
- Default 10-15 items. Clean, organized layout.
- Include items requiring written explanation, evidence, or comparison across sources.
- Passages can be longer and paired (two texts on one topic).""",
        math_item="include multi-step word problems, at least one \"explain or justify\" item, and space for models or work.",
        reading_item="use grade-level text, sometimes two paired texts; include evidence-based questions and a short written response.",
        reading_assess="""- Grade 5 includes CAASPP Smarter Balanced testing in ELA and math and the California Science Test (CAST), typically in spring. Occasional practice with similar item types is fine; strong instruction is the best preparation.
- Students who still struggle with decoding or fluency need targeted intervention alongside access to grade-level content through read-alouds, audio, and discussion.""",
        examples=[
            "/lesson-plan 5.NF.1 adding fractions with unlike denominators, 50 min",
            "/lesson-plan HMH reading Module 3 week 1 [attach page photos and your template]",
            "/unit-plan causes of the American Revolution, 4 weeks",
        ],
    ),
}


def fill(text: str, g: dict) -> str:
    tokens = {
        "SLUG": g["slug"], "DISPLAY": g["display"], "ADJ": g["adj"], "NOUN": g["noun"],
        "NOUN_PL": g["noun_pl"], "LABEL": g["label"], "GRADE_STD_LABEL": g["grade_std_label"],
        "STD": g["std"], "TEACH": g["teach"], "AGES": g["ages"], "AGE_SELF": g["age_self"],
        "MINUTES": str(g["minutes"]), "EXAMPLE_CODE": g["example_code"],
        "CODE_EXAMPLES": g["code_examples"], "MATH_DOMAINS": g["math_domains"],
        "HSS_THEME": g["hss_theme"], "TEST_RULE": g["test_rule"], "WHO": g["who"],
        "MATERIALS": g["materials"], "MATH_ITEM": g["math_item"],
        "READING_ITEM": g["reading_item"], "READING_ASSESS": g["reading_assess"],
        "EXAMPLES": "\n".join(g["examples"]),
    }
    for key, value in tokens.items():
        text = text.replace("{{" + key + "}}", value)
    assert "{{" not in text, f"unfilled token in output for {g['slug']}: " + text[text.index("{{"):][:40]
    return text


def build(code: str, g: dict) -> None:
    out = REPO / "plugins" / g["slug"]
    if out.exists():
        shutil.rmtree(out)
    (out / ".claude-plugin").mkdir(parents=True)
    manifest = {
        "name": g["slug"],
        "displayName": g["display"],
        "version": VERSION,
        "description": (
            f"Lesson plans, worksheets, rubrics, differentiation, and family communication for California "
            f"{g['adj']} teachers, aligned to California standards. Works with or without your curriculum "
            f"(HMH or others) and your school's lesson plan template."
        ),
        "author": {"name": "Liam Bayer"},
        "homepage": "https://github.com/LiamBayerSr/my-claude-plugins",
        "repository": "https://github.com/LiamBayerSr/my-claude-plugins",
        "license": "MIT",
        "keywords": ["education", "teacher", g["adj"], "california", "lesson-planning", "elementary"],
    }
    (out / ".claude-plugin" / "plugin.json").write_text(json.dumps(manifest, indent=2) + "\n")

    (out / "commands").mkdir()
    for cmd in sorted((TEMPLATES / "commands").glob("*.md")):
        (out / "commands" / cmd.name).write_text(fill(cmd.read_text(), g))

    teach_dir = out / "skills" / g["teach"]
    teach_dir.mkdir(parents=True)
    (teach_dir / "SKILL.md").write_text(fill((TEMPLATES / "teaching-skill.md").read_text(), g))

    std_dir = out / "skills" / g["std"]
    refs = std_dir / "references"
    refs.mkdir(parents=True)
    (std_dir / "SKILL.md").write_text(fill((TEMPLATES / "standards-skill.md").read_text(), g))
    for ref in sorted((HERE / "grades" / code / "references").glob("*.md")):
        shutil.copy(ref, refs / ref.name)
    shutil.copy(HERE / "shared" / "eld.md", refs / "eld.md")

    (out / "README.md").write_text(fill((TEMPLATES / "README.md").read_text(), g))
    print(f"built {g['slug']}")


def write_marketplace() -> None:
    path = REPO / ".claude-plugin" / "marketplace.json"
    data = json.loads(path.read_text())
    others = [p for p in data["plugins"] if not p["name"].startswith("ca-") or not p["name"].endswith("-teacher")]
    teachers = [
        {
            "name": g["slug"],
            "source": f"./plugins/{g['slug']}",
            "description": f"Planning, materials, differentiation, and family communication for California {g['adj']} teachers, aligned to state standards.",
        }
        for g in GRADES.values()
    ]
    data["plugins"] = teachers + others
    path.write_text(json.dumps(data, indent=2) + "\n")


if __name__ == "__main__":
    for code, grade in GRADES.items():
        build(code, grade)
    write_marketplace()
