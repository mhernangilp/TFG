import pandas as pd
import torch
import seaborn as sns
import matplotlib.pyplot as plt
from transformers import RobertaTokenizerFast, RobertaForSequenceClassification
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_auc_score, roc_curve
)
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
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# 3. Tokenización
encodings = tokenizer(texts, padding=True, truncation=True, max_length=512, return_tensors='pt')
encodings = {k: v.to(device) for k, v in encodings.items()}

# 4. Inferencia
with torch.no_grad():
    outputs = model(**encodings)
    logits = outputs.logits
    probs = torch.softmax(logits, dim=1)
    preds = logits.argmax(-1).cpu().numpy()
    proba = probs[:, 1].cpu().numpy()

# 5. Métricas
prec = precision_score(labels, preds, average='binary')
rec = recall_score(labels, preds, average='binary')
f1 = f1_score(labels, preds, average='binary')
roc_auc = roc_auc_score(labels, proba)

print("=== Métricas de Validación ===")
print(f"Precision:  {prec:.4f}")
print(f"Recall   :  {rec:.4f}")
print(f"F1-score :  {f1:.4f}")
print(f"ROC AUC  :  {roc_auc:.4f}")

# 6. Matriz de Confusión
cm = confusion_matrix(labels, preds)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Sí'], yticklabels=['No', 'Sí'])
plt.xlabel('Predicción')
plt.ylabel('Real')
plt.title('Matriz de Confusión')
plt.tight_layout()
plt.show()
