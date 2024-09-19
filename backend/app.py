from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import pandas as pd
import os

app = FastAPI()

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("./models/refined_model/")
tokenizer = AutoTokenizer.from_pretrained("./models/refined_model/")
nlp_pipeline = pipeline('text-classification', model=model, tokenizer=tokenizer)

# Data storage
feedback_file = 'feedback.csv'

class Query(BaseModel):
    text: str

class Feedback(BaseModel):
    text: str
    feedback: str

@app.post("/predict")
def get_model_prediction(query: Query):
    prediction = nlp_pipeline(query.text)
    return {"label": prediction[0]['label'], "score": prediction[0]['score']}

@app.post("/feedback")
def collect_feedback(feedback: Feedback):
    feedback_data = {'text': feedback.text, 'feedback': feedback.feedback}
    
    if not os.path.isfile(feedback_file):
        df = pd.DataFrame([feedback_data])
    else:
        df = pd.read_csv(feedback_file)
        df = df.append(feedback_data, ignore_index=True)
    
    df.to_csv(feedback_file, index=False)
    return {"status": "Feedback received"}
