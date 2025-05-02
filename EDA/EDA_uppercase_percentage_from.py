import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# Leer el dataset ya preparado
dataset_path = 'resources/processed_data/dataset.csv'
df = pd.read_csv(dataset_path)

# Asegurar tipos y columnas necesarias
required_columns = ['num_chars_from', 'special_chars_from', 'uppercase_percentage_from', 'date', 'subject', 'body', 'label']
if not all(col in df.columns for col in required_columns):
    raise ValueError("El CSV no contiene todas las columnas necesarias.")

# Rango de porcentajes (0%-2%, 2%-4%, ..., 18%-20%)
ranges = [(i, i + 2) for i in range(0, 20, 2)]  # Hasta 20%
ranges.append((20, float('inf')))  # +20%

# Función para asignar un porcentaje a un tramo
def get_range(percentage):
    for lower, upper in ranges:
        if lower <= percentage < upper:
            return f"{lower}-{int(upper)}%" if upper != float('inf') else "+20%"
    return "+20%"


# Crear contadores para phishing y no phishing
phishing_counts = Counter()
non_phishing_counts = Counter()

# Procesar el dataset
for _, row in df.iterrows():
    percentage = row['uppercase_percentage_from']
    label = row['label']
    if pd.notnull(percentage):
        range_label = get_range(percentage)
        if label == 1:
            phishing_counts[range_label] += 1
        else:
            non_phishing_counts[range_label] += 1

# Ordenar los tramos para el gráfico
# Ordenar los tramos para el gráfico
sorted_ranges = [f"{lower}-{int(upper)}%" if upper != float('inf') else "+20%" for (lower, upper) in ranges]
phishing_values = [phishing_counts[range_label] for range_label in sorted_ranges]
non_phishing_values = [non_phishing_counts[range_label] for range_label in sorted_ranges]


# Configurar el gráfico
x = np.arange(len(sorted_ranges))  # Posiciones para las etiquetas del eje x
width = 0.35  # Ancho de las barras

fig, ax = plt.subplots(figsize=(12, 6))
rects1 = ax.bar(x - width/2, non_phishing_values, width, label='No Phishing', color='blue')
rects2 = ax.bar(x + width/2, phishing_values, width, label='Phishing', color='red')

# Añadir etiquetas y título
ax.set_xlabel('Porcentaje de Mayúsculas en el Campo From')
ax.set_ylabel('Número de Correos')
ax.set_title('Distribución de Mayúsculas en Direcciones de Email')
ax.set_xticks(x)
ax.set_xticklabels(sorted_ranges, rotation=45)
ax.legend()

# Añadir etiquetas encima de las barras
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                f'{int(height)}', ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
