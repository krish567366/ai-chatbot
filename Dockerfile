# Stage 1: Build the frontend
FROM node:16 AS frontend-build

WORKDIR /app/frontend

# Copy package.json and install dependencies
COPY ./frontend/package.json ./frontend/package-lock.json ./
RUN npm install

# Copy all frontend files
COPY ./frontend/ ./

# Build the frontend
RUN npm run build

# Stage 2: Build the backend (FastAPI + Python)
FROM python:3.9-slim AS backend

WORKDIR /app

# Copy the backend files
COPY ./requirements.txt ./requirements.txt
COPY ./ ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend build from Stage 1
COPY --from=frontend-build /app/frontend/build ./frontend/build

# Set environment variables (optional)
ENV MODEL_PATH="./models/refined_model/"
ENV FEEDBACK_FILE="feedback.csv"

# Expose port 8000 for the FastAPI backend
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
