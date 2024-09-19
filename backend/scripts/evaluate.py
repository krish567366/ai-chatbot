# scripts/evaluate.py

from transformers import AutoModelForSequenceClassification, AutoTokenizer
from utils import load_and_prepare_data
from sklearn.metrics import accuracy_score

# Load the fine-tuned model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("./models/refined_model/")
tokenizer = AutoTokenizer.from_pretrained("./models/refined_model/")

# Load the dataset
dataset = load_and_prepare_data('imdb', 'bert-base-uncased')

# Make predictions and evaluate
def compute_accuracy():
    model.eval()
    predictions, labels = [], []
    
    for batch in dataset['test']:
        inputs = tokenizer(batch['text'], return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
            pred = torch.argmax(outputs.logits, dim=-1).item()
            predictions.append(pred)
            labels.append(batch['label'])
    
    accuracy = accuracy_score(labels, predictions)
    return accuracy

print("Test Accuracy:", compute_accuracy())
