"""Rebuild the Hyperliquid order book at any instant, order by order, with the wallet behind each order.

    OXARCHIVE_API_KEY=... python3 l4_book.py BTC "$(date -u -d yesterday +%F)T15:00:00Z" --orders 10

Shows the best levels and the largest wallets by resting size.
HIP-3 markets: pass --hip3 (e.g. xyz:NVDA). L4 history starts 2026-03-11.
"""
import argparse
from collections import Counter
from datetime import datetime

from oxa import api_key, get


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("symbol")
    parser.add_argument("at", help="ISO time, e.g. 2026-11-10T15:00:00Z")
    parser.add_argument("--orders", type=int, default=200, help="orders per side to read from the best price")
    parser.add_argument("--levels", type=int, default=8, help="price levels per side to print")
    parser.add_argument("--hip3", action="store_true")
    args = parser.parse_args()
    at = int(datetime.fromisoformat(args.at.replace("Z", "+00:00")).timestamp() * 1000)
    route = f"/hyperliquid/{'hip3/' if args.hip3 else ''}orderbook/{args.symbol}/l4"
    book = get(route, {"timestamp": at, "depth": args.orders}, api_key())["data"]
    print(f"{args.symbol} at {book['timestamp']} (checkpoint {book['checkpoint_timestamp']} + {book['diffs_applied']} diffs)")
    print(f"resting orders: {book['bid_count']} bids, {book['ask_count']} asks")
    for side in ("asks", "bids"):
        levels = Counter()
        for order in book[side]:
            levels[order["price"]] += order["size"]
        best = sorted(levels, reverse=(side == "bids"))[: args.levels]
        print(f"\n{side} (best {len(best)} levels)")
        for price in sorted(best, reverse=True):
            count = sum(1 for order in book[side] if order["price"] == price)
            print(f"  {price:>12}  {levels[price]:>12.5f}  {count} orders")
    wallets = Counter()
    for order in book["bids"] + book["asks"]:
        wallets[order["user_address"]] += order["size"] * order["price"]
    print(f"\nlargest wallets in the best {args.orders} orders per side (USD resting)")
    for wallet, usd in wallets.most_common(5):
        print(f"  {wallet}  {usd:,.0f}")


if __name__ == "__main__":
    main()
