# Clubroom
部活向けの課題を提出するシステムです。

### ライブラリについて
| ライブラリ | 説明 |
| ------------- | ---------------------------------------------- |
| fastapi       | APIサーバーが作れるフレームワークです。 |
| python-dotenv | .envファイルの項目を環境変数として扱うことができます。 |

## 環境構築

### レポジトリをクローン（ダウンロード）します。
```bash
# レポジトリをクローン
git clone https://github.com/ickta39/clubroom.git

# レポジトリの中に移動
cd clubroom/
```

### 仮想環境venvの構築（オプション）
このvenvを構築すると、プロジェクトごとに仮想的なPythonの環境が作成され、別のプロジェクトとのライブラリの競合を避けることができます。
```bash
# venvの構築
python -m venv .venv

# venvの有効化（Windows/cmd）
.\.venv\Scripts\activate.bat

# venvの有効化（Windows/PowerShell）
# * 環境により実行できない可能性があります。
.\.venv\Scripts\Activate.ps1

# venvの有効化（Linux, macOS等/bash）
source .venv/Scripts/activate
```

### ライブラリのインストール
```bash
# requirements.txt内のライブラリを一括でインストール
python -m pip install -r requirements.txt
```

### 実行
.envファイルに次の内容を書き込んでください。`GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`は別途Google Cloudで生成してきてください。
```
GOOGLE_CLIENT_ID=000000000000-abcdefghijklmnopqrstuvwxyz012345.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=GOCSPX-...
GOOGLE_SERVER_METADATA_URL=https://accounts.google.com/.well-known/openid-configuration
```

以上の設定ができると、ポート8000番にHTTPサーバーを実行します。
```bash
# 実行
python main.py
```