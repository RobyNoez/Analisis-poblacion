from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raiz = Path(__file__).parent.parent

archivo = raiz / "datos" / "población_extranjera_españa.xlsx"

df = pd.read_excel(archivo, header=None)


matriz = np.array([
    df.iloc[7, 1:26],
    df.iloc[9, 1:26]
], dtype=int)

print(matriz)

print("\nDimensiones: ", matriz.shape)

anios = matriz[0]
poblacion = matriz[1]

print("\n==========  ANALISIS POBLACIÓN EXTRANJERA ESPAÑA ==========")


plt.figure(figsize=(10, 5))
plt.plot(anios, poblacion, marker="o", linestyle='-')
plt.title("Población extranjera España")
plt.xlabel("Años")
plt.ylabel("Población")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
