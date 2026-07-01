# Bangladesh Healthcare Appointment Analysis

A data analysis project exploring patient appointment patterns across 8 divisions of Bangladesh — looking at no-show rates, specialty demand, wait times and patient demographics.

---

## What This Project Does

I analyzed 500+ appointment records to find patterns that could help healthcare providers understand patient behavior and improve service delivery.

**Key findings so far:**
- Overall appointment completion rate is **68.6%**
- **Dhaka** has the highest no-show rate at **14.6%** — likely due to traffic and urban lifestyle factors
- **Pediatricians** are the most visited specialty with 92 appointments
- **General Physicians** have the longest average wait time at **11.6 days**
- **Senior patients (56+)** make up the largest patient group

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

## How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/healthcare-appointment-analysis

# Install dependencies
pip install pandas numpy matplotlib

# Run the notebook
jupyter notebook analysis.ipynb
```

Or open directly in [Google Colab](https://colab.research.google.com/) — no setup needed.

---

## Tech Stack

- **Python** — core language
- **Pandas** — data loading, cleaning and analysis
- **NumPy** — numerical operations
- **Matplotlib** — visualizations *(will implement soon — see roadmap below)*

---

## Roadmap — What's Coming Next

This is just the starting point. I'm planning to expand this project in stages:

**Stage 2 — Visualizations**
- Add charts back with proper formatting and labels
- Build a dashboard style summary chart combining all 6 analyses

**Stage 3 — Machine Learning**
- Train a model to **predict appointment no-shows** before they happen
- Features will include division, specialty, wait days, age group and consultation fee
- Try Logistic Regression first, then Random Forest for comparison
- Evaluate using accuracy, precision, recall and confusion matrix

**Stage 4 — Deeper Insights**
- Correlation analysis between consultation fee and no-show rate
- Gender-based appointment pattern analysis
- Seasonal trend analysis across 2023 vs 2024

The goal is to eventually turn this into a complete end-to-end ML project — from raw data to a trained model that gives real, actionable predictions.

---

## About

Built by **Navidul Hoque** — a Backend Software Engineer transitioning into Data Science and AI Engineering.

This is one of my first hands-on data science projects as I work through a PGD in Data Science with ML & AI. Feedback and suggestions are welcome.

[LinkedIn](https://www.linkedin.com/in/navidul-hoque-04b850267)