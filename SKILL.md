---
name: writing-skill
description: Apply concise, evidence-based English and Markdown writing rules to README files, documentation, comments, commit messages, pull requests, issues, release notes, and technical prose. Read this skill when writing, rewriting, polishing, or reviewing English. Route Chinese text to chinese-skill, interface copy to web-ui, and repository submission mechanics to zakk-workflow.
---

# English Writing Control

## Use this skill for English

Read this file before writing or reviewing English prose, Markdown, comments, commits, PRs, or issues.
Send Chinese text to `chinese-skill`, even when the surrounding repository uses English.
Send interface labels, errors, and other product copy to `web-ui`.
Send branch, commit, push, and submission procedures to `zakk-workflow`.
This skill controls the writing itself, not the repository workflow.

## Read the repository rules first

Read the repository instructions, style guide, templates, current documents, and nearby accepted examples.
Use their terminology, heading order, line limits, and required fields.
Do not create a second convention beside an established one.
If an old document contradicts the implementation, verify the implementation and update or remove the old text.

## Put evidence before prose

Verify every command, option, path, version, default, output, compatibility claim, and performance claim before publishing it.
Use source code, executable help, tests, or observed output as evidence.
Label an unverified statement and say what remains unverified; never turn an expectation into a fact.
Delete claims such as “faster” or “more reliable” when no measurement or behavior supports them.
Keep code literals, commands, identifiers, numbers, and quoted output exact.

## Choose the reader and document type

Name the reader, their goal, their starting knowledge, and the observable result before drafting.
Use one dominant [Diátaxis](references/docs.md) type per page: tutorial for learning, how-to for a task, reference for exact lookup, or explanation for concepts and tradeoffs.
Move material that serves another goal to a linked page.
Order sections by the reader's task, not by the software's internal modules.

## Write direct sentences

Lead with the result, failure, decision, or required action.
Put one action, result, reason, or constraint in each sentence.
Name the actor and object; replace vague pronouns and abstract nouns with concrete names.
Prefer active voice when the actor matters. Use passive voice when the actor is unknown or irrelevant.
Use imperative verbs for instructions and commit subjects.
Put a condition before the action it limits.
Delete introductions, transitions, and conclusions that add no fact or action.
See [sentence patterns](references/sentences.md).

## Control vocabulary

Treat these common tells as revision prompts: `delve`, `tapestry`, `pivotal`, `vibrant`, `leverage`, `robust`, `seamless`, `ecosystem`, `crucial`, and `enhance`.
Replace each one with the exact action, object, constraint, or measured effect.
Use a technical term only when it is established in the project or needed for precision.
Define a necessary unfamiliar term at first use.
Use one term for one concept; do not rotate synonyms for variety.
Never infer authorship from a word or lint finding.
See the [vocabulary table](references/vocabulary.md).

## Structure Markdown and README files

Use headings that name a reader task or subject. Keep heading levels sequential.
Use lists for parallel items and numbered steps only for ordered actions.
Use bold only when a reader must scan for a field or warning; do not bold each paragraph lead.
Do not decorate headings with Emoji or use em dashes as general punctuation.
Open a README with what the project is, installation, and the shortest successful use.
Keep badge walls, slogans, feature adjectives, architecture detail, and exhaustive reference below the first task or on linked pages.
Use the [README rules](references/readme.md).

## Organize docs by reader task

Keep one page focused on one tutorial, how-to, reference, or explanation goal.
For every command, state prerequisites and the working directory before the command.
State the observable result after the command when readers need it to verify success.
Write FAQ headings as searchable questions. Answer the question in the first sentence.
Keep options and API tables complete in reference pages, not in tutorials.
Use the [documentation rules](references/docs.md).

## Keep comments useful

Document public API contracts: behavior, inputs, results, errors, panics, safety constraints, and non-obvious limits.
For internal code, explain only a reason the code cannot express: an invariant, compatibility constraint, security boundary, workaround, or surprising order.
Delete comments that restate the next assignment, branch, call, or return.
Keep the summary to one sentence unless callers need more contract details.
Use the [comment rules](references/comments.md).

## Write commits, PRs, and issues

Write a short imperative commit subject. Use the body for rationale and user-visible effects, not a work diary.
For a PR, state the failure or need, impact, reason for the change, risk-relevant verification, and known limits.
State unverified areas explicitly. Do not claim that all tests pass unless the listed command was run.
For an issue, provide a scoped title, environment, minimal reproduction, actual result, and expected result.
Separate observed facts from suspected causes.
Use the [commit, PR, and issue rules](references/commit-pr-issue.md).

## Run the linter

Run `python3 scripts/writing_lint.py <paths>` on changed English prose.
The default exit status is `1` only for non-advisory findings; advisory findings still print.
Use `--fail-level advisory` when every finding must fail the command.
Exit status `0` means no finding reached the selected failure level, `1` means at least one did, and `2` means the linter could not run.
Lint output is an editing prompt, not proof of authorship or a substitute for factual review.

## Check before delivery

1. The first sentence gives the result, problem, or required action.
2. Every claim has evidence or an explicit unverified label.
3. Every sentence carries one action, result, reason, or constraint.
4. Actors, objects, conditions, and terms are specific and stable.
5. The page has one reader goal and one dominant document type.
6. Commands include prerequisites and observable results where needed.
7. README readers can reach a first successful use from the opening sections.
8. Comments state contracts or non-obvious reasons, not syntax.
9. Commit, PR, and issue text records rationale and relevant evidence.
10. Formatting does not create a bold wall, decorative heading, or em-dash rhythm.
11. Links, paths, commands, options, and examples match the repository.
12. No filler, repeated conclusion, unsupported praise, or automated-author signature remains.
