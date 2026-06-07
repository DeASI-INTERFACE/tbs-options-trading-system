"""
================================================================================
TBS (Trading Bot System) #1-#100 - Options Trading Framework
================================================================================
Copyright (c) 2025-2026 Richard Patterson (De-ASI-INTERFACE)
MIT License - see LICENSE file for full terms.
VERSION: 1.0.0 | June 2026
================================================================================
"""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

class TradeMode(str, Enum):
    PAPER = "paper"
    LIVE = "live"
    BACKTEST = "backtest"

class OptionType(str, Enum):
    CALL = "call"
    PUT = "put"

class OrderType(str, Enum):
    MARKET = "market"
    LIMIT = "limit"
    DEBIT_SPREAD = "debit_spread"
    CREDIT_SPREAD = "credit_spread"
    IRON_CONDOR = "iron_condor"
    BUTTERFLY = "butterfly"
    CALENDAR = "calendar"
    DIAGONAL = "diagonal"
    RATIO = "ratio"
    CUSTOM = "custom"

@dataclass
class BotConfig:
    bot_id: str
    strategy_name: str
    symbols: list[str] = field(default_factory=list)
    max_daily_loss_pct: float = 0.02
    max_position_risk_pct: float = 0.01
    max_portfolio_delta: float = 0.30
    max_portfolio_vega: float = 0.50
    trade_mode: TradeMode = TradeMode.PAPER
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class OptionLeg:
    symbol: str
    option_type: OptionType
    strike: float
    expiration: str
    quantity: int
    side: str  # "buy" | "sell"

@dataclass
class TradeSignal:
    symbol: str
    strategy: str
    order_type: OrderType
    legs: list[OptionLeg]
    confidence: float
    max_loss: float
    max_gain: float
    expected_value: float
    metadata: dict[str, Any] = field(default_factory=dict)
