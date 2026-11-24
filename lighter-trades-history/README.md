# Lighter trades history

Pull every Lighter (or Lighter on Robinhood Chain) trade for a window, write them to CSV and print taker buy and sell volume and VWAP.

Python 3.9 or newer, standard library only. Free keys read the most recent 30 days; Build and above read the full archive.

```bash
export OXARCHIVE_API_KEY=0xa_your_api_key
python3 lighter_trades.py BTC 2026-11-10T15:00:00Z 2026-11-10T16:00:00Z --csv btc-trades.csv
python3 lighter_trades.py AAPL 2026-11-10T15:00:00Z 2026-11-10T16:00:00Z --robinhood-chain
```

## Output

Each fill has a maker row and a taker row with the same trade_id; the taker row (crossed = true) carries the aggressor side, so the summary counts taker rows.
