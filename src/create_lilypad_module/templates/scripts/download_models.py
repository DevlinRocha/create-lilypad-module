from config.constants import MODEL_URL


def download_models():
    # tokenizer = AutoTokenizer.from_pretrained(MODEL_URL)
    # model = AutoModelForSequenceClassification.from_pretrained(MODEL_URL)

    tokenizer.save_pretrained("./models")
    model.save_pretrained("./models")


if __name__ == "__main__":
    download_models()
