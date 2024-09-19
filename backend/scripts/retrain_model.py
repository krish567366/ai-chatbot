# scripts/retrain_model.py
import pandas as pd
from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification, AutoTokenizer
from sklearn.model_selection import train_test_split

# Load the feedback data
feedback_file = '../feedback.csv'
df = pd.read_csv(feedback_file)

# Prepare the dataset
texts = df['text'].tolist()
labels = df['feedback'].apply(lambda x: 1 if x == 'positive' else 0).tolist()

# Split data
train_texts, val_texts, train_labels, val_labels = train_test_split(texts, labels, test_size=0.2)

# Load model and tokenizer
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Tokenize data
train_encodings = tokenizer(train_texts, truncation=True, padding=True)
val_encodings = tokenizer(val_texts, truncation=True, padding=True)

class FeedbackDataset:
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset = FeedbackDataset(train_encodings, train_labels)
val_dataset = FeedbackDataset(val_encodings, val_labels)

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset
)

trainer.train()

# Save the model
model.save_pretrained("../models/refined_model/")
tokenizer.save_pretrained("../models/refined_model/")
