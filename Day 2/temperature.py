import nltk
from nltk.tokenize import word_tokenize

text = "tokenization using genai by temperature control is important for generating different types of responses."
tokens = word_tokenize(text)

token_length = len(tokens)

# temperature conditions
if token_length <= 5:
    temperature = 0.2
    temp = "factual"
elif token_length <= 15:
    temperature = 0.6
    temp = "balanced"
else:
    temperature = 0.9
    temp = "creative"
print("Selected temperature:", temperature)
print("Temperature type:", temp)