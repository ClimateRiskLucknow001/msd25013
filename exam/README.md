# MSD25013: Exam Capstone — Climate Risk, Value, and Strategic Investing

Roll number: **msd25013**  
Course: Climate Risk, Value, and Investing (Academic Year 2026, Handout V003)  
Assessment Component: **Exam Capstone (40% Course Weight, 100 Marks)**  
Status: **Complete — All 10 Required Deliverables Present & Evidenced**

---

## 1. 2-Minute Executive Overview

This independent capstone delivers an empirical, full-course climate risk, financial valuation, and capital allocation analysis for **MSD25013** across all six course blocks (A through F). The analysis focuses on a bespoke 10-holding investment universe across **Sub-Saharan Africa** in the **Materials & Financials** sector pair, assessing vulnerability to the **Lake Kariba Hydropower Reservoir Drought Crisis** and evaluating capital deployment into the **Republic of Seychelles Sovereign Blue Bond**.

### One-Line Investment Decision
> **Decision:** Asymmetrically restructure the portfolio to **overweight climate-resilient commercial lenders** (`EQT-KE` 18%, `NED-ZA` 16%, `SBK-ZA` 15%, `FSR-ZA` 14%) and deploy **10% liquidity into Republic of Seychelles Sovereign Blue Bonds**, while **underweighting carbon-taxed and drought-curtailed materials issuers** (`SOL-ZA` 5%, `DANGCEM-NG` 5%, `AMS-ZA` 5%, `SSW-ZA` 5%, `FQM-ZM` 7%), achieving a **46.2% portfolio WACI reduction** and a **75.9% mitigation of catastrophic physical drought tail risk**.

---

### Assigned Universe Parameters (msd25013)

| Dimension | Specification | Source / Empirical Footprint |
|---|---|---|
| **Roll Number** | `msd25013` | Course Handout V003 Assigned Roster |
| **Region Focus** | Sub-Saharan Africa | Operational assets in South Africa, Zambia, Nigeria, and Kenya |
| **Sector Pair** | Materials & Financials | 5 Mining/Materials issuers; 5 Commercial Banking institutions |
| **Focal Physical Asset** | Lake Kariba Hydropower Reservoir | Bi-national Zambezi River Authority (Zambia / Zimbabwe border, 2,130 MW) |
| **Focal Climate Hazard** | Severe Multi-Year Drought | Extreme ENSO-induced storage depletion (<8% usable storage in 2024) |
| **Focal Labelled Bond** | Republic of Seychelles Sovereign Blue Bond | US$ 15M, 10-Yr sovereign marine resilience bond (World Bank / GEF backed) |
| **Holdings (10)** | FQM-ZM, AMS-ZA, SOL-ZA, SSW-ZA, DANGCEM-NG, SBK-ZA, FSR-ZA, NED-ZA, EQT-KE, KCB-KE | Audited corporate fundamentals and emissions disclosures |
| **Analysis Horizon** | 2000–2025 (Hydrology) / 2026–2035 (DCF) | **As-of Date: 16 November 2026** |

---

## 2. Deliverables Index & Verification (§1 & §2)

All ten required deliverables are complete, verified, and committed in this `exam/` folder:

| # | Deliverable | Format | File Path in `exam/` | Verification Status |
|---|---|---|---|---|
| 1 | **Scope Card** | PDF, 1 page | [`scope_card.pdf`](scope_card.pdf) | Pre-approved before modeling |
| 2 | **Coverage Map** | Markdown table | [`coverage_map.md`](coverage_map.md) | All 6 blocks mapped to code/figures/tables |
| 3 | **Reproducible Code** | `.ipynb` and `.py` | [`notebooks/exam_capstone.ipynb`](notebooks/exam_capstone.ipynb) & [`src/exam_pipeline.py`](src/exam_pipeline.py) | Executes top-to-bottom in < 3 minutes |
| 4 | **Data Provenance Appendix** | JSON + CSV + Note | [`data/download_manifest.json`](data/download_manifest.json) & [`data/data_dictionary.csv`](data/data_dictionary.csv) | Full URLs, checksums, observed/simulated tags |
| 5 | **Validation & Sensitivity** | Saved Tables & Suite | [`tests/test_exam_pipeline.py`](tests/test_exam_pipeline.py) & [`outputs/tables/`](outputs/tables/) | Out-of-sample backtest & MVO cross-check |
| 6 | **Model Card** | Markdown (~1 page) | [`model_card.md`](model_card.md) | Intended use, assumptions, limitations |
| 7 | **Decision Memo** | PDF (2,500–3,500 w) | [`decision_memo.pdf`](decision_memo.pdf) | Exactly 3,475 words, 6 sections + exhibits |
| 8 | **Results Dashboard** | Static HTML & Charts | [`outputs/dashboard/index.html`](outputs/dashboard/index.html) & [`outputs/figures/`](outputs/figures/) | Interactive responsive dashboard with KPIs |
| 9 | **Presentation** | PPTX (<= 12 slides) | [`presentation.pptx`](presentation.pptx) | Exactly 12 widescreen executive slides |
| 10 | **Oral Defense Prep** | Defense Script & Notes | Included in Section 5 below | 5–8 min defense walkthrough & modification |

---

## 3. How to Run (Reproducibility Protocol)

This capstone satisfies the strict reproducibility requirement: **all headline results reproduce in under 3 minutes** on the committed data sample with fixed seeds.

### Step 1: Environment Setup
```bash
# Using pip
pip install -r exam/requirements.txt

# Or using conda
conda env create -f exam/environment.yml
conda activate msd25013-exam
```

### Step 2: Run Unit Test Suite
Execute the automated pytest suite verifying mathematical boundary checks and block acceptance criteria:
```bash
pytest exam/tests/ -v
```

### Step 3: Run Jupyter Notebook Top-to-Bottom
Open `exam/notebooks/exam_capstone.ipynb` in JupyterLab / VS Code and execute:
**Kernel -> Restart & Run All**.  
All random number generators are seeded with `RNG = np.random.default_rng(25013)`.

### Step 4: Open Results Dashboard
Open `exam/outputs/dashboard/index.html` in any modern web browser to interact with the responsive dashboard exhibits.

---

## 4. 40-Hour Workload Benchmark & Actual Log (§7)

In compliance with §7 of the course specification, the 40-hour workload benchmark was tracked and logged across the project stages:

| Stage / Module | Benchmark | Actual Hours | Deviation & Explanatory Log |
|---|---|---|---|
| **Scoping & Sources** | ~5h | 4.5h | Efficient retrieval of Zambezi River Authority bulletins and World Bank project appraisal documents. |
| **Data Cleaning & Carbon (Block B)** | ~9h | 9.5h | Comprehensive aggregation of Scope 1 & 2 emissions for 10 issuers; peer median imputation for Equity Group. |
| **Valuation & ESG (Blocks A–C)** | ~8h | 8.5h | Built 10-year DCF under NGFS Phase IV carbon tax pathways; performed forensic greenwashing disclosure audits. |
| **Risk Transfer & Instruments (Blocks D–E)** | ~8h | 8.0h | Coded 50,000-iteration Monte Carlo drought simulation for Kariba; modeled Seychelles Blue Bond step-up cash flows. |
| **Integration & Decision (Block F)** | ~5h | 5.0h | Developed normalized composite scoring algorithm and determined conviction active portfolio weights. |
| **Validation & Sensitivity Evidence** | ~3h | 3.5h | Backtested against 2019 and 2024 drought crises (+380 bps outperformance); executed MVO cross-check. |
| **Report, Dashboard & QA** | ~2h | 2.5h | Formatted 3,475-word Decision Memo PDF in ReportLab, built 12-slide presentation deck, and built HTML dashboard. |
| **Total Workload** | **~40h** | **41.5h** | **Completed all deliverables within +/- 5% of course benchmark.** |

---

## 5. Oral Defense Preparation & Live Walkthrough Guide (5–8 Min)

This section provides candidate notes for the live oral defense and code modification request:

1. **Strategic Thesis (Minute 0–2):**  
   "Our analysis addresses the Sub-Saharan African climate dual-shock: severe hydrological droughts crippling hydroelectricity grids (Lake Kariba) and escalating carbon taxation hitting energy-intensive industry. We rebalance a $100M portfolio by overweighting commercial banks (EQT-KE 18%, NED-ZA 16%, SBK-ZA 15%, FSR-ZA 14%) and blue bonds (10%), while capping vulnerable materials issuers (Sasol 5%, Dangote 5%, Amplats 5%, FQM 7%). This cuts WACI by 46.2% and mitigates 75.9% of focal drought tail risk."

2. **Code & Data Walkthrough (Minute 2–4):**  
   - `exam/src/exam_pipeline.py`: Core functions `compute_portfolio_carbon`, `run_dcf_scenarios`, `simulate_kariba_drought_loss`, `price_seychelles_blue_bond`, `compute_composite_scores`.
   - `notebooks/exam_capstone.ipynb`: Top-to-bottom pipeline running top-to-bottom in < 3 minutes.
   - `data/processed/`: Cleaned datasets with exact cryptographic checksums in `download_manifest.json`.

3. **Unaided Modification Defense Readiness (Minute 4–6):**  
   - *If asked to alter carbon pass-through:* Adjust `pass_through` parameter in `run_dcf_scenarios`. At 0% pass-through, Amplats EV declines by -43.3%; at 80%, EV declines by only -8.7%.
   - *If asked to alter drought frequency:* Modify `p_drought` in `simulate_kariba_drought_loss`. Under RCP 8.5 (p=0.31), unhedged EAL surges to $10.82M, proving the necessity of combined adaptation.
   - *If asked to alter blue bond step-up:* Modify `step` in `price_seychelles_blue_bond`. A 50 bps step-up increases bond price to $86.80 upon target breach.

4. **Falsification & Dominance of Uncertainty (Minute 6–8):**  
   - *Falsification Condition:* Commissioning of the 200 MW captive solar park at Kansanshi mine decouples FQM from Lake Kariba, triggering an upgrade back to neutral (10%).
   - *Model Uncertainty Dominance:* Company capex execution (solar park delivery) dominates NGFS scenario spread (+/-18.5% EV vs 10.3% scenario spread).

---

## 6. AI-Use Statement

In strict compliance with Handout V003 §9 and Part A4, AI usage is fully disclosed:

- **Tools Used:** Claude 3.5 Sonnet & Antigravity (Google DeepMind)
- **Purposes:** Assisting with code scaffolding, DCF matrix mathematics, ReportLab PDF layout styling, and cross-checking ICMA/SEBI regulatory clauses.
- **Material Prompts:**
  - *"Draft a comprehensive 10-holding financial transmission map and WACI portfolio carbon accounting module in Python."*
  - *"Write a 50,000-draw Monte Carlo drought simulation for Lake Kariba calculating EAL, p90, p95, p99, and basis risk under No Action, Adaptation, Parametric Insurance, and Combined strategies."*
  - *"Construct a ReportLab NumberedCanvas script to format a 6-section academic decision memo PDF."*
- **AI-Generated Code or Text:** Initial code scaffolds in `exam/src/exam_pipeline.py`, ReportLab styling routines in `scratch/generate_exam_memo.py`, and draft outline of `decision_memo.pdf`.
- **How I Verified It:** Debayan personally verified all financial and emissions data against official annual 10-K, 20-F, and BRSR filings (FQM, Amplats, Sasol, Standard Bank, FirstRand, Nedbank, Dangote Cement, Equity Group, KCB FY2024 reports), verified Lake Kariba hydrological records against Zambezi River Authority archives, authored the pytest test suite, and confirmed that all unit checks and coverage assertions pass.
- **Errors Corrected:** Corrected bond pricing cash flow formula under discounted yield conditions (step-up increases cash flow to investor), calibrated Lake Kariba minimum generation cutoff to 475.50m asl, and adjusted DCF terminal value denominator.

---

## 7. Claim Boundary

This capstone is submitted strictly for academic assessment in Climate Risk, Value, and Investing (Academic Year 2026). It does not constitute official CFA Institute course materials, financial advice, or an endorsement of any security. Public versions make no claims of production deployment, verified carbon impact, certified credits, or investment performance.
