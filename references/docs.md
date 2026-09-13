# Documentation by Reader Task

Choose one dominant purpose for each page. A page can link to another type but should not become a partial tutorial, option table, design essay, and troubleshooting guide at once.

## Tutorial

A tutorial gives a controlled learning experience to a reader who is new to the subject.

Required content:

- The learning outcome and starting knowledge.
- A safe, complete path with ordered steps.
- Inputs or fixture data supplied by the tutorial.
- Observable results at checkpoints.
- A brief explanation only where it helps the next step.

Do not interrupt the path with exhaustive options or production variants. Link to reference and how-to pages after the reader reaches the result.

## How-to guide

A how-to guide helps a reader with working knowledge complete one real task.

Required content:

- The exact goal and conditions under which the guide applies.
- Prerequisites before the first dependent action.
- The shortest supported sequence of actions.
- Observable success and relevant failure recovery.
- Links to reference entries for optional parameters.

Do not teach the whole system or list unrelated capabilities.

## Reference

Reference material provides exact facts for lookup.

Required content:

- Scope, version, and stability when they affect the contract.
- Complete names, syntax, types, defaults, ranges, and return values.
- Errors, side effects, state transitions, and compatibility constraints.
- Consistent ordering and terminology.
- Small examples only when they disambiguate the contract.

Do not hide required details in narrative or present a guided lesson as complete reference.

## Explanation

An explanation builds understanding of a concept, design, or tradeoff.

Required content:

- The concept and the question it answers.
- Relevant context and assumptions.
- Causes, constraints, alternatives, and consequences.
- Evidence for factual or performance claims.
- Links to procedures and exact reference material.

Do not turn a design explanation into a step-by-step installation guide.

## Document every command

Before a command, state its prerequisites, required working directory, input files, and environment variables. After it, state an observable result when readers need to confirm progress. Verify the command against the current executable or source.

Weak:

```text
Run migrate to update everything.
```

Direct:

```text
From the repository root, run `migrate schema.sql`. The command creates `schema.lock` and exits with status 0.
```

## Write searchable FAQ entries

Use the question a reader would search for: `Why does the client return error 60?` or `How do I change the cache directory?` Answer with the diagnosis, setting meaning, or required action in the first sentence. Put mechanism, exceptions, and costs after that answer.

Avoid headings such as `Troubleshooting issue` or `Configuration details`; they hide the symptom or task.

## Keep docs current

Update documentation in the same change as the behavior. Remove obsolete instructions and aliases instead of appending a correction that leaves both paths visible.

## Sources

- [Diátaxis](https://diataxis.fr/)
- [Django documentation](https://docs.djangoproject.com/en/6.1/)
- [Google documentation best practices](https://google.github.io/styleguide/docguide/best_practices.html)
- [pstack technical-writing skill](https://github.com/backnotprop/pstack/blob/main/skills/technical-writing/SKILL.md)
- [Bun quickstart](https://bun.com/docs/quickstart)
- [Tailscale quickstart](https://tailscale.com/docs/how-to/quickstart)
- [curl FAQ](https://curl.se/docs/faq.html)
- [Git FAQ](https://git-scm.com/docs/gitfaq)
