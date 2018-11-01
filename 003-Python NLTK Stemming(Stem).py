from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
exam = ["Python","Pythoner","Pythoning","Pythoned"]

for w in exam:
    print(pa.stem(w))
