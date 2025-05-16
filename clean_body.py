import pandas as pd
import re

def clean_attributes(text: str) -> str:
    patterns = [r'(href=")(.*?)(")',
                r'(style=")(.*?)(")',
                r'(src=")(.*?)(")']

    for pat in patterns:
        text = re.sub(pat, lambda m: f"{m.group(1)}{m.group(3)}", text)
    return text


def main():
    # Archivos de entrada y salida
    input_file = 'resources/processed_data/emails.csv'
    output_file = 'resources/processed_data/emails_clean.csv'

    # Cargar dataset
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: El archivo {input_file} no se encuentra.")
        return

    # Verificar columna 'body'
    if 'body' not in df.columns:
        print("Error: La columna 'body' no existe en el dataset.")
        return

    # Aplicar limpieza a cada fila de 'body'
    df['body'] = df['body'].astype(str).apply(clean_attributes)

    # Guardar resultado
    df.to_csv(output_file, index=False)
    print(f"Dataset limpiado guardado en: {output_file}")

if __name__ == '__main__':
    main()