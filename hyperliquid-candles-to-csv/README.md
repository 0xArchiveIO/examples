# Hyperliquid candles to CSV

Download OHLCV candles for any Hyperliquid, HIP-3 or Lighter market in any interval from 1m to 1w, following every page, to CSV.

Python 3.9 or newer, standard library only. Free keys read the most recent 30 days; Build and above read the full archive.

```bash
export OXARCHIVE_API_KEY=0xa_your_api_key
python3 candles_to_csv.py BTC 1h "$(date -u -d '8 days ago' +%F)" "$(date -u +%F)" > btc-1h.csv
python3 candles_to_csv.py xyz:NVDA 1d "$(date -u -d '28 days ago' +%F)" "$(date -u +%F)" --venue hip3 > nvda-1d.csv
python3 candles_to_csv.py ETH 15m "$(date -u -d '2 days ago' +%F)" "$(date -u -d yesterday +%F)" --venue lighter > eth-15m.csv

# Build and above: any window back to the first candle (Hyperliquid from 2025-03-22)
python3 candles_to_csv.py BTC 1d 2025-04-01 2025-10-01 > btc-1d-2025.csv
```

The end date is exclusive: a window ending today stops at yesterday's last candle, the last day Free serves after an account's first 30 days. On macOS, write `date -u -v-8d +%F` for `date -u -d '8 days ago' +%F`.

## Output

One CSV row per candle: timestamp, open, high, low, close, volume, quote_volume, trade_count. The progress count goes to stderr.
