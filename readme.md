# Bangladesh Healthcare Appointment Analysis

A data analysis project exploring patient appointment patterns across 8 divisions of Bangladesh — looking at no-show rates, specialty demand, wait times and patient demographics.

---

## What This Project Does

I analyzed 500+ appointment records to find patterns that could help healthcare providers understand patient behavior and improve service delivery.

**Key findings:**
- Overall appointment completion rate is **68.6%**
- **Dhaka** has the highest no-show rate at **14.6%** — likely due to traffic and urban lifestyle factors
- **Pediatricians** are the most visited specialty with 92 appointments
- **General Physicians** have the longest average wait time at **11.6 days**
- **Senior patients (56+)** make up the largest patient group

---

## Visualizations

Built a 6 panel dashboard covering all key analyses:

### Python (Matplotlib)
![Healthcare Analysis](/src/healthcare_analysis.png)

### Power BI (Interactive)
![Power BI Dashboard](/powerbi/healthcare.png)

A Power BI version of this dashboard is available in this repo at 
`powerbi/healthcare.pbix` — open it in Power BI Desktop to interact with it directly.

| Chart | What It Shows |
|---|---|
| Appointment Status Distribution | Pie chart of Completed / Cancelled / No-show rates |
| No-show Rate by Division | Which divisions have the highest missed appointments |
| Appointments by Doctor's Specialty | Most in demand specialties across the dataset |
| Average Wait Days by Specialty | Which specialties make patients wait the longest |
| Patient Age Group Distribution | Breakdown of Child, Young Adult, Middle Age and Senior patients |
| Monthly Appointment Trend (2024) | How appointment volume changed across the year |

---

## Dataset

The dataset contains 500 patient appointment records with the following columns:

| Column | Description |
|---|---|
| `patient_age` | Age of the patient |
| `patient_gender` | Male / Female |
| `division` | One of 8 Bangladesh divisions |
| `specialty` | Doctor specialty type |
| `appointment_status` | Completed / Cancelled / No-show |
| `consultation_fee_bdt` | Fee in Bangladeshi Taka |
| `wait_days` | Days waited before appointment |
| `appointment_date` | Date of appointment (2023–2024) |

---

## Analysis Covered

- Appointment status breakdown (Completed, Cancelled, No-show)
- No-show rate by division
- Most in demand specialties
- Average wait days by specialty
- Patient age group distribution
- Monthly appointment trend (2023–2024)

---

## Project Structure

Analysis and visualization are split into separate notebooks so each stays focused and easy to maintain:

| File | Purpose |
|---|---|
| `01_analysis.ipynb` | Loads, cleans and analyzes the appointment data. Saves results to `analysis_results.pkl`. |
| `02_visualization.ipynb` | Loads the pickled results and renders the 6-panel dashboard. |

Run them in order — `01` before `02`.

---

## How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/healthcare-appointment-analysis

# Install dependencies
pip install pandas matplotlib

# Run the notebook
jupyter notebook 01_analysis.ipynb

# then
jupyter notebook 02_visualization.ipynb 
```

Or open directly in [Google Colab](https://colab.research.google.com/) — no setup needed.

---

## Tech Stack

- **Python** — core language
- **Pandas** — data loading, cleaning and analysis
- **Matplotlib** — visualizations
- **Power BI** — interactive dashboard version

---

## Roadmap — What's Coming Next

The goal is to grow this into a complete, end-to-end project — from raw data to a decision-support system that combines AI predictions with human judgment (AI + HI), validated with proper statistical rigor.

### Stage 2 — Machine Learning Basics
- Train a model to **predict appointment no-shows** before they happen
- Handle class imbalance (no-shows are the minority class) using techniques like `class_weight` or oversampling
- Features: division, specialty, wait days, age group, consultation fee
- Start with Logistic Regression (interpretable baseline), then compare against Random Forest
- Evaluate using accuracy, precision, recall, F1-score, confusion matrix, and ROC-AUC

### Stage 3 — Statistical Foundations
- Correlation analysis between consultation fee and no-show rate
- Gender-based appointment pattern analysis
- Seasonal trend analysis across 2023 vs 2024
- Validate observed patterns with hypothesis testing:
  - Chi-square test (e.g. gender vs. specialty, division vs. appointment status)
  - One-way ANOVA (e.g. consultation fee vs. division)
- Report p-values and effect sizes alongside visualizations, not just descriptive charts

### Stage 4 — Decision-Focused Modeling (AI + HI)
- **Cost-sensitive evaluation**: build a cost matrix reflecting real-world impact (a missed appointment costs the clinic far more than an unnecessary reminder call) and optimize the model's decision threshold against it, rather than using a default 0.5 cutoff
- **Model explainability with SHAP**: surface the top factors behind each individual no-show prediction, so a human reviewer (scheduler/nurse) understands *why* a patient was flagged before acting on it
- **Human-in-the-loop simulation**: simulate a workflow where the model flags high-risk patients → staff follow up to confirm → outcomes are fed back into the training data, demonstrating how AI and human judgment work together rather than AI making decisions in isolation

### Stage 5 — Validation & Generalization
- Benchmark findings against a larger public healthcare no-show dataset (100k+ records)
- Test whether patterns identified in this dataset (e.g. wait time vs. no-show rate) hold up at scale
- Discuss where results agree or diverge, and why (sample size, regional/cultural context, data collection differences)
- Reflect critically on the limitations of the original dataset and what the larger-scale comparison reveals

---

## About

Built by **Navidul Hoque** — a Backend Software Engineer transitioning into Data Science and AI.

This is one of my first hands-on data science projects as I work through a PGD in Data Science with ML & AI. Feedback and suggestions are welcome.

[LinkedIn](https://www.linkedin.com/in/navidul-hoque-04b850267)
