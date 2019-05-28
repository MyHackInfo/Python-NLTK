# Processing Raw Text ##
'''
1. How can we write programs to access text from local files and from the Web, in
order to get hold of an unlimited range of language material?
2. How can we split documents up into individual words and punctuation symbols,
so we can carry out the same kinds of analysis we did with text corpora in earlier
chapters?
3. How can we write programs to produce formatted output and save it in a file?

We will consolidate your Python knowledge
and learn about strings, files, and regular expressions

'''
from __future__ import division
import nltk,re,pprint

## Accessing text from the web and from Disk. ##
'''
Project Gutenberg appears in the NLTK corpus collection.
Catalog of 25,000 free online books at http://www.gutenberg.org/catalog/
Over 50 other languages.
including Catalan, Chinese, Dutch, Finnish, French, German, Italian, Portuguese, and Spanish

Text number 2554 is an English translation of Crime and Punishment, and we can accessit
'''

from urllib import urlopen
url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()
type(raw)
len(raw)
raw[:75]

'''
We want to break up the string into words and punctuation.
This step is called tokenization, and it produces our familiar structure.
'''

tokens = nltk.word_tokenize(raw)
type(tokens)
len(tokens)
tokens[:10]

#the regular list operations, such as slicing.
text = nltk.Text(tokens)
type(text)
text[1020:1060]
text.collocations()

#The find() and rfind() (“reverse find”) methods help us get the right index values to use for slicing the string.

raw.find("PART I")
raw.rfind("End of Project Gutenberg's Crime")
raw = raw[5303:1157681]
raw.find("PART I")

## Dealing with HTML

'''
Much of the text on the Web is in the form of HTML documents. You can use a web
browser to save a page as text to a local file.
Python to do the work directly.

Getting text out of HTML is a sufficiently common task that NLTK provides a helper
function nltk.clean_html(), which takes an HTML string and returns raw text. We
can then tokenize this to get our familiar text structure
'''
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html= urlopen(url).read()
html[:60]

raw = nltk.clean_html(html)
tokens = nltk.word_tokenize(raw)
tokens

tokens = tokens[96:399]
text = nltk.Text(tokens)
text

## Processing RSS Feeds

'''
The blogosphere is an important source of text, in both formal and informal registers.
With the help of a third-party Python library called the Universal Feed Parser, freely
downloadable from http://feedparser.org/, we can access the content of a blog.
'''

import feedparser

llog = feedparser.parse("http://languagelog.ldc.upenn.edu/null/?feed=atom")
llog['feed']['title']
len(llog.entries)

post = llog.entries[2]
post.title
content = post.content[0].value
content[:70]

nltk.word_tokenize(nltk.html_clean(content))
nltk.word_tokenize(nltk.clean_html(llog.entries[2].content[0].value))


## Reading Local Files ##

'''
In order to read a local file, we need to use Python’s built-in open() function, followed
by the read() method.

open('document.txt', 'rU'). 'r' means to open the file for reading (the default), and 'U' stands
for “Universal”, which lets us ignore the different conventions used for marking newlines.

The strip() method to remove the newline character at the end of the input line.


## Extracting Text from PDF, MSWord, and Other Binary Formats ##
ASCII text and HTML text are human-readable formats. Text often comes in binary
formats—such as PDF and MSWord—that can only be opened using specialized software.
Third-party libraries such as pypdf and pywin32 provide access to these formats.

'''

f = open('owncorpus/Where Data Science.txt')
raw = f.read()
print(raw)

f1 =open('owncorpus/Where Data Science.txt' ,'rU')
for line in f1:
    print(line.strip())




