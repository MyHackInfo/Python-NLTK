# first install nltk! downloadable for free from http://www.nltk.org/
# using cmd type :-> pip install nltk
# import nltk that give error it not install proper
# Other wise its install .

import nltk

# Use this method for download some think that need for nltk.
#nltk.download()

from nltk.book import *

# Searching Text
# In python prompt:
#>>>text1
#>>>text2

#A concordance view shows us every occurrence of a given word, together with somecontext.
#>>>text1.concordance("monstrous")

#For example, search Sense and Sensibility for the word affection, using
#>>>text2.concordance("affection")

#What other words appear in a similar range of contexts? We can find out by appending the term similar to the name of the text in question, then inserting the relevant word in parentheses
#>>>text1.similar("monstrous")

#The term common_contexts allows us to examine just the contexts that are shared by two or more words, such as monstrous and very
#>>>text2.common_contexts(["monstrous", "very"])

#It is one thing to automatically detect that a particular word occurs in a text, and to display some words that appear in the same context. However, we can also determine the location of a word in the text: how many words from the beginning it appears. This positional information can be displayed using a dispersion plot
#>>>text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

#let’s try generating some random text in the various styles we have just seen. To do this, we type the name of the text followed by the term generate.
#>>>text3.generate()



# More info-
# tokenizing = word tokenizers.... sentence tokenizers
# lexicon and corporas
# corporas- body of text. ex: medical journals,persidential speeches,english language.
# lexicon- words and their means
# A lexicon, or lexical resource, is a collection of words and/or phrases along with associated information, such as part-of-speech and sense definitions

# investor-speak..... regular english-speak

# investor speak 'bull' = someone who is positive about the market
# english-speak 'bull' = scary animal you dont want runnig @ you
