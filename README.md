# Kalshi BTC 15-Min Trading Bot

Autonomous trading bot using 3-edge mathematical system with Claude decision layer.

## Performance Dashboard
*Auto-updated nightly at 11:30 PM ET*

| Metric | Value |
|--------|-------|
| Start Date | 2026-02-10 |
| Total Cycles Monitored | 0 |
| Total Trades Executed | 0 |
| Win Rate | --% |
| Total P/L | $0.00 |
| Best Single Trade | $0.00 |
| Worst Single Trade | $0.00 |
| Skip Rate | --% |
| Avg Claude Confidence on Wins | --% |
| Avg Claude Confidence on Losses | --% |

## Edge Performance

| Edge Type | Trades | Wins | Losses | Win Rate | Total P/L |
|-----------|--------|------|--------|----------|-----------|
| Late-Window Lock | 0 | 0 | 0 | --% | $0.00 |
| Speed Advantage | 0 | 0 | 0 | --% | $0.00 |
| Volatility Mispricing | 0 | 0 | 0 | --% | $0.00 |

## Recent Daily Summaries
*See /daily for full reports*

## System Architecture

### Three Mathematical Edges
1. **Late-Window Lock** (Primary): Final 3-minute mathematical advantage
2. **Speed Advantage** (Secondary): Real-time Binance vs delayed Kalshi
3. **Volatility Mispricing** (Tertiary): Low volatility + 50/50 pricing arbitrage

### Data Pipeline
- Real-time BTC feeds (Binance/Coinbase)
- 30-second market analysis cycles  
- Mathematical edge detection (70% confidence threshold)
- Instant WhatsApp notifications
- Nightly GitHub commits with Claude analysis

### Repository Structure
```
kalshi-btc-trading/
├── README.md                    # This file (auto-updated)
├── daily/                      # Human-readable daily reports
├── trades/                     # Individual trade JSON files
├── cycles/                     # Daily cycle analysis data
├── analytics/                  # Weekly summaries and performance analysis
└── config/                     # Active trading parameters
```

Last updated: 2026-02-10T08:44:41.986505