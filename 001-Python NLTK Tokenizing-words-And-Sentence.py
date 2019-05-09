'''
from nltk.book import *

# Counting Vocabulary
# Let’s begin by finding out the length of a text from start to finish, in terms of the words and punctuation symbols that appear.
# We use the term len to get the length of something, which we’ll apply here to the book of Genesis
>>> len(text3) //44764

# So Genesis has 44,764 words and punctuation symbols, or “tokens.”
# A token is the technical name for a sequence of characters—such as hairy, his,

## The vocabulary of a text is just the set of tokens that it uses, since in a set,
## all duplicates are collapsed together. In Python we can obtain the vocabulary items of text3 with the command: set(text3).
## When you do this, many screens of words will fly past
>>> sorted(set(text3))

# let’s calculate a measure of the lexical richness of the text.
>>> len(text3) / len(set(text3))

# let’s focus on particular words. We can count how often a word occurs in a text,
#  and compute what percentage of the text is taken up by a specific word
>>>text3.count("smote")  //5
>>> 100 * text4.count('a') / len(text4) //1.


# Create function do this work
# lexical_diversity() function
# percentage() function

def lexical_diversity(text):
    return len(text)/ len(set(text))

def percentage(count,total):
    return 100 * count / total


## We have two important building blocks—lists and strings ##

# Lists

>>>sets = ['one','two','four','ten','etc']
>>>len(sets)
>>>lexical_diversity(sets)

# Add two lists
# sent4 + sent1


# What if we want to add a single item to a list? This is known as appending.
# When we append() to a list

>>>sets.append("hey")

# Indexing Lists
>>>sets[2]
>>>sets.index('etc')

# Slicing
>>>sets[1:3]

# Variables
>>>sets1 = ['hey','its','me']


# Strings

# assign a string to a variable
# index a string
# and slice a string

>>>name = 'narsi'
>>>name[0]
>>>name[:3]

# Perform multiplication and addition with strings
>>>name * 2
>>>name + '!'

# We can join the words of a list to make a single string,
# or split a string into a list
>>> ''.join(['Money','python'])
>>> 'Money Python'.split()


## Frequency Distributions

# get = 5 time
# set = 7 time
# ready = 40 time
# NLTK provides built-in support for them. Let’s use a "FreqDist()"

>>> fd = FreqDist(text3)
>>> fd
>>> vocab = fd.keys()
>>> vocabv = fd.values()



>>>fd.plot(50, cumulative=True)

# If the frequent words don’t help us, how about the words that occur once only,
# the socalled hapaxes
>>>fd.hapaxes()


# Selection of Words

# the long words of a text; perhaps these will be more characteristic and informative.

>>> words = set(text1)
>>> long_words = [w for w in words if len(w) > 15]
>>>sorted(long_words)



## Automatic Natural Language Understanding ##
# Machine Translation
# Spoken Dialogue Systems. ((Turing Test)) Chatbots.

# Unit 1 Completed
# Language Processing and Python



'''
## Function of Plural word
def plural(word):
    if word.endswith('y'):
        return word[:-1]+ 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh','ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'


'''
from nltk.tokenize import sent_tokenize,word_tokenize

example_text = "Hello Mr. Narsi , what are you doing today?"

# sent_tokenize and word_tokenize use
print(sent_tokenize(example_text))
print(word_tokenize(example_text))

# We can use for loop to get all one by one
for i in word_tokenize(example_text):
    print("This is word_tokenize :",i)
'''
