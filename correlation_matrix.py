import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("resources/processed_data/testing_output.csv")

# Convertir 'date' a timestamp
df['date'] = pd.to_datetime(df['date']).astype(int) / 10**9  # Convertir a segundos

# Convertir variables categóricas en numéricas
df = pd.get_dummies(df, columns=['content_type', 'content_transfer_encoding'], drop_first=True)

# Calcular la matriz de correlación
corr_matrix = df.corr()

# Visualizar la matriz de correlación
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matriz de Correlación")
plt.show()


