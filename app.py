import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Restaurant Trend Analyzer", layout="wide")

st.title("🍽️ Restaurant Trend Analyzer")
st.markdown("Upload the Zomato dataset to begin analysis.")

# File uploader
uploaded_file = st.file_uploader("Upload Zomato CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Raw Data Preview")
    st.dataframe(df.head())

    st.subheader("🏙️ Top 10 Restaurant Locations")
    top_locations = df['location'].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(y=top_locations.index, x=top_locations.values, ax=ax)
    ax.set_xlabel("Number of Restaurants")
    ax.set_ylabel("Location")
    st.pyplot(fig)

    st.subheader("💰 Price Range Distribution")
    fig2, ax2 = plt.subplots()
    sns.countplot(data=df, x='price_range', ax=ax2)
    ax2.set_title("Distribution of Price Ranges")
    st.pyplot(fig2)

else:
    st.warning("👆 Please upload a CSV file to continu
