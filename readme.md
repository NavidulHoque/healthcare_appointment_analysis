# Bangladesh Healthcare Appointment Analysis

A healthcare analytics project analyzing 500 appointment records across 8 divisions of Bangladesh to identify appointment patterns, waiting-time trends and no-show behavior, extended with predictive modeling to estimate no-show risk before an appointment happens with a deeper operational performance review using Excel.

---

## What This Project Does

I analyzed 500 appointment records to find patterns that could help healthcare providers understand patient behavior and improve service delivery.

> All key findings below reflect the full 500-record dataset. 
> Can be scoped to a specific division/specialty via dynamic filtering — see below.

**Key findings:**

* No strong linear correlations found between age, fee, wait time, or appointment timing (all under ~0.10) — motivates the hypothesis testing planned in Stage 3
* Appointment completion rate is **68.6%**
* **Dhaka** has the highest overall no-show rate at **14.6%** across the full dataset
* **Pediatricians** are the most visited specialty with **92 appointments**
* **General Physicians** have the longest overall average wait time at **11.6 days**
* **Senior patients (56+)** make up the largest patient group with **162 patients**
* **Cardiologists** have the highest average consultation fee with **1557.8 BDT**
* **Predictive modeling** (Logistic Regression, Decision Tree, Random Forest) achieved ROC-AUC scores of **0.52–0.59** — indicating the current feature set has only weak predictive power for No-show risk (see *Predictive Modeling* section below)

---

## Visualizations

Built a 6 panel dashboard covering all key analyses:

### Python (Matplotlib)
The example below is rendered with `FILTER_DIVISION = "Dhaka"` active, so its numbers reflect Dhaka only (except No-show Rate by Division) — set both filters to `None` in `01_analysis.ipynb` for the full-dataset view.

![Healthcare Analysis](/python-analysis/healthcare_analysis.png)

### Power BI (Interactive)
![Power BI Dashboard](/powerbi/healthcare.png)

A Power BI version of this dashboard is available in this repo at 
`powerbi/healthcare.pbix` — open it in Power BI Desktop to interact with it directly.

### Excel (Detailed Business Analysis)

The Excel workbook goes beyond reproducing the initial dashboard analyses. It conducted a **detailed operational analysis of patient waiting times and appointment no-shows**, comparing performance across **2023 and 2024**.

The analysis examines changes across divisions, age groups and specialties and translates the findings into **business implications and suggested areas for further investigation**.

A separate report was created based on this detailed Excel analysis:

**[Detailed Analysis Report](https://drive.google.com/file/d/1d-OLGyjTmccbRypC3Rd5giu9S-_EOt4c/view?usp=sharing)**

Only selected dashboard visualizations are shown below for a quick overview. The complete set of visualizations, formulas, pivot tables, lookups and detailed analysis can be explored directly by opening the Excel workbook (`excel-sheets/appointments.xlsx`).

![Excel Dashboard](/excel-sheets/image1.png)
![Excel Dashboard](/excel-sheets/image2.png)


| Chart                              | What It Shows                                                   |
| ---------------------------------- | --------------------------------------------------------------- |
| Appointment Status Distribution    | Pie chart of Completed / Cancelled / No-show rates              |
| No-show Rate by Division           | Which divisions have the highest missed appointments            |
| Appointments by Doctor's Specialty | Most in demand specialties across the dataset                   |
| Average Wait Days by Specialty     | Which specialties make patients wait the longest                |
| Patient Age Group Distribution     | Breakdown of Child, Young Adult, Middle Age and Senior patients |
| Monthly Appointment Trend          | How appointment volume changed across the year                  |

---

## Dataset

The dataset contains 500 patient appointment records with the following columns:

| Column                 | Description                     |
| ---------------------- | ------------------------------- |
| `patient_age`          | Age of the patient              |
| `patient_gender`       | Male / Female                   |
| `division`             | One of 8 Bangladesh divisions   |
| `specialty`            | Doctor specialty type           |
| `appointment_status`   | Completed / Cancelled / No-show |
| `consultation_fee_bdt` | Fee in Bangladeshi Taka         |
| `wait_days`            | Days waited before appointment  |
| `appointment_date`     | Date of appointment (2023–2024) |

---

## Analysis Covered

* Correlation analysis between patient age, consultation fee, wait days and appointment timing
* Appointment status breakdown by division or specialty (Completed, Cancelled, No-show)
* No-show rate by division (unaffected by filters — always full dataset)
* Most in demand specialties
* Average wait days by specialty or by division, if a specialty only filter is active
* Patient age group distribution by division or specialty
* Monthly appointment trend (2023–2024)

**Dynamic filtering:** `01_analysis.ipynb` has a `FILTER_DIVISION` / `FILTER_SPECIALTY` config near the top. Appointment status, average wait days, specialty demand, age distribution and monthly appointment trend re-scope to match; no-show rate by division intentionally stays on the full dataset for comparison context. The key findings above are always the full dataset, the Python dashboard image is committed with `FILTER_DIVISION = "Dhaka"` to demonstrate the filtering in action.

---

## Predictive Modeling

> Business question: given information available before an appointment, what is the probability the patient will not show up?

Three classifiers were trained and compared on the same features, same stratified train/test split, and same preprocessing (`ColumnTransformer` + `Pipeline`):

| Model | ROC-AUC |
|---|---:|
| Logistic Regression | 0.520 |
| Decision Tree | 0.563 |
| **Random Forest** | **0.585** |

**Target:** `No-show` → 1, `Completed`/`Cancelled` → 0.

**Features used:** `patient_age`, `patient_gender`, `division`, `doctor_specialty`, `wait_days`, plus `quarter`, `day_of_week`, `day_type`, and `month_name` engineered from `appointment_date`. `consultation_fee_bdt`, `age_group`, and raw `appointment_date`/`year` were deliberately excluded — see the leakage/redundancy discussion in `03_predictive_modeling.ipynb`.

**Result:** Random Forest performed best, but all three models stayed close to the 0.5 random baseline — the available features don't yet separate No-shows from non-No-shows strongly. Predicted probabilities are converted into four risk bands (Low / Moderate / High / Very High) that a scheduling team could use for relative prioritization, but shouldn't yet be treated as reliable individual predictions. Full reasoning, limitations, and conclusion are in the notebook.

---

## Project Structure

Analysis and visualization are split into separate notebooks so each stays focused and easy to maintain. Power BI and Excel/Google Sheets versions of the dashboard are also included as standalone files — no code needed, just open them directly.

| File/Folder | Purpose |
|---|---|
| `python-analysis/01_analysis.ipynb` | Loads, cleans and analyzes the appointment data. Saves results to `analysis_results.pkl`. |
| `python-analysis/02_visualization.ipynb` | Loads the pickled results and renders the 6-panel dashboard. |
| `python-analysis/utils/filters.py` | `filter_appointments()` helper — applies the division/specialty filter used by `01_analysis.ipynb`. |
| `python-analysis/03_predictive_modeling.ipynb` | Trains and compares Logistic Regression, Decision Tree, and Random Forest models to predict appointment no-shows. |
| `data/appointments_clean.csv` | Cleaned dataset exported from `01_analysis.ipynb`; used as the input for predictive modeling. |
| `powerbi/healthcare.pbix` | Interactive Power BI version of the dashboard. Open in Power BI Desktop. |
| `excel-sheets/appointments.xlsx` | Data + formulas + pivot tables + lookup functions + charts. Open in Excel or Google Sheets to inspect every technique directly. |

Run the notebooks in order — `01` before `02`. The Power BI and Excel files are standalone and can be opened independently at any time.

---

## Tech Stack

* **Python** — core language
* **Pandas** — data loading, cleaning and analysis
* **Matplotlib** — visualizations
* **Power BI** — interactive dashboard version
* **Excel / Google Sheets** — formula-based analysis (COUNTIF, COUNTIFS, SUMIF, AVERAGEIF, UNIQUE), pivot tables and lookup functions
* **Scikit-learn** — Logistic Regression, Decision Tree, Random Forest, `ColumnTransformer` + `Pipeline` for preprocessing

---

## Roadmap — Project Development Plan

The goal is to progressively develop this project from descriptive healthcare analytics into a decision-support system that combines **data analysis, predictive modeling, statistical validation, and human judgment (AI + HI)**.

The stages below represent the planned development direction of the project rather than a fixed timeline. Each stage builds on the previous one, allowing the analysis to become progressively more predictive, statistically rigorous, and decision-oriented.

### Stage 1 — Descriptive & Operational Analytics
**Status: Completed**

Establish a clear understanding of healthcare appointment patterns and identify operational areas that may require further investigation.

- Exploratory analysis using Python/Pandas
- Correlation analysis
- Division and specialty segmentation
- Appointment status analysis
- Waiting time analysis
- No-show analysis
- Power BI dashboard
- Excel reproduction
- **2023–2024 year-over-year operational review**
- Division × age group × specialty analysis
- Translation of analytical findings into business implications and suggested areas for investigation

### Stage 2 — Predictive Analytics
**Status: Ongoing**

Extend the descriptive analysis into predictive modeling by exploring whether appointment no-shows can be identified before they occur.

**Completed so far:**
- Developed a model to **predict appointment no-shows**
- Used features such as division, specialty, waiting time, age, and calendar-derived signals (quarter, day of week, day type, month)
- Established an interpretable **Logistic Regression** baseline
- Compared the baseline with **Decision Tree** and **Random Forest** models
- Evaluated model performance using **ROC-AUC**
- Interpreted the results in terms of their potential usefulness for appointment management rather than focusing only on predictive accuracy
- Class-imbalance handling (e.g. `class_weight`, resampling) intentionally deferred to keep this stage a simple, interpretable baseline
  
**Planned next:**
- Explore appropriate approaches for handling class imbalance, since no-shows represent a minority class
- Hyperparameter tuning for Decision Tree and Random Forest
- Re-evaluate ROC-AUC after these improvements to see whether they meaningfully lift the current 0.52–0.59 range

### Stage 3 — Statistical Validation
**Status: Planned**

Strengthen the findings from the earlier stages by statistically testing observed relationships and patterns.

- Validate selected observations using hypothesis testing, including:
  - Chi-square tests for categorical relationships
  - One-way ANOVA for differences across groups
- Report **p-values and effect sizes** alongside visualizations to distinguish meaningful patterns from observations that may require further evidence

### Stage 4 — Decision-Focused Modeling (AI + HI)
**Status: Advanced Development Direction**

Move beyond prediction toward a decision-support approach in which AI assists human decision-makers.

- **Cost-sensitive evaluation:** incorporate the different real-world costs of missed appointments and unnecessary follow-up actions when selecting prediction thresholds
- **Model explainability with SHAP:** identify the factors contributing to individual no-show predictions so that staff can understand why a patient was flagged
- **Human-in-the-loop simulation:** explore a workflow where the model identifies higher-risk appointments, staff review or follow up on those cases, and the resulting outcomes can inform future model improvement
- Evaluate the role of human judgment alongside model predictions in operational decision-making

### Stage 5 — Validation & Generalization
**Status: Future Development**

Assess whether the patterns and conclusions identified in the initial dataset remain meaningful when evaluated against a larger and more diverse dataset.

- Benchmark selected findings against a larger public healthcare no-show dataset
- Test whether relationships identified in the original dataset, such as waiting time and no-show behavior, remain consistent at a larger scale
- Compare areas of agreement and divergence between datasets
- Examine possible explanations for differences, including sample size, regional context, population characteristics, and data collection methods
- Reflect on the limitations of the original dataset and how larger-scale validation affects the reliability and generalizability of the findings

### Overall Direction

The project is intended to evolve progressively:

**Descriptive Analytics → Predictive Analytics → Statistical Validation → Decision-Focused AI → Generalization**

The broader objective is not simply to build a machine learning model, but to explore how **analytics and AI can support real-world operational decisions while keeping human judgment in the decision-making process**.

---

## About

Built by **Navidul Hoque** — a Backend Software Engineer transitioning into Data Science and AI.

This is one of my first hands-on data science projects as I work through a PGD in Data Science with ML & AI. Feedback and suggestions are welcome.

This README will be updated as the project evolves, with predictive modeling as the next development stage.

[LinkedIn](https://www.linkedin.com/in/navidul-hoque-04b850267)
