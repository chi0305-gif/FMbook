# FMbook

- `index.html`：廣播講稿工作室（發布為 Claude Artifact 的原始檔，不含 doctype/head）。
- 每次修改 `index.html` 後：執行 `python3 build.py`，產生 `dist/廣播講稿工作室.html` 與 `dist/廣播講稿工作室.txt`（完整程式碼，內容相同），並把這兩個檔案傳給使用者。
