from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

exam = "Hey my name is narsi and i go to the python nltk field."
stop_words =set(stopwords.words('english'))

words = word_tokenize(exam)

# filtered_sent = []
# for w in words:
#     if w not in stop_words:
#         filtered_sent.append(w)

filtered_sent = [w for w in words if not w in stop_words]

print(filtered_sent)
