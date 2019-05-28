
## Regular Expressions for detecting word patterns ##

'''
Regular expressions give us a more powerful and flexible method for describing
the character patterns we are interested in.

To use regular expressions in Python, we need to import the re library using: import re.
We also need a list of words to search; we’ll use the Words Corpus again

We will use the
re.search(p, s)
'''
import re
import nltk

wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

#print([w for w in wordlist if re.search('ed$',w)])     # end with ed

# # The caret symbol ^ matches the start of a string, just like the $ matches the end
#print([w for w in wordlist if re.search('^p..j..t..$',w)])
#print([w for w in wordlist if re.search('..j..t..',w)])

# # The ? symbol specifies that the previous character is optional. Thus «^e-?mail$» will match both email and e-mail
#print([w for w in wordlist if re.search('^e-?mail$',w)])

# # Ranges and Closures
###############################################
'''
The T9 system is used for entering text on mobile phones (see Figure 3-5). Two or more
words that are entered with the same sequence of keystrokes are known as
textonyms.

T9: Text on 9 keys.

The first part of the expression, «^[ghi]», matches the start of a word followed by g,
h, or i. The next part of the expression, «[mno]», constrains the second character to be m,
n, or o. The third and fourth characters are also constrained. Only four words satisfy
all these constraints.

We could have written «^[hig][nom][ljk][fed]$» and matched the same
words.
'''
print([w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)])

##################################################################################
'''
That + simply means “one or more instances of the preceding item,”

That * which means “zero or more instances of the preceding item.”

The ^ operator has another function when it appears as the first character inside square
brackets. For example, «[^aeiouAEIOU]» matches any character other than a vowel

'''
chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
print([w for w in chat_words if re.search('^m+i+n+e+$', w)])

print([w for w in chat_words if re.search('^[ha]+$', w)])

print([w for w in chat_words if re.search('^[^aeiouAEIOU]+$', w)])


wsj = sorted(set(nltk.corpus.treebank.words()))

print([w for w in wsj if re.search('^[0-9]+\.[0-9]+$', w)])    # '0.16'
print([w for w in wsj if re.search('^[A-Z]+\$$', w)])          # 'US$'
print([w for w in wsj if re.search('^[0-9]{4}$', w)])          # '1903'
print([w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)]) # '10-day', '10-year'
print([w for w in wsj if re.search('(ed|ing)$', w)])           # 'Absorbed','According'


##########################################################################
'''
Operator Behavior
.        Wildcard, matches any character
^        abc Matches some pattern abc at the start of a string
abc$     Matches some pattern abc at the end of a string
[abc]    Matches one of a set of characters
[A-Z0-9] Matches one of a range of characters
ed|ing|s Matches one of the specified strings (disjunction)
*        Zero or more of previous item, e.g., a*, [a-z]* (also known as Kleene Closure)
+        One or more of previous item, e.g., a+, [a-z]+
?        Zero or one of the previous item (i.e., optional), e.g., a?, [a-z]?
{n}      Exactly n repeats where n is a non-negative integer
{n,}     At least n repeats
{,n}     No more than n repeats
{m,n}    At least m and no more than n repeats
a(b|c)+  Parentheses that indicate the scope of the operators
'''

'''
To the Python interpreter, a regular expression is just like any other string. If the string
contains a backslash followed by particular characters, it will interpret these specially.
For example, \b would be interpreted as the backspace character. In general, when
using regular expressions containing backslash, we should instruct the interpreter not
to look inside the string at all, but simply to pass it directly to the re library for processing.
We do this by prefixing the string with the letter r, to indicate that it is a raw
string. For example, the raw string r'\band\b' contains two \b symbols that are
interpreted by the re library as matching word boundaries instead of backspace characters.
If you get into the habit of using r'...' for regular expressions—as we will do
from now on—you will avoid having to think about these complications.
'''

print("set:",[w for w in wsj if re.search(r'\band\b', w)])


###############################################
'''
# Useful Applications of Regular Expressions:


# Finding Word Stems ( in stems session )
# Extracting Word Pieces
The re.findall() (“find all”) method finds all (non-overlapping) matches of the given
regular expression.

'''
import re
import nltk
word = 'supercalifraglilisticexpppialidocionsuaseasiasoasuesiweaweiweoweu'
match = re.findall(r'[aeiou]',word)
match2 = re.findall(r'[aeiou]{2,}',word)
print(match2)
print(len(match2))
mt3 = nltk.FreqDist(match2)
print(mt3.items())
print(mt3.tabulate())


####################################






