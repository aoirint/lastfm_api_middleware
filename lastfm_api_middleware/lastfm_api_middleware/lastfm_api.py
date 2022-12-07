from pathlib import Path
import requests


def dump_recenttracks(
  lastfm_user: str,
  lastfm_api_key: str,
  useragent: str,
  dump_path: Path,
):
  api_url = 'https://ws.audioscrobbler.com/2.0/'

  params = {
    'method': 'user.getrecenttracks',
    'user': lastfm_user,
    'api_key': lastfm_api_key,
    'format': 'json',
  }

  headers = {
    'User-Agent': useragent,
  }

  res = requests.get(api_url, params=params, headers=headers)
  res.raise_for_status()

  dump_path.parent.mkdir(parents=True, exist_ok=True)
  dump_path.write_text(res.text, encoding='utf-8')
