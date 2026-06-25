# FTB Translater

FTB Translater is a small desktop tool for translating modern FTB Quests language files with DeepSeek.

## v1 Scope

- Supports `en_us -> zh_cn` only.
- Supports modern FTB Quests lang files: `config/ftbquests/quests/lang/en_us.snbt`.
- Supports chapter-style FTB Quests files: `config/ftbquests/quests/chapters/*.snbt`.
- Writes `lang/zh_cn.snbt` in place for lang mode.
- Rewrites translatable text fields in `chapters/*.snbt` in place for chapter mode.
- Backs up the existing `lang` or `chapters` directory before writing.
- Stores translation cache and reports under `.ftb-translater/` inside the selected quests directory.

## Install

```powershell
python -m pip install -e .
```

## Run

```powershell
python main.py
```

Paste your DeepSeek API key in the GUI and save it. The key is stored in `.env` as plain text:

```text
DEEPSEEK_API_KEY=your_key_here
```

## Output

After translation, the tool writes:

- `config/ftbquests/quests/lang/zh_cn.snbt` in lang mode, or translated `chapters/*.snbt` in chapter mode
- `config/ftbquests/quests/.ftb-translater/cache.json`
- `config/ftbquests/quests/.ftb-translater/report-latest.json`
- `config/ftbquests/quests/.ftb-translater/backups/YYYYMMDD-HHMMSS/`

## Tests

```powershell
python -m unittest discover -s tests -v
```
