<!--
  OWNERSHIP: Richard Patterson (Entrepreneur & Trader, Akron, OH)
  PROJECT: TBS Options Trading System — 100-Bot Institutional Series
  COPYRIGHT: © 2026 Richard Patterson. All Rights Reserved.
  LICENSE: Proprietary. Unauthorized reproduction prohibited.
-->

# TBS Options Trading System

> **© 2026 Richard Patterson. All Rights Reserved.**  
> TBS #1–#100 | Institutional-Grade Options Bot Series — De-ASI-INTERFACE

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Solana](https://img.shields.io/badge/Solana-Options-purple)
![Series](https://img.shields.io/badge/Bot%20Series-TBS%20%231--100-brightgreen)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-success)
![License](https://img.shields.io/badge/License-Proprietary-red)

A 100-bot institutional options trading system engineered for Greeks analytics, implied volatility surface modeling, multi-leg strategy execution, and real-time risk management. Each bot in the TBS series is purpose-built for a specific options strategy or market regime.

---

## System Overview
## System Architecture

```
TBS Options Engine
  ├── Greeks Analytics Module    — Delta, Gamma, Theta, Vega, Rho per position
  ├── IV Surface Modeler         — Real-time implied volatility surface construction
  ├── Multi-Leg Strategy Engine  — Spreads, straddles, iron condors, calendars
  ├── Risk Manager               — Greeks-based exposure limits, drawdown guards
  └── Execution Layer            — Order routing with slippage controls

src/
  core.py             # BotConfig, TradeSignal, TradeMode
  bots/
    registry.py       # TBS-001 to TBS-100 bot definitions
    engine.py         # Execution engine + signal routing
  analytics/
    options.py        # Black-Scholes, Greeks, IV percentile
    volatility.py     # IV surface + skew analytics
  risk/
    manager.py        # Greeks-aware trade approval
    exposure.py       # Portfolio-level risk aggregation
  strategies/
    base.py           # Abstract base strategy
    spreads.py        # Vertical, calendar, diagonal
    volatility.py     # Long/short vol playbooks
    theta_harvest.py  # Defined-risk premium selling
config/
  default.yaml        # Default bot configuration
tests/
  test_registry.py
  test_risk.py
  test_analytics.py
  test_engine.py
.github/workflows/
  ci.yml              # Lint + test on every push/PR
docs/
  ARCHITECTURE.md
  STRATEGY_GUIDE.md
```

---

## Bot Series Index

| Range | Focus Area |
|---|---|
| TBS #1–#10 | Core Greeks analytics and single-leg execution |
| TBS #11–#25 | Multi-leg spreads (verticals, straddles, strangles) |
| TBS #26–#50 | IV surface modeling and term structure strategies |
| TBS #51–#75 | Regime-conditioned strategy selection |
| TBS #76–#100 | Portfolio-level Greeks hedging and risk orchestration |
| Range | Strategy Family |
|---|---|
| TBS #001–#010 | Directional Debit Spreads |
| TBS #011–#020 | Volatility Mean Reversion |
| TBS #021–#030 | Earnings Event Structures |
| TBS #031–#040 | Skew Dislocation Plays |
| TBS #041–#050 | Theta Harvest / Premium Selling |
| TBS #051–#060 | Gamma Scalping |
| TBS #061–#070 | Calendar & Diagonal Structures |
| TBS #071–#080 | Iron Condors & Butterflies |
| TBS #081–#090 | Ratio Spreads & Backspreads |
| TBS #091–#100 | Hedged Tail Risk / Macro Positioning |

---

## Core Capabilities

- **Greeks Analytics** — Real-time per-position delta, gamma, theta, vega, rho calculation
- **IV Surface Modeling** — Volatility smile construction across strikes and expirations
- **Multi-Leg Strategies** — Automated entry/exit for complex options structures
- **Real-Time Risk Management** — Greeks-based position limits and drawdown enforcement
- **Regime Detection** — Adaptive strategy selection based on market volatility regime
- **Greeks Analytics** — Real-time per-position delta, gamma, theta, vega, rho via Black-Scholes
- **IV Surface Modeling** — Volatility smile and skew construction across strikes and expirations
- **Multi-Leg Strategies** — Automated entry/exit for vertical spreads, straddles, iron condors, diagonals
- **Real-Time Risk Management** — Greeks-based position limits and drawdown enforcement
- **Regime Detection** — Adaptive strategy selection based on market volatility regime
- **CI/CD Gate** — GitHub Actions lint + test on every push and PR

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Analytics | NumPy, SciPy (Black-Scholes, Greeks, IV) |
| State | Redis for position and risk state persistence |
| Observability | Prometheus + Grafana dashboard |
| CI/CD | GitHub Actions |
| Deployment | Docker Compose |

---

## Quick Start

```bash
git clone https://github.com/De-ASI-INTERFACE/tbs-options-trading-system
cd tbs-options-trading-system
git checkout Richy
cp .env.example .env
# Configure API keys and risk parameters in .env
pip install -r requirements.txt
python main.py
```

---

## Environment Variables

```bash
# Exchange credentials
API_KEY=your_api_key
API_SECRET=your_api_secret

# Risk parameters
MAX_PORTFOLIO_DELTA=100
MAX_DRAWDOWN=0.10
POSITION_SIZE_LIMIT=0.05

# Observability
PROMETHEUS_PORT=8001
LOG_LEVEL=INFO
LOG_JSON=true

# Redis
REDIS_URL=redis://localhost:6379/1
```

---

## Risk Disclosure

Options trading involves significant risk and is not suitable for all investors. Leverage amplifies both gains and losses. This system is provided for research and development purposes only. Past performance is not indicative of future results. Never deploy capital you cannot afford to lose. Consult a licensed financial advisor before trading options.

---

## Roadmap

- [ ] Complete TBS #001–#010 core Greeks analytics bots
- [ ] IV surface modeling module (TBS #026–#050)
- [ ] Regime detection integration
- [ ] Portfolio-level Greeks hedging orchestrator
- [ ] Full 100-bot series deployment

---

*© 2026 Richard Patterson. All Rights Reserved.*  
*Built in Akron, Ohio. Engineered for institutional-grade options execution.*  
*Unauthorized reproduction or distribution of this software is strictly prohibited.*
