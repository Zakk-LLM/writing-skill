# Commit, PR, and Issue Text

Write enough for a maintainer to reproduce the problem, understand the decision, and judge the evidence. Do not turn repository text into a work log.

## Commit messages

Write a short imperative subject that names the affected behavior.

- Weak: `Update parser`
- Direct: `Reject empty names before parsing headers`

Use the body when the reason or user-visible effect is not clear from the diff. Explain the prior failure, why the chosen behavior is correct, and any compatibility consequence. Omit routine progress, generic test claims, and authoring narration.

## Pull requests

A non-trivial PR description should answer these questions in this order when they apply:

1. What fails or is needed, under which condition, and who or what is affected?
2. Why does the current behavior fail?
3. What behavior changes, and why is that change correct?
4. How was the risky path verified?
5. What remains limited, risky, or unverified?
6. Which issue, design decision, or benchmark supplies context?

Use headings only when the description is long enough to need scanning. Do not force every PR into empty `Summary`, `Changes`, and `Testing` sections.

State exact commands and observed outcomes. Replace `All tests pass` with the regression test or scenario that distinguishes old and new behavior. If a platform or path was not tested, say so without predicting its result.

Keep reviewer questions specific: `Should reused sessions invoke this callback?` Delete social closings and requests to merge quickly.

## Issues

Write a title with the component, trigger, and observable failure:

```text
parser: empty quoted key causes a panic
```

Include:

- Version, commit, operating system, architecture, and relevant configuration.
- The smallest executable reproduction and required input.
- The exact actual result, including status, error, or log excerpt.
- The expected result as an observable behavior.
- Regression range or comparison only when verified.

Separate evidence from diagnosis. Mark a proposed root cause as a hypothesis and provide the observation that supports it.

## Rewrite common generated patterns

| Pattern | Revision |
| --- | --- |
| `This PR aims to improve the overall robustness of...` | State the failing condition and changed behavior. |
| `Improved performance`, `Better errors`, `Enhanced UX` | Give a measurement, exact error, or visible behavior; otherwise delete it. |
| Bold `Problem`, `Solution`, and `Benefits` labels in every paragraph | Use plain paragraphs or descriptive headings only when scanning requires them. |
| `In summary, this makes the system more reliable.` | Delete the repeated conclusion. |
| `All tests pass.` | Name the risk-specific command and observed result. |
| `Maintainers should merge this ASAP.` | Delete it or ask a concrete blocking question. |
| `Please review and let me know your thoughts.` | Delete it; the PR already requests review. |
| A diary of attempted edits | Keep the failure, decision, rejected alternative when relevant, and evidence. |
| A root-cause claim before reproduction | Record the observation; label the cause as a hypothesis. |

## Sources

- [GitLab documentation style guide](https://docs.gitlab.com/development/documentation/styleguide/)
- [Linux kernel: submitting patches](https://docs.kernel.org/process/submitting-patches.html)
- [Rust compiler review policy](https://forge.rust-lang.org/compiler/reviews.html)
- [pstack technical-writing skill](https://github.com/backnotprop/pstack/blob/main/skills/technical-writing/SKILL.md)
- [Go issue 80517](https://github.com/golang/go/issues/80517)
- [curl issue 21606](https://github.com/curl/curl/issues/21606)
