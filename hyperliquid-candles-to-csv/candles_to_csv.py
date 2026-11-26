"""Download Hyperliquid OHLCV candles for any market and interval to CSV, every page.

    OXARCHIVE_API_KEY=... python3 candles_to_csv.py BTC 1h "$(date -u -d '8 days ago' +%F)" "$(date -u +%F)" > btc-1h.csv

Venues: pass --venue hip3 for HIP-3 markets (e.g. xyz:NVDA) or --venue lighter for Lighter.
Free keys read the most recent 30 days; Build and above read the full archive.
"""
import argparse
import csv
import sys
from datetime import datetime, timedelta, timezone

from oxa import api_key, pages

ROUTES = {
    "hyperliquid": "/hyperliquid/candles/{symbol}",
    "hip3": "/hyperliquid/hip3/candles/{symbol}",
    "lighter": "/lighter/candles/{symbol}",
}
FIELDS = ["timestamp", "open", "high", "low", "close", "volume", "quote_volume", "trade_count"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("symbol")
    parser.add_argument("interval", choices=["1m", "5m", "15m", "30m", "1h", "4h", "1d", "1w"])
    parser.add_argument("start", help="YYYY-MM-DD (UTC)")
    parser.add_argument("end", help="YYYY-MM-DD (UTC, exclusive)")
    parser.add_argument("--venue", choices=ROUTES, default="hyperliquid")
    args = parser.parse_args()
    route = ROUTES[args.venue].format(symbol=args.symbol)
    end = datetime.strptime(args.end, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    last_ms = (end - timedelta(milliseconds=1)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    # End one millisecond before the end date, so a window ending today never reads today (Free serves through yesterday).
    params = {"interval": args.interval, "start": f"{args.start}T00:00:00Z", "end": last_ms, "limit": 10000}
    writer = csv.DictWriter(sys.stdout, fieldnames=FIELDS, extrasaction="ignore")
    writer.writeheader()
    count = 0
    for row in pages(route, params, api_key()):
        if datetime.fromisoformat(row["timestamp"].replace("Z", "+00:00")) >= end:
            break  # the window here is end-exclusive
        writer.writerow(row)
        count += 1
    print(f"{count} candles", file=sys.stderr)


if __name__ == "__main__":
    main()
