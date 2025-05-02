from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
from project_01_talking_dictionary_app_part_1 import enterwordentry,textarea


# get_close_matches(word,possibilities,n,cutoff)
# close_match=get_close_matches('appel',['ape','appel','peach','puppy'],n=3,cutoff=0.6) #0.0-1.0
# print(close_match)
########functionality part

def search():

    data = json.load(open('E:/python projects/talking_dictionay_project/dictionary.json'))

    word = enterwordentry.get()

    word = word.lower()
    if word in data:

        meaning=data[word]

        textarea.delete(1.0,END)

        for item in meaning:

            textarea.insert(END,u'\u2022'+item+'\n\n')

    elif len(get_close_matches(word,data.keys()))>0:

        close_match=get_close_matches(word,data.keys())[0]

        res=messagebox.askyesno('Confirm',f'Did you mean {close_match} instead?')
        if res == True: 

            enterwordentry.delete(0,END)

            enterwordentry.insert(END,close_match)


            meaning=data[close_match]
            
            textarea.delete(1.0,END)    

            for item in meaning:

                
                textarea.insert(END,u'\u2022' + item + '\n\n')
        else:

            messagebox.showerror('Error','The word doesnt exist, Please double check it.')
            enterwordentry.delete(0,END)
            textarea.delete(1.0,END)

    else:
        
        messagebox.showinfo('Information','The word doesnt exist.')
        enterwordentry.delete(0,END)
        textarea.delete(1.0,END)
    



