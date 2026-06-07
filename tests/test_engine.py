"""Tests for execution engine — copyright De-ASI-INTERFACE"""
from src.bots.engine import TradingEngine
from src.core import BotConfig, TradeSignal, OrderType, OptionLeg, OptionType, TradeMode

def _make_config():
    return BotConfig(bot_id="tbs-001", strategy_name="test", trade_mode=TradeMode.PAPER)

def _make_signal(ev: float) -> TradeSignal:
    leg = OptionLeg("SPY", OptionType.CALL, 450.0, "2026-09-19", 1, "buy")
    return TradeSignal("SPY", "test", OrderType.DEBIT_SPREAD, [leg], 0.7, 100.0, 300.0, ev)

def test_accepts_positive_ev():
    eng = TradingEngine(_make_config())
    report = eng.submit_signal(_make_signal(0.15))
    assert report.accepted is True

def test_rejects_negative_ev():
    eng = TradingEngine(_make_config())
    report = eng.submit_signal(_make_signal(-0.10))
    assert report.accepted is False

def test_signal_count():
    eng = TradingEngine(_make_config())
    eng.submit_signal(_make_signal(0.1))
    eng.submit_signal(_make_signal(0.2))
    assert eng.signal_count == 2
