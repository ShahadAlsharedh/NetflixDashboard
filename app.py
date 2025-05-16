# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from scipy.stats import zscore

# 1. Page Config
st.set_page_config(page_title="Netflix Dashboard", layout="wide")

# 2. Load data
@st.cache_data
def load_data():
    return pd.read_csv("/Users/shahadadel/Desktop/Grad Project/PersonalProject/CleanData.csv")  # or use the cleaned dataframe saved to CSV

df = load_data()

# 3. Title
st.title("🎬 Netflix Movies & TV Shows Dashboard")

# 4. Sidebar filters
st.sidebar.header("Filter Content")
content_type = st.sidebar.multiselect("Select Type", options=df["type"].unique(), default=df["type"].unique())
genre = st.sidebar.multiselect("Select Genre", options=df["main_genre"].dropna().unique(), default=df["main_genre"].dropna().unique())
year_range = st.sidebar.slider("Release Year", int(df["releaseyear"].min()), int(df["releaseyear"].max()), (2010, 2023))

# 5. Filtered data
filtered_df = df[
    (df["type"].isin(content_type)) &
    (df["main_genre"].isin(genre)) &
    (df["releaseyear"].between(year_range[0], year_range[1]))
]

st.markdown(f"Showing **{len(filtered_df)}** titles")

# 6. Show EDA charts
st.subheader("📊 IMDb Rating Distribution")
fig1 = px.histogram(filtered_df[filtered_df['imdbaveragerating'] > 0], x="imdbaveragerating", nbins=20, title="Rating Distribution")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("🌍 Content by Release Year")
fig2 = px.histogram(filtered_df, x="releaseyear", color="type", title="Titles Over Years")
st.plotly_chart(fig2, use_container_width=True)


st.title("Thank You")
st.write("Made By Shahad Adel")
