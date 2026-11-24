# Model Card: Sub-Saharan Africa Climate Risk & Capital Allocation Framework

**Model Identifier:** `MSD25013-AFRICA-TRANSITION-V1`  
**Model Developer:** Debayan (Roll Number: `msd25013`)  
**As-of Date:** 16 November 2026  
**Course & Project:** Climate Risk, Value, and Investing — Exam Capstone (Academic Year 2026, Handout V003)

---

### 1. Intended Use & Target Audience
- **Primary Intended Use:** To provide a quantitative and fundamental multi-block decision framework for portfolio managers allocating capital across listed equities and labelled fixed income in Sub-Saharan Africa, specifically evaluating vulnerability to severe hydrological droughts (focal asset: Lake Kariba) and carbon tax transition policies.
- **Target Audience:** Investment Committees, Institutional Asset Managers, and Development Finance Institutions (DFIs) managing Africa-focused transition and resilience equity/debt strategies.

### 2. Inputs & Data Provenance
- **Corporate Fundamentals:** FY2024 annual revenues, EBITDA, market capitalization, and operational assets sourced from audited issuer financial statements and regulatory filings (JSE, LUSE, NGX, NSE).
- **Emissions & Climate Data:** Scope 1 and Scope 2 operational emissions retrieved from corporate sustainability reports, CDP disclosures, and TCFD filings. Missing disclosures (e.g. Equity Group Holdings) imputed using peer median benchmarks.
- **Hydrological Records:** Zambezi River Authority (ZRA) monthly reservoir elevations, water storage levels (m asl), river inflows (BCM), and power curtailment statistics for Lake Kariba (2000–2025).
- **Climate Scenarios:** NGFS Phase IV scenario portal (Orderly Net Zero 2050, Delayed Transition, Current Policies) and IPCC AR6 / CMIP6 regional precipitation projections for Southern Africa.
- **Labelled Fixed Income:** World Bank Project Appraisal Documents, GEF concessional grant filings, and DNV GL Second Party Opinions for the Republic of Seychelles Sovereign Blue Bond.

### 3. Method Summary
1. **Transmission Mapping:** Qualitative and quantitative classification of 10 holdings across physical vs transition channels, establishing causal pathways to operating margins and cash flows.
2. **Carbon Accounting & WACI:** Portfolio Weighted Average Carbon Intensity (WACI) computed under equal and market-cap weighting schemes, with missingness imputation and carbon concentration metrics.
3. **Transition DCF Modeling:** 10-year discounted cash flow framework incorporating escalating carbon tax trajectories ($5/t to $180/t), cost pass-through elasticity, and terminal value sensitivity.
4. **Constructed ESG Scoring:** Transparent, non-proprietary scoring engine separating quantitative disclosure quality (Score A) from controversy and water-vulnerability adjustments (Score B), quantifying ratings divergence.
5. **Physical Risk Monte Carlo Simulation:** 50,000-iteration stochastic drought loss model for Lake Kariba evaluating EAL, 90th/95th/99th percentile tail losses, exceedance probability, and basis risk under four structural risk strategies.
6. **Fixed Income Structuring:** Blended concessional bond pricing model incorporating partial credit guarantees and sustainability KPI step-up coupon mechanisms.
7. **Multi-Block Integration:** Normalized multi-criteria composite scoring algorithm determining active portfolio conviction weights.

### 4. Key Assumptions
- **Cost Pass-Through:** Assumed at 40% for energy-intensive mining/smelting issuers under carbon tax regimes due to rigid long-term industrial contracts.
- **Drought Event Frequency:** Base annual probability of severe Lake Kariba drought calibrated at 15.0% (historical 1-in-6.7 year cycle), rising to 22.0% under RCP 4.5 by 2035 and 31.0% under RCP 8.5 by 2045.
- **Adaptation Loss Attenuation:** Assumed at 45% based on combined engineering feasibility of intake retrofits, floating solar PV hybrids, and catchment reforestation.
- **Composite Weights:** 35% ESG Governance, 35% Carbon Intensity Penalty, 30% Physical Drought Risk Penalty based on fund mandate constraints.

### 5. Validation Performed
- **Out-of-Sample Backtesting:** Simulated portfolio allocation tested against historical 2019 and 2024 El Niño drought stress periods. The model's proposed active rebalancing (overweighting resilient banks, underweighting Kariba-dependent miners) would have mitigated portfolio drawdown by 380 bps.
- **Alternative Method Cross-Check:** Verified against a constrained Mean-Variance Optimization (MVO) portfolio with explicit carbon budget and water-stress constraints, yielding consistent directional sector allocations.
- **Unit Assertion Suite:** Automated pytest test suite (`exam/tests/test_exam_pipeline.py`) verifying mathematical monotonicity, boundary conditions, and coverage integrity across all six blocks.

### 6. Limitations & Dominance of Model Uncertainty
- **Tipping-Point Nonlinearity:** Historical parametric distributions may underestimate catastrophic non-linear hydrological collapse in the Zambezi basin if rainfall patterns shift permanently.
- **Financed Emissions Gaps:** Banking holdings lack audited Scope 3 Category 15 financed emissions disclosures, requiring operational proxy metrics until full ISSB S2 adoption.
- **Model Uncertainty Dominance:** Model uncertainty regarding captive renewable power deployment schedules and utility sovereign debt restructurings dominates long-term NGFS scenario pricing divergence.

### 7. Prohibited Uses & Governance Boundaries
- **NOT INVESTMENT ADVICE:** This model is developed strictly for educational and academic assessment purposes. It does not constitute investment advice, financial promotion, or a recommendation to buy or sell any financial asset.
- **CONSTRUCTED SCORES NOTICE:** All ESG scores, exposure indices, and risk weights are transparently constructed academic proxies and must not be cited as commercial or proprietary credit/sustainability ratings.
