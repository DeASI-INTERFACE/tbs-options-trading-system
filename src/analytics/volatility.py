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
import numpy as np

@dataclass
class IVSurfacePoint:
    strike: float
    expiration_days: int
    implied_vol: float

def compute_skew(calls: list[float], puts: list[float]) -> float:
    """Simple 25-delta skew estimate."""
    if not calls or not puts:
        return 0.0
    return float(np.mean(puts) - np.mean(calls))

def term_structure_slope(iv_near: float, iv_far: float, days_near: int, days_far: int) -> float:
    """Annualized term structure slope."""
    delta_days = days_far - days_near
    if delta_days == 0:
        return 0.0
    return (iv_far - iv_near) / delta_days * 365
