# Writing Skill

<!-- skill-map -->
## 总图

```text
任务进来
 ├─ 定结构（包结构、数据、部署形态、前端目录）
 │    └─▶ zakk-architecture ──界面取值──▶ web-ui
 │              └─ 必出三份文档：设计语言(web-ui) / 架构(本份) / 工作流(zakk-workflow)
 ├─ 一次改动（修复、小功能、文档、skill 改动）
 │    └─▶ zakk-maintain
 │          ├─ 1 计划写成文件 ──送审──▶ 另一个头脑
 │          ├─ 2 按批准的计划写说明书 ──派工──▶ dispatch --engine omp | codex | opencode
 │          ├─ 3 判 diff ──▶ zakk-review ；审者自己做消融、门禁、对拍 ；再派一个没看过计划的冷读
 │          └─ 4 落仓与报告 ──▶ zakk-workflow（分支、提交、合并请求、完成报告）
 ├─ 任何中文 ──▶ chinese-skill（横切：每份都读，压缩、恢复、切换任务后重读）
 └─ 任何英文正文 ──▶ writing-skill（横切：README、docs、注释、提交、PR、issue）
```
<!-- /skill-map -->

[English](README.md) | 简体中文 | [繁體中文](README.zh-TW.md)

Writing Skill 为编程 agent 提供可执行的英文与 Markdown 写作规范，使文字简洁，并以证据为依据。

规范覆盖 README、按任务组织的文档、代码注释、commit、PR 与 issue。`writing_lint.py` 检查公式化词汇和结构，但不会据此判断作者身份。

## 要求

- Python 3.11 或更高版本，用于运行检查器和仓库验证程序。
- agent 能从包含 `SKILL.md` 的目录发现 skill。

## 安装

将 `AGENT_SKILLS_DIR` 设为 agent 的 skill 目录，再克隆仓库：

```bash
export AGENT_SKILLS_DIR=/path/to/agent/skills
git clone https://github.com/Zakk-LLM/writing-skill.git "$AGENT_SKILLS_DIR/writing-skill"
```

确认 agent 能读取该 skill：

```bash
test -f "$AGENT_SKILLS_DIR/writing-skill/SKILL.md"
```

存在 `SKILL.md` 时，该命令以状态码 0 退出。

## 使用

agent 在编写或审查英文正文前应先读取 [SKILL.md](SKILL.md)。中文文本由 `chinese-skill` 处理；界面文案由 `web-ui` 处理；提交步骤由 `zakk-workflow` 处理。

对文件或目录运行检查器：

```bash
python3 scripts/writing_lint.py README.md references/
```

每条结果包含路径、行号、严重性、规则标识、修改指示与原文片段。默认命令只在发现非 advisory 问题时以状态码 1 退出；advisory 问题仍会输出，但不会使命令失败。

若仓库要求严格门禁，让 advisory 问题也使命令失败：

```bash
python3 scripts/writing_lint.py --fail-level advisory README.md
```

检查器会在应用正文规则前遮蔽 fenced code、inline code、URL 与 Markdown 链接。它不会自动改写文字，也不会判断作者身份。

## 查阅规范

- [词汇](references/vocabulary.md)列出常见生成式写作词、填充语、jargon 及具体改法。
- [句式](references/sentences.md)说明信息顺序、单句范围、语态、指令、修辞模板与视觉强调。
- [README 结构](references/readme.md)规定开头任务与最小章节。
- [文档类型](references/docs.md)区分 tutorial、how-to guide、reference、explanation 与 FAQ。
- [代码注释](references/comments.md)区分公开契约、内部理由与重复代码的注释。
- [commit、PR 与 issue 文本](references/commit-pr-issue.md)规定仓库沟通所需的证据与结构。

[示例](examples)分别提供 README、PR 描述与 issue 的公式化草稿和直接改写版本。

## 验证仓库

在仓库根目录运行：

```bash
python3 scripts/check_repository.py
```

验证程序检查必要文件、frontmatter、行数限制、来源章节、本地链接、词表数据、自身 lint 结果及改写前后的示例。成功时输出 `All repository checks passed.`，并以状态码 0 退出。

## 参与贡献

每条规则必须可执行：说明如何识别问题，以及应改成什么。修改 reference 时添加来源 URL。提交前运行仓库验证程序。

## 许可证

Writing Skill 采用 [MIT License](LICENSE)。
