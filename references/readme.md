# README Structure

A README gets a reader from identification to a first successful use. Keep only sections the project needs.

## Minimum structure

1. **Identity:** One sentence names the project, its type, and its primary purpose.
2. **Requirements:** State supported environments and prerequisites that affect installation or use.
3. **Installation:** Give the shortest supported installation path.
4. **First use:** Give one complete command or example that produces an observable result.
5. **Configuration or reference:** Document common settings or link to exact reference material.
6. **Contributing:** Link to the project's contribution process when contributions are accepted.
7. **License:** Name and link the license.

Omit a section that does not apply. Add support, security, compatibility, or development sections only when readers need them for a repository task.

## Use the first screen for the first task

Put the identity sentence, required prerequisite, installation command, and shortest successful use before project history or exhaustive detail. A reader should know what the project is and how to test the common path without following several links.

Place each command after its prerequisites. State the working directory or environment variable when the command depends on it. Follow the command with the output, created file, state change, or other result that confirms success.

## Keep these out of the opening

- A wall of build, coverage, download, funding, and social badges.
- A slogan or a paragraph of adjectives labeled `Features`.
- Architecture diagrams needed only by contributors.
- Full option, API, or configuration reference.
- Screenshots that precede the project identity and first task.
- Funding, merchandise, history, acknowledgements, or repeated navigation.

A feature list is useful only when each item names a recognizable capability, constraint, measurement, or evidence link. Remove claims such as `fast`, `modern`, and `powerful` without evidence.

## Order sections by reader tasks

Prefer `Install`, `Run the linter`, and `Configure exclusions` over headings copied from internal module names. Move uncommon workflows and exhaustive reference to dedicated pages. Link from the step where a reader first needs the detail.

## Models worth studying

Use these files for information order, not text to copy:

- [ripgrep README](https://github.com/BurntSushi/ripgrep/blob/master/README.md): identity, behavior, comparison, limits, installation, and links to deeper guides.
- [fzf README](https://github.com/junegunn/fzf/blob/master/README.md): identity followed by installation, shell integration, usage, examples, and advanced tasks. Do not copy its badge-heavy opening.
- [uv documentation home](https://docs.astral.sh/uv/): identity, install command, first successful command, then task-based routes.

## Sources

- [README Best Practices](https://github.com/jehna/readme-best-practices)
- [Google documentation best practices](https://google.github.io/styleguide/docguide/best_practices.html)
- [Google developer documentation style guide](https://developers.google.com/style)
- [ripgrep README](https://github.com/BurntSushi/ripgrep/blob/master/README.md)
- [fzf README](https://github.com/junegunn/fzf/blob/master/README.md)
- [uv documentation](https://docs.astral.sh/uv/)
