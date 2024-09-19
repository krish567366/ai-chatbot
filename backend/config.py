# config.py

class Config:
    # Model and Training Settings
    MODEL_NAME = "bert-large-uncased"  # Example: use BERT or any state-of-the-art model.
    EPOCHS = 5
    BATCH_SIZE = 16
    LEARNING_RATE = 3e-5
    MAX_SEQ_LENGTH = 128

    # Paths and Files
    MODEL_PATH = "./models/refined_model/"  # Directory for saving/loading models
    FEEDBACK_FILE = 'feedback.csv'  # File for storing feedback

    # Add other configurations here if needed
