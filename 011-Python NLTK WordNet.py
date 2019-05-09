# WordNet

# http://www.globalwordnet.org/.

'''
WordNet is a semantically oriented dictionary of English, similar to a traditional thesaurus
but with a richer structure. NLTK includes the English WordNet, with 155,287
words and 117,659 synonym sets. We’ll begin by looking at synonyms and how they
are accessed in WordNet.

we can conclude that
the words motorcar and automobile have the same meaning, i.e., they are synonyms.
We can explore these words with the help of WordNet:
'''

from nltk.corpus import wordnet as wn
car = wn.synsets('motorcar')
#print(car)

'''
Thus, motorcar has just one possible meaning and it is identified as car.n.01, the first
noun sense of car. The entity car.n.01 is called a synset, or “synonym set,” a collection
of synonymous words (or “lemmas”):
'''
wn.synset('car.n.01').lemma_names
print(wn.synset('car.n.01').lemma_names)

print(wn.synset('car.n.01').definition)
print(wn.synset('car.n.01').lemmas)
print(wn.synsets('car'))

