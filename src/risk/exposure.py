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
from src.analytics.options import OptionGreeks

@dataclass
class PortfolioExposure:
    positions: list[OptionGreeks] = field(default_factory=list)

    @property
    def net_delta(self) -> float:
        return round(sum(g.delta for g in self.positions), 6)

    @property
    def net_gamma(self) -> float:
        return round(sum(g.gamma for g in self.positions), 6)

    @property
    def net_theta(self) -> float:
        return round(sum(g.theta for g in self.positions), 6)

    @property
    def net_vega(self) -> float:
        return round(sum(g.vega for g in self.positions), 6)

    def add_position(self, greeks: OptionGreeks) -> None:
        self.positions.append(greeks)

    def summary(self) -> dict:
        return {
            "net_delta": self.net_delta,
            "net_gamma": self.net_gamma,
            "net_theta": self.net_theta,
            "net_vega": self.net_vega,
            "position_count": len(self.positions),
        }
