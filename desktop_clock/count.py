# -*- coding: utf-8 -*-
"""
@author: dlnb5
"""
#正向计时！！！
from tkinter import *
import time

import main_window
class Count():
    def __init__(self):
        self.t=main_window.Time_window()
        self.t.root1.title("正向计时 by dlnb526")
        self.t.frame1 = Frame(self.t.root1,padx=50,pady=50)
        self.t.frame1.grid(row=0,column=0)
        self.t.button1 = Button(self.t.frame1,text='开始',command=self.start,padx=50,pady=5)
        self.t.button1.grid(row=0,column=0,padx=100,pady=50)
        self.color = 'black'
        self.t.button2 = Button(self.t.frame1,text='字体颜色',command=self.coloradj)
        self.t.button2.grid(row=0,column=1,padx=5,pady=5)
        mainloop()
    def coloradj(self):
        self.color=colorchooser.askcolor(title='来选择颜色呀！')
        self.color=self.color[1]
    def start(self):
        print("开始计时")
        self.t.button1.grid_forget()
        self.time1 = IntVar()
        self.time1.set(0)
        self.label1 = Label(self.t.frame1,textvariable=self.time1,font=("Arial", 100),fg=self.color)
        self.label1.grid(row=0,column=0,columnspan=2,padx=100,pady=50)
        self.time_refresh()
        
    def time_refresh(self):
        try:
            self.t.button1.grid_forget()
            self.t.button2.grid_forget()
            self.t.button3.grid_forget()
        except:
            pass
        self.t.button2 =Button(self.t.frame1,text = '停止计时',command = self.stop)
        self.t.button2.grid(row=1,column=0,columnspan=2,padx=100,pady=50)
        print(self.time1.get())
        self.time1.set(self.time1.get()+1)
        self.loop = self.label1.after(1000, self.time_refresh)
    def stop(self):
        print('停止计时')
        self.label1.after_cancel(self.loop)
        self.t.button2.grid_forget()
        self.t.button2 =Button(self.t.frame1,text = '继续计时',command = self.time_refresh)
        self.t.button2.grid(row=1,column=0,padx=30,pady=50)
        self.t.button3 =Button(self.t.frame1,text = '重新开始',command = self.time_restart)
        self.t.button3.grid(row=1,column=1,padx=30,pady=50)
    def time_restart(self):
        try:
            self.t.button2.grid_forget()
            self.t.button3.grid_forget()
        except:
            pass
        self.time1.set(-1)
        self.t.button2 =Button(self.t.frame1,text = '停止计时',command = self.stop)
        self.t.button2.grid(row=1,column=0,columnspan=2,padx=100,pady=50)
        self.time1.set(self.time1.get()+1)
        self.loop = self.label1.after(1000, self.time_refresh)
        