import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def plot_distribution(df, column, label_value):
    filtered_df = df[df['label'] == label_value]
    plt.figure(figsize=(8, 5))
    sns.histplot(filtered_df[column], bins=5, kde=True, discrete=True)
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
