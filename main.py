import os
from pathlib import Path
from typing import Optional
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI
from fastapi.responses import FileResponse

from lastfm_api_middleware import lastfm_api


LASTFM_USER = os.environ['LASTFM_USER']
LASTFM_API_KEY = os.environ['LASTFM_API_KEY']
DUMP_PATH = Path(os.environ['DUMP_PATH'])

USERAGENT = 'aoirint_lastfm_api_middleware/0.0.0'

app = FastAPI()

recenttracks_last_fetched: Optional[datetime] = None
recenttracks_interval = timedelta(seconds=60)


@app.get('/v1/recenttracks')
def v1_recenttracks():
  global recenttracks_last_fetched

  now = datetime.now(tz=timezone.utc)
  if recenttracks_last_fetched is None or recenttracks_interval <= now - recenttracks_last_fetched:
    recenttracks_last_fetched_string = recenttracks_last_fetched.isoformat() if recenttracks_last_fetched is not None else 'None'
    print(f'[{now.isoformat()}] Fetch recenttracks (last_fetched_at: {recenttracks_last_fetched_string})')

    lastfm_api.dump_recenttracks(
      lastfm_user=LASTFM_USER,
      lastfm_api_key=LASTFM_API_KEY,
      useragent=USERAGENT,
      dump_path=DUMP_PATH,
    )
    recenttracks_last_fetched = now

  return FileResponse(DUMP_PATH)
