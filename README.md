# 0xArchive Examples

Notebook projects that turn 0xArchive market data into working analysis.

0xArchive is granular market data infrastructure for Hyperliquid and Lighter.xyz. Hyperliquid includes core perps, HIP-3 builder perps, HIP-4 outcome markets, and Hyperliquid Spot; Lighter.xyz is the second top-level venue API. Use these examples when you want proof before wiring an SDK, building an API loop, or exporting Parquet from the Data Catalog.

## Start Here

1. Create an account at [0xArchive signup](https://www.0xarchive.io/signup).
2. Copy an API key from the dashboard.
3. Choose the notebook that matches the dataset you want to inspect.
4. Run the notebook once before adapting it into a pipeline.

```bash
cp .env.example .env
# Add OXARCHIVE_API_KEY=0xa_your_api_key to .env
```

## Projects

| Project | Dataset | Venue scope | Tier | First output |
| --- | --- | --- | --- | --- |
| [Liquidation Heatmap](liquidation-heatmap/) | Liquidation events and price context | Hyperliquid | Free key for supported BTC workflows | Heatmap and scatter views of BTC liquidation clusters |
| [Funding Rate Scanner](funding-rate-scanner/) | Funding rates and spread calculations | Hyperliquid and Lighter.xyz | Free key for supported BTC workflows | Cross-venue funding chart, spread bands, and carry view |
| [HIP-3 Asset Dashboard](hip3-asset-dashboard/) | Funding, open interest, trades, candles | Hyperliquid HIP-3 | Free key for HIP-3 workflows | Dashboard for builder-perp price, flow, and derivatives context |

## Liquidation Heatmap

```bash
cd liquidation-heatmap
pip install -r requirements.txt
cp .env.example .env
jupyter notebook liquidation_heatmap.ipynb
```

Outputs:

- Price-vs-time liquidation heatmap
- Long/short liquidation scatter plot
- Time-of-day and day-of-week views
- Size distribution and P99 cascade detection

## Funding Rate Scanner

```bash
cd funding-rate-scanner
pip install -r requirements.txt
cp .env.example .env
jupyter notebook funding_rate_scanner.ipynb
```

Outputs:

- Hyperliquid vs Lighter funding comparison
- Funding spread with two-standard-deviation bands
- Annualized carry view
- Opportunity window and distribution summaries

## HIP-3 Asset Dashboard

```bash
cd hip3-asset-dashboard
pip install -r requirements.txt
cp .env.example .env
jupyter notebook hip3_asset_dashboard.ipynb
```

Outputs:

- Hyperliquid HIP-3 funding, open interest, and trade-flow views
- Funding distribution and annualized APR view
- Volume, fill-count, and trade-size summaries
- Price, volume, and open-interest overlays

## Choose Your Next Path

| If you want... | Go here |
| --- | --- |
| A recurring API loop | [SDK docs](https://www.0xarchive.io/docs/sdks) |
| A shell or agent workflow | [CLI docs](https://www.0xarchive.io/docs/cli) |
| Claude Code, ChatGPT Codex, or other coding-agent context | [AI Clients](https://www.0xarchive.io/docs/ai-clients) |
| File-based historical pulls | [Data Catalog](https://www.0xarchive.io/data) |
| Route, schema, and auth details | [Quick Start](https://www.0xarchive.io/docs/quick-start), [OpenAPI](https://www.0xarchive.io/openapi.json), [llms.txt](https://www.0xarchive.io/llms.txt) |

## Links

- [API Docs](https://www.0xarchive.io/docs)
- [Python SDK](https://pypi.org/project/oxarchive/)
- [TypeScript SDK](https://npmjs.com/package/@0xarchive/sdk)
- [Rust SDK](https://crates.io/crates/oxarchive)
- [CLI](https://npmjs.com/package/@0xarchive/cli)
- [MCP Server](https://mcp.0xarchive.io) (or [self-host](https://npmjs.com/package/@0xarchive/mcp-server))
- [0xArchive Skill](https://github.com/0xArchiveIO/0xarchive-skill)

## Requirements

- Python 3.10+
- Jupyter Notebook
- An 0xArchive API key

No notebook should require secrets in source control. Keep API keys in local `.env` files only.
