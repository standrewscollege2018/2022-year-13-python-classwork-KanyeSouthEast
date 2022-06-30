'''introduction to tkinter'''

#import tkinter
from tkinter import *


def say_hello():
    if message.get() =="Hello there!":
        message.set("") 
    else:
        message.set("Hello there!")
    

def print_input():
    message.set(input_field.get())
#setup the root window
root = Tk()
root.title("My first Tkinter GUI")
root.resizable(width=False, height=False)
root.geometry("800x500")
#root.configure(bg="red")

#add a label
heading_lbl = Label(root, text="a great GUI", fg="red", font=("Comic Sans MS", 25))
heading_lbl.grid(row=0, column=0)

#set up lavel to display hello fromsay_hello function
#set up a StringVar to store the text for the label
message = StringVar()
message_lbl = Label(root, textvariable=message, fg="magenta", font=("Comic Sans MS", 100))
message_lbl.grid(row=1, column=1)
#add button
pushme_btn = Button(root,text="push me daddy",width=40, height=1, command=say_hello)
pushme_btn.grid(row=1, column=0)

#get user input from entry field

get_btn = Button(root,text="Get input",width=40, height=5, command=print_input)
get_btn.grid(row=1, column=0)

input_field = Entry(root)
input_field.grid(row=2, column=0)

#start the program by running the GUI
root.mainloop()

