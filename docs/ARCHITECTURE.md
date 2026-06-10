# System Architecture — TBS #1–#100

> Copyright (c) 2025–2026 Richard Patterson (De-ASI-INTERFACE)

## Layers

**Strategy Layer** (`src/strategies/`) defines edge hypotheses. Each strategy extends `BaseOptionsStrategy` and implements `generate_signal()`. Strategies have no knowledge of execution or risk — they only evaluate market data and return a `TradeSignal` or `None`.

**Execution Layer** (`src/bots/engine.py`) receives signals, applies pre-flight EV checks, routes to the broker adapter, and logs execution reports.

**Risk Layer** (`src/risk/`) gates every trade against daily loss limits, position sizing, portfolio delta, and vega exposure. No signal bypasses the risk manager.

**Analytics Layer** (`src/analytics/`) provides pricing, Greeks computation, IV percentile, term structure, and skew — used by strategies and risk alike.

## Bot Registry

`BOT_REGISTRY` maps `tbs-001` through `tbs-100` to strategy families. Adding a new strategy means: create a `BaseOptionsStrategy` subclass, register it, and assign bot IDs.

## Data Flow

```
Market Data Feed
      ↑
BaseOptionsStrategy.generate_signal()
      ↓
RiskManager.approve_trade()
      ↓
TradingEngine.submit_signal()
      ↓
Broker Adapter (stub — wire to IBKR / Tastytrade / etc.)
```
