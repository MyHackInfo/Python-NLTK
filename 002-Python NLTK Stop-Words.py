# Stopwords
import nltk

'''
## Wordlist Corpora
NLTK includes some corpora that are nothing more than wordlists.

There is also a corpus of "stopwords", that is, high-frequency words such as the, to, and
also that we sometimes want to filter out of a document before further processing.


'''

# Unsual Words
def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)


#unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))

from nltk.corpus import stopwords
#stopwords.words('english')

#One more wordlist corpus is the Names Corpus, containing 8,000 first names categorized by gender.
names = nltk.corpus.names
names.fileids()

male_names = names.words('male.txt')
female_names= names.words('female.txt')

same_name = [w for w in male_names if w in female_names]
print(same_name)




'''
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

exam = "Hey my name is narsi and i go to the python nltk field."
stop_words =set(stopwords.words('english'))

words = word_tokenize(exam)

# filtered_sent = []
# for w in words:
#     if w not in stop_words:
#         filtered_sent.append(w)

filtered_sent = [w for w in words if not w in stop_words]

print(filtered_sent)
'''
