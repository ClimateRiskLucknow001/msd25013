# msd25013: Climate Risk, Value, and Investing (Student Capstone)

Roll number: **msd25013**  
Course: Climate Risk, Value, and Investing, academic year 2026 (handout V003)

## 2-minute overview

This repository holds my two integrated capstones for the course. Each one covers all six course blocks (A to F) and ends in one defensible investment decision.

**My assigned universe**

| Item | Choice | Evidence / Notes |
|---|---|---|
| **Region** | Sub-Saharan Africa | Primary operational exposures: Zambia, Zimbabwe, South Africa, Kenya |
| **Sector pair** | Materials & Financials | 2 Mining & Materials issuers; 2 Commercial & Diversified Banking issuers |
| **Focal physical asset** | Hydropower reservoir (drought): Lake Kariba | Zambezi River Authority (Zambia / Zimbabwe border, 2,130 MW) |
| **Focal labelled bond** | Blue / sustainability bond: Seychelles sovereign blue bond | Republic of Seychelles Sovereign Blue Bond (US$ 15M, 10-Yr, World Bank/GEF de-risked) |
| **Holdings** | FQM-ZM, AMS-ZA, SBK-ZA, EQT-KE | Full scope 8-12 holdings developed in exam capstone |
| **Data as-of date** | 16 November 2026 | Documented from latest audited FY24/25 corporate filings & hydrologic records |

**Decision question (practice):** "Should an Africa-focused sustainable transition fund overweight or underweight these Materials and Financials names given acute drought vulnerability (Kariba hydro-power crisis) and transition carbon risks, while allocating 10% to sovereign blue bonds?"

## Repository layout

```
msd25013/
  README.md            this file
  practice/            guided capstone (10% course component, completed)
    README.md
    requirements.txt
    coverage_map.md    where each of the six blocks is addressed
    data/              download_manifest.json, data_dictionary.csv, sample/
    notebooks/         practice_capstone.ipynb
    src/               pipeline.py
    tests/             test_practice_pipeline.py
    outputs/           figures/ and tables/
    decision_memo.pdf  3-page executive decision memo
  exam/                independent capstone (40% course component)
    README.md
    environment.yml | requirements.txt
    scope_card.pdf
    coverage_map.md
    data/              download_manifest.json, data_dictionary.csv, sample/, processed/
    notebooks/ | src/
    tests/
    outputs/           figures/, tables/, dashboard/
    model_card.md
    decision_memo.pdf  2,500-3,500 words
    presentation.pptx  <= 12 slides
```

## Capstones

| Capstone | Weight | Status | Link |
|---|---|---|---|
| Practice (guided) | 10% | Completed | [practice/](practice/) |
| Exam (independent) | 40% | In progress | [exam/](exam/) |

## How to run

1. Install requirements: `pip install -r practice/requirements.txt`
2. Open `practice/notebooks/practice_capstone.ipynb` in JupyterLab.
3. Choose **Kernel -> Restart & Run All**. Seeds are fixed, so results repeat.
4. Run unit tests: `pytest practice/tests/`

## Data and sources

Every source is listed with its URL, licence and retrieval date in `practice/data/download_manifest.json`. Each value is labelled `observed`, `assumed` or `simulated` in `practice/data/data_dictionary.csv`. Only small samples are committed. No credentials or restricted data are included.

## AI-use statement

AI assistance is allowed with disclosure. I remain responsible for every result and line of code.

- **Tools used:** Claude 3.5 Sonnet & Antigravity (Google DeepMind)
- **Purposes:** Assisting with code scaffolding, DCF matrix math, Monte Carlo simulation syntax, and ReportLab PDF layout.
- **Material prompts:** "Draft an integrated climate-investment pipeline in Python covering carbon WACI, DCF under carbon tax pathways, Monte Carlo drought risk simulation, and coupon step-up bond pricing."
- **AI-generated code or text in this repo:** Code scaffolds in `practice/src/pipeline.py`, ReportLab styling helper in `scratch/create_practice_deliverables.py`, and draft structure of `decision_memo.pdf`.
- **How I verified it:** Checked all figures against company financial and sustainability reports (FQM, Amplats, Standard Bank, Equity Group FY2024 filings), calibrated Kariba hydrology against Zambezi River Authority bulletins, wrote unit tests in `practice/tests/test_practice_pipeline.py`, and verified that all six blocks pass assertions.
- **Errors I corrected:** Corrected bond step-up cash flow logic (step-up increases coupon paid to bondholder upon missed sustainability target), calibrated Lake Kariba minimum operating reservoir level to 475.5m asl, and adjusted DCF terminal value denominator.

## Claim boundary

This is coursework for educational use. It is not an official CFA Institute assessment, and it makes no claim of production deployment, verified impact, certified credentials or investment performance. Nothing here is investment advice.
