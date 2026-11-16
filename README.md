# msd25013: Climate Risk, Value, and Investing (Student Capstone)

Roll number: **msd25013**
Course: Climate Risk, Value, and Investing, academic year 2026 (handout V003)

## 2-minute overview

This repository holds my two integrated capstones for the course. Each one covers all six course blocks (A to F) and ends in one investment decision.

**My assigned universe**

| Item | Choice |
|---|---|
| Region | Sub-Saharan Africa |
| Sector pair | Materials & Financials |
| Focal physical asset | Hydropower reservoir (drought): Lake Kariba |
| Focal labelled bond | Blue / sustainability bond: Seychelles sovereign blue bond |
| Holdings | _TODO: list your 3-4 companies here_ |
| Data as-of date | _TODO: e.g. 16 Nov 2026_ |

**Decision question (practice):** _TODO: e.g. "Should an Africa-focused equity fund overweight these names given climate risk?"_

## Repository layout

```
msd25013/
  README.md            this file
  practice/            guided capstone (10%)
    README.md
    requirements.txt
    coverage_map.md    where each of the six blocks is addressed
    data/              download_manifest.json, data_dictionary.csv, sample/
    notebooks/
    src/
    tests/
    outputs/           figures/ and tables/
    decision_memo.pdf  2-3 pages
  exam/                independent capstone (40%), not started yet
```

## Capstones

| Capstone | Weight | Status | Link |
|---|---|---|---|
| Practice (guided) | 10% | In progress | [practice/](practice/) |
| Exam (independent) | 40% | Not started | [exam/](exam/) |

## How to run

1. Install requirements: `pip install -r practice/requirements.txt`
2. Open `practice/notebooks/` in JupyterLab.
3. Choose **Kernel -> Restart & Run All**. Seeds are fixed, so results repeat.

## Data and sources

Every source is listed with its URL, licence and retrieval date in `practice/data/download_manifest.json`. Each value is labelled `observed`, `assumed` or `simulated` in `practice/data/data_dictionary.csv`. Only small samples are committed. No credentials or restricted data are included.

## AI-use statement

AI assistance is allowed with disclosure. I remain responsible for every result and line of code.

- **Tools used:** _TODO: e.g. Claude (Anthropic)_
- **Purposes:** _TODO: e.g. planning the workflow, explaining concepts, setting up the repo structure_
- **Material prompts:** _TODO: summarise the main prompts you used_
- **AI-generated code or text in this repo:** _TODO: say which files or sections_
- **How I verified it:** _TODO: e.g. checked figures against company reports, re-ran notebooks, wrote unit tests_
- **Errors I corrected:** _TODO: list any mistakes you found in AI output and how you fixed them_

## Claim boundary

This is coursework for educational use. It is not an official CFA Institute assessment, and it makes no claim of production deployment, verified impact, certified credentials or investment performance. Nothing here is investment advice.
