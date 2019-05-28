## Strings Text Processing at the Lowest Level ##

'''
It’s time to study a fundamental data type that we’ve been studiously avoiding so far.
In earlier we focused on a text as a list of words. We didn’t look too closely
at words and how they are handled in the programming language. By using NLTK’s
corpus interface we were able to ignore the files that these texts had come from. The
contents of a word, and of a file, are represented by programming languages as a fundamental
data type known as a string.

We explore strings in detail, and
show the connection between strings, words, texts, and files.
'''

# Basic Operations with Strings

'''
Strings are specified using single quotes<-1 or double quotes<-2 , as shown in the following
code example. If a string contains a single quote, we must backslash-escape the
quote<-3 so Python knows a literal quote character is intended, or else put the string in
double quotes<-2 . Otherwise, the quote inside the string<-4 will be interpreted as a close
quote, and the Python interpreter will report a syntax error:
'''

Name = 'narsi ' # <-1
print(Name)

fullname = "Narsi Gurjar with python's code" # <-2
print(fullname)

fullname1 = 'Narsi gurjar with python\'s code' # <-3
print(fullname1)

error = 'narsi gurjar with python\'s code' # <-4 without \
print(error)

'''
We need to use backslash or parentheses so that the interpreter knows that the
statement is not complete after the first line.
\ backslash
()parentheses

Unfortunately these methods do not give us a newline between the two lines of the
sonnet. Instead, we can use a triple-quoted string.

"""  triple quoted.

'''

cup = " We need to use backslash or parentheses"\
      "Instead, we can use a triple-quoted string:"
print("using \ backslash",cup)

up = (" We need to use backslash or parentheses"
      "Instead, we can use a triple-quoted string:")
print("using () ",up)

down="""We need to use backslash or parentheses
      Instead, we can use a triple-quoted string """

print("using triple-quoted",down)


# First let’s look at the + operation, known as concatenation

print('very'+'very'+'hot')
print('very'* 3)
#print('very'/ 3)
#print('very'- 3)

# Accessing Individual Characters
'''
1->for lists, strings are indexed, starting from zero. When we
index a string, we get one of its characters (or letters). A single character is nothing
special—it’s just a string of length 1.

2->where -1 is the index of the last character

3->We can write for loops to iterate over the characters in strings. This print statement
ends with a trailing comma, which is how we tell Python not to print a newline at the
end.
'''
print(cup[2])
#print(cup[200]) out of range give error.
print(cup[-2])
print(cup[-1])

for char in cup:
    print(list([[char]]),)


'''
We can count individual characters as well. We should ignore the case distinction by
normalizing everything to lowercase, and filter out non-alphabetic characters.
'''
import nltk
from nltk.corpus import gutenberg
raw = gutenberg.raw('melville-moby_dick.txt')
fdist= nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
print(fdist.keys())

'''
Method Functionality
s.find(t)       Index of first instance of string t inside s (-1 if not found)
s.rfind(t)      Index of last instance of string t inside s (-1 if not found)
s.index(t)      Like s.find(t), except it raises ValueError if not found
s.rindex(t)     Like s.rfind(t), except it raises ValueError if not found
s.join(text)    Combine the words of the text into a string using s as the glue
s.split(t)      Split s into a list wherever a t is found (whitespace by default)
s.splitlines()  Split s into a list of strings, one per line
s.lower()       A lowercased version of the string s
s.upper()       An uppercased version of the string s
s.titlecase()   A titlecased version of the string s
s.strip()       A copy of s without leading or trailing whitespace
s.replace(t, u) Replace instances of t with u inside s
'''






