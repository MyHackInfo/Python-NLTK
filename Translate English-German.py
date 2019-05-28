from nltk.corpus import swadesh
from tkinter import *

en2de = swadesh.entries(['en','de']) # English-German
translate = dict(en2de)

def translate_word():
    eng_word = english_word.get().lower()
    german_words = translate[eng_word]
    list1.insert(END,german_words)
    

window=Tk()
window.wm_title("Translater")

#Label for English Word and German word
l1 = Label(window,text="English Word")
l1.grid(row=1,column=0)

l2 = Label(window,text="German Word")
l2.grid(row=1,column=2)

#Entry text
english_word = StringVar()
e1 = Entry(window,textvariable=english_word)
e1.grid(row=1,column=1)

list1=Listbox(window,height=6,width=15)
list1.grid(row=2,column=3,columnspan=3)

#Button for Translate
b1 = Button(window,text="Translate",width=12,command=translate_word)
b1.grid(row=2,column=1,columnspan=2,rowspan=2)

# Main run command
window.mainloop()

