import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
import time

st.set_page_config(layout="wide")

st.title("🔐 Blockchain Smart Access System")

# -----------------------
# SAHTE VERİ OLUŞTURMA
# -----------------------
def generate_data(n=100):
    data = []
    for _ in range(n):
        data.append({
            "user": random.choice(["Resident", "Guest", "Courier"]),
            "status": random.choice(["Approved", "Denied"]),
            "time": random.randint(1, 24),
            "risk": random.randint(1, 100)
        })
    return pd.DataFrame(data)

df = generate_data(200)

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.header("🔎 Filters")

user_type = st.sidebar.selectbox(
    "User Type",
    df["user"].unique()
)

filtered_df = df[df["user"] == user_type]

# -----------------------
# TABLO
# -----------------------
st.subheader("📋 Access Logs")
st.dataframe(filtered_df)

# -----------------------
# GRAFİK - RİSK DAĞILIMI
# -----------------------
st.subheader("📊 Risk Distribution")

fig, ax = plt.subplots()
ax.hist(filtered_df["risk"], bins=15)
st.pyplot(fig)

# -----------------------
# GİRİŞ SİMÜLASYONU
# -----------------------
st.subheader("🚪 Access Simulation")

qr_validity = st.slider("QR Validity (seconds)", 5, 60, 20)
attempt_time = st.slider("Scan Time (seconds)", 0, 60, 10)

def validate_access(qr_time, attempt):
    if attempt <= qr_time:
        return "✅ Access Granted", random.randint(1, 30)
    else:
        return "❌ Access Denied", random.randint(70, 100)

result, risk_score = validate_access(qr_validity, attempt_time)

st.metric("Access Result", result)
st.metric("Risk Score", risk_score)

# -----------------------
# ZAMAN ANALİZİ
# -----------------------
st.subheader("⏱️ Entry Trend")

fig2, ax2 = plt.subplots()
ax2.plot(filtered_df["time"].values)
ax2.set_title("Entry Activity Over Time")
st.pyplot(fig2)

# -----------------------
# BLOCKCHAIN SİMÜLASYONU
# -----------------------
st.subheader("⛓️ Blockchain Log")

def fake_hash():
    return hex(random.getrandbits(128))

if st.button("Generate Block"):
    st.write("New Block Added:")
    st.code(fake_hash())
