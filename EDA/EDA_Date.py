import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset procesado directamente desde CSV
df = pd.read_csv('resources/processed_data/dataset.csv')

df = df.rename(columns={'date': 'hour'})
df = df.dropna(subset=['hour'])
df['hour'] = df['hour'].astype(int)

# Agrupar por hora y etiqueta
grouped = df.groupby(["hour", "label"]).size().unstack(fill_value=0)

# Ordenar columnas por label para asegurar el orden 0, 1
grouped = grouped[[0, 1]]

# Crear el gráfico con colores personalizados
grouped.plot(kind="bar", stacked=False, figsize=(12, 6), color=["blue", "red"])
plt.title("Distribución de emails por hora y etiqueta")
plt.xlabel("Hora del día")
plt.ylabel("Cantidad de emails")
plt.legend(["No phishing", "Phishing"], title="Etiqueta")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Mostrar el gráfico
plt.show()
