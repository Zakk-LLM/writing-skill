# Writing Skill

<!-- skill-map -->
## Map

```text
a task arrives
 ├─ define structure (package structure, data, deployment shape, frontend directories)
 │    └─▶ zakk-architecture ──interface values──▶ web-ui
 │              └─ Must produce three documents: design language (web-ui) / architecture
 │                 (this skill) / workflow (zakk-workflow)
 ├─ one change (fix, feature, documentation, skill change)
 │    └─▶ zakk-maintain
 │          ├─ 1. Write the plan as a file ──approve──▶ another mind
 │          ├─ 2. Write a specification from the approved plan ──dispatch──▶ dispatch --engine omp | codex | opencode
 │          ├─ 3. Judge the diff ──▶ zakk-review; reviewer performs ablation, gates, and differential checks;
 │          │   then dispatch an uninformed cold reader
 │          └─ 4. Land and report ──▶ zakk-workflow (branch, commit, pull request, completion report)
 ├─ any Chinese ──▶ chinese-skill (cross-cutting: every skill reads it; reread after compaction,
 │                  restoration, or task switching)
 └─ any English prose ──▶ writing-skill (cross-cutting: README, docs, comments, commit, PR, issue)
```
<!-- /skill-map -->

English | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

Writing Skill gives coding agents executable rules for concise, evidence-based English and Markdown.

It covers README files, task-based documentation, code comments, commit messages, pull requests, and issues. `writing_lint.py` reports formulaic vocabulary and structures without treating them as evidence of authorship.

## Requirements

- Python 3.11 or later for the linter and repository checker.
- An agent that discovers skills from a directory containing `SKILL.md`.

## Install

Set `AGENT_SKILLS_DIR` to your agent's skill directory, then clone the repository:

```bash
export AGENT_SKILLS_DIR=/path/to/agent/skills
git clone https://github.com/Zakk-LLM/writing-skill.git "$AGENT_SKILLS_DIR/writing-skill"
```

Confirm that the agent can read the skill:

```bash
test -f "$AGENT_SKILLS_DIR/writing-skill/SKILL.md"
```

The command exits with status 0 when `SKILL.md` is present.

## Use the skill

Agents should read [SKILL.md](SKILL.md) before writing or reviewing English prose. Chinese text belongs to `chinese-skill`; interface copy belongs to `web-ui`; submission procedures belong to `zakk-workflow`.

Run the linter on files or directories:

```bash
python3 scripts/writing_lint.py README.md references/
```

Each finding includes a path, line number, severity, rule identifier, revision instruction, and sample. The default command exits with status 1 for non-advisory findings. Advisory findings print without failing the command.

Make advisory findings fail when a repository requires a strict gate:

```bash
python3 scripts/writing_lint.py --fail-level advisory README.md
```

The linter masks fenced code, inline code, URLs, and Markdown links before applying prose rules. It does not rewrite text or identify its author.

## Apply the references

- [Vocabulary](references/vocabulary.md) lists common generated-prose tells, filler, jargon, and concrete revisions.
- [Sentences](references/sentences.md) covers information order, sentence scope, voice, instructions, rhetorical templates, and visual emphasis.
- [README structure](references/readme.md) defines the opening task and minimum sections.
- [Documentation types](references/docs.md) separates tutorials, how-to guides, reference material, explanations, and FAQ entries.
- [Code comments](references/comments.md) separates public contracts from internal rationale and redundant narration.
- [Commit, PR, and issue text](references/commit-pr-issue.md) defines evidence and structure for repository communication.

The [examples](examples) pair generated-style drafts with direct revisions for a README, PR description, and issue.

## Verify the repository

From the repository root, run:

```bash
python3 scripts/check_repository.py
```

The checker validates required files, frontmatter, line limits, source sections, local links, vocabulary data, self-linting, and the before-and-after controls. It prints `All repository checks passed.` and exits with status 0 on success.

## Contribute

Keep each rule executable: state how to recognize the problem and what to write instead. Add a source URL to the affected reference. Run the repository checker before committing.

## License

Writing Skill is available under the [MIT License](LICENSE).
