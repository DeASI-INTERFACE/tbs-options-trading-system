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

STRATEGY_MAP = {
    range(1, 11): "directional_debit_spread",
    range(11, 21): "volatility_mean_reversion",
    range(21, 31): "earnings_event_structure",
    range(31, 41): "skew_dislocation",
    range(41, 51): "theta_harvest",
    range(51, 61): "gamma_scalping",
    range(61, 71): "calendar_diagonal",
    range(71, 81): "iron_condor_butterfly",
    range(81, 91): "ratio_backspread",
    range(91, 101): "tail_risk_macro",
}

def _get_strategy(n: int) -> str:
    for r, strat in STRATEGY_MAP.items():
        if n in r:
            return strat
    return "unassigned"

@dataclass
class BotDefinition:
    bot_id: str
    name: str
    strategy: str
    description: str

BOT_REGISTRY: dict[str, BotDefinition] = {
    f"tbs-{i:03d}": BotDefinition(
        bot_id=f"tbs-{i:03d}",
        name=f"TBS Bot #{i}",
        strategy=_get_strategy(i),
        description=f"Options trading node #{i} — strategy: {_get_strategy(i)}"
    )
    for i in range(1, 101)
}

def get_bot(bot_id: str) -> BotDefinition:
    if bot_id not in BOT_REGISTRY:
        raise KeyError(f"Unknown bot ID: {bot_id}")
    return BOT_REGISTRY[bot_id]
