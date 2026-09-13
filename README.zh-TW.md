# Writing Skill

[English](README.md) | [简体中文](README.zh-CN.md) | 繁體中文

Writing Skill 為程式開發 agent 提供可執行的英文與 Markdown 寫作規範，使文字簡潔，並以證據為依據。

規範涵蓋 README、按任務組織的文件、程式碼註釋、commit、PR 與 issue。`writing_lint.py` 檢查套式詞彙和結構，但不會據此判斷作者身分。

## 要求

- Python 3.11 或更新版本，用於執行檢查器和儲存庫驗證程式。
- agent 能從包含 `SKILL.md` 的目錄發現 skill。

## 安裝

將 `AGENT_SKILLS_DIR` 設為 agent 的 skill 目錄，再複製儲存庫：

```bash
export AGENT_SKILLS_DIR=/path/to/agent/skills
git clone https://github.com/Zakk-LLM/writing-skill.git "$AGENT_SKILLS_DIR/writing-skill"
```

確認 agent 能讀取該 skill：

```bash
test -f "$AGENT_SKILLS_DIR/writing-skill/SKILL.md"
```

存在 `SKILL.md` 時，該命令以結束狀態 0 結束。

## 使用

agent 在編寫或審查英文內容前應先讀取 [SKILL.md](SKILL.md)。中文文字由 `chinese-skill` 處理；介面文案由 `web-ui` 處理；提交步驟由 `zakk-workflow` 處理。

對檔案或目錄執行檢查器：

```bash
python3 scripts/writing_lint.py README.md references/
```

每條結果包含路徑、行號、嚴重性、規則識別碼、修改指示與原文片段。預設命令只在發現非 advisory 問題時以結束狀態 1 結束；advisory 問題仍會輸出，但不會使命令失敗。

若儲存庫要求嚴格門禁，讓 advisory 問題也使命令失敗：

```bash
python3 scripts/writing_lint.py --fail-level advisory README.md
```

檢查器會在應用正文規則前遮蔽 fenced code、inline code、URL 與 Markdown 連結。它不會自動改寫文字，也不會判斷作者身份。

## 查閱規範

- [詞彙](references/vocabulary.md)列出常見生成式寫作詞、填充語、jargon 及具體改法。
- [句式](references/sentences.md)說明資訊順序、單句範圍、語態、指令、修辭模板與視覺強調。
- [README 結構](references/readme.md)規定開頭任務與最小章節。
- [文件類型](references/docs.md)區分 tutorial、how-to guide、reference、explanation 與 FAQ。
- [程式碼註釋](references/comments.md)區分公開契約、內部理由與重複程式碼的註釋。
- [commit、PR 與 issue 文字](references/commit-pr-issue.md)規定儲存庫溝通所需的證據與結構。

[範例](examples)分別提供 README、PR 描述與 issue 的套式草稿和直接改寫版本。

## 驗證儲存庫

在儲存庫根目錄執行：

```bash
python3 scripts/check_repository.py
```

驗證程式檢查必要檔案、frontmatter、行數限制、來源章節、本機連結、詞表資料、自身 lint 結果及改寫前後的對照範例。成功時輸出 `All repository checks passed.`，並以結束狀態 0 結束。

## 參與貢獻

每條規則必須可執行：說明如何識別問題，以及應改成什麼。修改 reference 時新增來源 URL。提交前執行儲存庫驗證程式。

## 授權

Writing Skill 採用 [MIT License](LICENSE)。
