# Vocabulary

Use this table as an editing prompt, not an authorship detector. A listed word can be correct when it carries a precise project meaning.

| Word or phrase | Why it fails | Replace it with |
| --- | --- | --- |
| `delve into` | Announces research instead of naming the task. | `inspect`, `compare`, or the exact operation. |
| `tapestry` | Uses a decorative metaphor where components should be named. | The components and their relationship. |
| `pivotal` | Claims importance without stating the consequence. | The decision or behavior that depends on it. |
| `vibrant` | Promotes a community or product without evidence. | A count, activity, or omit the claim. |
| `leverage` | Hides whether the action means use, depend on, or exploit. | `use`, `call`, `reuse`, or the exact verb. |
| `robust` | Does not identify the failures that are handled. | The handled input, error, or recovery behavior. |
| `seamless` | Claims an absence of friction without a testable boundary. | The omitted step or preserved interface. |
| `ecosystem` | Can blur packages, maintainers, tools, and users. | The exact group. |
| `synergy` | Claims a benefit without an operation or result. | The interaction and measured result. |
| `landscape` | Replaces a bounded set with a broad metaphor. | The named tools, market, or problem set. |
| `crucial` | Adds emphasis instead of impact. | The failure that follows if the condition is missed. |
| `showcase` | Promotes an example instead of stating what it demonstrates. | `shows`, `prints`, `returns`, or the observed result. |
| `underscore` | Often adds rhetorical emphasis. | `shows`, `requires`, or delete the sentence. |
| `testament` | Turns evidence into praise. | The evidence and the conclusion it supports. |
| `enhance` | Does not say what changed. | `reduce`, `add`, `reject`, or another measured action. |
| `utilize` | Is longer than `use` without adding meaning. | `use`, unless the domain distinguishes utilization. |
| `in order to` | Adds words before a purpose. | `to`. |
| `it should be noted that` | Delays the fact and tells readers how to value it. | Start with the fact. |
| `simply` | Can hide prerequisites or dismiss difficulty. | State the required step or omit it. |
| `obviously` | Substitutes confidence for evidence. | State the evidence or omit it. |
| `overall` | Often introduces an unsupported aggregate judgment. | Name the measured dimension or omit it. |
| `various` | Conceals the number or categories. | List the items or give the count. |

## Use jargon only for precision

1. Check the repository, upstream API, protocol, or field glossary for the established term.
2. Keep the term when a shorter everyday word would change its meaning.
3. Define an unfamiliar necessary term at first use with its category and distinguishing property.
4. Use the same term for the same concept throughout the document.
5. Replace team slang, business language, and unexplained acronyms with concrete names.
6. Do not rotate synonyms for style; synonym changes can imply different objects.

A linter cannot decide whether a term is necessary. Review the term against the reader's knowledge and the project's usage.

## Sources

- [Google developer documentation style guide: jargon](https://developers.google.com/style/jargon)
- [Microsoft Writing Style Guide: avoid jargon](https://learn.microsoft.com/en-us/style-guide/word-choice/avoid-jargon)
- [GOV.UK style guide](https://www.gov.uk/guidance/style-guide)
- [Wikipedia: signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [no-slop](https://github.com/Byk3y/no-slop)
- [slop-gate](https://github.com/hwajongpark/slop-gate)
- [vale-ai-tells](https://github.com/tbhb/vale-ai-tells)
- [pstack technical-writing skill](https://github.com/backnotprop/pstack/blob/main/skills/technical-writing/SKILL.md)
