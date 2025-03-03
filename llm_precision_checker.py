import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def plot_distribution(df, column, label_value):
    filtered_df = df[df['label'] == label_value]
    
    # Asegurar que el rango siempre tenga valores de 0 a 4 con frecuencia correcta
    min_val, max_val = 0, 4
    all_values = pd.Series(range(min_val, max_val + 1))
    
    # Contar valores existentes y asegurarse de que los faltantes sean 0
    value_counts = filtered_df[column].value_counts().reindex(range(min_val, max_val + 1), fill_value=0)
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x=value_counts.index, y=value_counts.values, color='blue', alpha=0.6)
    plt.title(f'Distribución de {column} para label {label_value}')
    plt.xlabel(column)
    plt.ylabel('Frecuencia')
    plt.show()

def main(filepath):
    df = load_data(filepath)
    
    plot_distribution(df, 'subject', 1)
    plot_distribution(df, 'body', 1)
    plot_distribution(df, 'subject', 0)
    plot_distribution(df, 'body', 0)

if __name__ == "__main__":
    filepath = "resources/processed_data/testing_output.csv"  # Cambia esto por la ruta de tu archivo
    main(filepath)
