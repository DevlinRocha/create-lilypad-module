FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
  build-essential \
  wget \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /outputs

COPY run_inference.py .
COPY model /model

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV HF_HOME=/model
ENV TRANSFORMERS_OFFLINE=1

ENTRYPOINT ["python", "/workspace/run_inference.py"]
