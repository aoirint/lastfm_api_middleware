import os
import requests
from pathlib import Path

LAST_FM_USER = os.environ['LAST_FM_USER']
LAST_FM_API_KEY = os.environ['LAST_FM_API_KEY']
DUMP_PATH = Path(os.environ['DUMP_PATH'])

USERAGENT = 'aoirint_lastfm_api_middleware/0.0.0'

def main():
  api_url = 'https://ws.audioscrobbler.com/2.0/'

  params = {
    'method': 'user.getrecenttracks',
    'user': LAST_FM_USER,
    'api_key': LAST_FM_API_KEY,
    'format': 'json',
  }

  headers = {
    'User-Agent': USERAGENT,
  }

  res = requests.get(api_url, params=params, headers=headers)
  res.raise_for_status()

  DUMP_PATH.parent.mkdir(parents=True, exist_ok=True)
  DUMP_PATH.write_text(res.text, encoding='utf-8')


if __name__ == '__main__':
  main()
