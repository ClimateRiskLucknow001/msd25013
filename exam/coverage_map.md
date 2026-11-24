# Coverage Map — Exam Capstone (MSD25013)

Course: Climate Risk, Value, and Investing (Academic Year 2026, Handout V003)  
Student Roll Number: **msd25013**  
Assigned Universe: **Sub-Saharan Africa · Materials & Financials · Lake Kariba Hydropower Reservoir (Drought) · Republic of Seychelles Sovereign Blue Bond**  
Repository Location: `exam/coverage_map.md`

---

### Full-Course Acceptance Coverage Matrix

| Block | Covered? | Where (notebook section / figure / table) | One-line what you did |
|---|---|---|---|
| **A Foundations & transmission** | yes | `notebooks/exam_capstone.ipynb` §Stage 1; `outputs/figures/fig1_transmission_map.png`; `outputs/tables/table1_holdings_universe.csv` | Classified 10 Sub-Saharan Africa holdings into physical vs transition exposures with causal transmission notes to revenue/margins |
| **B Climate data & portfolio carbon** | yes | `notebooks/exam_capstone.ipynb` §Stage 2; `outputs/figures/fig2_carbon_intensity_waci.png`; `outputs/tables/table2_portfolio_carbon_quality.csv` | Built documented climate/emissions dataset (90% reported coverage), imputed EQT-KE gap, calculated WACI of 1,077.9 tCO2e/MUSD and analyzed 88% carbon concentration |
| **C ESG, stewardship, ratings** | yes | `notebooks/exam_capstone.ipynb` §Stage 4; `outputs/figures/fig4_esg_ratings_divergence.png`; `outputs/tables/table4_esg_reconciliation_audit.csv` | Reconciled constructed disclosure vs controversy ratings (mean divergence 1.28 pts), audited FQM Kariba backup diesel omission, and drafted binding AGM stewardship resolution |
| **D Risk management & transfer** | yes | `notebooks/exam_capstone.ipynb` §Stage 5; `outputs/figures/fig5_kariba_loss_exceedance.png`; `outputs/tables/table5_kariba_risk_transfer_cases.csv` | Executed 50,000-draw Monte Carlo drought model for Lake Kariba across Baseline, RCP 4.5, and RCP 8.5 scenarios; quantified EAL ($5.24M to $1.52M) and basis risk for combined layered resilience |
| **E Instruments, markets & policy** | yes | `notebooks/exam_capstone.ipynb` §Stage 6; `outputs/tables/table6_blue_bond_cashflows.csv` | Modeled Seychelles Sovereign Blue Bond blended concessional cash flows, evaluated +25 bps step-up pricing ($83.04 vs $84.92), and synthesized South African / SEBI policy context |
| **F Integration & decision** | yes | `notebooks/exam_capstone.ipynb` §Stage 7; `outputs/figures/fig6_composite_portfolio_allocation.png`; `outputs/tables/table7_final_capital_allocation.csv`; `decision_memo.pdf` §1 | Formulated defensible multi-block capital allocation overweighting resilient commercial banks (EQT-KE, NED-ZA, SBK-ZA) and blue bonds, underweighting drought/carbon-stressed miners |

---

### Block Acceptance Criteria Verification

- [x] **A — Foundations & transmission:** Each of the 10 holdings classified as physical- and/or transition-exposed with an empirical transmission mechanism.
- [x] **B — Climate data & portfolio carbon:** Documented dataset in `data/`, quality report (missingness, units, coverage), WACI computed for equal and market-cap weights.
- [x] **A-B — Valuation under transition:** 10-year DCF scenario cash flows for Amplats (`AMS-ZA`) and Sasol (`SOL-ZA`) comparing Baseline ($5/t), Orderly Net Zero ($120/t), and Delayed Transition ($180/t spike) with pass-through sensitivity.
- [x] **C — ESG, stewardship, ratings:** Transparently constructed Score A and Score B, empirical ratings divergence, forensic disclosure/greenwashing audit of FQM and Sasol, and binding AGM stewardship engagement plan.
- [x] **D — Risk management & transfer:** No-action expected loss for Lake Kariba focal asset, >=3 strategies (adaptation, parametric insurance, combined layered resilience), 90th/95th/99th tail losses, exceedance curve, and basis-risk note.
- [x] **E — Instruments, markets & policy:** Republic of Seychelles Sovereign Blue Bond credit de-risking, cash flow schedule, KPI step-up coupon impact, and regional (SADC/South Africa) and Indian (SEBI) policy comparative synthesis.
- [x] **F — Integration & decision:** Single capital-allocation thesis synthesizing all blocks, explicit hurdle metrics, out-of-sample validation cross-check, and definitive falsification/reversal conditions.
