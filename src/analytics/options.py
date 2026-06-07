"""
================================================================================
TBS (Trading Bot System) #1-#100 - Options Trading Framework
================================================================================
Copyright (c) 2025-2026 Richard Patterson (De-ASI-INTERFACE)
MIT License - see LICENSE file for full terms.
================================================================================
"""
from __future__ import annotations
import math
from dataclasses import dataclass
from scipy.stats import norm  # type: ignore

@dataclass
class OptionGreeks:
    delta: float
    gamma: float
    theta: float
    vega: float
    rho: float

def black_scholes(
    spot: float,
    strike: float,
    t: float,
    vol: float,
    rate: float,
    call: bool = True,
) -> float:
    """Black-Scholes option price."""
    if t <= 0 or vol <= 0:
        return max(0.0, spot - strike) if call else max(0.0, strike - spot)
    d1 = (math.log(spot / strike) + (rate + 0.5 * vol**2) * t) / (vol * math.sqrt(t))
    d2 = d1 - vol * math.sqrt(t)
    if call:
        return spot * norm.cdf(d1) - strike * math.exp(-rate * t) * norm.cdf(d2)
    return strike * math.exp(-rate * t) * norm.cdf(-d2) - spot * norm.cdf(-d1)

def compute_greeks(
    spot: float,
    strike: float,
    t: float,
    vol: float,
    rate: float,
    call: bool = True,
) -> OptionGreeks:
    """Compute all first-order Greeks."""
    if t <= 0 or vol <= 0:
        return OptionGreeks(0.0, 0.0, 0.0, 0.0, 0.0)
    sqrt_t = math.sqrt(t)
    d1 = (math.log(spot / strike) + (rate + 0.5 * vol**2) * t) / (vol * sqrt_t)
    d2 = d1 - vol * sqrt_t
    nd1 = norm.pdf(d1)
    delta = norm.cdf(d1) if call else norm.cdf(d1) - 1
    gamma = nd1 / (spot * vol * sqrt_t)
    theta_raw = (-(spot * nd1 * vol) / (2 * sqrt_t) - rate * strike * math.exp(-rate * t) * (norm.cdf(d2) if call else norm.cdf(-d2))) / 365
    vega = spot * nd1 * sqrt_t / 100
    rho = (strike * t * math.exp(-rate * t) * (norm.cdf(d2) if call else norm.cdf(-d2))) / 100
    return OptionGreeks(delta=round(delta, 6), gamma=round(gamma, 6), theta=round(theta_raw, 6), vega=round(vega, 6), rho=round(rho, 6))

def iv_percentile(current_iv: float, iv_history: list[float]) -> float:
    """IV Percentile: where current IV ranks vs historical IVs."""
    if not iv_history:
        return 0.0
    below = sum(1 for v in iv_history if v < current_iv)
    return round(below / len(iv_history) * 100, 2)
