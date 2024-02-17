# lastfm_api_middleware

[Last.fm](https://www.last.fm/)からユーザのScrobble情報を取得して結果を返すAPIサーバ。個人サイトなどに自分のScrobble情報を表示するために使うことを想定しています。

## 機能

### 対応サービス

- [Last.fm](https://www.last.fm/)

1ユーザのみ、データ取得できます。
複数のユーザからデータを取得したい場合、必要な数のAPIサーバを起動してください（各サービスに過剰なアクセスが発生しないように注意してください）。

### キャッシュ

APIサーバから各サービスに過剰なアクセスが発生しないように、取得結果を1分間キャッシュします。キャッシュ間隔の間に再度APIサーバへのリクエストがあった場合、キャッシュした内容を返します。

## リリース

ソースコードおよびDockerイメージを配布しています。

- [GitHub](https://github.com/aoirint/lastfm_api_middleware)
- [Docker Hub](https://hub.docker.com/r/aoirint/lastfm_api_middleware)

## デプロイ手順

Docker Composeおよびリバースプロキシを使ったデプロイを想定しています。

### 1. 永続化ディレクトリを作成

永続化のため、`UID=2000`、`GID=2000`のデータディレクトリを作成します（Docker Volumeで代用可）。

```shell
mkdir -p data
sudo chown -R 2000:2000 data
```

### 2. .envファイルを作成

`template.env`を`.env`としてコピーして、設定します。設定項目については、[設定](#設定)の項目を参照してください。

### 3. Docker Composeサービスを起動

`docker-compose.yml`をコピーして、以下のコマンドを実行します。

```shell
sudo docker compose up -d
```

### 4. リバースプロキシを設定

必要に応じて、nginxやcloudflaredを設定してください。

## （開発者向け）開発環境

- Python 3.11
- Docker Engine 23.0+

## （開発者向け）実行手順

### 1. 永続化ディレクトリを作成

永続化のため、`UID=2000`、`GID=2000`のデータディレクトリを作成します（Docker Volumeで代用可）。

```shell
mkdir -p data
sudo chown -R 2000:2000 data
```

### 2. .envファイルを作成

`template.env`を`.env`としてコピーして、設定します。設定項目については、[設定](#設定)の項目を参照してください。

### 3. Dockerイメージをビルド

```shell
sudo docker build -t aoirint/lastfm_api_middleware .
```

### 4. Dockerイメージを実行

```shell
sudo docker run --rm --init --env-file "./.env" -v "./data:/data" -p "127.0.0.1:8000:8000" aoirint/lastfm_api_middleware
```

## 設定

環境変数または`.env`ファイルで設定します。

|項目|詳細|
|:--|:--|
|LASTFM_USER|Last.fmのユーザ名（username）|
|LASTFM_API_KEY|Last.fm APIのAPIキー|
|DUMP_PATH|キャッシュの保存先（JSONファイルのパス）|
|CORS_ALLOW_ORIGINS|CORSを許可するオリジンのリスト（カンマ区切り）|
|HOST_DATA_DIR|（Docker Composeの場合のみ）ホスト側からコンテナにマウントするデータディレクトリのパス|
|HOST_PORT|（Docker Composeの場合のみ）ホスト側にバインドするAPIサーバのTCPポート番号|

## （開発者向け） ライブラリ管理

ライブラリ管理には[Poetry](https://python-poetry.org/docs/#installation)を使っています。
