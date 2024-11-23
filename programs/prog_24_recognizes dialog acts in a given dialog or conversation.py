from transformers import pipeline

# Load the zero-shot classification pipeline
classifier = pipeline("zero-shot-classification")

def recognize_dialog_acts(dialog, labels):
    results = classifier(dialog, labels)
    return results["labels"][0]  # Highest scoring label

dialog = "Could you please tell me the time?"
labels = ["Request", "Question", "Greeting", "Command"]
act = recognize_dialog_acts(dialog, labels)
print("Dialog Act:", act)
