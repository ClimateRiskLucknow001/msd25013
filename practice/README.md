# MSD25013: Practice Capstone — Climate Risk, Value, and Investing

Roll number: **msd25013**  
Course: Climate Risk, Value, and Investing (Academic Year 2026, Handout V003)  
Status: **Completed (10% Course Component / 20 Marks)**

---

## 1. 2-Minute Executive Overview

This practice capstone delivers an integrated, end-to-end climate risk and investment evaluation for **MSD25013** across all six course blocks (A through F). The investment universe focuses on **Sub-Saharan Africa** across the **Materials & Financials** sector pair, assessing vulnerability to the **Lake Kariba Hydropower Reservoir Drought Crisis** and evaluating capital allocation into the **Republic of Seychelles Sovereign Blue Bond**.

### Assigned Universe Specification

| Parameter | Specification | Notes & Evidence |
|---|---|---|
| **Roll Number** | `msd25013` | Handout Roster assigned universe |
| **Region** | Sub-Saharan Africa | Primary operational exposures: Zambia, Zimbabwe, South Africa, Kenya |
| **Sector Pair** | Materials & Financials | 2 Mining/Materials holdings; 2 Commercial Banking holdings |
| **Focal Physical Asset** | Hydropower Reservoir (Drought) | Lake Kariba / Zambezi River Authority (Zambia / Zimbabwe) |
| **Focal Labelled Bond** | Blue / Sustainability Bond | Republic of Seychelles Sovereign Blue Bond (US$ 15M, 10-Yr) |
| **Holdings (4)** | FQM-ZM, AMS-ZA, SBK-ZA, EQT-KE | Equal weight baseline (25.0% each) |
| **As-of Date** | 16 November 2026 | Documented from latest audited FY24/25 filings |

### One-Line Investment Decision
> **Decision:** Overweight climate-resilient commercial lenders (`EQT-KE` to 40%, `SBK-ZA` to 30%) and allocate 10% to the Seychelles Sovereign Blue Bond, while underweighting drought-curtailed and carbon-taxed miners (`FQM-ZM` to 15%, `AMS-ZA` to 15%) subject to active board-level stewardship on off-grid renewable energy self-generation.

---

## 2. Repository Layout (practice/)

```
practice/
├── README.md                      <- This overview & execution guide
├── requirements.txt               <- Python dependencies
├── coverage_map.md                <- Table verifying coverage of Blocks A to F
├── data/
│   ├── download_manifest.json     <- Sources, URLs, retrieval dates, checksums
│   ├── data_dictionary.csv        <- Field definitions, observed/estimated/simulated status
│   └── sample/                    <- Small committable sample datasets
│       ├── holdings_sample.csv
│       ├── focal_asset_kariba.csv
│       └── seychelles_blue_bond.csv
├── notebooks/
│   └── practice_capstone.ipynb    <- Primary runnable notebook covering Stages 0-7
├── src/
│   └── pipeline.py                <- Core analytical functions
├── tests/
│   └── test_practice_pipeline.py  <- Pytest suite verifying pipeline integrity
├── outputs/
│   ├── figures/                   <- High-resolution saved charts (sensitivity, exceedance, composite)
│   └── tables/                    <- Saved CSV tables for all 6 blocks
└── decision_memo.pdf              <- 3-page executive decision memo PDF
```

---

## 3. How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r practice/requirements.txt
   ```
2. **Execute Pytest Suite:**
   ```bash
   pytest practice/tests/
   ```
3. **Run Notebook:**
   Open `practice/notebooks/practice_capstone.ipynb` in JupyterLab / VS Code and execute **Kernel -> Restart & Run All**. All seeds are fixed (`RNG = np.random.default_rng(25013)`), producing fully reproducible numbers in under 1 minute.

---

## 4. Summary of Key Findings Across Course Blocks

- **Block A (Foundations & Transmission):** First Quantum Minerals (`FQM-ZM`) exhibits primary physical risk transmission: a 67% decline in Lake Kariba water levels caused 16-21 hours/day load shedding in Zambia, triggering emergency diesel generation that inflates operating costs by 22%. Anglo American Platinum (`AMS-ZA`) faces transition risk: reliance on Eskom coal power exposes smelting operations to escalating South African carbon taxes.
- **Block B (Data & Portfolio Carbon):** Portfolio WACI is **226.7 tCO2e / MUSD** under equal weighting. Handling a real-world disclosure gap for Equity Group Holdings (`EQT-KE`) via peer median imputation (95.0 tCO2e/MUSD) yields 100% effective carbon coverage.
- **Block C (ESG & Stewardship):** Ratings reconciliation shows an average divergence of 1.7 points between disclosure quality and controversy-adjusted scores. An audit of FQM's sustainability claim revealed an omission of backup diesel emissions during Kariba load-shedding. Active stewardship demands co-investment in a 460 MW renewable microgrid by Q3 2027.
- **Block D (Physical Risk & Risk Transfer):** Kariba hydropower asset expected annual loss (EAL) under no-action is **$2.62M** with a 95th percentile tail loss of **$18.45M**. An integrated strategy combining engineering adaptation (spillway intake lowering + floating solar PV) and parametric water-level insurance reduces EAL to **$0.85M** (-67.6%) and 95th percentile loss to **$4.62M**.
- **Block E (Labelled Bonds & Policy):** The Seychelles Sovereign Blue Bond structure utilizes World Bank and GEF credit guarantees to lower effective borrowing costs from 6.65% to 3.25%. A 25 bps coupon step-up for marine management KPI underperformance provides credible investor protection, fully aligned with ICMA Blue Bond Principles and SADC climate finance guidelines.
- **Block F (Integration & Decision):** Multi-criteria integration produces composite scores: `EQT-KE` (+0.142) and `SBK-ZA` (+0.078) lead the portfolio, while `FQM-ZM` (-0.231) and `AMS-ZA` (-0.198) lag, establishing an actionable capital re-allocation thesis.

---

## 5. AI-Use Statement

- **Tools Used:** Claude 3.5 Sonnet & Antigravity (Google DeepMind)
- **Purposes:** Drafting code scaffolds, debugging matrix operations, drafting ReportLab PDF layout styles, and cross-checking ICMA/SEBI regulatory clauses.
- **Material Prompts:**
  - *"Draft a clean DCF model in Python that calculates Enterprise Value sensitivity across NGFS carbon prices from $0 to $150/tCO2 for an energy-intensive smelting holding."*
  - *"Write a Monte Carlo drought risk simulator for Lake Kariba calculating EAL and 95th percentile tail loss under baseline, adaptation, parametric insurance, and combined cases."*
- **Verification Performed:** All generated code was personally checked, refactored into `pipeline.py`, executed against unit assertions in `test_practice_pipeline.py`, and verified against official Zambezi River Authority hydrological bulletins and corporate annual 10-K/BRSR filings.
- **Errors Corrected:** Corrected an initial sign error in the bond coupon step-up cash flow formula (where missed KPI steps up coupon payment to investors rather than stepping down) and calibrated Lake Kariba minimum operating levels to 475.5m asl.

---

## 6. Claim Boundary

This project is submitted strictly for academic assessment in Climate Risk, Value, and Investing (Academic Year 2026). It does not constitute official CFA Institute course materials, financial advice, or an endorsement of any security.
