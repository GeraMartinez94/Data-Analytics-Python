# analisis_datos.py

import pandas as pd
import numpy as np

# Paso 4: Cargar Datos
datos = pd.read_csv('datos.csv')

# Paso 5: Visualizar los Datos
print("Datos Originales:")
print(datos)

# Paso 6: Realizar Análisis con NumPy y Pandas
media_edad = np.mean(datos['Edad'])
altura_promedio = np.mean(datos['Altura'])

# Paso 7: Mostrar Resultados
print("\nAnálisis:")
print(f"Edad Promedio: {media_edad}")
print(f"Altura Promedio: {altura_promedio}")

# Paso 8: Guardar Resultados
resultados = pd.DataFrame({'Edad Promedio': [media_edad], 'Altura Promedio': [altura_promedio]})
resultados.to_csv('resultados.csv', index=False)

print("\nResultados Guardados en resultados.csv")
