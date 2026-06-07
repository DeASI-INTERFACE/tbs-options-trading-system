"""
================================================================================
TBS (Trading Bot System) #1-#100 - Options Trading Framework
================================================================================
Copyright (c) 2025-2026 Richard Patterson (De-ASI-INTERFACE)
MIT License - see LICENSE file for full terms.
================================================================================
"""
from __future__ import annotations
from src.core import BotConfig, TradeSignal
from src.strategies.base import BaseOptionsStrategy

class ThetaHarvestStrategy(BaseOptionsStrategy):
    """Defined-risk premium selling. TBS #041-#050 family."""

    def generate_signal(self, market_data: dict) -> TradeSignal | None:
        iv_pct = market_data.get("iv_percentile", 0)
        if iv_pct < 50:
            return None  # Only sell premium in elevated IV environments
        return None  # Stub — wire to broker legs

    def describe(self) -> str:
        return "Theta Harvest — sell premium in high-IV environments with defined max loss"
