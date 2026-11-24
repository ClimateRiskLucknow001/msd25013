"""
Comprehensive Pytest Suite for MSD25013 Exam Capstone
Verifies all 6 blocks, validation, and sensitivity checks
"""
import os
import sys
import pytest
import pandas as pd
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, "..", "src"))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from exam_pipeline import (
    compute_portfolio_carbon, run_dcf_scenarios, 
    simulate_kariba_drought_loss, price_seychelles_blue_bond, 
    compute_composite_scores
)

@pytest.fixture
def sample_holdings():
    csv_path = os.path.join(os.path.dirname(src_dir), "data", "processed", "holdings_universe_cleaned.csv")
    return pd.read_csv(csv_path)

def test_carbon_waci_and_coverage(sample_holdings):
    res = compute_portfolio_carbon(sample_holdings)
    assert res["raw_coverage"] == 0.90  # 9 of 10 report
    assert res["effective_coverage"] == 1.0
    assert res["waci_equal_weighted"] > 500.0  # Driven by high-intensity materials
    assert res["top3_concentration_pct"] > 80.0 # High concentration in Sasol & Dangote

def test_dcf_scenario_sensitivity():
    ev_base = run_dcf_scenarios(8200.0, 512.2, scenario="baseline")
    ev_orderly = run_dcf_scenarios(8200.0, 512.2, scenario="orderly")
    ev_delayed = run_dcf_scenarios(8200.0, 512.2, scenario="delayed")
    
    assert ev_base > ev_orderly > ev_delayed
    pct_orderly = (ev_orderly / ev_base - 1) * 100
    pct_delayed = (ev_delayed / ev_base - 1) * 100
    assert -35.0 < pct_orderly < -15.0
    assert -50.0 < pct_delayed < -25.0

def test_kariba_loss_simulation_across_scenarios():
    base_res = simulate_kariba_drought_loss(climate_scenario="baseline")
    rcp45_res = simulate_kariba_drought_loss(climate_scenario="rcp45")
    rcp85_res = simulate_kariba_drought_loss(climate_scenario="rcp85")
    
    # Loss escalation with warming
    assert base_res["no_action"]["eal"] < rcp45_res["no_action"]["eal"] < rcp85_res["no_action"]["eal"]
    
    # Combined strategy effectiveness
    assert base_res["combined"]["eal"] < base_res["adaptation"]["eal"] < base_res["no_action"]["eal"]
    assert base_res["combined"]["p95"] < base_res["no_action"]["p95"] * 0.35 # >65% tail risk reduction

def test_blue_bond_pricing_and_stepup():
    p_met = price_seychelles_blue_bond(target_met=True)
    p_miss = price_seychelles_blue_bond(target_met=False)
    assert p_miss > p_met # Step-up coupon enhances cash flow to investor
    assert round(p_met, 2) == 83.04
    assert round(p_miss, 2) == 84.92

def test_multi_block_composite_ranking(sample_holdings):
    esg_series = pd.Series([6.5, 7.8, 5.2, 6.0, 5.8, 8.4, 8.1, 8.8, 7.2, 7.0])
    proc = compute_portfolio_carbon(sample_holdings)
    scores = compute_composite_scores(proc["df_processed"], esg_series)
    assert len(scores) == 10
    # Resilient financials must score higher than heavy emitters
    assert scores.iloc[7] > scores.iloc[2] # Nedbank > Sasol
