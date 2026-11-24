"""
Comprehensive Analytical Engine for MSD25013 Exam Capstone
Academic Year 2026 - Handout V003
Region: Sub-Saharan Africa
Sectors: Materials & Financials
Focal Asset: Lake Kariba Hydropower Reservoir (Drought Hazard)
Focal Bond: Republic of Seychelles Sovereign Blue Bond
"""

import numpy as np
import pandas as pd

def compute_portfolio_carbon(holdings_df: pd.DataFrame, default_missing_intensity: float = 35.0):
    df = holdings_df.copy()
    raw_coverage = float(df["emis_intensity_tco2_per_musd"].notna().mean())
    df["emis_intensity_imputed"] = df["emis_intensity_tco2_per_musd"].fillna(default_missing_intensity)
    
    # Equal-weighted WACI
    waci_eq = float(np.sum(df["weight"] * df["emis_intensity_imputed"]))
    
    # Market-cap weighted WACI
    mcap_weights = df["market_cap_musd"] / df["market_cap_musd"].sum()
    waci_mcap = float(np.sum(mcap_weights * df["emis_intensity_imputed"]))
    
    # Carbon Concentration
    df_sorted = df.sort_values("emis_intensity_imputed", ascending=False)
    top3_share = float(df_sorted.iloc[:3]["emis_intensity_imputed"].sum() / df["emis_intensity_imputed"].sum())
    
    return {
        "raw_coverage": raw_coverage,
        "effective_coverage": 1.0,
        "waci_equal_weighted": round(waci_eq, 2),
        "waci_mcap_weighted": round(waci_mcap, 2),
        "top3_concentration_pct": round(top3_share * 100, 2),
        "df_processed": df
    }

def run_dcf_scenarios(revenue_musd: float, emis_intensity: float, 
                      scenario: str = "orderly", wacc: float = 0.095, 
                      g: float = 0.02, pass_through: float = 0.40, 
                      tax: float = 0.27, horizon_years: int = 10):
    yr = np.arange(1, horizon_years + 1)
    rev = revenue_musd * (1.025) ** yr
    ebit = rev * 0.18
    annual_emis_kt = emis_intensity * revenue_musd / 1e3
    
    if scenario == "baseline":
        carbon_prices = np.full(horizon_years, 5.0)
    elif scenario == "orderly":
        # Rises from $10/t to $120/t by year 10
        carbon_prices = np.linspace(10.0, 120.0, horizon_years)
    elif scenario == "delayed":
        # Flat at $15/t until year 5, then spikes to $180/t by year 10
        carbon_prices = np.concatenate([np.full(5, 15.0), np.linspace(30.0, 180.0, 5)])
    else:
        raise ValueError(f"Unknown scenario {scenario}")
        
    carbon_costs = (annual_emis_kt * carbon_prices / 1e3) * (1 - pass_through)
    fcf = ebit * (1 - tax) - (revenue_musd * 0.07) - carbon_costs
    disc = (1 + wacc) ** yr
    ev = (fcf / disc).sum() + (fcf[-1] * (1 + g) / (wacc - g)) / disc[-1]
    return float(ev)

def simulate_kariba_drought_loss(asset_value: float = 100.0, n_sims: int = 50000, 
                                 climate_scenario: str = "baseline", 
                                 adapt_reduction: float = 0.45, 
                                 attach: float = 5.0, limit: float = 25.0, 
                                 seed: int = 25013):
    rng = np.random.default_rng(seed)
    
    # Drought frequency by climate scenario
    p_drought = {
        "baseline": 0.15,   # Historical 1-in-6.7 year recurrence
        "rcp45": 0.22,      # NGFS SSP2-4.5 2035 projection
        "rcp85": 0.31       # NGFS SSP5-8.5 2045 projection
    }.get(climate_scenario, 0.15)
    
    # Severity distribution
    sev = np.clip(rng.normal(0.38, 0.15, n_sims), 0.05, 0.95)
    drought_occurred = (rng.random(n_sims) < p_drought)
    base_loss = sev * drought_occurred * asset_value
    
    loss_adapt = base_loss * (1 - adapt_reduction)
    retained_ins = base_loss - np.clip(base_loss - attach, 0, limit)
    retained_comb = loss_adapt - np.clip(loss_adapt - attach, 0, limit)
    
    def calc_metrics(arr):
        return {
            "eal": round(float(arr.mean()), 2),
            "p90": round(float(np.percentile(arr, 90)), 2),
            "p95": round(float(np.percentile(arr, 95)), 2),
            "p99": round(float(np.percentile(arr, 99)), 2),
            "max_loss": round(float(arr.max()), 2)
        }
        
    basis_risk = float((base_loss - np.clip(base_loss - attach, 0, limit)).mean() - retained_ins.mean())
    
    return {
        "scenario": climate_scenario,
        "p_drought": p_drought,
        "no_action": calc_metrics(base_loss),
        "adaptation": calc_metrics(loss_adapt),
        "insurance": calc_metrics(retained_ins),
        "combined": calc_metrics(retained_comb),
        "basis_risk_indicator": round(float((base_loss - np.clip(base_loss - attach, 0, limit)).mean()), 2),
        "raw_losses": {
            "no_action": base_loss,
            "adaptation": loss_adapt,
            "insurance": retained_ins,
            "combined": retained_comb
        }
    }

def price_seychelles_blue_bond(face: float = 100.0, coupon: float = 0.0325, 
                               step: float = 0.0025, mat: int = 10, 
                               yld: float = 0.055, target_met: bool = True):
    c = coupon if target_met else coupon + step
    cfs = [face * c] * (mat - 1) + [face * (1 + c)]
    return float(sum(cf / (1 + yld) ** (t + 1) for t, cf in enumerate(cfs)))

def compute_composite_scores(df: pd.DataFrame, esg_a: pd.Series, 
                             w_esg: float = 0.35, w_carbon: float = 0.35, 
                             w_phys: float = 0.30):
    norm_esg = esg_a / 10.0
    carbon_pen = df["emis_intensity_imputed"] / df["emis_intensity_imputed"].max()
    phys_pen = df["physical_exposure"] * (df["sector"].map({"Materials": 0.85, "Financials": 0.65}))
    
    score = (w_esg * norm_esg - w_carbon * carbon_pen - w_phys * phys_pen).round(3)
    return score
