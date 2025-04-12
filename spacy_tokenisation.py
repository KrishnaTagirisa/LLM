import spacy

# Load English tokenizer, POS tagger, parser, NER
# python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Hello there! How are you doing today? This is a sample NLP tokenization example."

# Process the text
doc = nlp(text)

# Tokenization
print("spaCy Tokenization:")
for token in doc:
    print(token.text)
