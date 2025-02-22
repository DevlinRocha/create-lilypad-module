import sys
from config.constants import MODEL_IDENTIFIER

# TODO: Configure the model(s) needed for your module.
# Download the model(s) and tokenizer(s) for your module from the Hugging Face model hub.
# https://huggingface.co/docs/hub/en/models-downloading
# from transformers import AutoTokenizer, AutoModelForSequenceClassification

# TODO: Update `../requirements.txt`.


def download_models():
    if not MODEL_IDENTIFIER:
        print(
            "❌ Error: Model identifier is not configured.",
            file=sys.stderr,
            flush=True,
        )
        print("👉 /config/constants.py")
        sys.exit(1)

    try:
        print(f"Downloading model `{MODEL_IDENTIFIER}`...")
        # TODO: Initialize `model` and `tokenizer`.
        # tokenizer = AutoTokenizer.from_pretrained(MODEL_IDENTIFIER)
        # model = AutoModelForSequenceClassification.from_pretrained(MODEL_IDENTIFIER)
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
