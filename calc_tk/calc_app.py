#===============================
#imports
#===============================

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import all_feature
from tkinter import Menu

class app(tk.Frame):
    def __init__(self, win):
        super().__init__(win, width=40, height=50, relief= tk.SUNKEN)
        self.grid(row=0, padx=2, pady=2)
        self.main_gui()
        self.history_gui()

    def main_gui(self):
        self.cal_box = tk.StringVar()
        cb = ttk.Entry(self, width=28, textvariable=self.cal_box, font=10)
        cb.grid(row=0, column=0, sticky = tk.E)
        cb.focus() #place cursor on the cb object which is entry widget 

        w = tk.Frame()
        cb.grid(row=0, column=0, sticky=tk.W)

        r=0
        button_byx = ttk.Button(w, text="1/x")  # clicking button creates event
        button_byx.grid(row = r, column=0, sticky=tk.W)
        button_byx.bind('<Button>', lambda event: all_feature.num_by_rev(self, event))

        button_8 = ttk.Button(w, text="X^2")
        button_8.grid(row = r, column=1, sticky=tk.W)
        button_8.bind('<Button>', lambda event: all_feature.num_power(self, event))

        button_9 = ttk.Button(w, text="sqrt")
        button_9.grid(row = r, column=2, sticky=tk.W)
        button_9.bind('<Button>', lambda event: all_feature.square_root(self, event))

        button_x = ttk.Button(w, text="÷")
        button_x.grid(row = r, column=3, sticky=tk.W)
        button_x.bind('<Button>', lambda event: all_feature.press_num(self, event, '*'))

        r=1
        button_7 = ttk.Button(w, text="7")
        button_7.grid(row = r, column=0,sticky = tk.W)
        button_7.bind('<Button>', lambda event:all_feature.press_num(self, event, '7')) #widget.bind(event, handler)

        button_8 = ttk.Button(w, text="8")
        button_8.grid(row = r, column=1, sticky = tk.W)
        button_8.bind('<Button>', lambda event: all_feature.press_num(self, event, '8'))

        button_9 = ttk.Button(w, text="9")
        button_9.grid(row = r, column=2, sticky = tk.W)
        button_9.bind('<Button>', lambda event: all_feature.press_num(self, event, '9'))

        button_x = ttk.Button(w, text="x")
        button_x.grid(row = r, column=3, sticky=tk.W)
        button_x.bind('<Button>', lambda event: all_feature.press_num(self, event, '*'))

        r=2
        button_4 = ttk.Button(w, text="4")
        button_4.grid(row = r, column=0, sticky = tk.W)
        button_4.bind('<Button>', lambda event: all_feature.press_num(self, event, '4'))

        button_5 = ttk.Button(w, text="5")
        button_5.grid(row = r, column=1, sticky = tk.W)
        button_5.bind('<Button>', lambda event: all_feature.press_num(self, event, '5'))

        button_6 = ttk.Button(w, text="6")
        button_6.grid(row = r, column=2, sticky=tk.W)
        button_6.bind('<Button>', lambda event: all_feature.press_num(self, event, '6'))

        button_m = ttk.Button(w, text="-")
        button_m.grid(row = r, column=3, sticky=tk.W)
        button_m.bind('<Button>', lambda event: all_feature.press_num(self, event, '-'))

        r=3
        button_1 = ttk.Button(w, text="1")
        button_1.grid(row = r, column=0, sticky=tk.W)
        button_1.bind('<Button>', lambda event: all_feature.press_num(self, event, '1'))

        button_2 = ttk.Button(w, text="2")
        button_2.grid(row = r, column=1, sticky=tk.W)
        button_2.bind('<Button>', lambda event: all_feature.press_num(self, event, '2'))

        button_3 = ttk.Button(w, text="3")
        button_3.grid(row = r, column=2, sticky=tk.W)
        button_3.bind('<Button>', lambda event: all_feature.press_num(self, event, '3'))

        button_p = ttk.Button(w, text="+")
        button_p.grid(row = r, column=3, sticky=tk.W)
        button_p.bind('<Button>', lambda event: all_feature.press_num(self, event, '+'))

        r=4
        button_0 = ttk.Button(w, text="0")
        button_0.grid(row = r, column=0, sticky=tk.W)
        button_0.bind('<Button>', lambda event: all_feature.press_num(self, event, '0'))

        button_pt = ttk.Button(w, text=".")
        button_pt.grid(row = r, column=1, sticky=tk.W)
        button_pt.bind('<Button>', lambda event: all_feature.press_num(self, event, '.'))

        button_c = ttk.Button(w, text="clear")
        button_c.grid(row = r, column=2, sticky=tk.W)
        button_c.bind('<Button>', lambda event: all_feature.clear(self, event))

        button_eq = ttk.Button(w, text="=")
        button_eq.grid(row = r, column=3, sticky=tk.W)
        button_eq.bind('<Button>', lambda event: all_feature.evaluate(self, event))

        w.grid(row=1, column=0, pady=2, padx=2, sticky = tk.W)

    def history_gui(self):
        h = tk.Frame()
        scrol_h = 3
        scrol_w = 33
        scr = scrolledtext.ScrolledText(self, width = scrol_w, height = scrol_h, wrap = tk.WORD)
       # scr.grid(column = 0, columnspan =1 , sticky = tk.W)

if __name__ == "__main__":
    win = tk.Tk()
    win.configure(background="light gray")
    win.title("Calculator")
    win.resizable(False, False)
    gui = app(win)
    
    win.mainloop()

