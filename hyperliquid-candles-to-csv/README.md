# Hyperliquid candles to CSV

Download OHLCV candles for any Hyperliquid, HIP-3 or Lighter market in any interval from 1m to 1w, following every page, to CSV.

Python 3.9 or newer, standard library only. Free keys read the most recent 30 days; Build and above read the full archive.

```bash
export OXARCHIVE_API_KEY=0xa_your_api_key
python3 candles_to_csv.py BTC 1h 2026-10-01 2026-11-01 > btc-1h.csv
python3 candles_to_csv.py xyz:NVDA 1d 2026-09-01 2026-11-01 --venue hip3 > nvda-1d.csv
python3 candles_to_csv.py ETH 15m 2026-11-01 2026-11-02 --venue lighter > eth-15m.csv
```

## Output

One CSV row per candle: timestamp, open, high, low, close, volume, quote_volume, trade_count. The progress count goes to stderr.
