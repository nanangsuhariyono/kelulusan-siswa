import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Kelulusan Siswa", layout="centered")

st.title("📚 Data Kelulusan Siswa")

uploaded_file = st.file_uploader("📤 Upload file CSV nilai siswa", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    df['Rata-rata'] = df.iloc[:, 2:].mean(axis=1)
    df['Status'] = df['Rata-rata'].apply(lambda x: 'LULUS' if x >= 70 else 'TIDAK LULUS')

    search = st.text_input("🔍 Cari siswa (Nama atau NIS)")

    if search:
        hasil = df[df['Nama'].str.contains(search, case=False) | df['NIS'].astype(str).str.contains(search)]
    else:
        hasil = df

    st.write("### 📊 Hasil Kelulusan:")
    st.dataframe(hasil)

    csv = hasil.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Data", data=csv, file_name="hasil_kelulusan.csv", mime='text/csv')

else:
    st.info("Silakan upload file CSV dengan format yang sesuai.")
