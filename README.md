# lastfm_api_middleware

## リポジトリ

- [GitHub](https://github.com/aoirint/lastfm_api_middleware)
- [Docker Hub](https://hub.docker.com/r/aoirint/lastfm_api_middleware)


## 使い方

```shell
mkdir -p data
sudo chown -R 2000:2000 data

sudo docker build -t aoirint/lastfm_api_middleware .
sudo docker run --rm --init --env-file "$PWD/.env" -v "$PWD/data:/data" -p "127.0.0.1:8000:8000" aoirint/lastfm_api_middleware
```

## ライブラリ管理

ライブラリ管理に[Poetry](https://python-poetry.org/docs/#installation)を使っています。

ライブラリに変更があった場合、以下のコマンドでrequirements.txtを更新します（DockerイメージやCIで使われます）。

```shell
poetry export --without-hashes -o requirements.txt
poetry export --without-hashes --with dev -o requirements-dev.txt
```
