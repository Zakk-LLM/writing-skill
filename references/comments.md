# Code Comments

A comment earns its maintenance cost when it states a contract or a reason that the code cannot express.

## Document public API contracts

Start with a one-sentence summary of what the exported item does. Add only details callers need:

- Input meaning and valid ranges.
- Return value and state changes.
- Errors, panics, or exceptions callers must handle.
- Safety requirements and undefined behavior.
- Non-obvious performance or concurrency guarantees.
- A short example when the API is not clear from its signature.

Describe stable behavior, not a replaceable internal algorithm. Follow the language's documentation convention; Go comments normally begin with the declared name, while Rust API docs use a concise summary followed by sections such as `Examples`, `Errors`, `Panics`, and `Safety` when needed.

Go:

```go
// ParseHeader returns ErrEmptyHeader when line contains no field name.
func ParseHeader(line string) (Header, error)
```

Rust:

```rust
/// Returns the cached value, or `None` after the entry expires.
pub fn get(&self, key: &str) -> Option<&Value>
```

## Explain internal reasons

Keep an internal comment only when it explains one of these facts:

- An invariant that another edit could violate.
- A compatibility constraint or upstream behavior.
- A security or trust boundary.
- A workaround and the condition for removing it.
- A surprising order, lock, allocation, or performance tradeoff.

Put the comment next to the decision it protects. Include an issue or upstream link when future removal depends on external behavior.

## Delete narration

Delete a comment when nearby code already says the same thing.

```python
# Increment retries.
retries += 1
```

Keep the reason when it changes how a maintainer may edit the line.

```python
# Count the first failed request so the three-attempt limit includes it.
retries += 1
```

High-confidence narration includes `return the result` before a return, `set X` before a direct assignment to `x`, and `call X` before a direct call to `x`. A linter should report only these narrow patterns; it cannot determine the value of a general comment.

## Keep comments bounded

Keep a simple API summary or internal reason to one sentence and no more than three lines. Use a longer public API comment only when it documents caller-visible errors, safety, examples, or constraints. Move design history and multi-paragraph rationale to a design document, then link it from a short comment if the code still needs the constraint.

## Sources

- [Go Doc Comments](https://go.dev/doc/comment)
- [Rust API documentation guidelines](https://rust-lang.github.io/api-guidelines/documentation.html)
- [Rust API comment conventions](https://rust-lang.github.io/rfcs/0505-api-comment-conventions.html)
- [Google documentation best practices](https://google.github.io/styleguide/docguide/best_practices.html)
