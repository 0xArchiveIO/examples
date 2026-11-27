# L4 order book at a chosen time

Rebuild the Hyperliquid or HIP-3 order book at a chosen time, order by order, and see the wallets resting the most size.

Python 3.9 or newer, standard library only. Free keys read the most recent 30 days; Build and above read the full archive, which starts 11 Mar 2026.

```bash
export OXARCHIVE_API_KEY=0xa_your_api_key
python3 l4_book.py BTC "$(date -u -d yesterday +%F)T15:00:00Z"
python3 l4_book.py xyz:NVDA "$(date -u -d yesterday +%F)T15:00:00Z" --hip3 --levels 5

# Build and above: older dates in the archive
python3 l4_book.py BTC 2026-06-01T00:00:00Z
```

## Output

The checkpoint and number of diffs applied, resting order counts per side, the best price levels with order counts, and the five largest wallets by resting dollars.
