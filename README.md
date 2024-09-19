---

# AI Chatbot with Model Fine-tuning

This project is an AI-powered chatbot that uses a fine-tuned language model based on state-of-the-art NLP technologies. The model is fine-tuned on Hugging Face datasets and supports adaptive learning, allowing it to improve over time based on user feedback.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Adaptive Learning](#adaptive-learning)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project demonstrates the creation of a conversational AI chatbot that can be fine-tuned on specific datasets and improved over time via adaptive learning. The chatbot interacts with users through a simple React frontend, and the backend is built using FastAPI with Hugging Face model integration for NLP tasks.

## Features

- **Fine-tuning**: Use datasets from Hugging Face to fine-tune the model for optimal performance.
- **Adaptive learning**: The chatbot adapts based on feedback received from user interactions.
- **RESTful API**: FastAPI-based backend providing model prediction and feedback collection.
- **Frontend**: React-based interface for user interactions with the chatbot.
- **Docker Support**: The project is fully containerized using Docker for easy deployment.

## File Structure

```bash
ai_model_finetuning/
├── app.py                    # Main script for the FastAPI backend.
├── config.py                 # Configuration for hyperparameters, API keys, etc.
├── requirements.txt          # Python dependencies.
├── README.md                 # Documentation (this file).
├── models/                   # Folder for saved models.
│   └── refined_model/        # Pre-trained and fine-tuned model storage.
├── scripts/                  # Backend training scripts.
│   ├── train.py              # Fine-tuning script.
│   ├── evaluate.py           # Model evaluation.
│   └── utils.py              # Helper functions.
├── data/                     # Folder for datasets (optional if processed offline).
├── frontend/                 # React frontend files.
│   ├── public/               # Static HTML assets.
│   │   └── index.html        # Main HTML file.
│   ├── src/                  # React app components.
│   │   ├── components/
│   │   │   ├── ChatBox.js    # Chat interface component.
│   │   │   ├── InputBox.js   # Input box for user queries.
│   │   │   ├── Message.js    # Message display.
│   │   └── styles.css        # Basic styles.
│   ├── package.json          # Frontend dependencies.
├── .gitignore                # Ignoring unnecessary files.
└── Dockerfile                # Docker configuration for containerization.
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/krish567366/ai_chatbot_with_model.git
   cd ai_model_finetuning
   ```

2. **Install dependencies:**
   Create a virtual environment and install required Python packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Install frontend dependencies:**
   Navigate to the `frontend/` directory and install the required dependencies:
   ```bash
   cd frontend
   npm install
   ```

## Running the Application

### Using Docker (Recommended)
To build and run the application in a containerized environment:

1. **Build the Docker image:**
   ```bash
   docker build -t ai-model-finetuning .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 8000:8000 ai-model-finetuning
   ```

3. Access the application:
   - **Backend API**: `http://localhost:8000`
   - **Frontend**: `http://localhost:8000`

### Running Locally

1. **Backend:**
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Frontend:**
   ```bash
   cd frontend
   npm start
   ```

## API Endpoints

- **POST /predict**: Send a message to the chatbot and receive a response.
  - Request Body: `{ "message": "Hello" }`
  - Response: `{ "response": "Hi! How can I help you?" }`

- **POST /feedback**: Submit feedback to improve the model.
  - Request Body: `{ "message": "Hello", "response": "Hi!", "feedback": "positive" }`
  - Response: `{ "status": "Feedback received" }`

## Adaptive Learning

The project incorporates adaptive learning through a feedback loop:
- User responses are evaluated, and feedback is collected.
- This feedback is stored in a CSV file (`feedback.csv`) and used to retrain the model over time, making it more responsive and accurate based on real-world data.

## Technologies Used

- **Backend**: FastAPI, Hugging Face Transformers, Python
- **Frontend**: React, Axios
- **Model**: Pre-trained transformer models (BERT, GPT, etc.)
- **Containerization**: Docker
- **Data**: Hugging Face datasets
- **Adaptive Learning**: CSV-based feedback storage for model improvement

## Contributing

Contributions are welcome! If you’d like to contribute:
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
