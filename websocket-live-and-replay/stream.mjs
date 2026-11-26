// Stream live trades, or replay any past window on the same socket, for Hyperliquid or Lighter.
//
//   OXARCHIVE_API_KEY=... node stream.mjs live trades BTC
//   OXARCHIVE_API_KEY=... node stream.mjs live lighter_trades BTC
//   OXARCHIVE_API_KEY=... node stream.mjs replay trades BTC "$(date -u -d yesterday +%F)T15:00:00Z" "$(date -u -d yesterday +%F)T15:01:00Z"
//
// Node 22 or newer (built-in WebSocket). Reconnects with backoff and re-subscribes after a drop (up to 8 times);
// exits on a refused key or subscription.
const key = process.env.OXARCHIVE_API_KEY;
if (!key) throw new Error('Set OXARCHIVE_API_KEY (create a key at https://0xarchive.io/dashboard).');
const [mode = 'live', channel = 'trades', symbol = 'BTC', start, end] = process.argv.slice(2);
const URL = 'wss://api.0xarchive.io/ws?version=2026-10-01';
let attempts = 0;
let received = 0;
let refused = false;
let done = false; // set before every intentional close, whatever close code the socket reports

function connect() {
  const socket = new WebSocket(URL, { headers: { Authorization: `Bearer ${key}` } });
  socket.onopen = () => {
    attempts = 0;
    const request = mode === 'replay'
      ? { op: 'replay', channel, symbol, start: Date.parse(start), end: Date.parse(end) }
      : { op: 'subscribe', channel, symbol };
    socket.send(JSON.stringify(request));
  };
  socket.onmessage = (event) => {
    const message = JSON.parse(String(event.data));
    switch (message.type) {
      case 'subscribed':
      case 'replay_started':
        console.error(`${message.type} ${channel} ${symbol}`);
        break;
      case 'data':
      case 'historical_data':
        received += Array.isArray(message.data) ? message.data.length : 1;
        console.log(JSON.stringify(message.data));
        if (mode === 'live' && received >= 20) { done = true; socket.close(1000); }
        break;
      case 'replay_completed':
        console.error(`replay completed: ${received} rows`);
        done = true;
        socket.close(1000);
        break;
      case 'error':
        console.error(`error ${message.error_code ?? ''}: ${message.message ?? JSON.stringify(message)}`);
        if (['unauthorized', 'forbidden'].includes(message.error_code)) {
          refused = true;
          done = true;
          socket.close(1000);
          process.exitCode = 1;
        }
        break;
      default:
        break;
    }
  };
  socket.onclose = (event) => {
    if (done || event.code === 1000) return;
    if (attempts >= 8) {
      console.error(`connection closed (${event.code}); giving up after 8 reconnects. Check the key and the plan.`);
      process.exitCode = 1;
      return;
    }
    const wait = Math.min(30_000, 1000 * 2 ** attempts++);
    console.error(`connection closed (${event.code}); reconnecting in ${wait / 1000}s`);
    setTimeout(connect, wait);
  };
}

connect();
