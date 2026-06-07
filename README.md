<!-- Copyright (c) 2026 De-ASI-INTERFACE / Richard Patterson - MIT License -->

# TBS Options Trading System
### TBS #1 - TBS #100 | Institutional-Grade Options Bot Series

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-blue.svg)](https://www.typescriptlang.org/)
[![Node.js](https://img.shields.io/badge/Node.js-20+-green.svg)](https://nodejs.org/)
[![CI](https://github.com/De-ASI-INTERFACE/tbs-options-trading-system/actions/workflows/ci.yml/badge.svg)](https://github.com/De-ASI-INTERFACE/tbs-options-trading-system/actions)

---

## Overview

**TBS** (Trading Bot System) is a 100-bot options-only trading architecture built to institutional standards. Each numbered bot (`TBS-001` through `TBS-100`) is a self-contained strategy module that inherits the shared core engine, risk layer, and execution infrastructure.

| Layer | Purpose |
|---|---|
| **Core Engine** | Greeks calculation, IV surface, Black-Scholes/Binomial pricing |
| **Risk Manager** | Delta/Gamma/Vega/Theta limits, portfolio-level drawdown circuit breakers |
| **Strategy Bus** | Hot-swappable strategy modules (TBS-001 to TBS-100) |
| **Execution Layer** | Smart order routing, multi-leg spread execution, slippage modeling |
| **Data Layer** | Real-time option chain ingestion, historical vol surface reconstruction |
| **Monitoring** | Grafana dashboards, Prometheus metrics, structured JSON logging |

---

## Architecture

```
tbs-options-trading-system/
├── src/
│   ├── core/              # Engine: pricing, Greeks, IV surface
│   ├── risk/              # Risk manager, position limits, circuit breakers
│   ├── strategies/        # TBS-001 through TBS-100 strategy modules
│   ├── execution/         # Order router, broker adapters, fill tracking
│   ├── data/              # Market data feeds, option chain normalization
│   ├── monitoring/        # Metrics, alerts, Grafana integration
│   └── utils/             # Math, date helpers, logger
├── tests/                 # Unit + integration tests (Jest)
├── .github/workflows/     # CI/CD pipelines
├── docker/                # Dockerfiles + compose
├── configs/               # Per-bot YAML configs
└── src/scripts/           # Bot launcher, backtest runner, health check
```

---

## Quick Start

```bash
# Install
npm install

# Configure
cp configs/tbs-001.example.yml configs/tbs-001.yml

# Run a single bot
npm run bot -- --id 1

# Run tests
npm test

# Backtest TBS-001
npm run backtest -- --id 1 --from 2025-01-01 --to 2025-12-31
```

---

## Strategy Taxonomy (TBS-001 to TBS-100)

| Range | Strategy Family |
|---|---|
| TBS-001-010 | Volatility Arbitrage (IV Rank / IV Percentile) |
| TBS-011-020 | Delta-Neutral Theta Decay (Iron Condors, Butterflies) |
| TBS-021-030 | Directional Spreads (Debit/Credit Vertical Spreads) |
| TBS-031-040 | Calendar & Diagonal Spreads |
| TBS-041-050 | Earnings Volatility Plays |
| TBS-051-060 | VWAP / Order Flow Mean Reversion |
| TBS-061-070 | Gamma Scalping |
| TBS-071-080 | Long Volatility / Tail Risk Hedging |
| TBS-081-090 | Ratio Spreads & Backspreads |
| TBS-091-100 | ML-Enhanced Signal Strategies |

---

## Risk Framework

All bots share a hard risk envelope enforced at the portfolio level:

- **Max Portfolio Delta**: configurable per-account notional
- **Max Single-Position Vega**: 2% of NAV
- **Daily Drawdown Circuit Breaker**: halts all bots at configurable % loss
- **Gamma Spike Protection**: auto-flattens positions when gamma exceeds threshold
- **Theta Floor**: minimum daily theta collection requirement per bot class

---

## Copyright

Copyright (c) 2026 De-ASI-INTERFACE / Richard Patterson. All rights reserved.
See [LICENSE](LICENSE) and [NOTICE](NOTICE) for details.

> **Risk Disclaimer**: Options trading involves substantial risk of loss.
> This software is for research purposes only. Trade at your own risk.
