"""
================================================================================
TBS (Trading Bot System) #1-#100 - Options Trading Framework
================================================================================
Copyright (c) 2025-2026 Richard Patterson (De-ASI-INTERFACE)
MIT License - see LICENSE file for full terms.
================================================================================
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from src.core import TradeSignal, BotConfig

class BaseOptionsStrategy(ABC):
    """Abstract base for all TBS strategy implementations."""

    def __init__(self, config: BotConfig):
        self.config = config

    @abstractmethod
    def generate_signal(self, market_data: dict) -> TradeSignal | None:
        """Evaluate market data and return a signal, or None if no edge."""
        ...

    @abstractmethod
    def describe(self) -> str:
        """Return a human-readable description of the strategy."""
        ...
