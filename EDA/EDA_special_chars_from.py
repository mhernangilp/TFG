import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# Cargar el dataset ya procesado
dataset_path = 'resources/processed_data/dataset.csv'
df = pd.read_csv(dataset_path)

# Crear contadores para phishing y no phishing
phishing_counts = Counter()
non_phishing_counts = Counter()

# Rango de números de caracteres no alfanuméricos (0-1, 1-2, ..., 10+)
ranges = [(i, i + 1) for i in range(0, 10, 1)]

def get_range(count):
    for lower, upper in ranges:
        if lower <= count < upper:
            return f"{lower}-{upper}"
    return f"{ranges[-1][1]}+"

# Procesar los valores del dataset
for _, row in df.iterrows():
    count = row['special_chars_from']
    label = row['label']
    range_label = get_range(count)
    if label == 1:
        phishing_counts[range_label] += 1
    else:
        non_phishing_counts[range_label] += 1

# Ordenar los tramos para el gráfico
sorted_ranges = [f"{lower}-{upper}" for lower, upper in ranges[:-1]] + [f"{ranges[-1][1]}+"]
phishing_values = [phishing_counts[range_label] for range_label in sorted_ranges]
non_phishing_values = [non_phishing_counts[range_label] for range_label in sorted_ranges]

# Configurar el gráfico
x = np.arange(len(sorted_ranges))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 6))
rects1 = ax.bar(x - width/2, non_phishing_values, width, label='No Phishing (Label 0)', color='blue')
rects2 = ax.bar(x + width/2, phishing_values, width, label='Phishing (Label 1)', color='red')

# Añadir etiquetas y título
ax.set_xlabel('Número de Caracteres No Alfanuméricos en el Campo From')
ax.set_ylabel('Número de Correos')
ax.set_title('Distribución de Caracteres No Alfanuméricos en Direcciones de Email')
ax.set_xticks(x)
ax.set_xticklabels(sorted_ranges, rotation=45)
ax.legend()

def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                f'{int(height)}', ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)

plt.tight_layout()
plt.show()
