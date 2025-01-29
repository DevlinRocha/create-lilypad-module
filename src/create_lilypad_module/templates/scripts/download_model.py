from config.constants import MODEL_URL


def download_model():
    # tokenizer = AutoTokenizer.from_pretrained(MODEL_URL)
    # model = AutoModelForSequenceClassification.from_pretrained(MODEL_URL)

    tokenizer.save_pretrained("./model")
    model.save_pretrained("./model")


if __name__ == "__main__":
    download_model()
