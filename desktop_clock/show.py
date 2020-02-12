# -*- coding: utf-8 -*-
"""
@author: dlnb5
"""
#当前时间
from tkinter import *
import time
import main_window

class Show():
    def __init__(self):
        self.t=main_window.Time_window()
        self.t.root1.title("当前时间 by dlnb526")
        self.t.menubar1.add_command(label='字体颜色',command=self.coloradj)
        self.t.frame1 = Frame(self.t.root1,padx=50,pady=50)
        self.t.frame1.grid(row=0,column=0)
        self.color='black'
        self.time1 = StringVar()
        self.time1.set('%02d:%02d:%02d'%(time.localtime()[3],time.localtime()[4],time.localtime()[5]))
        self.t.label1 = Label(self.t.frame1,textvariable=self.time1,font=("Arial", 100))
        self.t.label1.grid(row=0,column=0,padx=10,pady=10)
        self.time_refresh()
        mainloop()
    def time_refresh(self):
            self.t.label1 = Label(self.t.frame1,textvariable=self.time1,font=("Arial", 100),fg=self.color)
            self.t.label1.grid(row=0,column=0,padx=10,pady=10)
            self.time1.set('%02d:%02d:%02d'%(time.localtime()[3],time.localtime()[4],time.localtime()[5]))

            self.loop = self.t.label1.after(1000, self.time_refresh)
    def coloradj(self):
        self.color=colorchooser.askcolor(title='来选择颜色呀！')
        self.color=self.color[1]
