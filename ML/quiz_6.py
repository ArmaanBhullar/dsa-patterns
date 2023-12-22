import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')
text = """I waited for the train. The train was late. Dr. Jiao and Seung Jun took the bus. I looked for
Seung Jun and Dr. Jiao at the bus station."""
result = [word_tokenize(t) for t in sent_tokenize(text)]
print(len(result))
print(result[2][7])