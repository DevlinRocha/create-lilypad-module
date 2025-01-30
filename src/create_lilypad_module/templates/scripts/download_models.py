# Download the model(s) and tokenizer(s) for your module from the Hugging Face model hub
# https://huggingface.co/docs/hub/en/models-downloading


# from transformers import AutoTokenizer, AutoModelForSequenceClassification


def download_models():
    MODEL_IDENTIFIER = ""

    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_IDENTIFIER)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_IDENTIFIER)
        tokenizer.save_pretrained("./models")
        model.save_pretrained("./models")
        print("✅ Models downloaded successfully.")
    except:
        print("❌ Error downloading models.")
        print("⛔️ Have you configured the download script?")
        print("👉 /scripts/download_models.py")


if __name__ == "__main__":
    download_models()
