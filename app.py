import streamlit as st

beranda = st.Page("pages/beranda.py", title="Beranda")
visualisasi = st.Page("pages/visualisasi.py", title="Visualisasi")
prediksi = st.Page("pages/prediksi.py", title="Prediksi")

pg = st.navigation([beranda, visualisasi, prediksi])
st.set_page_config(page_title="Analisis Sentimen")
pg.run()


