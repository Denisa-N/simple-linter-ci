FROM python:3.8-slim-buster

WORKDIR /app

# Copy dependencies first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Default command
CMD ["python", "app.py"]

