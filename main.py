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
        self.Button = tk.Button(self)
        self.Button["text"] = "Нарисовать"
        self.Button.pack(side="top")
        self.Button["command"] = self.draw
        self.Entry = tk.Entry(self)
        self.Entry.pack(side="top")
        self.Entry2 = tk.Entry(self)
        self.Entry2.pack(side="top")

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
        canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
        toolbar = NavigationToolbar2TkAgg(canvas, self)   


    def draw(self):
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
        y2 = self.Entry2.get()
        if y2 == "cos(x)":
            y2= np.cos(x)
        elif y2 == "sin(x)":
            y2 = np.sin(x)
        elif y2 == "tan(x)":
            y2 = np.tan(x)
        elif y2 == "ctan(x)":
            y2 = -np.tan(x)
        line, = a.plot(x, y)

        anim = animation.FuncAnimation(fig, self.animate,
                                       interval=100, repeat=False)
        canvas.show()
    def animate(self,i,):
        
        line, = a.plot(x[:i*m], y2[:i*m], color='red', lw=1)
        #line, = a.pl ot(x[:i*m], y[:i*m], color='white', lw=2)
if __name__ == '__main__':
    root = Root()
    root.mainloop()
