from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("butter"))
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("cacti"))

print(lemmatizer.lemmatize("butter",pos="a"))
print(lemmatizer.lemmatize("butter",pos="v"))
print(lemmatizer.lemmatize("butter",pos="n"))
print(lemmatizer.lemmatize("butter",pos="v"))
