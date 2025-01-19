import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer el archivo CSV
file_path = 'resources/processed_data/testing_output.csv'  # Cambia esto si el archivo tiene otro nombre

# Cargar el archivo CSV en un DataFrame
data = pd.read_csv(file_path)

# Reemplazar valores 'NULL' con NaN y convertir las columnas necesarias a float
data = data.replace('NULL', np.nan)
data['subject'] = pd.to_numeric(data['subject'], errors='coerce')
data['body'] = pd.to_numeric(data['body'], errors='coerce')
data['label'] = pd.to_numeric(data['label'], errors='coerce')

# Valores esperados
expected_values = {0: 0, 1: 4}

# Calcular las diferencias absolutas entre los valores y los esperados
data['subject_error'] = data.apply(lambda row: abs(row['subject'] - expected_values[row['label']]) if not pd.isna(row['subject']) else np.nan, axis=1)
data['body_error'] = data.apply(lambda row: abs(row['body'] - expected_values[row['label']]) if not pd.isna(row['body']) else np.nan, axis=1)

# Calcular precisión como el inverso del error medio (menor error = mayor precisión)
subject_precision = 1 - data['subject_error'].mean() / 4
body_precision = 1 - data['body_error'].mean() / 4

print(f"Precisión del campo 'subject': {subject_precision:.2f}")
print(f"Precisión del campo 'body': {body_precision:.2f}")

# Crear gráficos para visualizar los errores
plt.figure(figsize=(10, 6))

# Gráfico de errores para 'subject'
plt.subplot(2, 1, 1)
plt.scatter(data.index, data['subject_error'], label='Error en subject', color='blue', alpha=0.7)
plt.axhline(y=0, color='green', linestyle='--', label='Error mínimo')
plt.axhline(y=4, color='red', linestyle='--', label='Error máximo')
plt.title("Errores en el campo 'subject'")
plt.ylabel("Error absoluto")
plt.legend()

# Gráfico de errores para 'body'
plt.subplot(2, 1, 2)
plt.scatter(data.index, data['body_error'], label='Error en body', color='orange', alpha=0.7)
plt.axhline(y=0, color='green', linestyle='--', label='Error mínimo')
plt.axhline(y=4, color='red', linestyle='--', label='Error máximo')
plt.title("Errores en el campo 'body'")
plt.ylabel("Error absoluto")
plt.xlabel("Índice del mensaje")
plt.legend()

plt.tight_layout()
plt.show()
