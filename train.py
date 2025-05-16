import pandas as pd
import torch
from transformers import (
    RobertaTokenizerFast,
    RobertaForSequenceClassification,
    Trainer,
    TrainingArguments
)
from peft import get_peft_model, LoraConfig, TaskType
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# 1. Carga del dataset de entrenamiento
train_df = pd.read_csv('resources/processed_data/emails_train.csv')
texts = (train_df['subject'].fillna('') + ' ' + train_df['body'].fillna('')).tolist()
labels = train_df['label'].tolist()

# 2. Tokenizer y modelo base
tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base')
base_model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=2)

# 3. Configuración LoRA
e_config = LoraConfig(
    task_type=TaskType.SEQ_CLS,
    inference_mode=False,
    r=8,
    lora_alpha=32,
    lora_dropout=0.1
)
model = get_peft_model(base_model, e_config)

# 4. Tokenización
def tokenize(texts_list):
    return tokenizer(texts_list, padding=True, truncation=True, max_length=512, return_tensors='pt')

encodings = tokenize(texts)

# 5. Dataset PyTorch
class EmailDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        item = {k: v[idx] for k, v in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx], dtype=torch.long)
        return item

train_dataset = EmailDataset(encodings, labels)

# 6. Argumentos de entrenamiento
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    learning_rate=3e-5,
    logging_steps=50,
    save_steps=100,
    save_total_limit=3,
    fp16=torch.cuda.is_available(),
    remove_unused_columns=False
)

# 7. Trainer
t = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    tokenizer=tokenizer
)

# 8. Entrenar y guardar
if __name__ == '__main__':
    t.train()
    t.save_model('./final_model')
    print("Modelo entrenado y guardado en './final_model'.")