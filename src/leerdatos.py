from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Obtenemos la ruta del fichero Excel que utilizamos
raiz = Path(__file__).parent.parent

archivo = raiz / "datos" / "población_extranjera_españa.xlsx"

# Leemos el fichero Excel sin los encabezados
df = pd.read_excel(archivo, header=None)


# Confeccionamos la matriz de años y población extranjera
matriz = np.array([
    df.iloc[7, 1:26],
    df.iloc[9, 1:26]
], dtype=int)

# Mostramos el contenido y las dimensiones de la matriz generada
print(matriz)

print("\nDimensiones: ", matriz.shape)

# Separamos años y datos de población
anios = matriz[0]
poblacion = matriz[1]

print("\n==========  ANALISIS DE LA POBLACIÓN EXTRANJERA ESPAÑA ==========")


# Generamos el gráfico conforme a los datos
plt.figure(figsize=(10, 5))
plt.plot(anios, poblacion, marker="o", linestyle='-')

plt.title("Evolución de la población extranjera en España")
plt.xlabel("Año")
plt.ylabel("Número de personas")

# Mostramos los años y giramos las etiquetas
plt.xticks(anios, rotation=45)

plt.grid(True)
plt.tight_layout()
plt.show()
