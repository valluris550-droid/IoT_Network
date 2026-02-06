import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# ------------------ Streamlit Page Config ------------------
st.set_page_config(
    page_title="IoT Network Data Analysis",
    layout="wide"
)

# ------------------ Load Dataset ------------------
# IMPORTANT:
# Put IOT_NETWORK_DATA.csv in the SAME folder as app.py
DATA_PATH = "IOT_NETWORK_DATA.csv"

df = pd.read_csv(DATA_PATH)

# ------------------ Plot Styling ------------------
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# ------------------ App Title ------------------
st.title("IoT Network Data Analysis")

# ------------------ Question 1 ------------------
st.subheader("1. Distribution of Device Types")
fig, ax = plt.subplots()
sns.countplot(data=df, x='device_type', palette='Set2', ax=ax)
st.pyplot(fig)

# ------------------ Question 2 ------------------
st.subheader("2. Protocol Usage Share")
fig, ax = plt.subplots()
df['protocol_type'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=ax
)
ax.set_ylabel("")
st.pyplot(fig)

# ------------------ Question 3 ------------------
st.subheader("3. Average Energy Usage by Device Type")
fig, ax = plt.subplots()
sns.barplot(data=df, x='device_type', y='energy_usage', ci=None, ax=ax)
st.pyplot(fig)

# ------------------ Question 4 ------------------
st.subheader("4. Latency vs Jitter")
fig, ax = plt.subplots()
sns.scatterplot(
    data=df.sample(1000),
    x='latency',
    y='jitter',
    hue='device_type',
    alpha=0.6,
    ax=ax
)
st.pyplot(fig)

# ------------------ Question 5 ------------------
st.subheader("5. Packet Loss Rate Distribution")
fig, ax = plt.subplots()
sns.histplot(
    df['packet_loss_rate'],
    bins=30,
    kde=True,
    color='red',
    ax=ax
)
st.pyplot(fig)
