"""
Pipeline module for MSD25013 Practice Capstone
Sub-Saharan Africa: Materials & Financials
Focal Asset: Lake Kariba Hydropower Reservoir (Drought Hazard)
Focal Bond: Republic of Seychelles Sovereign Blue Bond
"""

import numpy as np
import pandas as pd

def compute_waci(holdings_df: pd.DataFrame, default_missing_intensity: float = 95.0):
    df = holdings_df.copy()
    raw_cov = float(df["emis_intensity_tco2_per_musd"].notna().mean())
    imputed_series = df["emis_intensity_tco2_per_musd"].fillna(default_missing_intensity)
    waci = float(np.sum(df["weight"] * imputed_series))
    return {"raw_coverage": raw_cov, "effective_waci": waci, "imputed_intensity": imputed_series}

def run_valuation_dcf(revenue_musd: float, emis_intensity: float, carbon_price: float, 
                      wacc: float = 0.095, g: float = 0.02, pass_through: float = 0.40, 
                      tax: float = 0.27, horizon_years: int = 10):
    yr = np.arange(1, horizon_years + 1)
    rev = revenue_musd * (1.025) ** yr
    ebit = rev * 0.18
    annual_emis_kt = emis_intensity * revenue_musd / 1e3
    carbon_cost = (annual_emis_kt * carbon_price / 1e3) * (1 - pass_through)
    fcf = ebit * (1 - tax) - revenue_musd * 0.07 - carbon_cost
    disc = (1 + wacc) ** yr
    ev = (fcf / disc).sum() + (fcf[-1] * (1 + g) / (wacc - g)) / disc[-1]
    return float(ev)

def simulate_physical_loss(asset_value: float = 50.0, n_sims: int = 20000, 
                           p_drought: float = 0.15, adapt_reduction: float = 0.42, 
                           attach: float = 2.50, limit: float = 12.0, seed: int = 25013):
    rng = np.random.default_rng(seed)
    sev = np.clip(rng.normal(0.35, 0.14, n_sims), 0.05, 0.95)
    drought_occurred = (rng.random(n_sims) < p_drought)
    loss = sev * drought_occurred * asset_value
    
    retained_ins = loss - np.clip(loss - attach, 0, limit)
    loss_adapt = loss * (1 - adapt_reduction)
    retained_comb = loss_adapt - np.clip(loss_adapt - attach, 0, limit)
    
    def metric_dict(x):
        return {"eal": round(float(x.mean()), 2), "p95": round(float(np.percentile(x, 95)), 2)}
    
    return {
        "no_action": metric_dict(loss),
        "adaptation": metric_dict(loss_adapt),
        "insurance": metric_dict(retained_ins),
        "combined": metric_dict(retained_comb),
        "raw_loss": loss,
        "combined_loss": retained_comb
    }

def price_blue_bond(face: float = 100.0, coupon: float = 0.0325, step: float = 0.0025, 
                    mat: int = 10, yld: float = 0.055, target_met: bool = True):
    c = coupon if target_met else coupon + step
    cfs = [face * c] * (mat - 1) + [face * (1 + c)]
    return float(sum(cf / (1 + yld) ** (t + 1) for t, cf in enumerate(cfs)))
