import streamlit as st
import pandas as pd
import datetime

# File per salvare i dati
FILE_DATI = "work_hours.csv"

# Carica i dati esistenti
try:
    df = pd.read_csv(FILE_DATI)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Data", "Ore", "Categoria"])

# Titolo della web app
st.title("📅 Registro Ore di Lavoro")

# Selezione della data
data = st.date_input("Seleziona la data", datetime.date.today())

# Input delle ore
ore = st.number_input("Ore lavorate (0.5 = mezz'ora)", min_value=0.0, step=0.5)

# Selezione della categoria
categoria = st.selectbox("Seleziona la categoria", ["Straordinario", "Malattia", "Permessi"])

# Bottone per salvare i dati
if st.button("Salva Registro"):
    nuovo_record = pd.DataFrame([[data, ore, categoria]], columns=["Data", "Ore", "Categoria"])
    df = pd.concat([df, nuovo_record], ignore_index=True)
    df.to_csv(FILE_DATI, index=False)
    st.success(f"Dati salvati: {data} - {ore}h ({categoria})")

# Mostra i dati registrati
st.subheader("📊 Riepilogo Ore Registrate")
st.dataframe(df)

# Mostra il totale per categoria
st.subheader("📈 Totale Ore per Categoria")
if not df.empty:
    totali = df.groupby("Categoria")["Ore"].sum()
    st.write(totali)
else:
    st.write("Nessun dato registrato.")
