# lastfm_api_middleware

```shell
mkdir -p data
sudo chown -R 2000:2000 data

sudo docker buildx build -t aoirint/lastfm_api_middleware .
sudo docker run --rm --init --env-file "$PWD/.env" -v "$PWD/data:/data" aoirint/lastfm_api_middleware
```
