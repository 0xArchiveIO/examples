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

**Requirements:** Free tier API key — [0xarchive.io/dashboard](https://0xarchive.io/dashboard)

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

**Requirements:** Free tier API key — [0xarchive.io/dashboard](https://0xarchive.io/dashboard)

### [HIP-3 Asset Dashboard](hip3-asset-dashboard/)

A Jupyter notebook that visualizes funding rates, open interest, and trade flow for HIP-3 builder perps on Hyperliquid. Includes:

- Funding rate time series with positive/negative shading and annualized APR view
- Funding rate distribution with skew/kurtosis statistics
- Open interest vs price overlay and OI rate-of-change analysis
- Buy/sell volume breakdown and cumulative volume delta
- Price action with volume bars and open interest
- Hourly volume profile (volume, fill count, avg fill size)
- Trade size distribution with summary statistics

**Quick start:**

```bash
cd hip3-asset-dashboard
pip install -r requirements.txt
cp .env.example .env        # then add your API key
jupyter notebook hip3_asset_dashboard.ipynb
```

**Requirements:** Pro+ API key — [0xarchive.io/dashboard](https://0xarchive.io/dashboard) (HIP-3 data is not available on the free tier)

## Requirements

- Python 3.10+
