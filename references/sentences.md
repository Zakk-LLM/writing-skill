# Sentences

## Lead with the conclusion

Put the result, failure, decision, or required action in the first independent clause.

- Weak: `After reviewing the implementation, we found that the cache is not cleared.`
- Direct: `The cache remains populated after logout.`

A weak lead describes the writer's process. Replace it with the fact the reader needs.

## Keep one matter in each sentence

A sentence is overloaded when it combines independent actions, results, reasons, or exceptions that readers may need to act on separately. Split it at the change of subject or purpose.

- Weak: `Install the package and edit the file so the service can start, but keep the old key for clients.`
- Direct: `Install the package. Edit `config.toml` before starting the service. Keep the old key for clients older than 2.4.`

Keep a cause with its result when separating them would hide the relationship.

## Name actors and objects

Replace `it`, `this`, `the process`, and nominalizations when their referent is not immediate.

- Weak: `This performs validation before processing.`
- Direct: `The parser rejects an empty header before decoding the body.`

Use concrete verbs. Replace `perform an evaluation of` with `evaluate` and `make a modification to` with `modify`.

## Prefer active voice when the actor matters

- Weak: `The configuration is loaded by the worker.`
- Direct: `The worker loads the configuration.`

Keep passive voice when the actor is unknown, irrelevant, or intentionally hidden: `The connection is closed after 30 seconds.` A passive-voice lint finding is advisory.

## Use imperative instructions

Start a procedure step with the action: `Run`, `Open`, `Set`, or `Compare`. Address the reader as `you` only when naming the reader prevents ambiguity. Do not call the reader `the user`.

Put prerequisites and conditions first:

- Weak: `Run the migration with --offline if the host has no network access.`
- Direct: `If the host has no network access, run `migrate --offline`.`

## Remove contrast templates

Patterns such as `not only X, but also Y` and `it is not X; it is Y` often manufacture emphasis. State the two facts or the real correction.

- Weak: `The flag not only skips downloads but also improves reliability.`
- Direct: ``--offline` skips downloads. It does not retry missing packages.`

Keep a contrast when the distinction corrects a likely error: `The timeout limits each request, not the whole job.`

## Remove rhetorical triplets

Three broad adjectives or abstract nouns can imitate completeness without evidence.

- Weak: `The change improves reliability, scalability, and maintainability.`
- Direct: `The worker retries interrupted uploads twice.`

Keep a three-item list when the set is real and each item is defined or measured.

## End on the last fact

Delete recap openings such as `In conclusion`, `In summary`, and `Ultimately` when the paragraph repeats earlier claims. Add a final section only when it gives a new decision, next action, or unresolved limit.

## Limit visual emphasis

Two or more consecutive paragraphs or list items that begin with bold labels form a bold wall. Convert them to descriptive headings, a table with meaningful columns, or plain sentences.

Use an em dash only when its interruption is clearer than a comma, colon, parentheses, or a new sentence. More than one em dash on a prose line or repeated em dashes across nearby lines usually need revision.

Do not put Emoji in headings. Name the task or subject instead.

## Sources

- [GOV.UK style guide](https://www.gov.uk/guidance/style-guide)
- [Google developer documentation style guide: voice](https://developers.google.com/style/voice)
- [Google developer documentation style guide: highlights](https://developers.google.com/style/highlights)
- [Wikipedia: signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [no-slop](https://github.com/Byk3y/no-slop)
- [slop-gate](https://github.com/hwajongpark/slop-gate)
