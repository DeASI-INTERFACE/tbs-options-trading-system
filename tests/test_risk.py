"""Tests for risk manager — copyright De-ASI-INTERFACE"""
from src.risk.manager import RiskManager, RiskMetrics

def test_blocks_on_drawdown():
    rm = RiskManager(max_daily_loss_pct=0.02)
    ok, msg = rm.approve_trade(0.005, RiskMetrics(drawdown_pct=0.03))
    assert ok is False
    assert "Daily loss" in msg

def test_allows_small_position():
    rm = RiskManager()
    ok, msg = rm.approve_trade(0.005, RiskMetrics())
    assert ok is True

def test_blocks_oversized_position():
    rm = RiskManager(max_position_risk_pct=0.01)
    ok, msg = rm.approve_trade(0.05, RiskMetrics())
    assert ok is False

def test_blocks_delta_breach():
    rm = RiskManager(max_portfolio_delta=0.30)
    ok, msg = rm.approve_trade(0.005, RiskMetrics(portfolio_delta=0.29))
    assert ok is False
