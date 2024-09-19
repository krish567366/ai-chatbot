# scripts/train.py

import torch
from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
from utils import load_and_prepare_data
from config import MODEL_NAME, EPOCHS, BATCH_SIZE, LEARNING_RATE

# Load the dataset and model
dataset = load_and_prepare_data('imdb', MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)

# Set training arguments
training_args = TrainingArguments(
    output_dir="./models/refined_model/",
    evaluation_strategy="epoch",
    learning_rate=LEARNING_RATE,
    per_device_train_batch_size=BATCH_SIZE,
    num_train_epochs=EPOCHS,
    weight_decay=0.01,
    load_best_model_at_end=True
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset['train'],
    eval_dataset=dataset['test'],
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
trainer.save_model("./models/refined_model/")
