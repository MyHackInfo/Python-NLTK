# Pronouncing Dictionary

'''
A slightly richer kind of lexical resource is a table (or spreadsheet), containing a word
plus some properties in each row. NLTK includes the CMU Pronouncing Dictionary
for U.S. English, which was designed for use by speech synthesizers.
'''

import nltk

entries = nltk.corpus.cmudict.entries()
print(len(entries))

for entry in entries[100:200]:
    print(entry)
