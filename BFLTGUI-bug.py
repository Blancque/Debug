from tkinter import *

root = Tk()
root.title("Test")
root.geometry("300x300")
input_box = Entry (root, width=20, bg="light grey")
input_box.grid(row=0, column=0, sticky=E)
Button(root, text="Translate!", command=translate(phrase).grid(row=1, column=0, sticky=W)
output_box = Text (root, text = translation, width=20, height=5, bg="light grey")
output.grid(row=2, column=0, sticky= W)

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "a" :
            translation = translation + "os"
        elif letter.lower() in "e" :
            translation = translation + "rek"
        elif letter.lower() in "i" :
            translation = translation + "ve"
        elif letter.lower() in "o" :
            translation = translation + "aya"
        elif letter.lower() in "u" :
            translation = translation + "per"
            #constonats
        elif letter.lower() in "b":
            translation = translation + "meh"
        elif letter.lower() in "c":
            translation = translation + "lu"
        elif letter.lower() in "d":
            translation = translation + "ith"
        elif letter.lower() in "f":
            translation = translation + "av"
        elif letter.lower() in "g":
            translation = translation + "en"
        elif letter.lower() in "h":
            translation = translation + "ti"
        elif letter.lower() in "j":
            translation = translation + "lie"
        elif letter.lower() in "k":
            translation = translation + "el"
        elif letter.lower() in "l":
            translation = translation + "au"
        elif letter.lower() in "m":
            translation = translation + "eth"
        elif letter.lower() in "n":
            translation = translation + "leh"
        elif letter.lower() in "p":
            translation = translation + "gli"
        elif letter.lower() in "q":
            translation = translation + "ke"
        elif letter.lower() in "r":
            translation = translation + "uld"
        elif letter.lower() in "s":
            translation = translation + "vri"
        elif letter.lower() in "t":
            translation = translation + "lux"
        elif letter.lower() in "v":
            translation = translation + "nie"
        elif letter.lower() in "w":
            translation = translation + "gla"
        elif letter.lower() in "x":
            translation = translation + "oth"
        elif letter.lower() in "y":
            translation = translation + "ne"
        elif letter.lower() in "z":
            translation = translation + "gu"
        else:
            translation = translation + letter

    return translation

translate()

root.mainloop()
