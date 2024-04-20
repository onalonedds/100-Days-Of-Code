import pandas as pd
import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AdamW
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Load tokenizer and model
model_name = "DeepPavlov/rubert-base-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)

# Assuming CUDA is available, otherwise replace 'cuda' with 'cpu'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)


class ReviewsDataset(Dataset):
    def __init__(self, texts, labels, tokenizer):
        self.tokenizer = tokenizer
        self.texts = texts
        self.labels = labels

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        inputs = self.tokenizer(text, padding='max_length', truncation=True, max_length=512, return_tensors="pt")
        item = {key: val.squeeze() for key, val in inputs.items()}
        item['labels'] = torch.tensor(self.labels[idx], dtype=torch.long)
        return item


# Load and prepare data
data = pd.read_csv("reviews.csv")
texts = data["Text"].tolist()
labels = data["Label"].tolist()

test_data = pd.read_csv("rev_test.csv")
test_texts = test_data["Text"].tolist()
test_labels = test_data["Label"].tolist()

# Split data for demonstration (consider using your actual train/test split)
# train_texts, val_texts, train_labels, val_labels = train_test_split(texts, labels, test_size=0.1, random_state=42)

train_dataset = ReviewsDataset(texts, labels, tokenizer)
val_dataset = ReviewsDataset(test_texts, test_labels, tokenizer)

train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=8, shuffle=False)

optimizer = AdamW(model.parameters(), lr=2e-5)

# Training loop (simplified)
model.train()
for epoch in range(3):  # Example: 3 epochs
    for batch in train_loader:
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
    print(f"Epoch {epoch + 1}, Loss: {loss.item()}")

# Evaluation loop
model.eval()
predictions = []
with torch.no_grad():
    for batch in val_loader:
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(**batch)
        logits = outputs.logits
        preds = torch.argmax(logits, dim=-1)
        predictions.extend(preds.cpu().numpy())

accuracy = accuracy_score(test_labels, predictions)
print(f"Validation accuracy: {accuracy:.2f}")
print(predictions)
