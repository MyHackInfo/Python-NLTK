from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
exam = ["Python","Pythoner","Pythoning","Pythoned"]

for w in exam:
    print(pa.stem(w))


###############################
'''
# Finding Word Stems
Some language processing tasks we want to ignore word endings,
and just deal with word stems.

Although we will ultimately use NLTK’s built-in stemmers.

'''
import re
import nltk

def stem(word):
    for suffix in ['ing','ly','ed','ious','ies','ive','es','s','ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
        return word


reg = re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
print(reg)

'''
Here, re.findall() just gave us the suffix even though the regular expression matched
the entire word. This is because the parentheses have a second function, to select substrings
to be extracted. If we want to use the parentheses to specify the scope of the
disjunction, but not to select the material to be output, we have to add ?:, which is just
one of many arcane subtleties of regular expressions. Here’s the revised version.
'''
reg1 = re.findall(r'^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
print(reg1)


'''
However, we’d actually like to split the word into stem and suffix. So we should just
parenthesize both parts of the regular expression:
'''
reg2 = re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
regs2 = re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'process')
print(reg2)
print(regs2)

'''
The regular expression incorrectly found an -s suffix instead of an -es suffix. This demonstrates
another subtlety: the star operator is “greedy” and so the .* part of the expression
tries to consume as much of the input as possible. If we use the “non-greedy”
version of the star operator, written *?, we get what we want:

This works even when we allow an empty suffix, by making the content of the second
parentheses optional:
'''
reg3 = re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')
regs3 = re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$', 'language')
print(reg3)
print(regs3)



def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem

raw = """DENNIS: Listen, strange women lying in ponds distributing swords
 is no basis for a system of government. Supreme executive power derives from
 a mandate from the masses, not from some farcical aquatic ceremony."""

tokens = nltk.word_tokenize(raw)
print([stem(t) for t in tokens])

