# scripts/utils.py

from datasets import load_dataset
from transformers import AutoTokenizer

def load_and_prepare_data(dataset_name, model_name, max_length=128):
    # Load dataset from Hugging Face Hub
    dataset = load_dataset(dataset_name)

    # Load the tokenizer for the chosen pre-trained model
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Tokenize the data
    def tokenize(batch):
        return tokenizer(batch['text'], padding='max_length', truncation=True, max_length=max_length)

    # Apply tokenization to the dataset
    tokenized_dataset = dataset.map(tokenize, batched=True)
    
    # Set format to tensors for training with PyTorch
    tokenized_dataset.set_format(type='torch', columns=['input_ids', 'attention_mask', 'label'])
    
    return tokenized_dataset
