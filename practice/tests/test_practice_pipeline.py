"""
Unit tests for MSD25013 Practice Capstone
"""
import pytest
import pandas as pd
import numpy as np
from practice.src.pipeline import compute_waci, run_valuation_dcf, simulate_physical_loss, price_blue_bond

def test_waci_computation():
    df = pd.DataFrame({
        "weight": [0.25, 0.25, 0.25, 0.25],
        "emis_intensity_tco2_per_musd": [283.8, 512.2, 15.6, np.nan]
    })
    res = compute_waci(df, 95.0)
    assert res["raw_coverage"] == 0.75
    assert round(res["effective_waci"], 1) == 226.7

def test_valuation_sensitivity():
    base_ev = run_valuation_dcf(8200.0, 512.2, carbon_price=5.0)
    high_ev = run_valuation_dcf(8200.0, 512.2, carbon_price=120.0)
    assert base_ev > high_ev
    pct_impact = (high_ev / base_ev - 1) * 100
    assert -30.0 < pct_impact < -15.0

def test_physical_loss_simulation():
    res = simulate_physical_loss()
    assert res["adaptation"]["eal"] < res["no_action"]["eal"]
    assert res["combined"]["eal"] < res["insurance"]["eal"]
    assert res["combined"]["p95"] < res["no_action"]["p95"]

def test_blue_bond_pricing():
    p_met = price_blue_bond(target_met=True)
    p_miss = price_blue_bond(target_met=False)
    assert p_miss > p_met # Step-up coupon increases bond cash flows
