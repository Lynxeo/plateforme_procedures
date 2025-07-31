import streamlit as st
import pandas as pd

st.title("🔍 Recherche dans un fichier Excel")

uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel("procedures.xlsx")

    st.write("Aperçu du fichier complet :")
    st.dataframe(df)

    # Choisir la colonne qui contient le code (ex: "Code", "ID", etc.)
    colonne_code = st.selectbox("Choisissez la colonne du code à rechercher :", df.columns.tolist())

    # Entrer un code à rechercher
    code = st.text_input("🔎 Entrez le code à rechercher :")

    if code:
        result = df[df[colonne_code].astype(str) == code]
        if not result.empty:
            st.success("✅ Résultat trouvé :")
            st.dataframe(result)
        else:
            st.warning("❌ Aucun résultat trouvé pour ce code.")
