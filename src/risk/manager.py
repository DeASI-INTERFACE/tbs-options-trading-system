"""
================================================================================
TBS (Trading Bot System) #1-#100 - Options Trading Framework
================================================================================
Copyright (c) 2025-2026 Richard Patterson (De-ASI-INTERFACE)
MIT License - see LICENSE file for full terms.
================================================================================
"""
from __future__ import annotations
from dataclasses import dataclass
from loguru import logger

@dataclass
class RiskMetrics:
    portfolio_delta: float = 0.0
    portfolio_gamma: float = 0.0
    portfolio_theta: float = 0.0
    portfolio_vega: float = 0.0
    drawdown_pct: float = 0.0
    open_risk_pct: float = 0.0

class RiskManager:
    """Greeks-aware trade approval and portfolio risk gating."""

    def __init__(
        self,
        max_daily_loss_pct: float = 0.02,
        max_position_risk_pct: float = 0.01,
        max_portfolio_delta: float = 0.30,
        max_portfolio_vega: float = 0.50,
    ):
        self.max_daily_loss_pct = max_daily_loss_pct
        self.max_position_risk_pct = max_position_risk_pct
        self.max_portfolio_delta = max_portfolio_delta
        self.max_portfolio_vega = max_portfolio_vega

    def approve_trade(self, expected_risk_pct: float, metrics: RiskMetrics) -> tuple[bool, str]:
        if metrics.drawdown_pct >= self.max_daily_loss_pct:
            msg = f"Daily loss limit hit: {metrics.drawdown_pct:.2%} >= {self.max_daily_loss_pct:.2%}"
            logger.warning(msg)
            return False, msg
        if expected_risk_pct > self.max_position_risk_pct:
            msg = f"Position too large: {expected_risk_pct:.2%} > {self.max_position_risk_pct:.2%}"
            logger.warning(msg)
            return False, msg
        if abs(metrics.portfolio_delta) + 0.05 > self.max_portfolio_delta:
            msg = "Portfolio delta would exceed limit"
            logger.warning(msg)
            return False, msg
        if abs(metrics.portfolio_vega) + 0.05 > self.max_portfolio_vega:
            msg = "Portfolio vega would exceed limit"
            logger.warning(msg)
            return False, msg
        return True, "approved"
