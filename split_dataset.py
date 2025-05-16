import pandas as pd
from sklearn.model_selection import train_test_split

# Ruta del dataset original
data_path = 'resources/processed_data/emails_clean.csv'
# Rutas de salida
train_path = 'resources/processed_data/emails_train.csv'
val_path = 'resources/processed_data/emails_val.csv'

# Carga y baraja el dataset
full_df = pd.read_csv(data_path)
full_df = full_df.sample(frac=1, random_state=42).reset_index(drop=True)

# División 80/20 estratificada
train_df, val_df = train_test_split(
    full_df,
    test_size=0.2,
    stratify=full_df['label'],
    random_state=42
)

# Guardado de archivos
train_df.to_csv(train_path, index=False)
val_df.to_csv(val_path, index=False)

print(f"Conjunto de entrenamiento guardado en: {train_path}")
print(f"Conjunto de validación guardado en: {val_path}")