FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  wget \
  && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /workspace

# Install module dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add models
RUN mkdir /models
ARG MODEL_URL
ADD MODEL_URL /models

# Create output directory
RUN mkdir -p /outputs

# Copy source code
COPY src /src

# Set environment variables
ENV HF_HOME=/models
ENV TRANSFORMERS_OFFLINE=1

# Set entrypoint
ENTRYPOINT ["python", "/src/run_inference.py"]
