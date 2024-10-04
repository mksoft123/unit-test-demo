# Use the official Python 3.9 slim image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pytest

# Copy the rest of the application code, including tests
COPY . .

# Command to run the application
CMD ["python", "my_app.py"]
