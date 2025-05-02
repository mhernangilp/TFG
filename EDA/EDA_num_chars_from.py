import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset desde archivo CSV
df = pd.read_csv('resources/processed_data/dataset.csv')

plt.figure(figsize=(10, 3))
plt.scatter(df['num_chars_from'], df['label'], c=df['label'], cmap='coolwarm', alpha=0.6)

plt.title("Relación entre el número de caracteres en la dirección y si es phishing")
plt.xlabel("Número de caracteres en la dirección (From)")
plt.ylabel("Phishing (1) / No Phishing (0)")
plt.yticks([0, 1])  # Mostrar solo 0 y 1
plt.ylim(-0.5, 1.5)
plt.grid(True)
plt.show()
