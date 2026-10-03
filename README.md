# Flask Hello World 一頁式網站

[![CI/CD Pipeline](https://github.com/zoechen794/practice0929/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/zoechen794/practice0929/actions/workflows/ci-cd.yml)

基於 Python Flask 框架所建立的一頁式網站範例，並整合 **GitHub Actions** 與 **Render** 實作 CI/CD 自動化測試與部屬流程。

---

## 專案結構

```
practice0929/
├── .github/
│   └── workflows/
│       └── ci-cd.yml         # GitHub Actions CI/CD 自動化流程
├── templates/
│   └── index.html            # 一頁式網頁前端範本 (HTML/CSS/JS)
├── tests/
│   └── test_app.py           # Pytest 單元測試
├── app.py                    # Flask 主程式
├── pytest.ini                # Pytest 設定檔
├── render.yaml               # Render 雲端部屬 Blueprint 設定檔
├── requirements.txt          # Python 相依套件清單 (含 Flask、Gunicorn、Pytest)
└── README.md                 # 專案說明文件
```

---

## 本地開發與啟動

### 1. 建立並啟用虛擬環境
```bash
# 建立虛擬環境
python -m venv venv

# Windows PowerShell 啟用
.\venv\Scripts\Activate.ps1

# macOS / Linux 啟用
source venv/bin/activate
```

### 2. 安裝套件
```bash
pip install -r requirements.txt
```

### 3. 執行單元測試
```bash
pytest
```

### 4. 啟動本機伺服器
```bash
python app.py
```
開啟瀏覽器並造訪：[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## CI/CD 與 Render 部屬說明

本專案已建立完整 CI/CD 流程：
1. **CI (持續整合)**：每次 Push 或 PR 至 `main` 分支時，GitHub Actions 會自動執行環境建置、語法檢查與 Pytest 單元測試。
2. **CD (持續部屬)**：當測試全數通過後，自動透過 Deploy Hook 觸發 Render 進行最新版本部屬。

### Render 與 GitHub 設定步驟

#### 步驟 1：在 Render 上建立 Web Service
1. 登入 [Render](https://render.com/)。
2. 點選 **New +** -> **Web Service**（或 **Blueprint** 並選取本儲存庫）。
3. 連接您的 GitHub 專案 `zoechen794/practice0929`。
4. 設定參數：
   - **Environment**：`Python`
   - **Build Command**：`pip install -r requirements.txt`
   - **Start Command**：`gunicorn app:app`
   - **Plan**：`Free`

#### 步驟 2：取得 Deploy Hook 並設定 GitHub Secret（推薦）
1. 在 Render 的 Web Service 設定頁面中，進入 **Settings**。
2. 找到 **Deploy Hook** 區塊，點選產生/複製 Hook 網址（格式類似 `https://api.render.com/deploy/srv-xxxx?key=yyyy`）。
3. 前往 GitHub 儲存庫：`Settings` -> `Secrets and variables` -> `Actions`。
4. 點選 **New repository secret**：
   - **Name**：`RENDER_DEPLOY_HOOK_URL`
   - **Value**：貼上剛剛複製的 Render Deploy Hook 網址。
5. （可選）在 Render 設定中關閉 **Auto-Deploy**，改由 GitHub Actions 測試通過後才觸發部屬，以確保每次發布到線上的程式都是經過測試驗證的穩定版本。
