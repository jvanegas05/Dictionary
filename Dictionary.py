# import Required Library
from tkinter import *
from PyDictionary import PyDictionary
# Create objets
dictionary = PyDictionary( )
root = Tk( )
# set geometry
root.geometry("400x400")
def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonim.config(text=dictionary.antonym(word.get()))
# Add labels, Button and Frames
Label(root,text="Dictionary", font=("Helvetica 20 bold"), fg="Green").pack(pady=10)
# Frame 1
frame = Frame(root)
Label(frame, text="Type Word", font=("Helvetica 15 bold")).pack(side=LEFT)
word  = Entry (frame, font=("Helvetica 15 bold"))
word.pack( )
frame.pack(pady=10)
# Frame 2
framel = Frame (root)
Label(framel, text="Meaning:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
meaning = Label(framel, text="", font=( "Helvetica 10"))
meaning.pack()
frame1.pack(pady=10)
# Frame 3
frame2 = Frame (root)
Label(frame2, text="Synonym:-", font=("Helvetica 10 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Helvetica 10"))
synonym.pack()
frame2.pack(pady=10)
# Frame 4
frame3= Frame (root)
Label(frame3, text="Antonym:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font=("Helvetica 10"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)
Button(root, text="Submit", font=("Helvetica 15 bold"), command=dict).pack()
# Execute Tkinter
root.mainloop()
