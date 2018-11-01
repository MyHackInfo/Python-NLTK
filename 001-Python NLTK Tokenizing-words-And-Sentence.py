from nltk.tokenize import sent_tokenize,word_tokenize

example_text = "Hello Mr. Narsi , how are you doing today? The is some one that can help you. The car race you winng."

# sent_tokenize and word_tokenize use
print(sent_tokenize(example_text))
print(word_tokenize(example_text))

# We can use for loop to get all one by one
for i in word_tokenize(example_text):
    print("This is word_tokenize :",i)
