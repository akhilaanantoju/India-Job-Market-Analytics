"""
app.py
------
Job Market & Skill Demand Analytics Dashboard – India Edition
Self-contained Streamlit application.

All 500 job-posting records are generated in-memory at startup.
No external files, databases, or APIs are required.

Run with:
    streamlit run app.py
"""

import random
import streamlit as st
import pandas as pd
import plotly.express as px

# ===========================================================================
# PAGE CONFIGURATION – must be the very first Streamlit call
# ===========================================================================
st.set_page_config(
    page_title="India Job Market Analytics",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ===========================================================================
# SECTION 1 – DATASET GENERATION
# Generates 500 realistic fictional Indian IT job-posting records in-memory.
# Uses a fixed random seed so results are reproducible across every run.
# ===========================================================================

@st.cache_data
def generate_dataset() -> pd.DataFrame:
    """
    Build and return a DataFrame of 500 synthetic Indian IT job postings.
    Cached by Streamlit so it is computed only once per session.
    """

    random.seed(42)

    # -----------------------------------------------------------------------
    # Reference data pools
    # -----------------------------------------------------------------------
    JOB_TITLES = [
        "Data Analyst", "Data Scientist", "Business Analyst",
        "Software Developer", "Java Developer", "Python Developer",
        "ML Engineer", "BI Analyst", "Cloud Engineer", "Data Engineer",
    ]

    COMPANIES = [
        "Infosys", "TCS", "Wipro", "HCL Technologies", "Tech Mahindra",
        "Cognizant", "Capgemini India", "Mphasis", "Hexaware Technologies",
        "L&T Infotech", "Mindtree", "Persistent Systems", "Zensar Technologies",
        "NIIT Technologies", "Mastech Digital", "Cyient", "Coforge",
        "Sonata Software", "Sasken Technologies", "Infoedge India",
    ]

    LOCATIONS = [
        "Bengaluru", "Hyderabad", "Pune", "Chennai", "Mumbai",
        "Delhi", "Noida", "Gurgaon", "Kochi",
    ]

    EMPLOYMENT_TYPES = ["Full-Time", "Part-Time", "Contract", "Internship"]

    # Skill requirement probabilities per role
    # Order: python  java   sql   excel  aws   azure  power_bi  tableau  ml    da
    SKILL_PROFILES = {
        "Data Analyst":      [0.65, 0.10, 0.90, 0.85, 0.30, 0.25, 0.60, 0.55, 0.30, 0.95],
        "Data Scientist":    [0.95, 0.10, 0.80, 0.45, 0.55, 0.45, 0.20, 0.30, 0.90, 0.85],
        "Business Analyst":  [0.30, 0.10, 0.70, 0.90, 0.20, 0.15, 0.65, 0.55, 0.20, 0.80],
        "Software Developer":[0.65, 0.85, 0.55, 0.20, 0.55, 0.45, 0.10, 0.08, 0.25, 0.35],
        "Java Developer":    [0.15, 0.99, 0.60, 0.20, 0.50, 0.40, 0.08, 0.08, 0.20, 0.30],
        "Python Developer":  [0.99, 0.15, 0.60, 0.25, 0.55, 0.40, 0.10, 0.10, 0.50, 0.55],
        "ML Engineer":       [0.95, 0.20, 0.60, 0.20, 0.65, 0.50, 0.10, 0.10, 0.95, 0.70],
        "BI Analyst":        [0.40, 0.15, 0.85, 0.70, 0.30, 0.30, 0.88, 0.80, 0.20, 0.78],
        "Cloud Engineer":    [0.65, 0.60, 0.40, 0.15, 0.92, 0.88, 0.10, 0.05, 0.25, 0.25],
        "Data Engineer":     [0.90, 0.55, 0.88, 0.30, 0.75, 0.60, 0.15, 0.10, 0.40, 0.65],
    }

    # INR annual salary bands (min_base, max_base) – realistic 2024 Indian IT market
    SALARY_BASES = {
        "Data Analyst":      (400_000,   900_000),
        "Data Scientist":    (800_000, 1_800_000),
        "Business Analyst":  (500_000, 1_100_000),
        "Software Developer":(500_000, 1_300_000),
        "Java Developer":    (450_000, 1_200_000),
        "Python Developer":  (500_000, 1_300_000),
        "ML Engineer":       (900_000, 2_000_000),
        "BI Analyst":        (450_000, 1_000_000),
        "Cloud Engineer":    (700_000, 1_600_000),
        "Data Engineer":     (700_000, 1_700_000),
    }

    # Minimum–maximum experience bands per role
    EXPERIENCE_BASES = {
        "Data Analyst":      (1, 5),
        "Data Scientist":    (2, 7),
        "Business Analyst":  (1, 5),
        "Software Developer":(1, 6),
        "Java Developer":    (1, 6),
        "Python Developer":  (1, 6),
        "ML Engineer":       (2, 7),
        "BI Analyst":        (1, 5),
        "Cloud Engineer":    (2, 7),
        "Data Engineer":     (2, 7),
    }

    # -----------------------------------------------------------------------
    # Generate 500 records
    # -----------------------------------------------------------------------
    SKILL_COLS = [
        "python", "java", "sql", "excel", "aws",
        "azure", "power_bi", "tableau", "machine_learning", "data_analysis",
    ]
    NUM_RECORDS = 500
    rows = []

    for i in range(1, NUM_RECORDS + 1):
        title  = random.choice(JOB_TITLES)
        probs  = SKILL_PROFILES[title]
        skills = [1 if random.random() < p else 0 for p in probs]

        sal_base_min, _ = SALARY_BASES[title]
        salary_noise = random.randint(-50_000, 150_000)
        salary_min   = max(200_000, round((sal_base_min + salary_noise) / 10_000) * 10_000)
        salary_range = random.randint(200_000, 600_000)
        salary_max   = salary_min + salary_range

        exp_lo, exp_hi = EXPERIENCE_BASES[title]
        experience = random.randint(exp_lo, exp_hi)

        emp_type = random.choices(
            EMPLOYMENT_TYPES,
            weights=[0.72, 0.06, 0.15, 0.07],
        )[0]

        row = {
            "job_id":           f"JOB{i:04d}",
            "job_title":        title,
            "company":          random.choice(COMPANIES),
            "location":         random.choice(LOCATIONS),
            "experience_years": experience,
            "salary_min":       salary_min,
            "salary_max":       salary_max,
            "employment_type":  emp_type,
        }
        # Attach skill flags
        for col, val in zip(SKILL_COLS, skills):
            row[col] = val

        rows.append(row)

    # -----------------------------------------------------------------------
    # Build DataFrame and add derived column
    # -----------------------------------------------------------------------
    df = pd.DataFrame(rows)
    df["salary_avg"] = (df["salary_min"] + df["salary_max"]) / 2
    return df


# ===========================================================================
# SECTION 2 – HELPER UTILITIES
# ===========================================================================

def fmt_inr(value) -> str:
    """Convert a raw INR integer to a human-readable lakhs string, e.g. ₹8.80 L."""
    if pd.isna(value):
        return "N/A"
    return f"\u20b9{value / 100_000:,.2f} L"


# Skill columns referenced throughout the dashboard
SKILL_COLS = [
    "python", "java", "sql", "excel", "aws",
    "azure", "power_bi", "tableau", "machine_learning", "data_analysis",
]


# ===========================================================================
# SECTION 3 – DATA LOADING  (calls the cached generator)
# ===========================================================================

try:
    df_full = generate_dataset()
except Exception as exc:
    st.error(f"Failed to generate dataset: {exc}")
    st.stop()


# ===========================================================================
# SECTION 4 – SIDEBAR FILTERS
# ===========================================================================

st.sidebar.image("https://img.icons8.com/fluency/96/job.png", width=64)
st.sidebar.title("Filters")

# Job Role
all_roles = sorted(df_full["job_title"].unique())
selected_roles = st.sidebar.multiselect("Job Role", options=all_roles, default=all_roles)

# Location
all_locations = sorted(df_full["location"].unique())
selected_locations = st.sidebar.multiselect("Location", options=all_locations, default=all_locations)

# Employment Type
all_emp_types = sorted(df_full["employment_type"].unique())
selected_emp_types = st.sidebar.multiselect("Employment Type", options=all_emp_types, default=all_emp_types)

# Experience slider
exp_min = int(df_full["experience_years"].min())
exp_max = int(df_full["experience_years"].max())
selected_exp = st.sidebar.slider(
    "Experience (years)",
    min_value=exp_min,
    max_value=exp_max,
    value=(exp_min, exp_max),
)

# ===========================================================================
# SECTION 5 – FILTERING LOGIC
# Apply all sidebar selections to produce the working dataframe `df`
# ===========================================================================

df = df_full[
    df_full["job_title"].isin(selected_roles) &
    df_full["location"].isin(selected_locations) &
    df_full["employment_type"].isin(selected_emp_types) &
    df_full["experience_years"].between(*selected_exp)
].copy()

st.sidebar.markdown(f"**{len(df):,} jobs** match current filters")

# ===========================================================================
# SECTION 6 – PAGE HEADER
# ===========================================================================

st.title("India Job Market & Skill Demand Analytics Dashboard")
st.markdown(
    "Explore Indian IT job-posting data to discover in-demand skills, salary ranges (INR), "
    "experience requirements, and hiring trends across roles and cities."
)
st.markdown("---")

# ===========================================================================
# SECTION 7 – KPI CARDS
# ===========================================================================

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric("Total Jobs", f"{len(df):,}")
with kpi2:
    avg_min = df["salary_min"].mean()
    st.metric("Avg Min Salary (INR)", fmt_inr(avg_min))
with kpi3:
    avg_max = df["salary_max"].mean()
    st.metric("Avg Max Salary (INR)", fmt_inr(avg_max))
with kpi4:
    avg_exp = df["experience_years"].mean()
    st.metric("Avg Experience", f"{avg_exp:.1f} yrs" if not pd.isna(avg_exp) else "N/A")

st.markdown("---")

# ===========================================================================
# GUARD – stop rendering charts when no rows match the current filters
# ===========================================================================

if df.empty:
    st.warning("No records match the selected filters. Please adjust the sidebar.")
    st.stop()

# ===========================================================================
# SECTION 8 – CHARTS
# ===========================================================================

# --- Row 1: Jobs by Role  |  Jobs by Location ---------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Jobs by Job Role")
    role_counts = df["job_title"].value_counts().reset_index()
    role_counts.columns = ["Job Role", "Count"]
    fig_role = px.bar(
        role_counts,
        x="Count", y="Job Role",
        orientation="h",
        color="Count",
        color_continuous_scale="Blues",
        labels={"Count": "Number of Jobs"},
        title="Distribution of Jobs by Role",
    )
    fig_role.update_layout(coloraxis_showscale=False, margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig_role, use_container_width=True)

with col2:
    st.subheader("Jobs by Location")
    loc_counts = df["location"].value_counts().reset_index()
    loc_counts.columns = ["Location", "Count"]
    fig_loc = px.bar(
        loc_counts,
        x="Count", y="Location",
        orientation="h",
        color="Count",
        color_continuous_scale="Teal",
        labels={"Count": "Number of Jobs"},
        title="Distribution of Jobs by Location",
    )
    fig_loc.update_layout(coloraxis_showscale=False, margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig_loc, use_container_width=True)

# --- Row 2: Most Demanded Skills  |  Avg Salary by Role ----------------
col3, col4 = st.columns(2)

with col3:
    st.subheader("Most Demanded Skills")
    # Sum each binary skill column to count jobs requiring that skill
    skill_counts = df[SKILL_COLS].sum().sort_values(ascending=False).reset_index()
    skill_counts.columns = ["Skill", "Jobs Requiring Skill"]
    skill_counts["Skill"] = skill_counts["Skill"].str.replace("_", " ").str.title()
    fig_skills = px.bar(
        skill_counts,
        x="Jobs Requiring Skill", y="Skill",
        orientation="h",
        color="Jobs Requiring Skill",
        color_continuous_scale="Oranges",
        title="Number of Jobs Requiring Each Skill",
    )
    fig_skills.update_layout(coloraxis_showscale=False, margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig_skills, use_container_width=True)

with col4:
    st.subheader("Average Salary by Job Role (INR Lakhs)")
    salary_by_role = (
        df.groupby("job_title")
        .agg(Avg_Min=("salary_min", "mean"), Avg_Max=("salary_max", "mean"))
        .reset_index()
        .rename(columns={"job_title": "Job Role"})
        .sort_values("Avg_Min", ascending=False)
    )
    # Convert to Lakhs for a readable axis
    salary_by_role["Avg_Min_L"] = salary_by_role["Avg_Min"] / 100_000
    salary_by_role["Avg_Max_L"] = salary_by_role["Avg_Max"] / 100_000

    salary_long = salary_by_role.melt(
        id_vars="Job Role",
        value_vars=["Avg_Min_L", "Avg_Max_L"],
        var_name="Salary Type",
        value_name="Salary (INR Lakhs)",
    )
    salary_long["Salary Type"] = salary_long["Salary Type"].map(
        {"Avg_Min_L": "Avg Min Salary", "Avg_Max_L": "Avg Max Salary"}
    )
    fig_salary = px.bar(
        salary_long,
        x="Salary (INR Lakhs)", y="Job Role",
        color="Salary Type",
        orientation="h",
        barmode="group",
        color_discrete_map={
            "Avg Min Salary": "#4C78A8",
            "Avg Max Salary": "#F58518",
        },
        title="Average Min & Max Salary by Role (in Lakhs \u20b9)",
    )
    fig_salary.update_layout(margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig_salary, use_container_width=True)

# --- Row 3: Experience Distribution  |  Jobs by Employment Type --------
col5, col6 = st.columns(2)

with col5:
    st.subheader("Experience Distribution")
    fig_exp = px.histogram(
        df,
        x="experience_years",
        nbins=10,
        color_discrete_sequence=["#636EFA"],
        labels={"experience_years": "Years of Experience", "count": "Number of Jobs"},
        title="Distribution of Required Experience",
    )
    fig_exp.update_layout(bargap=0.1, margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig_exp, use_container_width=True)

with col6:
    st.subheader("Jobs by Employment Type")
    emp_counts = df["employment_type"].value_counts().reset_index()
    emp_counts.columns = ["Employment Type", "Count"]
    fig_emp = px.pie(
        emp_counts,
        names="Employment Type",
        values="Count",
        color_discrete_sequence=px.colors.qualitative.Set2,
        title="Share of Jobs by Employment Type",
        hole=0.35,
    )
    fig_emp.update_layout(margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig_emp, use_container_width=True)

# ===========================================================================
# SECTION 9 – DATA TABLE (searchable)
# ===========================================================================

st.markdown("---")
st.subheader("Job Postings Data Table")

search_query = st.text_input(
    "Search by job title, company, or location",
    placeholder="e.g. Data Scientist, Infosys, Bengaluru ...",
)

df_display = df.copy()
if search_query.strip():
    q = search_query.strip().lower()
    mask = (
        df_display["job_title"].str.lower().str.contains(q, na=False) |
        df_display["company"].str.lower().str.contains(q, na=False) |
        df_display["location"].str.lower().str.contains(q, na=False)
    )
    df_display = df_display[mask]

# Format salary columns as INR Lakhs strings for display
df_display = df_display.copy()
df_display["salary_min_fmt"] = df_display["salary_min"].apply(fmt_inr)
df_display["salary_max_fmt"] = df_display["salary_max"].apply(fmt_inr)

TABLE_COLS = [
    "job_id", "job_title", "company", "location",
    "experience_years", "salary_min_fmt", "salary_max_fmt", "employment_type",
]
COL_LABELS = {
    "job_id":           "Job ID",
    "job_title":        "Job Title",
    "company":          "Company",
    "location":         "Location",
    "experience_years": "Exp (Yrs)",
    "salary_min_fmt":   "Min Salary",
    "salary_max_fmt":   "Max Salary",
    "employment_type":  "Employment Type",
}

st.dataframe(
    df_display[TABLE_COLS].rename(columns=COL_LABELS).reset_index(drop=True),
    use_container_width=True,
    height=350,
)
st.caption(f"Showing {len(df_display):,} of {len(df):,} filtered records")

# ===========================================================================
# SECTION 10 – BUSINESS INSIGHT CALCULATIONS & KEY INSIGHTS PANEL
# ===========================================================================

st.markdown("---")
st.subheader("Key Insights")

most_demanded_skill     = df[SKILL_COLS].sum().idxmax().replace("_", " ").title()
most_common_role        = df["job_title"].value_counts().idxmax()
top_location            = df["location"].value_counts().idxmax()
highest_avg_salary_role = df.groupby("job_title")["salary_avg"].mean().idxmax()
overall_avg_exp         = df["experience_years"].mean()

ins1, ins2, ins3 = st.columns(3)
ins4, ins5, _    = st.columns(3)

with ins1:
    st.info(f"**Most Demanded Skill**\n\n{most_demanded_skill}")
with ins2:
    st.info(f"**Most Common Job Role**\n\n{most_common_role}")
with ins3:
    st.info(f"**Top Hiring Location**\n\n{top_location}")
with ins4:
    st.info(f"**Highest Avg Salary Role**\n\n{highest_avg_salary_role}")
with ins5:
    st.info(f"**Avg Experience Required**\n\n{overall_avg_exp:.1f} years")

# ===========================================================================
# FOOTER
# ===========================================================================

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:grey; font-size:13px;'>"
    "India Job Market &amp; Skill Demand Analytics Dashboard &mdash; College Project"
    "</p>",
    unsafe_allow_html=True,
)
