"""Tests for TBS bot registry — copyright De-ASI-INTERFACE"""
from src.bots.registry import BOT_REGISTRY, get_bot

def test_registry_has_100_bots():
    assert len(BOT_REGISTRY) == 100

def test_first_and_last():
    assert "tbs-001" in BOT_REGISTRY
    assert "tbs-100" in BOT_REGISTRY

def test_bot_ids_sequential():
    for i in range(1, 101):
        assert f"tbs-{i:03d}" in BOT_REGISTRY

def test_get_bot():
    b = get_bot("tbs-001")
    assert b.bot_id == "tbs-001"
    assert b.strategy == "directional_debit_spread"

def test_strategy_families():
    assert get_bot("tbs-041").strategy == "theta_harvest"
    assert get_bot("tbs-051").strategy == "gamma_scalping"
    assert get_bot("tbs-091").strategy == "tail_risk_macro"
