# WebSocket live and replay

Stream live Hyperliquid or Lighter trades, or replay any past window on the same socket. Reconnects with backoff after a drop, up to 8 times, and exits on a refused key or subscription.

Node 22 or newer (built-in WebSocket), no packages.

```bash
export OXARCHIVE_API_KEY=0xa_your_api_key
node stream.mjs live trades BTC
node stream.mjs live lighter_trades BTC
D=$(date -u -d yesterday +%F)   # macOS: date -u -v-1d +%F
node stream.mjs replay trades BTC "${D}T15:00:00Z" "${D}T15:01:00Z"
```

## Output

One JSON array per message on stdout; connection events (`subscribed`, `replay_started`, `replay_completed`, errors) on stderr. Live mode stops after 20 trades; replay stops at `replay_completed`.

Free streams live for an account's first 30 days and replays the most recent 30 days; Build and above stream live and replay the full archive. Channel list: [WebSocket channels](https://docs.0xarchive.io/websocket/channels).
