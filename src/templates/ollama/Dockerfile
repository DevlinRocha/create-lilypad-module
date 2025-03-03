# Use the existing Ollama Docker image as the base
FROM ollama/ollama

# Set environment variables
ARG MODEL_ID="${MODEL_NAME}:${MODEL_VERSION}"
ENV MODEL_ID=$MODEL_ID \
  OLLAMA_HOST=0.0.0.0

# Set the working directory
WORKDIR /app

# Update and install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends curl \
  && rm -rf /var/lib/apt/lists/* \
  # Run ollama in the background and pull the specified model
  && nohup bash -c "ollama serve &" && \
    until curl -s http://127.0.0.1:11434 > /dev/null; do \
        echo "Waiting for ollama to start..."; \
        sleep 5; \
    done && \
    ollama pull $MODEL_ID \
  # Create outputs directory and set permissions
  && mkdir -p ./outputs && chmod 777 ./outputs

EXPOSE 11434

# Copy source code
COPY src ./src

RUN chmod +x ./src/run_model

# Set outputs directory as a volume
VOLUME ./outputs

# Set the entrypoint to the script
ENTRYPOINT ["/app/src/run_model"]
