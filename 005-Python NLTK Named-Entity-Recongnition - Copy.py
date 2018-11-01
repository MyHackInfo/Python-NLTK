import nltk
from nltk.corpus import state_union
from nltk.totenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWbush.txt")
sample_text = state_union.raw("2006-GWbush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            nameEnt = nltk.ne_chunk(tagged,binary=True)
            nameEnt.draw()

        except Exception as e:
            print(str(e))

process_content()
