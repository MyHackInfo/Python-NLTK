# Comparative Wordlists

'''
Another example of a tabular lexicon is the comparative wordlist. NLTK includes
so-called Swadesh wordlists, lists of about 200 common words in several languages.
The languages are identified using an ISO 639 two-letter code
'''

import nltk

from nltk.corpus import swadesh
#print(swadesh.fileids(),"=======")

#print(swadesh.words('en'))


'''
We can access cognate words from multiple languages using the entries() method,
specifying a list of languages. With one further step we can convert this into a simple
dictionary (we’ll learn about dict())
'''

en2fr = swadesh.entries(['en','fr'])
#print(fr2en)

# You can create dictionary to translate one language to another language words
# translate french to english
translate = dict(en2fr)
#print(translate['dog'])



'''
We can make our simple translator more useful by adding other source languages. Let’s
get the German-English and Spanish-English pairs, convert each to a dictionary using
dict(), then update our original translate dictionary with these additional mappings
'''

de2en = swadesh.entries(['de','en']) # German-English
es2en = swadesh.entries(['es','en']) # Spanish-English
translate.update(dict(de2en))
translate.update(dict(es2en))

print(translate['Hund'])
print(translate['perro'])




