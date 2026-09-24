# PROJECT REPORT

---

## Title

**Job Market & Skill Demand Analytics Dashboard**
*(India IT Job Market Edition)*

---

## Abstract

This project presents a **self-contained** web-based data analytics dashboard built to analyse the Indian IT job market. The entire application — dataset generation, data processing, analytics, and the user interface — is contained within a **single Python file: `app.py`**. All 500 job-posting records are generated in-memory at startup using Python's `random` module and Pandas; no external CSV files, databases, or APIs are required. The application is built with Pandas for data processing, Plotly for interactive charts, and Streamlit for the web interface. It runs locally with a single command and works entirely offline. The goal is to demonstrate how data analytics tools can be used to draw meaningful insights from job market data in a simple, visual, and interactive way.

---

## 1. Introduction

The Indian IT sector is one of the fastest-growing industries in the world, with companies like Infosys, TCS, Wipro, and Cognizant employing hundreds of thousands of professionals. Every year, lakhs of engineering graduates enter the job market looking for roles in software development, data science, cloud computing, and business analytics.

However, for a fresh graduate or a student planning their career, it is often difficult to answer basic questions such as:

- Which programming skills should I learn first?
- Which cities have the most IT jobs?
- How much salary can I expect for a particular role?
- How many years of experience do most jobs require?

This project attempts to answer these questions through a fully interactive analytics dashboard. By loading a structured dataset of job postings and applying filters, charts, and summaries, the dashboard turns raw data into clear and useful insights.

---

## 2. Problem Statement

Job seekers in India, particularly fresh BTech graduates, often lack access to a consolidated view of the IT job market. They rely on scattered job portals, which present individual listings without any aggregated analysis. There is no easy way for a student to quickly see which skills are most in demand across hundreds of postings, compare salary ranges across different roles, or identify which cities are hiring the most.

This project addresses this gap by building a local analytics dashboard that processes job posting data and presents it visually, enabling users to explore and filter the data according to their own interests.

---

## 3. Objectives

1. Create a structured dataset of realistic Indian IT job postings with details such as job title, company, location, salary range, experience required, and technical skills.
2. Build an interactive web-based dashboard that displays this data through charts, KPI cards, and a searchable table.
3. Allow users to filter the data by job role, city, employment type, and experience level using sidebar controls.
4. Identify and display key insights such as the most demanded skill, highest-paying role, and top hiring city.
5. Display all salary values in Indian Rupees (INR), formatted in Lakhs (L) for readability.
6. Ensure the entire application runs locally using only free, open-source Python libraries.

---

## 4. Existing System

Currently, job seekers must visit platforms like Naukri, LinkedIn, or Indeed to search for job postings. These platforms have the following limitations when used for market analysis:

- **No aggregated view**: Each posting is shown individually; there is no summary of demand across hundreds of jobs.
- **No skill demand chart**: Users cannot easily see which skills appear most frequently across postings.
- **No salary comparison**: Salary ranges are often hidden or inconsistent, making it hard to compare roles.
- **Requires login and internet**: Most platforms require account creation and do not provide raw data for analysis.
- **No filtering for analysis**: Filtering is designed for job searching, not for data analysis or research purposes.

---

## 5. Proposed System

The proposed system is a locally running, **self-contained** Streamlit dashboard that solves all the above limitations:

- **Aggregated analysis**: All 500 job postings are generated and summarised at once inside `app.py`.
- **Skill demand visualisation**: A horizontal bar chart shows exactly how many jobs require each skill.
- **Salary comparison**: A grouped bar chart compares average minimum and maximum salaries for all 10 job roles.
- **No login, no CSV, no database required**: The application runs entirely offline; data is generated in-memory at startup.
- **Interactive filters**: Users can filter by role, location, employment type, and experience using sidebar controls, and all charts and KPIs update instantly.
- **Key Insights panel**: Automatically computed summaries highlight the most important findings from the filtered data.
- **Single file submission**: The complete application is in one file (`app.py`), making it easy to submit and share.

---

## 6. Technologies Used

| Technology | Version | Purpose |
|---|---|---|
| Python | 3.9+ | Core programming language; also used for in-memory data generation |
| Pandas | 2.0+ | DataFrame creation, filtering, grouping, aggregation |
| Streamlit | 1.32+ | Web-based interactive dashboard framework |
| Plotly Express | 5.18+ | Interactive charts (bar, histogram, donut pie) |

> No CSV file or external data storage is used. The `random` module (part of Python's standard library) generates all records inside `app.py`.

### Why these technologies?

- **Python** is the standard language for data analysis and is taught in most BTech programmes. Its standard `random` module is used to generate the synthetic dataset.
- **Pandas** provides powerful and simple tools for working with tabular data entirely in memory.
- **Streamlit** allows building a complete web dashboard in pure Python without any HTML, CSS, or JavaScript.
- **Plotly** creates professional-looking interactive charts that support hover tooltips and zooming.

---

## 7. System Requirements

### Hardware Requirements

| Component | Minimum |
|---|---|
| Processor | Intel Core i3 or equivalent |
| RAM | 4 GB |
| Storage | 500 MB free space |
| Display | 1280 × 720 resolution or higher |

### Software Requirements

| Software | Requirement |
|---|---|
| Operating System | Windows 10 / macOS / Ubuntu |
| Python | Version 3.9 or higher |
| pip | Python package manager |
| Web Browser | Chrome, Firefox, or Edge (for the Streamlit UI) |
| Internet | Not required to run the application |

### Python Packages

```
streamlit>=1.32.0
pandas>=2.0.0
plotly>=5.18.0
```

---

## 8. Dataset Description

### Source

The dataset is synthetically generated **inside `app.py`** using Python's `random` module and Pandas. It uses a fixed random seed (`random.seed(42)`) to ensure the same 500 records are produced every time the application starts. While the data is fictional, the salary ranges, skill probabilities, and company names are based on realistic patterns from the 2024 Indian IT job market.

No CSV file is read or written. The data exists only in memory during the application session.

### Structure

**500 rows · 21 columns** (18 raw + `salary_avg` derived column added at generation time)

### Columns

| Column | Data Type | Description | Example |
|---|---|---|---|
| `job_id` | String | Unique identifier for each posting | JOB0001 |
| `job_title` | String | The role being advertised | Data Scientist |
| `company` | String | Name of the hiring company | Infosys |
| `location` | String | City where the job is based | Bengaluru |
| `experience_years` | Integer | Minimum years of experience required | 3 |
| `salary_min` | Integer | Minimum annual salary in INR (absolute) | 800000 |
| `salary_max` | Integer | Maximum annual salary in INR (absolute) | 1400000 |
| `employment_type` | String | Type of employment | Full-Time |
| `python` | 0 or 1 | Whether Python is required | 1 |
| `java` | 0 or 1 | Whether Java is required | 0 |
| `sql` | 0 or 1 | Whether SQL is required | 1 |
| `excel` | 0 or 1 | Whether Excel is required | 1 |
| `aws` | 0 or 1 | Whether AWS is required | 0 |
| `azure` | 0 or 1 | Whether Azure is required | 0 |
| `power_bi` | 0 or 1 | Whether Power BI is required | 1 |
| `tableau` | 0 or 1 | Whether Tableau is required | 0 |
| `machine_learning` | 0 or 1 | Whether ML skills are required | 0 |
| `data_analysis` | 0 or 1 | Whether data analysis skills are required | 1 |

### Job Roles Covered (10 roles)

BI Analyst, Business Analyst, Cloud Engineer, Data Analyst, Data Engineer, Data Scientist, Java Developer, ML Engineer, Python Developer, Software Developer

### Locations Covered (9 Indian cities)

Bengaluru, Hyderabad, Pune, Chennai, Mumbai, Delhi, Noida, Gurgaon, Kochi

### Companies Covered (20 companies)

Infosys, TCS, Wipro, HCL Technologies, Tech Mahindra, Cognizant, Capgemini India, Mphasis, Hexaware Technologies, L&T Infotech, Mindtree, Persistent Systems, Zensar Technologies, NIIT Technologies, Mastech Digital, Cyient, Coforge, Sonata Software, Sasken Technologies, Infoedge India

---

## 9. Data Processing Methodology

All data generation and processing is done inside `app.py`. The following steps are performed:

### Step 1: Dataset Generation
The `generate_dataset()` function uses Python's `random` module to build 500 job-posting records and converts them into a Pandas DataFrame. It is decorated with `@st.cache_data` so it runs only once per session.

```python
@st.cache_data
def generate_dataset() -> pd.DataFrame:
    random.seed(42)
    # ... build 500 rows using reference data pools ...
    df = pd.DataFrame(rows)
    df["salary_avg"] = (df["salary_min"] + df["salary_max"]) / 2
    return df
```

### Step 2: Derived Column
The `salary_avg` column (midpoint of min and max salary) is added during generation. It is used for salary ranking in the Key Insights section.

```python
df["salary_avg"] = (df["salary_min"] + df["salary_max"]) / 2
```

### Step 3: Error Handling
The generator is wrapped in a `try/except` block. If anything goes wrong, Streamlit displays a clear error message and stops execution rather than crashing silently.

```python
try:
    df_full = generate_dataset()
except Exception as exc:
    st.error(f"Failed to generate dataset: {exc}")
    st.stop()
```

### Step 4: Sidebar Filtering
When the user adjusts any sidebar filter, the full dataset `df_full` is filtered using Pandas boolean masking to produce a filtered dataframe `df`. All charts and KPIs are computed from `df`, not from `df_full`.

```python
df = df_full[
    df_full["job_title"].isin(selected_roles) &
    df_full["location"].isin(selected_locations) &
    df_full["employment_type"].isin(selected_emp_types) &
    df_full["experience_years"].between(*selected_exp)
].copy()
```

### Step 5: Aggregations for Charts
Each chart uses a specific Pandas aggregation:
- **Role / Location / Employment type charts**: `value_counts()` to count occurrences.
- **Skill demand chart**: `.sum()` on binary skill columns (each 0 or 1), giving the number of jobs requiring each skill.
- **Salary chart**: `.groupby().agg()` to compute average minimum and maximum salary per role, then divided by 100,000 to convert to Lakhs.

### Step 6: INR Formatting
A helper function `fmt_inr()` converts raw rupee integers to a readable string:

```python
def fmt_inr(value: float) -> str:
    lakhs = value / 100_000
    return f"₹{lakhs:,.2f} L"
```

For example, `880000` becomes `₹8.80 L`.

---

## 10. Dashboard Features

### 1. Project Title and Description
The top of the page displays the dashboard title "India Job Market & Skill Demand Analytics Dashboard" and a one-line description of the project's purpose.

### 2. KPI Cards (4 cards)
Four metric cards at the top of the page provide an immediate summary:

| Card | What it shows |
|---|---|
| Total Jobs | Number of job postings matching current filters |
| Avg Min Salary (INR) | Average minimum salary across filtered jobs, in Lakhs |
| Avg Max Salary (INR) | Average maximum salary across filtered jobs, in Lakhs |
| Avg Experience | Average minimum experience required, in years |

### 3. Sidebar Filters (4 filters)
Users can narrow down the dataset using four controls on the left sidebar:

| Filter | Type | Options |
|---|---|---|
| Job Role | Multi-select | All 10 job titles |
| Location | Multi-select | All 9 Indian cities |
| Employment Type | Multi-select | Full-Time, Part-Time, Contract, Internship |
| Experience (years) | Range slider | 1 to 7 years |

When any filter is changed, all charts, KPI cards, the data table, and Key Insights update automatically.

### 4. Six Interactive Charts
All charts are built with Plotly Express and support hover tooltips, zoom, and pan.

### 5. Searchable Data Table
Below the charts, a full data table is displayed. A text search box allows the user to filter rows by typing any part of a job title, company name, or location. Salary values in the table are displayed in `₹X.XX L` format.

### 6. Key Insights Panel
Five automatically computed insight cards are shown at the bottom:
- Most Demanded Skill
- Most Common Job Role
- Top Hiring Location
- Highest Average Salary Role
- Average Experience Required

All values update when sidebar filters are changed.

---

## 11. Data Visualizations

### Chart 1: Jobs by Job Role *(Horizontal Bar Chart)*
- **Data**: Count of job postings per role using `value_counts()`
- **Colour scale**: Blues
- **Purpose**: Shows which roles are most frequently posted in the dataset

### Chart 2: Jobs by Location *(Horizontal Bar Chart)*
- **Data**: Count of job postings per city using `value_counts()`
- **Colour scale**: Teal
- **Purpose**: Identifies which cities have the highest hiring activity

### Chart 3: Most Demanded Skills *(Horizontal Bar Chart)*
- **Data**: Sum of each binary skill column across all filtered rows
- **Colour scale**: Oranges
- **Purpose**: Ranks the 10 technical skills by how many job postings require them

### Chart 4: Average Salary by Job Role *(Grouped Horizontal Bar Chart)*
- **Data**: Average minimum and maximum salary per role, expressed in INR Lakhs
- **Colours**: Blue for Avg Min Salary, Orange for Avg Max Salary
- **Purpose**: Allows direct comparison of salary ranges across all roles

### Chart 5: Experience Distribution *(Histogram)*
- **Data**: Distribution of the `experience_years` column
- **Bins**: 10
- **Purpose**: Shows how many jobs are available at each experience level

### Chart 6: Jobs by Employment Type *(Donut Pie Chart)*
- **Data**: Count of jobs by employment type
- **Hole**: 35% (donut style)
- **Purpose**: Shows the proportion of Full-Time, Contract, Part-Time, and Internship postings

---

## 12. Key Insights

The following insights are computed from the full 500-record dataset. These values will update dynamically when filters are applied in the live application.

| Insight | Value |
|---|---|
| Most Demanded Skill | SQL (required by 345 jobs — 69.0% of all postings) |
| Second Most Demanded Skill | Python (required by 336 jobs — 67.2%) |
| Most Common Job Role | Business Analyst (varies with 9-city distribution) |
| Top Hiring Location | Gurgaon (highest count across 9 Indian cities) |
| Highest Average Salary Role | ML Engineer (average ₹11.51 L per annum) |
| Average Experience Required | 3.9 years |
| Predominant Employment Type | Full-Time (354 jobs — 70.8% of all postings) |

### Salary Overview by Role

| Job Role | Avg Min Salary | Avg Max Salary |
|---|---|---|
| ML Engineer | ₹9.47 L | ₹13.55 L |
| Data Engineer | ₹7.63 L | ₹11.82 L |
| Data Scientist | ₹8.45 L | ₹12.22 L |
| Cloud Engineer | ₹7.44 L | ₹11.36 L |
| Business Analyst | ₹5.46 L | ₹9.77 L |
| Python Developer | ₹5.50 L | ₹9.34 L |
| Software Developer | ₹5.45 L | ₹9.09 L |
| Java Developer | ₹4.94 L | ₹8.96 L |
| BI Analyst | ₹5.06 L | ₹8.89 L |
| Data Analyst | ₹4.48 L | ₹8.69 L |

### Skill Demand Summary

| Skill | Jobs Requiring It | Percentage |
|---|---|---|
| SQL | 345 | 69.0% |
| Python | 336 | 67.2% |
| Data Analysis | 304 | 60.8% |
| AWS | 248 | 49.6% |
| Azure | 211 | 42.2% |
| Excel | 207 | 41.4% |
| Machine Learning | 204 | 40.8% |
| Java | 184 | 36.8% |
| Power BI | 151 | 30.2% |
| Tableau | 118 | 23.6% |

---

## 13. Results

The dashboard was successfully built and tested locally. The following results were observed:

1. **SQL and Python** are the top two skills demanded across the Indian IT job market in this dataset, appearing in 69% and 67.2% of all job postings respectively.

2. **ML Engineer** commands the highest average salary (₹11.51 L per annum), followed by Data Scientist (₹10.33 L) and Data Engineer (₹9.73 L).

3. **Gurgaon** leads all cities in job postings, followed by Mumbai and Pune (with Remote removed, jobs are distributed across 9 Indian cities only).

4. **Full-Time employment** accounts for 70.8% of all postings, confirming that it remains the dominant mode of employment in the Indian IT sector.

5. The average minimum experience required across all roles is **3.9 years**, with the majority of jobs falling in the 2–5 year bracket.

6. The interactive filters work correctly — selecting a single role, city, or employment type updates all six charts, all four KPI cards, the data table, and the Key Insights panel instantly.

7. The search box correctly filters the data table by job title, company name, and location.

---

## 14. Advantages

1. **Completely offline**: No internet connection, API key, login, or subscription is required.
2. **Single-file architecture**: The entire application — data generation, processing, and UI — is in one file (`app.py`), making it trivial to submit, share, or deploy.
3. **No external data dependency**: Data is generated in-memory; the app works even if every other file in the project folder is deleted.
4. **Instant interactivity**: Streamlit re-renders all components immediately when any filter is changed.
5. **Readable salary format**: The `fmt_inr()` function converts raw integers like `880000` into `₹8.80 L`, which is much easier to read.
6. **Reproducible dataset**: The generator uses `random.seed(42)`, so the exact same 500 records are produced every time, making results consistent.
7. **Lightweight**: The project requires no database, no server configuration, and no build tools. It can run on any computer with Python installed.

---

## 15. Limitations

1. **Synthetic data**: The dataset is generated programmatically and does not represent real job postings. Insights drawn from it cannot be applied to actual hiring decisions.
2. **In-memory only**: The dataset is not saved to disk. Each time the app starts, the same 500 records are regenerated from scratch (though `@st.cache_data` avoids this within a single session).
3. **No time dimension**: There is no date column in the dataset, so trends over time (e.g., skill demand growth month by month) cannot be analysed.
4. **Limited company coverage**: Only 20 companies are included. The dataset does not represent start-ups, product companies, or foreign MNCs operating in India.
5. **No geographic map**: Location data is limited to a dropdown filter. A map-based visualisation would give a stronger geographic picture.
6. **Skills scope**: Only 10 skills are tracked. Important skills like React, Docker, Kubernetes, Spark, and communication skills are not included.
7. **No export feature**: Users cannot download the filtered data as an Excel or CSV file from within the dashboard.

---

## 16. Future Enhancements

1. **Live data scraping**: Connect to job portals such as Naukri or LinkedIn (via their APIs or with permission) to automatically update the dataset with real job postings.
2. **Time-series analysis**: Add a posting date column and plot how skill demand and salary levels change over weeks or months.
3. **More skills and roles**: Expand the skill columns to include Docker, Kubernetes, React, Node.js, and Spark; add more niche roles such as MLOps Engineer and DevOps Engineer.
4. **Map visualisation**: Use Plotly's map chart or Folium to show job density across Indian cities on an actual geographic map.
5. **Salary calculator**: Add an input form where a user can select their skills and experience level, and the dashboard recommends an expected salary range.
6. **Export to Excel**: Add a download button so users can export the filtered data table as an Excel or CSV file.
7. **Cloud deployment**: Deploy the application to Streamlit Community Cloud so that it is accessible from any device without local installation.
8. **Company-level analysis**: Add a company filter and show which companies are hiring the most and which offer the best salaries.

---

## 17. Conclusion

This project successfully demonstrates how Python-based data analytics tools can be used to build a meaningful and interactive job market dashboard. The application generates, processes, filters, and visualises 500 synthetic Indian IT job postings entirely within a single Python file — no CSV, no database, and no external services required. It presents the data across six interactive charts, four KPI cards, a searchable table, and an auto-computed insights panel.

The dashboard clearly shows that SQL and Python are the most universally demanded skills, that ML Engineers command the highest salaries in the Indian IT market, that Mumbai is the leading hiring city in the dataset, and that most jobs require 2–5 years of experience.

The project is simple enough for a BTech student to understand and modify, yet complete enough to demonstrate real data analytics concepts including data loading, cleaning, filtering, aggregation, visualisation, and insight generation — all using industry-standard open-source tools.

---

## 18. How to Run the Project

### Prerequisites
- Python 3.9 or higher must be installed on your computer.
- `pip` must be available (it comes with Python by default).

### Step 1: Install Required Packages

Open a terminal or command prompt, navigate to the project folder, and run:

```bash
pip install -r requirements.txt
```

### Step 2: Launch the Dashboard

```bash
streamlit run app.py
```

Streamlit will start a local web server and automatically open the dashboard in your default web browser at:

```
http://localhost:8501
```

That is all. There is no Step 3 — `app.py` generates its own data internally at startup.

### Files Required to Run

Only these files are needed:

| File | Purpose |
|---|---|
| `app.py` | The complete self-contained application |
| `requirements.txt` | Python package list |

### Files for Submission

| File | Purpose |
|---|---|
| `app.py` | Complete application |
| `requirements.txt` | Dependencies |
| `README.md` | Project overview |
| `PROJECT_REPORT.md` | This report |

### Development Files (Not Required to Run)

The files `generate_dataset.py` and `job_postings.csv` were used during development but are **not required** by `app.py`. The application works correctly even if these files are absent.

---

*Report prepared for BTech College Project submission.*
*Project: Job Market & Skill Demand Analytics Dashboard — India Edition*
