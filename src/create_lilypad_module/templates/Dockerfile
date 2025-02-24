# Use the existing ollama Dockerfile as the base
FROM ollama/ollama

# Set environment variables
ARG MODEL_ID="${MODEL_NAME}:${MODEL_VERSION}"
ENV MODEL_ID=$MODEL_ID \
OLLAMA_HOST=0.0.0.0

# Set the working directory
WORKDIR /app

# Update and install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends curl \
  && rm -rf /var/lib/apt/lists/*

# Run ollama in the background and pull the specified model
RUN nohup bash -c "ollama serve &" && \
    until curl -s http://127.0.0.1:11434 > /dev/null; do \
        echo "Waiting for ollama to start..."; \
        sleep 5; \
    done && \
    ollama pull $MODEL_ID

EXPOSE 11434

# Create outputs directory and set permissions
RUN mkdir -p ./outputs && chmod 777 ./outputs

# Set outputs directory as a volume
VOLUME ./outputs

# Copy a script to start ollama and handle input
COPY src ./src
RUN chmod +x ./src/run_model

# Set the entrypoint to the script
ENTRYPOINT ["/app/src/run_model"]
