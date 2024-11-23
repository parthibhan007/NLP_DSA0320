# Install transformers library
#pip install transformers
from transformers import MarianMTModel, MarianTokenizer

def translate_text_to_french(text):
    model_name = "Helsinki-NLP/opus-mt-en-fr"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    inputs = tokenizer.encode(text, return_tensors="pt", max_length=512, truncation=True)
    translated = model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

text = "The weather is beautiful today."
translated_text = translate_text_to_french(text)
print("Translated Text:", translated_text)
