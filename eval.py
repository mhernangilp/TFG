import pandas as pd
import torch
from transformers import RobertaTokenizerFast, RobertaForSequenceClassification
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from peft import PeftModel

# 1. Carga del dataset de validación
val_df = pd.read_csv('resources/processed_data/emails_val.csv')
texts = (val_df['subject'].fillna('') + ' ' + val_df['body'].fillna('')).tolist()
labels = val_df['label'].tolist()

# 2. Tokenizer y carga de modelo
tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base')
base_model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=2)
model = PeftModel.from_pretrained(base_model, './final_model')
model.eval()

# 3. Tokenización
encodings = tokenizer(texts, padding=True, truncation=True, max_length=512, return_tensors='pt')

# 4. Inferencia
def predict(enc):
    with torch.no_grad():
        out = model(**{k: v.to(model.device) for k, v in enc.items()})
        return out.logits.argmax(-1).cpu().numpy()

preds = predict(encodings)

# 5. Métricas
acc = accuracy_score(labels, preds)
prec, rec, f1, _ = precision_recall_fscore_support(labels, preds, average='binary')
print(f"Validation Accuracy: {acc:.4f}")
print(f"Precision: {prec:.4f}")
print(f"Recall: {rec:.4f}")
print(f"F1-score: {f1:.4f}")

# 6. Ejemplos\print("\nSample predictions vs. true labels:")
for i in range(min(10, len(labels))):
    print(f"Email idx={i}: true={labels[i]} pred={preds[i]}")