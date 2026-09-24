# Job Market & Skill Demand Analytics Dashboard

## Introduction

This is a **self-contained** data analytics dashboard for the Indian IT job market.  
The entire application — dataset generation, data processing, and the interactive UI — lives in a **single file: `app.py`**.

No CSV files, databases, APIs, or external services are needed.  
Running `streamlit run app.py` is all that is required.

---

## Problem Statement

Job seekers and students often lack a consolidated, visual view of the IT job market. This dashboard analyses 500 realistic fictional Indian IT job postings to surface insights on skill demand, salary ranges, hiring cities, and experience requirements — all in one interactive page.

---

## Objectives

1. Generate 500 synthetic Indian IT job-posting records in-memory at startup.
2. Provide interactive filters for role, location, employment type, and experience.
3. Display in-demand skills, salary ranges (INR), and hiring trends through interactive charts.
4. Show automatically computed key insights from the filtered data.
5. Work entirely offline with no external dependencies beyond three Python libraries.

---

## Technologies Used

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.9+ | Core language |
| Pandas | 2.0+ | Data generation, filtering, aggregation |
| Streamlit | 1.32+ | Interactive web dashboard |
| Plotly Express | 5.18+ | Interactive charts |

---

## Architecture – Self-Contained Single File

All logic is in `app.py`, organised into 10 clearly labelled sections:

| Section | Responsibility |
|---|---|
| 1 | Dataset generation (500 records, in-memory, `random.seed(42)`) |
| 2 | Helper utilities (`fmt_inr` INR formatter) |
| 3 | Data loading (calls cached generator) |
| 4 | Sidebar filter widgets |
| 5 | Filtering logic (boolean masking with Pandas) |
| 6 | Page header |
| 7 | KPI cards |
| 8 | Six Plotly charts |
| 9 | Searchable data table |
| 10 | Business insight calculations + Key Insights panel |

---

## Dataset Description

Generated internally by `app.py` every session (cached for the duration of the session):

- **500 job postings**, 10 Indian IT roles, 9 Indian cities, 20 companies
- **Salary**: INR per annum, stored as integers, displayed in Lakhs (₹X.XX L)
- **Skills**: 10 binary columns (0/1) — Python, Java, SQL, Excel, AWS, Azure, Power BI, Tableau, Machine Learning, Data Analysis
- **Seed**: `random.seed(42)` — results are identical on every run

---

## Features

- **KPI Cards** — Total Jobs · Avg Min Salary · Avg Max Salary · Avg Experience
- **Sidebar Filters** — Job Role · Location · Employment Type · Experience (slider)
- **6 Interactive Charts** — Jobs by Role · Jobs by Location · Most Demanded Skills · Avg Salary by Role · Experience Distribution · Employment Type donut
- **Searchable Data Table** — search by title, company, or location; salary shown in ₹ Lakhs
- **Key Insights Panel** — Most demanded skill · Most common role · Top location · Highest salary role · Avg experience

---

## How to Install

```bash
# 1. Navigate to the project folder
cd Job_Market_Analytics

# 2. (Optional) create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt
```

---

## How to Run

```bash
streamlit run app.py
```

The dashboard opens automatically at **http://localhost:8501**.

No other steps are required. `app.py` generates all data internally on startup.

---

## Files for Submission

| File | Description |
|---|---|
| `app.py` | Complete self-contained application |
| `requirements.txt` | Python package dependencies |
| `README.md` | This file |
| `PROJECT_REPORT.md` | Full project report |

> The files `generate_dataset.py` and `job_postings.csv` are **development files** and are **not required** to run the application.

---

## Expected Results

- SQL and Python are the top demanded skills.
- ML Engineer commands the highest average salary (~₹11.5 L).
- Mumbai leads all cities in job postings.
- ~71% of postings are Full-Time roles.
- Average experience required is ~3.9 years.

---

## Future Enhancements

- Scrape live job postings from job portals to replace synthetic data.
- Add a time-series chart to track skill demand trends over time.
- Include a salary calculator based on selected skills and experience.
- Deploy to Streamlit Community Cloud for public access.
