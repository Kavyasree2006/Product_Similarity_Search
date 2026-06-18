
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dataset Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Fashion Dataset Analytics")

# ---------------- Load Dataset ----------------

df = pd.read_csv(
    "styles.csv",
    on_bad_lines="skip"
)

# ---------------- Metrics ----------------

st.subheader("Dataset Overview")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Products",
    len(df)
)

col2.metric(
    "Categories",
    df["masterCategory"].nunique()
)

col3.metric(
    "Article Types",
    df["articleType"].nunique()
)

col4.metric(
    "Colors",
    df["baseColour"].nunique()
)

st.divider()

# ================= CATEGORY DISTRIBUTION =================

st.subheader("📂 Category Distribution")

fig1 = px.histogram(
    df,
    x="masterCategory",
    color="masterCategory",
    title="Products by Category"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.divider()

# ================= GENDER DISTRIBUTION =================

st.subheader("👨 👩 Gender Distribution")

gender_counts = df["gender"].value_counts().reset_index()
gender_counts.columns = ["Gender","Count"]

fig2 = px.pie(
    gender_counts,
    names="Gender",
    values="Count",
    hole=0.4,
    title="Gender Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# ================= SEASON DISTRIBUTION =================

st.subheader("🌤 Season Distribution")

season_counts = df["season"].value_counts().reset_index()
season_counts.columns = ["Season","Count"]

fig3 = px.bar(
    season_counts,
    x="Season",
    y="Count",
    color="Season",
    text_auto=True,
    title="Products by Season"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.divider()

# ================= TOP COLORS =================

st.subheader("🎨 Top 10 Colors")

color_counts = (
    df["baseColour"]
    .value_counts()
    .head(10)
    .reset_index()
)

color_counts.columns = ["Color","Count"]

fig4 = px.bar(
    color_counts,
    x="Color",
    y="Count",
    color="Color",
    text_auto=True,
    title="Most Common Colors"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.divider()

# ================= ARTICLE TYPES =================

st.subheader("👕 Top 15 Article Types")

article_counts = (
    df["articleType"]
    .value_counts()
    .head(15)
    .reset_index()
)

article_counts.columns = ["Article Type","Count"]

fig5 = px.bar(
    article_counts,
    x="Article Type",
    y="Count",
    color="Article Type",
    text_auto=True,
    title="Popular Article Types"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.divider()

# ================= RAW DATA =================

with st.expander("View Dataset Sample"):

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

st.divider()

# ================= SUMMARY =================

st.subheader("📌 Key Insights")

st.success(
"""
✔ Large-scale fashion dataset

✔ Multiple categories and article types

✔ Diverse color distribution

✔ Suitable for similarity search and recommendation systems

✔ Supports deep learning feature extraction
"""
)

st.divider()

st.caption(
"Built with ❤️ using Streamlit + Plotly"
)
