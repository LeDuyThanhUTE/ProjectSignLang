from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from subprocess32 import call
from PIL import Image, ImageFile

window = Tk()
window.title("Sign Language Translator")
window.geometry('405x500')


def start():
    window.destroy()
    call(['python', 'Project.py'])

def tutorial():
    messagebox.showinfo('Tutorial','Bấm P để quay lại menu, Esc để thoát')

def exit():
    window.destroy()


img1 = PhotoImage(file ='Image/Menu.png')

frame1= LabelFrame(window, text = 'SIGN LANGUAGE TRANSLATOR')
frame1.config(width=500,height=100)
frame1.grid(row=1, column=0)
frame2=Frame(window)
frame2.config(width=500,height=400)
frame2.grid(row=0,column=0)
canvas = Label(frame2,image=img1).grid(row=0,column=0)

btn1 = Button(frame1,text="Start",command = start).grid(column=0, row=0)
btn2 = Button(frame1,text="Tutorial",command = tutorial).grid(column=1, row=0)
btn3 = Button(frame1,text="Exit",command = exit).grid(column=2, row=0)


window.mainloop()