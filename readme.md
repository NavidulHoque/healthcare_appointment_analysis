# Bangladesh Healthcare Appointment Analysis

A healthcare analytics project based on **500 appointment records from 8 divisions of Bangladesh**. The project explores patient behavior, appointment attendance, waiting times, and the operational issues that may affect healthcare service delivery.

The analysis was developed using **Python, Excel, and Power BI**, with the goal of turning raw appointment data into clear business insights. The project was then extended into predictive modeling to test whether the available data could be used to predict **patient no-shows** and **waiting times** before an appointment happens.

---

## What This Project Does

The project analyzes 500 healthcare appointment records to answer practical questions such as:

* Where are appointments most frequently being missed?
* Which specialties have the highest demand?
* Which patients and divisions experience longer waiting times?
* How does appointment activity change over time?
* Can the available information be used to predict whether a patient will miss an appointment?
* Can the available information be used to predict how many days a patient will have to wait?

### Key Findings

* The exploratory analysis found **no meaningful relationship between patient age, consultation fee, and waiting time**.
* **68.6%** of appointments were completed.
* **Dhaka** had the highest overall no-show rate at **14.6%**.
* **Pediatricians** were the most frequently visited specialty, with **92 appointments**.
* **General Physicians** had the longest average waiting time at **11.6 days**.
* **Senior patients (56+)** were the largest age group, with **162 patients**.
* Predictive modeling was tested for both no-shows and waiting times. The available data did not contain strong enough patterns to make reliable predictions.

---

## Visualizations

### Excel — Detailed Business Analysis

The Excel workbook goes beyond the initial summary analysis and provides a **detailed operational view of appointment activity, waiting times, and no-shows across 2023 and 2024**.

The workbook contains two focused dashboards:

#### 1. Waiting Time Dashboard

Examines patient waiting times across:

* Divisions
* Medical specialties
* Age groups
* Time periods

The dashboard helps identify where patients are waiting longer and which areas require further investigation.

#### 2. Appointment Volume and No-Show Dashboard

Combines appointment demand and attendance analysis, focusing on how appointment activity is distributed and where missed appointments occur across:

* Divisions
* Medical specialties
* Age groups
* Monthly trends

The dashboard helps identify where and when appointment demand is concentrated and **where no-shows are concentrated and which patient groups or specialties may require closer attention**.

The Excel analysis was used to produce a separate business-focused report comparing **2023 and 2024 performance**, including key findings, business implications, and suggested areas for further investigation.

**Detailed Analysis Report:**
[Detailed Analysis Report](https://drive.google.com/file/d/1PnTLh_ZEAL63WnPt3WAY5iU_O9Lr-JdM/view?usp=sharing)

The complete Excel workbook contains the underlying data, formulas, PivotTables, lookups, and detailed analysis:

`excel-sheets/appointments.xlsx`

#### Excel Dashboard Screenshots

<!-- Add Excel dashboard screenshots here -->

![Excel Appointment Volume Dashboard](/excel-sheets/image1.png)

![Excel Waiting Time / No-Show Dashboard](/excel-sheets/image2.png)

---

### Power BI — Interactive Dashboard

An interactive Power BI dashboard is **coming soon**.

The Power BI version will provide an interactive way to explore the same healthcare appointment data and findings.

---

## Dataset

The cleaned dataset (`data/appointments_clean.csv`) contains **500 healthcare appointment records**.

| Column               | Description                                               |
| -------------------- | --------------------------------------------------------- |
| `Age`                | Age of the patient                                        |
| `Gender`             | Male / Female                                             |
| `Division`           | One of 8 divisions of Bangladesh                          |
| `Doctor Specialty`   | Type of doctor seen, such as Pediatrician or Cardiologist |
| `Appointment Status` | Completed / Cancelled / No-show                           |
| `Consultation Fee`   | Consultation fee in Bangladeshi Taka (BDT)                |
| `Wait Days`          | Number of days between booking and the appointment        |
| `Appointment Date`   | Date of the appointment, covering 2023–2024               |

Several additional fields were created during data preparation and used throughout the analysis:

* **Age Group** — Child / Young Adult / Middle Age / Senior
* **Day of Week** — The day on which the appointment took place
* **Day Type** — Weekday / Weekend
* **No Show Flag** — A simple indicator used for no-show analysis and predictive modeling

---

## Analysis Covered

The project covers the following areas:

* Relationship between patient age, consultation fee, and waiting time
* Appointment status breakdown
* No-show rate
* Most frequently visited medical specialties
* Average, total, maximum, and minimum waiting times
* Patient age group distribution
* Monthly appointment trends across 2023–2024
* Year-over-year changes in waiting times and no-shows
* Division, age-group, and specialty-level comparisons

The deeper Excel analysis focuses particularly on waiting times and no-shows, helping connect the findings to practical business problems and areas for further investigation.

---

## Predictive Modeling

The project also tested whether the available appointment data could be used to make predictions **before an appointment happens**.

Two prediction tasks were explored:

1. **Predicting whether a patient will miss an appointment**
2. **Predicting how many days a patient will have to wait**

The goal was not simply to build a model that produces a number. The goal was to find out whether the available information actually contains enough useful patterns to support reliable predictions.

### 1. Will the Patient Show Up?

**Business question:**
Given information available before an appointment happens, can we predict whether a patient will miss the appointment?

Three different approaches were tested:

* Logistic Regression
* Decision Tree
* Random Forest

Each model was tested before and after fine-tuning.

#### Result

| Model               | Before Fine-Tuning | After Fine-Tuning |
| ------------------- | -----------------: | ----------------: |
| Logistic Regression |              0.595 |             0.584 |
| Decision Tree       |              0.484 |             0.574 |
| **Random Forest**   |              0.531 |         **0.588** |

The scores above use **ROC-AUC**, a common measure for evaluating how well a model can perform. A score of **0.50 is roughly equivalent to random guessing**, while a score closer to **1.00 indicates stronger predictive ability**.

The fine-tuned Random Forest achieved the highest ROC-AUC score of **0.588**, indicating only weak predictive performance. This suggests that the available information is not sufficient for reliable no-show prediction.

The information used included:

* Age Group
* Gender
* Division
* Doctor Specialty
* Wait Days
* Quarter
* Month
* Day of Week
* Weekday / Weekend

The result suggests that these variables alone are **not sufficient for reliable no-show prediction**.

Patient absence are likely affected by operational factors that are not included in the dataset, such as:

* Reminder history
* Travel distance

The full analysis, model comparisons, and limitations are available in:

`python-analysis/02_no_show_predictive_modeling.ipynb`

---

### 2. How Many Days Will the Patient Wait?

**Business question:**
Given information available when a patient books an appointment, can we predict how many days the patient will have to wait?

Because waiting time is a number rather than a yes/no outcome, different prediction methods were used:

* Linear Regression
* Ridge Regression
* Decision Tree
* Random Forest
* Gradient Boosting

The models were also fine-tuned and compared.

#### Result

| Model                 | Before Fine-Tuning | After Fine-Tuning |
| --------------------- | -----------------: | ----------------: |
| Naive Mean baseline |            -0.0049 |           -0.0049 |
| Linear Regression     |            -0.0670 |           -0.0670 |
| Ridge Regression      |            -0.0655 |           -0.0192 |
| Decision Tree         |            -1.2566 |           -0.0615 |
| Random Forest         |            -0.1296 |           -0.0421 |
| **Gradient Boosting** |            -0.0909 |       **-0.0073** |

The scores are called **R²**, which shows how well a model predicts  waiting time. An **R² of 0** means the model performs about the same as simply predicting the average waiting time (Naive Mean baseline). A **negative R²** means the model performs worse than that baseline.

**No model outperformed the naive baseline, either before or after fine-tuning.** The fine-tuned Gradient Boosting model came closest, with an R² of **-0.0073**, but this is still effectively the same as predicting the average waiting time for every patient. This suggests that the available features contain **very little useful information for predicting waiting time**.

The available information included factors such as:

* Patient age
* Gender
* Division
* Doctor Specialty
* Booking date

Waiting times are likely affected by operational factors that are not included in the dataset, such as:

* Clinic capacity
* Staff availability
* Doctor workload

This is an important finding because it shows that **more complex modeling does not automatically produce useful predictions when the underlying data does not contain enough information**.

The full analysis and limitations are available in:

`python-analysis/03_wait_days_predictive_modeling.ipynb`

---

## Project Structure

The project is divided into separate notebooks and files so that each part of the analysis remains focused and easy to explore.

| File / Folder                                            | Purpose                                                                                         |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `python-analysis/01_analysis.ipynb`                      | Loads the cleaned data, and explores the appointment data and produces some useful analysis              |
| `python-analysis/02_no_show_predictive_modeling.ipynb`   | Builds and compares models for predicting patient no-shows                                      |
| `python-analysis/03_wait_days_predictive_modeling.ipynb` | Builds and compares models for predicting patient waiting time                                  |
| `python-analysis/utils/filters.py`                       | Helper function used to filter the analysis by division and specialty                           |
| `data/appointments.csv`                                  | Original, unprocessed dataset                                                                   |
| `data/appointments_clean.csv`                            | Cleaned dataset with additional calculated fields                                               |
| `powerbi/healthcare.pbix`                                | Power BI dashboard file                                                                         |
| `excel-sheets/appointments.xlsx`                         | Excel workbook containing the detailed analysis, formulas, PivotTables, and dashboards |

The Python notebooks should be run in order:

`01_analysis.ipynb` → `02_no_show_predictive_modeling.ipynb` → `03_wait_days_predictive_modeling.ipynb`

The Excel and Power BI files can be opened independently.

---

## Tech Stack

* **Python** — Data analysis and preparation
* **Pandas** — Data cleaning and analysis
* **Matplotlib** — Data visualization
* **Excel** — Detailed analysis, formulas, PivotTables, and dashboards
* **Power BI** — Interactive dashboard development
* **Scikit-learn** — Predictive modeling, model comparison, preprocessing, and fine-tuning

Models used:

* Logistic Regression
* Decision Tree
* Random Forest
* Linear Regression
* Ridge Regression
* Gradient Boosting

---

## About

Built by **Navidul Hoque** — a Backend Software Engineer transitioned into Data Science and AI.

This is one of my first hands-on data science projects while pursuing a **Post Graduate Diploma in Data Science with Machine Learning and Artificial Intelligence**.

The project reflects my interest in using **data, technology, and analytical thinking to understand real-world business and operational problems**.

Feedback and suggestions are welcome.

[LinkedIn](https://www.linkedin.com/in/navidul-hoque-04b850267)
