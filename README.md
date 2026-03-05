# YAMAP GPX Downloader

English | 日本語は下へスクロール

## English

This Python script automatically downloads all your GPX hiking activities from [YAMAP](https://yamap.com) using Playwright. It keeps track of which activities have already been downloaded so you can safely restart it at any time.

## Features

- Logs in with your YAMAP email and password.
- Detects your user profile automatically.
- Loops through all activity pages automatically.
- Downloads GPX files and keeps the filenames suggested by YAMAP.
- Skips already downloaded activities using a log file (`downloaded.log`).
- Skips already downloaded activities when duplicate file is found.
- Uses headless Chromium.
- Randomized sleep between downloads to reduce server load.

## Requirements

- Python 3.11+  
- [Playwright](https://playwright.dev/python/)  
- Ubuntu/Debian Linux (or similar) with basic libraries installed for Chromium

## Setup

### Clone the repository:

```bash
git clone git@github.com:Michanoku/yamap-gpx-downloader.git
cd yamap-gpx-downloader
```

### Install Python dependencies:

```bash
pip install -r requirements.txt
```

### Install Playwright browsers:

```bash
playwright install
```

### Run the script:

```bash
python gpx_downloader.py
```

You will be prompted to enter your YAMAP email and password.
The script will download all your activities to the download folder.
Successfully downloaded activities are logged in downloaded.log to avoid duplicates.

## Notes

Only your own YAMAP account can be used with this script. Do not share your credentials.
The log file stores activity URLs, not filenames. This ensures the script doesn’t redownload the same activity.
You can safely interrupt and restart the script at any time. It will skip already downloaded activities.
Additional libraries may have to be installed for Playwright to work.

## 日本語

この Python スクリプトは、Playwright を使用して [YAMAP](https://yamap.com) から自分の登山活動の GPX データを自動的にダウンロードします。  
すでにダウンロード済みのアクティビティは記録されるため、いつでも安全に再実行できます。

## 主な機能

- YAMAP のメールアドレスとパスワードでログイン
- ユーザープロフィールを自動検出
- すべてのアクティビティページを自動巡回
- YAMAP が指定したファイル名のまま GPX を保存
- ログファイル（`downloaded.log`）を使用して既存データをスキップ
- 同名ファイルが存在する場合もスキップ
- ヘッドレス Chromium を使用
- サーバー負荷軽減のため、ダウンロード間にランダムな待機時間を設定

## 動作環境

- Python 3.11 以上  
- [Playwright](https://playwright.dev/python/)   
- Ubuntu / Debian 系 Linux（Chromium 用の必要ライブラリがインストールされていること）

## セットアップ

### リポジトリをクローン

```bash
git clone git@github.com:Michanoku/yamap-gpx-downloader.git
cd yamap-gpx-downloader
```

### Python 依存パッケージをインストール

```bash
pip install -r requirements.txt
```

### Playwright ブラウザをインストール

```bash
playwright install
```

### スクリプトを実行

```bash
python gpx_downloader.py
```

実行時に YAMAP のメールアドレスとパスワードの入力を求められます。
ダウンロードされた GPX ファイルは download フォルダに保存されます。
成功したアクティビティの URL は downloaded.log に記録され、重複ダウンロードを防ぎます。

## 注意事項

本スクリプトは自分の YAMAP アカウントでのみ使用してください。

ログファイルにはファイル名ではなく、アクティビティの URL が保存されます。
これにより、同じアクティビティの再ダウンロードを防ぎます。

スクリプトは途中で停止しても、再実行すれば未取得分のみダウンロードされます。

Playwright の動作には追加のシステムライブラリが必要になる場合があります。

## MIT LICENSE

Copyright (c) 2026 Michael Werker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.