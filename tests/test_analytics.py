"""Tests for options analytics — copyright De-ASI-INTERFACE"""
import math
from src.analytics.options import black_scholes, compute_greeks, iv_percentile

def test_call_price_positive():
    price = black_scholes(100, 100, 0.25, 0.2, 0.05, call=True)
    assert price > 0

def test_put_call_parity():
    s, k, t, v, r = 100, 100, 0.25, 0.2, 0.05
    call = black_scholes(s, k, t, v, r, call=True)
    put = black_scholes(s, k, t, v, r, call=False)
    parity = call - put - (s - k * math.exp(-r * t))
    assert abs(parity) < 0.01

def test_greeks_delta_range():
    g = compute_greeks(100, 100, 0.25, 0.2, 0.05, call=True)
    assert 0 < g.delta < 1

def test_iv_percentile():
    hist = [0.2, 0.25, 0.30, 0.35]
    assert iv_percentile(0.28, hist) == 50.0

def test_zero_time_intrinsic_only():
    price = black_scholes(110, 100, 0, 0.2, 0.05, call=True)
    assert price == 10.0
