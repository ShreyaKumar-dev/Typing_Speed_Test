from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from time import * 
import random as r 
import io,os
import sys
from tkinter import messagebox

def inside():
    global choice
    choice = True
    
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error +1
    return error 
    
def out():
    win=Tk()
    win.title("Typing speed calculator")
    win.geometry("300x150")
    win.config(bg = 'lightgreen') 
    lab_text1 = Label(win, text = "Thank you !",font = ("Baskerville Old Face",20),
                    bg = 'lightgreen', fg = 'black', anchor="center")
    lab_text1.pack(pady=40)
    win.after(10000,lambda:win.destroy())
    global choice
    choice = False
    
def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_R = round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed)

def NewWin():
    root.destroy()
    choice = False
    top1 = Tk()
    top1.title("    Typing Speed Calculator")
    top1.geometry("520x400")
    top1.config(bg = 'cyan')  
    icon = os.path.join(sys.path[0],"calculator.ico")
    top1.iconbitmap(icon)

    # Heading
    Res = Label(top1, text = "RESULT!!", font = ("Baskerville Old Face",20),
                bg = 'cyan', fg = 'black', anchor="center")
    Res.pack(pady=40)

    Speed = Label(top1, text = "Speed:", font = ("Baskerville Old Face",20),
                bg = 'cyan', fg = 'black', anchor="w").place(x=50,y=100)
    user = name_var.get()
    a = speed_time(time_1,time_2,user)
    Speed_Res = Label(top1,text=a,font = ("Baskerville Old Face",20),
                    bg = 'cyan', fg = 'black', anchor="w").place(x=130,y=100)
    Speed_Res_Style = Label(top1,text="wpm",font = ("Baskerville Old Face",20),
                            bg = 'cyan', fg = 'black', anchor="w").place(x=160,y=100)

    Errors = Label(top1, text = "Errors:", font = ("Baskerville Old Face",20),
                bg = 'cyan', fg = 'black', anchor="w").place(x=50,y=160)
    Choice = Label(top1, text = "Do you want to try again?", font = ("Baskerville Old Face",20),
                bg = 'cyan', fg = 'black', anchor="w").place(x=150,y=220)
    b = mistake(test1,user)
    Errors_Res = Label(top1,text=b,font = ("Baskerville Old Face",20),
                    bg = 'cyan', fg = 'black', anchor="w").place(x=130,y=160)
    
    button1 = Button(top1, text="YES!", padx=30, pady=1, font = ("Bodoni MT",18), 
                    bg="cyan",highlightbackground="cyan" ,fg='black',command=inside)
    button1.pack()
    button1.place(x=60, y=280)
    
    button2 = Button(top1, text="NO", padx=30, pady=1, font = ("Bodoni MT",18), 
                    bg="cyan",highlightbackground="cyan" ,command=out)
    button2.pack()
    button2.place(x=340, y=280)
    top1.after(10000,lambda:top1.destroy())
    
    top1.grab_set()    

# 1st Basic Window
choice = True
while(choice == True):
    root = Tk()
    time_1 = time()
    messagebox.showinfo(title="Message", message='Do you want to start?')
    root.title("    Typing Speed Calculator")
    root.geometry("500x400")
    root.resizable(False,False)                    
    root.config(bg = 'blueviolet')  # For the background of window : Slategray1 : lavender
    icon = os.path.join(sys.path[0],"calculator.ico")
    root.iconbitmap(icon)    # For the icon

    # Heading
    lab_text = Label(root, text = "Check Your Typing Speed", font = ("Baskerville Old Face",20),
                    bg = 'blueviolet', fg = 'white', anchor="center")
    lab_text.pack(pady=40)

    # Random Sentence
    test = ["Please take your dog, Cali, out for a walk he really needs some exercise!",
            "What a beautiful day it is on the beach, here in beautiful and sunny Hawaii.",
            "Rex Quinfrey, a renowned scientist, created plans for an invisibility machine.",
            "Do you know why all those chemicals are so hazardous to the environment?",
            "I have three things to do today: wash my car, call my mother, and feed my dog."]
    test1 = r.choice(test)
    ran_txt = Label(root, text = test1, font = ("Goudy Old Style",12),bg="blueviolet", fg="white")
    ran_txt.pack()
    ran_txt.place(x=0.5, y=100, height=100, width=480)
    # ran_txt.place(x=50,y=100)

    # Enter Here direction
    lab_text = Label(root, text = "Enter Here ↓ ", font = ("Bodoni MT",15),bg = "blueviolet") 
    lab_text.pack()
    lab_text.place(x=195, y=200, height= 40, width=120)
    time_2 = time()

    # Input Box
    name_var = StringVar()    
    name_entry = Entry(root,textvariable = name_var, font=('calibre',10,'normal'))  
    name_entry.pack() 
    name_entry.place(x=50, y=250, height= 40, width=400) 

    # Done Button after the Input
    button = Button(root, text="DONE", padx=30, pady=1.5, font = ("Bodoni MT",18), 
                    bg="blueviolet",highlightbackground="blueviolet",command=NewWin)
    button.pack()
    button.place(x=165, y=325)
    root.mainloop()


