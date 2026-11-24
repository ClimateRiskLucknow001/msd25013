# msd25013: Climate Risk, Value, and Investing (Student Capstone Repository)

Roll number: **msd25013**  
Course: Climate Risk, Value, and Investing, Academic Year 2026 (Handout V003)  
Candidate: **Debayan** (GitHub: `Debayan2024`)

---

## 1. 2-Minute Executive Overview

This repository houses the two integrated, full-course capstones for **MSD25013**. Both projects carry an assigned Sub-Saharan Africa investment universe across **Materials & Financials** through all six course blocks (A through F) to one defensible, actionable capital allocation decision.

### Assigned Universe Parameters (msd25013)

| Dimension | Specification | Source / Empirical Footprint |
|---|---|---|
| **Roll Number** | `msd25013` | Handout Roster assigned universe |
| **Region** | Sub-Saharan Africa | Primary operational exposures: South Africa, Zambia, Nigeria, Kenya |
| **Sector Pair** | Materials & Financials | 5 Mining/Materials issuers; 5 Commercial Banking institutions |
| **Focal Physical Asset** | Hydropower Reservoir (Drought): Lake Kariba | Zambezi River Authority (Zambia / Zimbabwe border, 2,130 MW) |
| **Focal Labelled Bond** | Blue / Sustainability Bond: Seychelles Sovereign Blue Bond | Republic of Seychelles Sovereign Blue Bond (US$ 15M, 10-Yr, World Bank/GEF de-risked) |
| **Holdings** | FQM-ZM, AMS-ZA, SOL-ZA, SSW-ZA, DANGCEM-NG, SBK-ZA, FSR-ZA, NED-ZA, EQT-KE, KCB-KE | 10 listed corporate entities with audited FY2024/25 fundamentals |
| **Data As-of Date** | 16 November 2026 | Documented from latest audited corporate filings & ZRA hydrologic archives |

**Headline Decision:** Asymmetrically restructure the portfolio to **overweight climate-resilient commercial lenders** (`EQT-KE` 18%, `NED-ZA` 16%, `SBK-ZA` 15%, `FSR-ZA` 14%) and deploy **10% liquidity into Republic of Seychelles Sovereign Blue Bonds**, while **underweighting carbon-taxed and drought-curtailed materials issuers** (`SOL-ZA` 5%, `DANGCEM-NG` 5%, `AMS-ZA` 5%, `SSW-ZA` 5%, `FQM-ZM` 7%), achieving a **46.2% portfolio WACI reduction** and a **75.9% mitigation of catastrophic physical drought tail risk**.

---

## 2. Capstones Status & Links

| Capstone | Weight | Status | Link | Key Deliverables |
|---|---|---|---|---|
| **Practice (Guided)** | 10% | **Completed** | [practice/](practice/) | `practice_capstone.ipynb`, `coverage_map.md`, `decision_memo.pdf` (3 pages), unit tests |
| **Exam (Independent)** | 40% | **Completed** | [exam/](exam/) | `scope_card.pdf`, `coverage_map.md`, `model_card.md`, `decision_memo.pdf` (3,475 words), `presentation.pptx` (12 slides), interactive HTML dashboard, pytest suite |

---

## 3. Repository Layout

```
msd25013/
├── README.md                          <- This repository overview & index
├── .gitignore                         <- Ignored build artifacts & cache
├── practice/                          <- Guided Capstone (10% Course Component)
│   ├── README.md                      <- Practice overview, findings, how-to-run
│   ├── requirements.txt               <- Dependencies
│   ├── coverage_map.md                <- Table verifying Blocks A through F
│   ├── data/                          <- download_manifest.json, data_dictionary.csv, sample/
│   ├── notebooks/                     <- practice_capstone.ipynb (runnable top-to-bottom)
│   ├── src/                           <- pipeline.py
│   ├── tests/                         <- test_practice_pipeline.py
│   ├── outputs/                       <- figures/ and tables/
│   └── decision_memo.pdf              <- 3-page executive decision memo
└── exam/                              <- Independent Capstone (40% Course Component)
    ├── README.md                      <- Full overview, 40h benchmark log, defense guide
    ├── environment.yml                <- Conda environment specification
    ├── requirements.txt               <- Pip dependencies
    ├── scope_card.pdf                 <- Approved 1-page scope card PDF
    ├── coverage_map.md                <- Verified coverage map across all 6 blocks
    ├── model_card.md                  <- 1-page model card (intended use, assumptions, limits)
    ├── decision_memo.pdf              <- 3,475-word comprehensive decision memo PDF
    ├── presentation.pptx              <- 12-slide executive pitch deck
    ├── data/
    │   ├── download_manifest.json     <- Sources, URLs, retrieval dates, checksums
    │   ├── data_dictionary.csv        <- Field definitions & observed/estimated/simulated status
    │   ├── sample/                    <- Small committable samples (holdings, hydrology, bonds)
    │   └── processed/                 <- Clean processed data
    ├── notebooks/
    │   └── exam_capstone.ipynb        <- Runnable full-course pipeline (< 3 mins)
    ├── src/
    │   └── exam_pipeline.py           <- Analytical engine for Blocks A through F
    ├── tests/
    │   └── test_exam_pipeline.py      <- Automated pytest validation test suite
    └── outputs/
        ├── figures/                   <- High-resolution plots (transmission, WACI, DCF, exceedance)
        ├── tables/                    <- Saved CSV tables for all 6 blocks
        └── dashboard/
            └── index.html             <- Interactive responsive HTML results dashboard
```

---

## 4. How to Run & Reproduce Headline Results

All computations are fully reproducible offline on the committed dataset in under 3 minutes with fixed seeds (`RNG = np.random.default_rng(25013)`).

1. **Install Dependencies:**
   ```bash
   pip install -r exam/requirements.txt
   ```
2. **Execute Full Pytest Suite:**
   ```bash
   pytest practice/tests/ -v
   pytest exam/tests/ -v
   ```
3. **Execute Notebooks:**
   Open either `practice/notebooks/practice_capstone.ipynb` or `exam/notebooks/exam_capstone.ipynb` in JupyterLab / VS Code and execute **Kernel -> Restart & Run All**.

4. **Launch Results Dashboard:**
   Open `exam/outputs/dashboard/index.html` in any browser to explore interactive exhibits, KPI summary cards, and tables.

---

## 5. AI-Use Statement

In strict compliance with Handout V003 §9 and Part A4, AI usage is fully disclosed:

- **Tools Used:** Claude 3.5 Sonnet & Antigravity (Google DeepMind)
- **Purposes:** Assisting with initial code scaffolding, matrix operations, ReportLab PDF formatting routines, and regulatory cross-checks.
- **Material Prompts:**
  - *"Draft a comprehensive 10-holding financial transmission map and WACI portfolio carbon accounting module in Python."*
  - *"Write a 50,000-draw Monte Carlo drought simulation for Lake Kariba calculating EAL, p90, p95, p99, and basis risk under No Action, Adaptation, Parametric Insurance, and Combined strategies."*
  - *"Construct a ReportLab NumberedCanvas script to format a 6-section academic decision memo PDF."*
- **AI-Generated Code or Text:** Initial code scaffolds in `src/`, ReportLab styling routines in `scratch/`, and draft section outlines for `decision_memo.pdf`.
- **How I Verified It:** Debayan personally checked and verified all financial data against audited annual 10-K, 20-F, and BRSR filings (FQM, Amplats, Sasol, Standard Bank, FirstRand, Nedbank, Dangote Cement, Equity Group, KCB FY2024 reports), verified Lake Kariba hydrological records against Zambezi River Authority archives, authored all unit test suites in `practice/tests/` and `exam/tests/`, and verified that all unit checks and coverage assertions pass.
- **Errors Corrected:** Corrected bond pricing cash flow formula under discounted yield conditions (step-up increases cash flow to investor), calibrated Lake Kariba minimum generation cutoff to 475.50m asl, and adjusted DCF terminal value denominator.

---

## 6. Claim Boundary

This project is submitted strictly for academic assessment in Climate Risk, Value, and Investing (Academic Year 2026). It does not constitute official CFA Institute course materials, financial advice, or an endorsement of any security. Public versions make no claims of production deployment, verified carbon impact, certified credits, or investment performance.
