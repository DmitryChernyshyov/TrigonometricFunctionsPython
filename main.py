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
    y = np.cos(x)
    m = 5
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
       # self.hi_there["command"] = self.Draw
        self.Entry = tk.Entry(self)
        self.Entry.pack(side="top")
        self.Entry2 = tk.Entry(self)
        self.Entry2.pack(side="top")
    def animate(self,i,):
       
        line, = a.plot(x[:i*m], y[:i*m], color='red', lw=1)
        line, = a.plot(x[:i*m], y[:i*m], color='white', lw=2)
    def matlotCanvas(self):
        y = np.cos(x)
        y2 = np.cos(x)

        line, = a.plot(x, np.sin(x))
        a.spines['left'].set_position('zero')
        a.spines['bottom'].set_position('zero')
        a.spines['top'].set_visible(False)
        a.spines['right'].set_visible(False)
        a.set_xlim(-2, 9)
        a.set_ylim(-1.4, 1.4)
        a.grid(ls='solid', lw=0.2)
        #line, = a.plot(x, np.sin(x))
        #anim = animation.FuncAnimation(fig, self.animate,  fargs=(), interval=20, repeat=False)


        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
        toolbar = NavigationToolbar2TkAgg(canvas, self)   
        anim = animation.FuncAnimation(fig, self.animate, fargs=(),
                                       interval=30, repeat=True)
        canvas.show()
if __name__ == '__main__':
    root = Root()
    root.mainloop()
