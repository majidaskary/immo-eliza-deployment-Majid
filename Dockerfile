# Use Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose ports
EXPOSE 8000
EXPOSE 8501

# Start both FastAPI and Streamlit servers with a delay for Streamlit
CMD uvicorn app:app --host 0.0.0.0 --port 8000 & \
    sleep 5 && streamlit run streamlit.py --server.port=8501 --server.address=0.0.0.0
