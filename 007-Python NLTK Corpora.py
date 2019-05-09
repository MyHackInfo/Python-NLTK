# Accessing Text Corpora

'''
As just mentioned, a text corpus is a large body of text. Many corpora are designed to
contain a careful balance of material in one or more genres

Corpora like doctor, scientist,etc.

# Gutenberg Corpus:>
NLTK includes a small selection of texts from the Project Gutenberg electronic text
archive, which contains some 25,000 free electronic books, hosted at http://www.gu
tenberg.org/. We begin by getting the Python interpreter to load the NLTK package,
then ask to see nltk.corpus.gutenberg.fileids()

Most NLTK corpus readers include a variety of access methods apart
from words(), raw(), and sents().

'''

import nltk
print(nltk.corpus.gutenberg.fileids())

#lets take one of them
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
emma_raw = nltk.corpus.gutenberg.raw('austen-emma.txt')
emma_sents = nltk.corpus.gutenberg.sents('austen-emma.txt')
print("length of austen-emma.txt",len(emma))
print("length of raw austen-emma.txt",len(emma_raw))
print("length of sents austen-emma.txt",len(emma_sents))



# Web and Chat Text

'''
Although Project Gutenberg contains thousands of books, it represents established
literature. It is important to consider less formal language as well. NLTK’s small collection
of web text includes content from a Firefox discussion forum, conversations
overheard in New York, the movie script of Pirates of the Carribean, personal advertisements,
and wine reviews

'''
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65],'....')


from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print(chatroom)

# And Some other corpus

#Brown Corpus
#Reuters Corpus
#Inaugural Address Corpus
#Annotated Text Corpora
#Corpora in Other Languages
#Text Corpus Structure


# Loading Your Own Corpus
from nltk.corpus import PlaintextCorpusReader
corpus_root ='\owncorpus'
wordlists = PlaintextCorpusReader(corpus_root,'.*')
print(wordlists.fileids())


'''
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample = gutenberg.raw("bible-kjv.txt")
tok = sent_tokenize(sample)
print(tok[5:15])
'''
