import csv
from collections import Counter

csv.field_size_limit(10**8)

def count_labels(csv_filename):
    with open(csv_filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        if not header:
            print("El archivo CSV está vacío o no tiene encabezado.")
            return
        
        label_counts = Counter(row[-1] for row in reader if row)
    
    for label, count in label_counts.items():
        print(f"{label}: {count}")

if __name__ == "__main__":
    csv_filename = "emails_train.csv"
    count_labels(csv_filename)