#===============================
#imports
#===============================

import tkinter as tk
#from . import all_feature
from tkinter import *
from tkinter import ttk
#create tk instance
win = tk.Tk()
#Add title
win.title("Calculator")

top_frame = ttk.Frame(win, width=50, height=50, relief=SUNKEN)
top_frame.grid(row = 0,column = 0, padx=10, pady=10)

bottom_frame = ttk.Frame(win, width=50, height=500, relief=SUNKEN)
bottom_frame.grid(row =1, column =0, padx=10, pady=10)


cal_box = StringVar()
cb = Entry(top_frame, width =24, textvariable = cal_box, font =10)
cb.grid(row =0 , column=0)
cal_box.set("0")

def get_7():
    cal_sel = cal_box.get()
    if cal_sel == "0":
        cal_box.set("7")
    else:
        cal_sel += "7"
        cal_box.set(cal_sel)

def get_c():
    cal_box.set("0")

def get_8():
    cal_box.set("8")

def get_9():
    cal_box.set("9")

def get_x():
    cal_box.set("x")

def get_4():
    cal_box.set("4")

def get_eq():
    cal_sel = cal_box.get()
    res = eval(cal_sel)
    cal_box.set(res)
#add all label
action_pc = Button(bottom_frame, text = "%", command = get_7, height = 2, width = 4, bg='white', fg='black')
action_pc.grid(row =0,column =0)

action_ce = Button(bottom_frame, text = "CE", command = get_8 , height = 2, width = 4)
action_ce.grid(row =0,column =1)

action_c = Button(bottom_frame, text = "C", command = get_c , height = 2, width = 4)
action_c.grid(row =0,column =2)

action_x = Button(bottom_frame, text = "ꓫ", command = get_x , height = 2, width = 4)
action_x.grid(row =0,column =3)


#add all label
action_7 = Button(bottom_frame, text = "7", command = get_7, height = 2, width = 4, bg='white', fg='black')
action_7.grid(row =1,column =0)

action_8 = Button(bottom_frame, text = "8", command = get_8 , height = 2, width = 4)
action_8.grid(row =1,column =1)

action_9 = Button(bottom_frame, text = "9", command = get_9 , height = 2, width = 4)
action_9.grid(row =1,column =2)

action_x = Button(bottom_frame, text = "ꓫ", command = get_x , height = 2, width = 4)
action_x.grid(row =1,column =3)


action_4 = Button(bottom_frame, text = "4", command = get_4, height = 2, width = 4, bg='white', fg='black')
action_4.grid(row =2,column =0)
action_eq = Button(bottom_frame, text = "=", command = get_eq, height = 2, width = 4, bg='white', fg='black')
action_eq.grid(row =2,column =4)
#===============================
#Start GUI
#===============================
win.mainloop()