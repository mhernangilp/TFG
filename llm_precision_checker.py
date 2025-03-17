import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def round_values(value):
    return 0 if value <= 2 else 4

def compute_accuracy(df, column):
    df['rounded'] = df[column].apply(round_values)
    correct_zeros = df[(df['rounded'] == 0) & (df['label'] == 0)].shape[0]
    correct_fours = df[(df['rounded'] == 4) & (df['label'] == 1)].shape[0]
    total_correct = correct_zeros + correct_fours
    total = df.shape[0]
    accuracy = total_correct / total if total > 0 else 0
    print(f'Precisión para {column}: {accuracy:.4f}')

def plot_distribution(df, column, label_value):
    filtered_df = df[df['label'] == label_value]
    
    min_val, max_val = 0, 4
    value_counts = filtered_df[column].value_counts().reindex(range(min_val, max_val + 1), fill_value=0)
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x=value_counts.index, y=value_counts.values, color='blue', alpha=0.6)
    plt.title(f'Distribución de {column} para label {label_value}')
    plt.xlabel(column)
    plt.ylabel('Frecuencia')
    plt.show()

def main(filepath):
    df = load_data(filepath)
    
    for column in ['subject', 'body']:
        compute_accuracy(df, column)
    
    plot_distribution(df, 'subject', 1)
    plot_distribution(df, 'body', 1)
    plot_distribution(df, 'subject', 0)
    plot_distribution(df, 'body', 0)

if __name__ == "__main__":
    filepath = "resources/processed_data/testing_output.csv"
    main(filepath)
