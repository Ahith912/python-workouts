from gtts import gTTS
import os
from tkinter import *
root = Tk()
canvas = Canvas(root,width=500,height=500)
canvas.pack()

def texttospeech():
    text = entry.get()
    output = gTTS(text=text,lang="en",slow=False)
    output.save("output1.mp3")
    os.system("start output1.mp3")

entry = Entry(root)
canvas.create_window(200,150,window=entry)
button = Button(text="Go",command=texttospeech)
canvas.create_window(200,200,window=button)
root.mainloop()