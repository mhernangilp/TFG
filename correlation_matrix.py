import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('resources/processed_data/dataset.csv')

# Eliminar la columna 'label'
df = df.drop(columns=['label'])

# Calcular la matriz de correlación
correlation_matrix = df.corr()

# Mostrar la matriz de correlación como heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación')
plt.tight_layout()
plt.show()
