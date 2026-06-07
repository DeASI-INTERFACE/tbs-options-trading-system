"""
================================================================================
TBS (Trading Bot System) #1-#100 - Options Trading Framework
================================================================================
Copyright (c) 2025-2026 Richard Patterson (De-ASI-INTERFACE)
MIT License - see LICENSE file for full terms.
================================================================================
"""
from __future__ import annotations
from dataclasses import dataclass, field
from loguru import logger
from src.core import TradeSignal, BotConfig

@dataclass
class ExecutionReport:
    accepted: bool
    reason: str
    bot_id: str
    signals: list[TradeSignal] = field(default_factory=list)

class TradingEngine:
    """Central execution engine for TBS options trading signals."""

    def __init__(self, config: BotConfig):
        self.config = config
        self._signals: list[TradeSignal] = []

    def submit_signal(self, signal: TradeSignal) -> ExecutionReport:
        if signal.expected_value <= 0:
            reason = "negative expected value — signal rejected"
            logger.warning(f"[{self.config.bot_id}] {reason}")
            return ExecutionReport(False, reason, self.config.bot_id)
        self._signals.append(signal)
        logger.info(f"[{self.config.bot_id}] Signal accepted: {signal.strategy} | EV={signal.expected_value:.4f}")
        return ExecutionReport(True, "signal accepted", self.config.bot_id, [signal])

    @property
    def signal_count(self) -> int:
        return len(self._signals)
