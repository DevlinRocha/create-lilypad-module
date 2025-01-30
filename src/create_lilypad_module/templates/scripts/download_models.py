import sys

# from transformers import AutoTokenizer, AutoModelForSequenceClassification


def download_models():
    # TODO: Set this to your model's Hugging Face identifier
    MODEL_IDENTIFIER = ""

    # Remove the following if statement code block and configure the models the module needs.
    # Download the model(s) and tokenizer(s) for your module from the Hugging Face model hub
    # https://huggingface.co/docs/hub/en/models-downloading
    if not MODEL_IDENTIFIER:
        print(
            "❌ Error: Model download script is not configured.",
            file=sys.stderr,
            flush=True,
        )
        print("👉 /scripts/download_models.py")
        sys.exit(1)

    try:
        print(f"Downloading model `{MODEL_IDENTIFIER}`...")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_IDENTIFIER)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_IDENTIFIER)
        tokenizer.save_pretrained("./models")
        model.save_pretrained("./models")
        print("✅ Models downloaded successfully.")
    except Exception as error:
        print(
            f"❌ Error downloading models: {error}",
            file=sys.stderr,
            flush=True,
        )
        sys.exit(1)


if __name__ == "__main__":
    download_models()
