import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.0xarchive.io/v1"


def api_key():
    key = os.environ.get("OXARCHIVE_API_KEY")
    if not key:
        sys.exit("Set OXARCHIVE_API_KEY (create a key at https://0xarchive.io/dashboard).")
    return key


def get(path, params, key):
    """GET one page, retrying 429 and 5xx with backoff. Returns the decoded body."""
    url = f"{API}{path}?{urllib.parse.urlencode(params)}"
    for attempt in range(6):
        request = urllib.request.Request(url, headers={"X-API-Key": key, "User-Agent": "0xarchive-examples"})
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code == 429 or error.code >= 500:
                time.sleep(2 ** attempt)
                continue
            sys.exit(f"{error.code} {error.reason}: {error.read().decode()[:300]}")
    sys.exit(f"gave up after retries: {url}")


def pages(path, params, key):
    """Yield every row, following meta.next_cursor until the API stops returning one."""
    params = dict(params)
    while True:
        body = get(path, params, key)
        yield from body.get("data", [])
        cursor = body.get("meta", {}).get("next_cursor")
        if not cursor:
            return
        params["cursor"] = cursor
