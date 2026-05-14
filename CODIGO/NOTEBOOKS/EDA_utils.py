
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
plt.style.use("seaborn-v0_8")
sns.set_palette("tab10")
from datetime import datetime

import os
os.getcwd()

# FORMULA
def dataframe_to_png(df, filename): #introducir filename con .png
    # Estilo profesional
    plt.style.use("seaborn-v0_8-whitegrid")

    # Tamaño dinámico según número de filas
    fig, ax = plt.subplots(figsize=(12, 1 + len(df) * 0.5))
    ax.axis("off")

    # Crear tabla
    table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        cellLoc="center",
        loc="center",
        colColours=["#1f77b4"] * len(df.columns)  # encabezado azul
    )

    # Ajustes de estilo
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 1.3)

    # Colorear filas alternas
    for i in range(len(df)):
        color = "#f7f7f7" if i % 2 == 0 else "white"
        for j in range(len(df.columns)):
            table[(i + 1, j)].set_facecolor(color)

    # Bordes finos
    for key, cell in table.get_celld().items():
        cell.set_edgecolor("#4d4d4d")
        cell.set_linewidth(0.4)

    # Guardar imagen
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()

    return filename