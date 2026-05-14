# EDA

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
plt.style.use("seaborn-v0_8")
sns.set_palette("tab10")
from datetime import datetime
import dataframe_image as dfi

import os
os.getcwd()

########

from EDA_utils import dataframe_to_png

###################################################
#PASO 1:
###################################################
# Trabajamos el dataset top_500_metadata.csv para realizar una clasificaion
# de los criptoactivos mas relevantes en base a un ranking de parametros financiero

#Cargamos los datos de metadata
df = pd.read_csv("../DATA/top_500_metadata.csv")

# Extraemos de la tabla original las columnas que nos sirven para la resolucion del ejercicio
metadata = df[["symbol","market_cap", "total_volume","ath","current_price","high_24h","low_24h" ]]

#Limpieza basica de los datos que contienen las columnas con las que vamos a trabajar.
#Convertimos columnas las columnas str a columnas numericas
cols_numeric = ["market_cap", "total_volume","ath","current_price","high_24h","low_24h"]
for col in cols_numeric:
    metadata[col] = pd.to_numeric(metadata[col], errors="coerce")

# ------------  
dfi.export(metadata.head(20),"top_500_metadata_20.png",table_conversion='chrome')    
# ------------  

# Eliminar filas con datos faltantes en métricas clave
metadata = metadata.dropna(subset=cols_numeric)

# calculamos las metricas necesarias desde el dataset metadata

#Volatilidad 24H
metadata["volatility_24h"] = (metadata["high_24h"] - metadata["low_24h"]) / metadata["current_price"]

#distancia al ATH
metadata["ath_distance"] = (metadata["ath"] - metadata["current_price"]) / metadata["ath"]

# ------------  
dfi.export(metadata.head(20),"metadata.png",table_conversion='chrome')
# ------------  

#Establecemos un RANKING MULTICRITERIO:
#Este Ranking es equilibrado y alineado con metodologías de análisis financiero.
#Ponderamos los datos selecionados con los siguientes factores.
#Market Cap → 40%
#Total Volumen → 30%
#Volatility_24h → 20%
#ATH_distance → 10%

metadata["ranking"] = (0.40 * metadata["market_cap"] + 0.30 * metadata["total_volume"] + 0.20 * metadata["volatility_24h"] + 0.10 * metadata["ath_distance"])

#seleccionamos los 5 criptoactivos mas IMPORTANES basandonos en el ranking.
top5 = metadata.sort_values("ranking", ascending=False).head(5)
top5_assets = top5["symbol"].tolist()

print("Los 5 criptoactivos seleccionados son:")
print(top5_assets)

top5_assets
top5

# ------------  
dfi.export(top5,"top_5_assets.png",table_conversion='chrome')
# ------------  
  

# Graficas de seleccion de los 5 criptoactivos mas relevantes

# Paleta de colores personalizada (uno por gráfico)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

sns.set_theme(style="whitegrid", font_scale=1.2)

fig, axes = plt.subplots(2, 2, figsize=(14, 9))
axes = axes.ravel()

# --- Gráfico 1: Market Cap ---
sns.barplot(
    data=top5,
    x="symbol",
    y="market_cap",
    ax=axes[0],
    color=colors[0]
)
axes[0].set_title("Market Cap Top 5", fontsize=14, weight="bold")
axes[0].set_xlabel("")
axes[0].set_ylabel("Market Cap")

# --- Gráfico 2: Volumen ---
sns.barplot(
    data=top5,
    x="symbol",
    y="total_volume",
    ax=axes[1],
    color=colors[1]
)
axes[1].set_title("Volumen Total", fontsize=14, weight="bold")
axes[1].set_xlabel("")
axes[1].set_ylabel("Volumen")

# --- Gráfico 3: Volatilidad ---
sns.barplot(
    data=top5,
    x="symbol",
    y="volatility_24h",
    ax=axes[2],
    color=colors[2]
)
axes[2].set_title("Volatilidad 24h Top 5", fontsize=14, weight="bold")
axes[2].set_xlabel("")
axes[2].set_ylabel("Volatilidad (%)")

# --- Gráfico 4: Distancia al ATH ---
sns.barplot(
    data=top5,
    x="symbol",
    y="ath_distance",
    ax=axes[3],
    color=colors[3]
)
axes[3].set_title("Distancia al ATH Top 5", fontsize=14, weight="bold")
axes[3].set_xlabel("")
axes[3].set_ylabel("Distancia (%)")

plt.tight_layout()
plt.savefig("top5_metricsX4.png", dpi=300, bbox_inches="tight")
plt.show()

###################################################
#PASO 2:
###################################################

# preparamos los datos del dataset crypto_ohlc.csv
# para hacer calculo de los ratios financieros relevantes

#2.1 leemos el dataset
ohlc = pd.read_csv("../DATA/crypto_ohlc.csv")

# 2.2 Transformacion de columnas.
cols_numeric = ["open", "high","low","close"]
for col in cols_numeric:
    ohlc[col] = pd.to_numeric(ohlc[col], errors="coerce")

# Eliminar filas con datos faltantes en métricas clave
ohlc = ohlc.dropna(subset=cols_numeric)

# Filtrar solo los 5 activos seleccionados
ohlc_top5 = ohlc[ohlc["symbol"].isin(top5_assets)]
ohlc_top5

#eliminamos las columnas que no nos aportan nada
ohlc_top5 = ohlc_top5.drop(columns=["coin_id"], errors="ignore")

#Transformamos la columna fecha a tipo de caracter date
ohlc_top5['date'] = pd.to_datetime(ohlc_top5['timestamp'], unit='ms')

# ------------  
dfi.export(ohlc_top5.head(20),"ohlc_top5.png",table_conversion='chrome')
# ------------  

# 2.3. Calculo de rentabilidades de 2025 para contrastar las hipotesis
# Filtrar año 2025
ohlc_2025 = ohlc_top5[
    (ohlc_top5["date"] >= "2025-01-01") &
    (ohlc_top5["date"] <= "2025-12-31")
]

# Rentabilidad anual por activo
returns_2025 = (
    ohlc_2025.groupby("symbol")
    .apply(lambda df: (df["close"].iloc[-1] - df["close"].iloc[0]) / df["close"].iloc[0])
    .reset_index(name="annual_return")
)

returns_2025
# ------------ 
dfi.export(returns_2025,"rentabilidad_2025.png",table_conversion='chrome')
# ------------ 

# Ordenar por fecha y criptoactivo
ohlc_top5 = ohlc_top5.sort_values(["symbol", "date"], ascending=[True, True])
ohlc_top5

# RATIO: Rentabilidad diaria
ohlc_top5["daily_return"] = ohlc_top5.groupby("symbol")["close"].pct_change()
# Eliminar filas con datos faltantes en daily_return
ohlc_top5 = ohlc_top5.dropna(subset=['daily_return'])

#**excluyendo USDT por datos corruptos.**
ohlc_top5_R = ohlc_top5[ohlc_top5["symbol"] != "usdt"]
ohlc_top5_R["symbol"].unique()

# GRAFICO RETORNOS DIARIOS
import matplotlib.pyplot as plt
import seaborn as sns

# Estilo profesional
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 7))

# Paleta elegante por símbolo
palette = sns.color_palette("Set2", n_colors=ohlc_top5_R["symbol"].nunique())

sns.boxplot(
    data=ohlc_top5_R,
    x="symbol",
    y="daily_return",
    palette=palette,
    linewidth=1.5,
    fliersize=3,
    boxprops=dict(alpha=0.8),
)

# Título y ejes
plt.title("Distribución de Retornos Diarios (2025)", fontsize=16, weight="bold")
plt.xlabel("Criptomoneda", fontsize=13)
plt.ylabel("Retorno Diario", fontsize=13)

# Líneas horizontales suaves
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("Retorno_Diario_BOXPLOT.png", dpi=300, bbox_inches="tight")
plt.show()

# RATIO: Volatilidad diaria
# sin USDT
volatility = (
    ohlc_top5_R.groupby("symbol")["daily_return"]
    .std()
    .reset_index(name="daily_volatility")
)

volatility
# ------------ 
dfi.export(volatility,"daily_volatility.png",table_conversion='chrome')
# ------------ 

# grafico CIRCULAR. Volatilidad Diaria
# Filtrar USDT
df_vol_no_usdt = volatility[volatility["symbol"] != "usdt"]

# Colores profesionales (azules suaves)
colors = plt.cm.Greens_r(np.linspace(0.3, 0.9, len(df_vol_no_usdt)))

# Crear figura
fig, ax = plt.subplots(figsize=(8, 8))

# Pie chart
wedges, texts, autotexts = ax.pie(
    df_vol_no_usdt["daily_volatility"],
    labels=df_vol_no_usdt["symbol"].str.upper(),
    autopct="%1.1f%%",
    startangle=90,
    colors=colors,
    pctdistance=0.8,
    textprops={"fontsize": 12, "color": "#333"}
)

# Donut: círculo blanco interior
centre_circle = plt.Circle((0, 0), 0.60, fc="white")
fig.gca().add_artist(centre_circle)

# Título elegante
plt.title(
    "Distribución de Volatilidad Diaria (excluyendo USDT)",
    fontsize=16,
    fontweight="bold",
    pad=20
)

# Ajustes finales
plt.tight_layout()
plt.savefig("Volatilidad_Diaria.png", dpi=300, bbox_inches="tight")
plt.show()

#4. Rentabilidad acumulada en 2025
ohlc_2025 = ohlc_top5[(ohlc_top5["date"] >= "2025-01-01") & (ohlc_top5["date"] <= "2025-12-31")]

ohlc_2025["cum_return"] = (1 + ohlc_top5["daily_return"]).groupby(ohlc_top5["symbol"]).cumprod()


# Gráfico de rentabilidad acumulada
#**Excluimos USDT por datos corruptos.**

#Sacamos la rentabilidad acumulada de cada activo en una grafica independiente
# Colores fijos por símbolo
color_map = {
    "btc": "#1f77b4",   # azul
    "eth": "#ff7f0e",   # naranja
    "xrp": "#2ca02c",   # verde
    "bnb": "#d62728"    # rojo
}

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.ravel()

symbols = ["btc", "eth", "xrp", "bnb"]

for i, sym in enumerate(symbols):
    ax = axes[i]
    df = ohlc_2025[ohlc_2025["symbol"] == sym]

    ax.plot(
        df["date"],
        df["cum_return"],
        label=sym.upper(),
        linewidth=2.2,
        color=color_map[sym]
    )

    ax.set_title(f"{sym.upper()} — Rentabilidad Acumulada 2025", fontsize=13, weight="bold")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Rentabilidad acumulada")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend()

plt.tight_layout()
plt.savefig("Retabilidad_AcumualdaX4.png", dpi=300, bbox_inches="tight")
plt.show()

#5. Máximo Drawdown
#sin USDT
def max_drawdown(series):
    cumulative = (1 + series).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()

drawdowns = (
    ohlc_top5_R.groupby("symbol")["daily_return"]
    .apply(max_drawdown)
    .reset_index(name="max_drawdown")
)

drawdowns

# ------------ 
dfi.export(drawdowns,"max_drawdon.png",table_conversion='chrome')
# ------------ 

# grafico de BARRAS
# Estilo profesional
sns.set_theme(style="whitegrid", font_scale=1.2)

# Colores fijos por símbolo
color_map = {
    "btc": "#1f77b4",   # azul
    "eth": "#ff7f0e",   # naranja
    "xrp": "#2ca02c",   # verde
    "bnb": "#d62728"    # rojo
}

# Ordenar de mayor a menor drawdown (opcional pero profesional)
df_plot = df_drawdown.sort_values("max_drawdown", ascending=True)

# Crear lista de colores en el mismo orden que el DataFrame
colors = [color_map[s] for s in df_plot["symbol"]]

plt.figure(figsize=(10, 5))

sns.barplot(
    data=df_plot,
    x="max_drawdown",
    y="symbol",
    palette=colors,
    linewidth=1.3,
    edgecolor="black"
)

plt.title("Máximo Drawdown por Activo", fontsize=16, weight="bold")
plt.xlabel("Max Drawdown (%)")
plt.ylabel("Activo")

plt.grid(axis="x", linestyle="--", alpha=0.35)
plt.tight_layout()
plt.savefig("Maximo_Dradown.png", dpi=300, bbox_inches="tight")
plt.show()

#6. Sharpe Ratio (riesgo–retorno)
#excluyendo USDT por datos corruptos.
sharpe = (
    ohlc_top5_R.groupby("symbol")["daily_return"]
    .apply(lambda x: x.mean() / x.std())
    .reset_index(name="sharpe_ratio")
)

sharpe

#--------
dfi.export(sharpe,"sharpe_ratio.png",table_conversion='chrome')
#--------

#7. Tabla resumen para contrastar hipótesis
#Excluimos USDT por datos corruptos).
summary = (
    returns_2025
    .merge(volatility, on="symbol")
    .merge(drawdowns, on="symbol")
    .merge(sharpe, on="symbol")
)

summary
#------
dfi.export(summary,"summary.png",table_conversion='chrome')
#------

# exportamos grafico HEATMAP
# Estilo profesional
sns.set_theme(style="whitegrid", font_scale=1.2)

plt.figure(figsize=(10, 3))

# Tabla como heatmap suave
sns.heatmap(
    summary.set_index("symbol"),
    annot=True,
    fmt=".4f",
    cmap="Greens",
    linewidths=0.5,
    cbar=False
)

plt.title("Resumen de Métricas Financieras 2025", fontsize=16, fontweight="bold", pad=20)
plt.xlabel("")
plt.ylabel("")

plt.tight_layout()
plt.show()

#🔗 8. HEATMAP.Correlación entre los activos.
pivot_returns = ohlc_2025.pivot_table(index="date", columns="symbol", values="daily_return")

plt.figure(figsize=(8,6))
sns.heatmap(pivot_returns.corr(), annot=True, cmap="Greens", vmin=-1,vmax=1)
plt.title("Correlación entre Retornos Diarios (2025)")
plt.tight_layout()
plt.savefig("Correlacion_activos_HEATMAP_verde.png", dpi=300, bbox_inches="tight")
plt.show()

# TABLA SUMARY



# --- Tu tabla ---
summary = (
    returns_2025
    .merge(volatility, on="symbol")
    .merge(drawdowns, on="symbol")
    .merge(sharpe, on="symbol")
)

# Exportar a PNG

# --- Función para convertir un DataFrame en imagen ---
dataframe_to_png(summary, filename="sumary_table.png")
# ------------    
# por libreria
dfi.export(summary,"sumary_table_2.png",table_conversion='chrome')  
# ------------   


# SACAMOS LAS GRAFICAS RESUMEN DE METRICAS

# Estilo profesional
sns.set_theme(style="whitegrid", font_scale=1.2)

# Colores corporativos por símbolo
color_map = {
    "btc": "#1f77b4",   # azul
    "eth": "#ff7f0e",   # naranja
    "xrp": "#2ca02c",   # verde
    "bnb": "#d62728"    # rojo
}

# Crear lista de colores en el mismo orden que summary
colors = [color_map[s] for s in summary["symbol"]]

fig, axes = plt.subplots(2, 2, figsize=(14, 9))
axes = axes.ravel()

# --- Rentabilidad anual ---
sns.barplot(
    data=summary,
    x="symbol",
    y="annual_return",
    ax=axes[0],
    palette=colors,
    edgecolor="black",
    linewidth=1.2
)
axes[0].set_title("Rentabilidad Anual 2025", fontsize=15, weight="bold")
axes[0].set_xlabel("")
axes[0].set_ylabel("Rentabilidad (%)")
axes[0].grid(axis="y", linestyle="--", alpha=0.35)
# --- Volatilidad diaria ---
sns.barplot(
    data=summary,
    x="symbol",
    y="daily_volatility",
    ax=axes[1],
    palette=colors,
    edgecolor="black",
    linewidth=1.2
)
axes[1].set_title("Volatilidad Diaria 2025", fontsize=15, weight="bold")
axes[1].set_xlabel("")
axes[1].set_ylabel("Volatilidad (%)")
axes[1].grid(axis="y", linestyle="--", alpha=0.35)

# --- Máximo drawdown ---
sns.barplot(
    data=summary,
    x="symbol",
    y="max_drawdown",
    ax=axes[2],
    palette=colors,
    edgecolor="black",
    linewidth=1.2
)
axes[2].set_title("Máximo Drawdown 2025", fontsize=15, weight="bold")
axes[2].set_xlabel("")
axes[2].set_ylabel("Drawdown (%)")
axes[2].grid(axis="y", linestyle="--", alpha=0.35)

# --- Sharpe Ratio ---
sns.barplot(
    data=summary,
    x="symbol",
    y="sharpe_ratio",
    ax=axes[3],
    palette=colors,
    edgecolor="black",
    linewidth=1.2
)
axes[3].set_title("Sharpe Ratio 2025", fontsize=15, weight="bold")
axes[3].set_xlabel("")
axes[3].set_ylabel("Sharpe Ratio")
axes[3].grid(axis="y", linestyle="--", alpha=0.35)

plt.tight_layout()
plt.savefig("Resumen_Metricas.png", dpi=300, bbox_inches="tight")
plt.show()