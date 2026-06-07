# TBS #1–#100 Options Trading System

> **Copyright (c) 2025–2026 Richard Patterson (De-ASI-INTERFACE)**
> Licensed under MIT — see [LICENSE](./LICENSE) for full terms.

Institutional-grade options-only trading bot framework built as a 100-bot series (TBS #1–#100). Engineered for production deployment with strict risk controls, options Greeks analytics, IV surface modeling, multi-leg strategy templates, and GitHub Actions CI/CD.

---

## Architecture Overview

```
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

## Bot Series (TBS #1–#100)

Each bot ID (`tbs-001` through `tbs-100`) maps to a dedicated strategy slot.

| Range | Strategy Family |
|---|---|
| #001–#010 | Directional Debit Spreads |
| #011–#020 | Volatility Mean Reversion |
| #021–#030 | Earnings Event Structures |
| #031–#040 | Skew Dislocation Plays |
| #041–#050 | Theta Harvest / Premium Selling |
| #051–#060 | Gamma Scalping |
| #061–#070 | Calendar & Diagonal Structures |
| #071–#080 | Iron Condors & Butterflies |
| #081–#090 | Ratio Spreads & Backspreads |
| #091–#100 | Hedged Tail Risk / Macro Positioning |

---

## Quick Start

```bash
git clone https://github.com/De-ASI-INTERFACE/tbs-options-trading-system
cd tbs-options-trading-system
pip install -e .[dev]
pytest -q
```

---

## Risk Disclaimer

This software is not financial advice. Options trading involves substantial risk of loss. Always paper trade before going live. Use hard position-size limits and daily loss caps.

---

## License & Copyright

MIT License — see [LICENSE](./LICENSE).
Proprietary trading logic and strategies are confidential IP of De-ASI-INTERFACE.
