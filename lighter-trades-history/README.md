# Lighter trades history

Pull every Lighter (or Lighter on Robinhood Chain) trade for a window, write them to CSV and print taker buy and sell volume and VWAP.

Python 3.9 or newer, standard library only. Free keys read the most recent 30 days; Build and above read the full archive.

```bash
export OXARCHIVE_API_KEY=0xa_your_api_key
D=$(date -u -d '10 days ago' +%F)   # finalized Lighter history runs about a week behind; macOS: date -u -v-10d +%F
python3 lighter_trades.py BTC "${D}T15:00:00Z" "${D}T16:00:00Z" --csv btc-trades.csv
python3 lighter_trades.py AAPL "${D}T15:00:00Z" "${D}T16:00:00Z" --robinhood-chain
```

## Output

Each fill has a maker row and a taker row with the same trade_id; the taker row (crossed = true) carries the aggressor side, so the summary counts taker rows.
