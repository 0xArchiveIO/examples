"""Download Hyperliquid OHLCV candles for any market and interval to CSV, every page.

    OXARCHIVE_API_KEY=... python3 candles_to_csv.py BTC 1h 2026-10-01 2026-11-01 > btc-1h.csv

Venues: pass --venue hip3 for HIP-3 markets (e.g. xyz:NVDA) or --venue lighter for Lighter.
Free keys read the most recent 30 days; Build and above read the full archive.
"""
import argparse
import csv
import sys

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
    params = {"interval": args.interval, "start": f"{args.start}T00:00:00Z", "end": f"{args.end}T00:00:00Z", "limit": 10000}
    writer = csv.DictWriter(sys.stdout, fieldnames=FIELDS, extrasaction="ignore")
    writer.writeheader()
    count = 0
    for row in pages(route, params, api_key()):
        if row["timestamp"] >= params["end"]:
            break  # the API includes a candle opening exactly at end; the window here is end-exclusive
        writer.writerow(row)
        count += 1
    print(f"{count} candles", file=sys.stderr)


if __name__ == "__main__":
    main()
