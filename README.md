# 0xArchive SDK Examples

Example data projects built with the [0xArchive Python SDK](https://pypi.org/project/oxarchive/).

## Projects

### [Liquidation Heatmap](liquidation-heatmap/)

A Jupyter notebook that visualizes BTC liquidation events on Hyperliquid. Includes:

- Price vs time heatmap of liquidation clusters
- Scatter plot with long/short coloring and price overlay
- Time-of-day and day-of-week analysis
- Liquidation size distribution
- Cascade detection (P99 burst events)
- Long vs short imbalance over time

**Quick start:**

```bash
cd liquidation-heatmap
pip install -r requirements.txt
cp .env.example .env        # then add your API key
jupyter notebook liquidation_heatmap.ipynb
```

Requires a free API key from [0xarchive.io/dashboard](https://0xarchive.io/dashboard).

### [Funding Rate Scanner](funding-rate-scanner/)

A Jupyter notebook that compares BTC funding rates across Hyperliquid and Lighter.xyz. Includes:

- Cross-exchange funding rate comparison (side-by-side line chart)
- Rate differential / spread with ±2σ threshold bands
- Annualized carry visualization (APR from rate differential)
- Arbitrage opportunity window detection
- Cumulative hypothetical P&L from spread-harvesting
- Distribution analysis with skew/kurtosis stats

**Quick start:**

```bash
cd funding-rate-scanner
pip install -r requirements.txt
cp .env.example .env        # then add your API key
jupyter notebook funding_rate_scanner.ipynb
```

Requires a free API key from [0xarchive.io/dashboard](https://0xarchive.io/dashboard).

## Requirements

- Python 3.10+
- Free tier: BTC only, 30-day lookback, 15 req/sec
