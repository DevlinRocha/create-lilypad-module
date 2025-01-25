from ..config.constants import MODEL_NAME


def download_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

    tokenizer.save_pretrained("./model")
    model.save_pretrained("./model")


if __name__ == "__main__":
    download_model()
