# app.py

import pandas as pd
import numpy as np
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords

# Descargar stopwords (solo la primera vez)
nltk.download("stopwords")

# Cargar datos
df = pd.read_csv("santa_isabel.csv")
df.drop(["Atributos", "page"], axis=1, inplace=True)

# Limpieza básica
df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")
df[["normal_price", "low_price", "high_price"]] = df[["normal_price", "low_price", "high_price"]].replace(0, np.nan)

for col in ["normal_price", "low_price", "high_price"]:
    df[col] = df.groupby("categoria2")[col].transform(lambda x: x.fillna(x.median()))

df.fillna(df.median(numeric_only=True), inplace=True)
df.drop_duplicates(inplace=True)

# Preparar vectorizador con stopwords en español
stopwords_es = stopwords.words("spanish")
vectorizador = TfidfVectorizer(stop_words=stopwords_es)
matriz_titulos = vectorizador.fit_transform(df["title"])

# Función recomendador
def recomendar_producto(nombre_producto, n=5):
    idx = df[df["title"].str.contains(nombre_producto, case=False, na=False)].index
    if len(idx) == 0:
        return None
    idx = idx[0]
    similitudes = cosine_similarity(matriz_titulos[idx], matriz_titulos).flatten()
    similares_idx = similitudes.argsort()[::-1][1:n+1]

    recomendados = df.iloc[similares_idx][["title", "brand", "normal_price", "low_price"]].copy()

    # Si el producto no está en oferta, mostrar "-" en low_price
    recomendados["low_price"] = recomendados.apply(
        lambda row: f"${int(row['low_price']):,}" if row["low_price"] < row["normal_price"] else "-", axis=1
    )
    recomendados["normal_price"] = recomendados["normal_price"].apply(lambda x: f"${int(x):,}")

    recomendados.rename(
        columns={
            "title": "Producto",
            "brand": "Marca",
            "normal_price": "Precio Normal",
            "low_price": "Precio con Oferta",
        },
        inplace=True,
    )
    return recomendados

# --- STREAMLIT UI ---

st.title("Recomendador de Productos - Santa Isabel")

# Centrar logo con columnas y st.image usando use_container_width=True
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("logo.png", use_container_width=True)

# Entrada usuario
producto_busqueda = st.text_input("Ingrese el nombre del producto para recomendar:")

if producto_busqueda:
    resultado = recomendar_producto(producto_busqueda)
    if resultado is None:
        st.warning("Producto no encontrado, intente con otro término.")
    else:
        st.subheader(f"Recomendaciones para '{producto_busqueda}':")
        st.dataframe(resultado)

# Opcional: mostrar algunos KPIs o análisis rápido
if st.checkbox("Mostrar KPIs básicos"):
    porc_oferta = df["oferta"].mean() * 100
    descuento_prom = ((df["normal_price"] - df["low_price"]) / df["normal_price"] * 100).mean()
    st.write(f"% de productos en oferta: {porc_oferta:.2f}%")
    st.write(f"Descuento promedio: {descuento_prom:.2f}%")
