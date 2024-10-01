# Use the official Python 3.10 slim image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["python", "my_app.py"]
