"""Pull every Lighter trade for a market and window, with taker buy/sell volume and VWAP.

    OXARCHIVE_API_KEY=... python3 lighter_trades.py BTC "$(date -u -d '10 days ago' +%F)T15:00:00Z" "$(date -u -d '10 days ago' +%F)T16:00:00Z" --csv btc-trades.csv

Lighter trades are served once finalized; meta.finalized_through says how far that is.
Every fill has two rows, the maker's and the taker's, sharing trade_id. The taker row (crossed = true) carries the
aggressor side, so volume and counts below use taker rows only.
"""
import argparse
import csv
from datetime import datetime

from oxa import api_key, pages


def millis(value):
    return int(datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp() * 1000)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("symbol")
    parser.add_argument("start", help="ISO time, e.g. 2026-11-10T15:00:00Z")
    parser.add_argument("end", help="ISO time")
    parser.add_argument("--csv", help="write every trade to this file")
    parser.add_argument("--robinhood-chain", action="store_true", help="read Lighter on Robinhood Chain (e.g. AAPL)")
    args = parser.parse_args()
    venue = "rh-lighter" if args.robinhood_chain else "lighter"
    params = {"start": millis(args.start), "end": millis(args.end), "limit": 50000}
    rows = list(pages(f"/{venue}/trades/{args.symbol}", params, api_key()))
    if args.csv and rows:
        with open(args.csv, "w", newline="") as handle:
            fields = list(dict.fromkeys(key for row in rows for key in row))
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
    takers = [r for r in rows if r.get("crossed")]
    buys = sum(float(r["size"]) for r in takers if r["side"] == "B")
    sells = sum(float(r["size"]) for r in takers if r["side"] == "A")
    notional = sum(float(r["size"]) * float(r["price"]) for r in takers)
    size = buys + sells
    print(f"{len(takers)} fills ({len(rows)} rows)  taker buy {buys:.4f}  taker sell {sells:.4f}  vwap {notional / size:.2f}" if size else "no trades in window")


if __name__ == "__main__":
    main()
