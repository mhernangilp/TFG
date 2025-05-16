import pandas as pd
import torch
from transformers import RobertaTokenizerFast, RobertaForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from peft import get_peft_model, LoraConfig, TaskType

# 1. Load full dataset
data = pd.read_csv('resources/processed_data/emails_clean.csv')

# 2. Split into train and validation (80/20 stratified)
train_df, val_df = train_test_split(
    data, test_size=0.2, stratify=data['label'], random_state=42
)

# 3. Prepare texts and labels
def preprocess(df):
    texts = (df['subject'].fillna('') + ' ' + df['body'].fillna('')).tolist()
    labels = df['label'].tolist()
    return texts, labels

train_texts, train_labels = preprocess(train_df)
val_texts, val_labels = preprocess(val_df)

# 4. Load tokenizer and base model
tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base')
base_model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=2)

# 5. Configure LoRA adapters
peft_config = LoraConfig(
    task_type=TaskType.SEQ_CLS,
    inference_mode=False,
    r=8,
    lora_alpha=32,
    lora_dropout=0.1
)
model = get_peft_model(base_model, peft_config)

# 6. Tokenize datasets
def tokenize(texts):
    return tokenizer(texts, padding=True, truncation=True, max_length=512, return_tensors='pt')

train_encodings = tokenize(train_texts)
val_encodings = tokenize(val_texts)

# 7. Create PyTorch Dataset class
class EmailDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        item = {key: tensor[idx] for key, tensor in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx], dtype=torch.long)
        return item

# 8. Instantiate datasets
train_dataset = EmailDataset(train_encodings, train_labels)
val_dataset = EmailDataset(val_encodings, val_labels)

# 9. Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    learning_rate=3e-5,
    logging_steps=50,
    save_steps=100,
    fp16=torch.cuda.is_available(),
    remove_unused_columns=False
)

# 10. Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer
)

# 11. Train LoRA adapters
trainer.train()

# 1) Guardar el modelo completo (base + adapters)
trainer.save_model('./final_model')

# 2) (Opcional) Guardar solo los adapters LoRA
model.save_pretrained('./lora_adapters_only')


# 12. Predict on validation set
pred_output = trainer.predict(val_dataset)
preds = pred_output.predictions.argmax(axis=-1)

# 13. Compute and print metrics
accuracy = accuracy_score(val_labels, preds)
precision, recall, f1, _ = precision_recall_fscore_support(val_labels, preds, average='binary')
print(f"Validation Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-score: {f1:.4f}")

# 14. Show sample predictions
print("\nSample predictions vs. true labels:")
for i in range(min(10, len(val_labels))):
    idx = val_df.index[i]
    print(f"Email idx={idx}: true={val_labels[i]} pred={preds[i]}")
