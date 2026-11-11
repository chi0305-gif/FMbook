"""把 index.html 包成完整網頁，輸出 dist/廣播講稿工作室.html 與 .txt（內容相同）。"""
from pathlib import Path

ROOT = Path(__file__).parent
HEAD = """<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""

src = (ROOT / "index.html").read_text(encoding="utf-8").rstrip()
out = HEAD + src + "\n</body>\n</html>\n"
(ROOT / "dist").mkdir(exist_ok=True)
for ext in ("html", "txt"):
    (ROOT / "dist" / f"廣播講稿工作室.{ext}").write_text(out, encoding="utf-8")
