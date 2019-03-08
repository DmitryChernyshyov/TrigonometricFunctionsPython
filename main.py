# -*- coding: utf8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math
# my_package/__init__.py
#import numpy.core._dtype_ctypes
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from datetime import datetime
import time
class Root(Tk):
    global x
    x = np.linspace(-math.pi/2,5*math.pi/2,100)
    global m
    global y
    m = 5
    y = 0
    global a
    global ax
    global fig
    global y2
    fig = Figure(figsize=(6,4) , dpi=100)
    a = fig.add_subplot(111)
    ax = fig.gca()
    def __init__(self):
        super(Root, self).__init__()

        self.title("TrigonometricFunctions")
        self.minsize(600,400)
        self.create_widgets()
        self.matlotCanvas()

    def create_widgets(self):
        f_topmain = Frame()
        f_top = Frame(f_topmain)
        f_topsub = Frame(f_top)
        f_topsub2 = Frame(f_top)
        f_top2 = Frame(f_topmain)
        f_top2sub = Frame(f_topmain)
        f_top2sub2 = Frame(f_topmain)
        l1 = Label(f_topsub, width=5, height=1,  text="F(y)=  ")
        l1sub = Label(f_topsub, width=6, height=1,  text="K or A = ")
        l2 = Label(f_top2sub, width=4, height=1,  text="F(y)=  ")
        l1sub2 = Label(f_top2sub, width=6, height=1,  text="K or A = ")

        self.Button = tk.Button(f_topmain)
        self.Button["text"] = "Нарисовать"
        self.Button["command"] = self.draw
        self.Entry3 = Entry(f_topsub2)
        self.Entry = Entry(f_topsub2)
        self.Entry.pack(side = TOP)
        self.Entry2 = Entry(f_top2sub2)
        self.Entry4 = Entry(f_top2sub2)

        f_top2sub.pack(side= LEFT, padx=5, pady=5)
        f_top2sub2.pack(side= LEFT, padx=5, pady=5)
        f_topsub.pack(side= LEFT, padx=5, pady=5)
        f_topsub2.pack(side= LEFT, padx=5, pady=5)
        f_top.pack(side= LEFT, padx=5, pady=5)
        f_top2.pack(side= LEFT, padx=5, pady=5)
        self.Entry3.pack(side = TOP)
        self.Entry2.pack(side = TOP)
        self.Entry4.pack(side = TOP)
        self.Button.pack(side = RIGHT, padx=5, pady=5)

        l1.pack(side=TOP)
        l1sub.pack(side=TOP)
        l2.pack(side=TOP)
        l1sub2.pack(side=TOP)
        f_topmain.pack(side= TOP,padx=5, pady=5)
    def matlotCanvas(self):
        a.plot(-3.14/2, np.sin(-3.14/2), -3.14/2, np.cos(-3.14/2), marker = 'o')
        a.plot(0,1,1.7,1, marker = 'o')
        a.spines['left'].set_position('zero')
        a.spines['bottom'].set_position('zero')
        a.spines['top'].set_visible(False)
        a.spines['right'].set_visible(False)
        a.set_xlim(-2, 9)
        a.set_ylim(-1.4, 1.4)
        a.grid(ls='solid', lw=0.2)

        #anim = animation.FuncAnimation(fig, self.animate,  fargs=(), interval=20, repeat=False)
        global canvas
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().pack(side =TOP, fill = BOTH)
        toolbar = NavigationToolbar2TkAgg(canvas, self)


    def draw(self):
        a.cla()
        anim = ""
        a.plot(-3.14/2, np.sin(-3.14/2), -3.14/2, np.cos(-3.14/2), marker = 'o')
        a.plot(0,1,1.7,1, marker = 'o')
        a.spines['left'].set_position('zero')
        a.spines['bottom'].set_position('zero')
        a.spines['top'].set_visible(False)
        a.spines['right'].set_visible(False)
        a.set_xlim(-2, 9)
        a.set_ylim(-1.4, 1.4)
        a.grid(ls='solid', lw=0.2)
        global y2
        y = self.Entry.get()
        if y == "cos(x)":
            y = np.cos(x)
        elif y == "sin(x)":
            y = np.sin(x)
        elif y == "tan(x)":
            y = np.tan(x)
        elif y == "ctan(x)":
            y = -np.tan(x)
        elif y == "sin(|x|)":
            y = abs(np.sin(x))
        elif y == "cos(|x|)":
            y = abs(np.cos(x))
        elif y == "tan(|x|)":
            y = abs(np.tan(x))
        elif y == "ctan(|x|)":
            y = -abs(np.tan(x))
        elif y == "cos(x+a)":
            y = np.cos(x+k)
        elif y == "sin(x+a)":
            y = np.sin(x+k)
        elif y == "tan(x+a)":
            y = np.tan(x+k)
        elif y == "ctan(x+a)":
            y = -np.tan(x+k)
        elif y == "ctan(x)+a":
            y = -np.tan(x)+k
        elif y == "tan(x)+a":
            y = np.tan(x)+k
        elif y == "sin(x)+a":
            y = np.sin(x)+k
        elif y == "cos(x)+a":
            y = np.cos(x)+k
        elif y == "kcos(x)":
            y = k*np.cos(x)
        elif y == "ksin(x)":
            y = k*np.sin(x)
        elif y == "ktan(x)":
            y = k*np.tan(x)
        elif y == "kctan(x)":
            y = -k*np.tan(x)
        elif y == "cos(kx)":
            y = np.cos(k*x)
        elif y == "sin(kx)":
            y = np.sin(k*x)
        elif y == "tan(kx)":
            y = np.tan(k*x)
        elif y == "ctan(kx)":
            y = -np.tan(k*x)
        else:
            y = np.cos(x)


        y2 = self.Entry2.get()
        if y2 == "cos(x)":
            y2 = np.cos(x)
        elif y2 == "sin(x)":
            y2 = np.sin(x)
        elif y2 == "tan(x)":
            y2 = np.tan(x)
        elif y2 == "ctan(x)":
            y2 = -np.tan(x)
        elif y2 == "sin(|x|)":
            y2 = abs(np.sin(x))
        elif y2 == "cos(|x|)":
            y2 = abs(np.cos(x))
        elif y2 == "tan(|x|)":
            y2 = abs(np.tan(x))
        elif y2 == "ctan(|x|)":
            y2 = -abs(np.tan(x))
        elif y2 == "cos(x+a)":
            y2 = np.cos(x+k2)
        elif y2 == "sin(x+a)":
            y2 = np.sin(x+k2)
        elif y2 == "tan(x+a)":
            y2 = np.tan(x+k2)
        elif y2 == "ctan(x+a)":
            y2 = -np.tan(x+k2)
        elif y2 == "ctan(x)+a":
            y2 = -np.tan(x)+k2
        elif y2 == "tan(x)+a":
            y2 = np.tan(x)+k2
        elif y2 == "sin(x)+a":
            y2 = np.sin(x)+k2
        elif y2 == "cos(x)+a":
            y2 = np.cos(x)+k2
        elif y2 == "kcos(x)":
            y2 = k2*np.cos(x)
        elif y2 == "ksin(x)":
            y2 = k2*np.sin(x)
        elif y2 == "ktan(x)":
            y2 = k2*np.tan(x)
        elif y == "kctan(x)":
            y2 = -k2*np.tan(x)
        elif y2 == "cos(kx)":
            y2 = np.cos(k2*x)
        elif y2 == "sin(kx)":
            y2 = np.sin(k2*x)
        elif y2 == "tan(kx)":
            y2 = np.tan(k2*x)
        elif y == "ctan(kx)":
            y2 = -np.tan(k2*x)
        else:
            y2 = np.cos(x)
        line, = a.plot(x, y)

        anim = animation.FuncAnimation(fig, self.animate,
                                       interval=100, repeat=False)
        canvas.show()
    def animate(self,i,):

        line, = a.plot(x[:i*m], y2[:i*m], color='red', lw=1)

        #line, = a.pl ot(x[:i*m], y[:i*m], color='white', lw=2)
if __name__ == '__main__':
    root = Root()
    mainmenu = Menu(root)
    root.config(menu=mainmenu)
    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Открыть...")
    filemenu.add_command(label="Новый")
    filemenu.add_command(label="Сохранить...")
    filemenu.add_command(label="Выход")

    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="Помощь")
    helpmenu.add_command(label="О программе")

    mainmenu.add_cascade(label="Файл", menu=filemenu)
    mainmenu.add_cascade(label="Справка", menu=helpmenu)
    root.mainloop()
