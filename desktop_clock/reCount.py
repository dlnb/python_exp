# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:25:35 2020

@author: dlnb5
"""

#倒计时！！！
from tkinter import *
import time
import main_window
from tkinter import colorchooser
class Recount():
    def __init__(self):
        self.t=main_window.Time_window()
        self.t.root1.title("倒计时 by dlb526")
        self.inputtime()      
        mainloop()
    def inputtime(self):
        #倒计时--秒模式
        try:
            self.t.frame1.grid_forget()
        except:
            pass
        self.t.frame1 = Frame(self.t.root1,padx=30,pady=30)
        self.t.frame1.grid(row=0,column=0)
        self.t.label1 = Label(self.t.frame1,text='请输入定时时间',padx=50,pady=10)
        self.t.label1.grid(row=1,column=0)      
        self.t.entry1 = Entry(self.t.frame1,fg='red',justify='right',width=30,relief="flat",borderwidth=8)
        self.t.entry1.grid(row=2,column=0,padx=10,pady=10,sticky=N+S)
        self.t.label2 = Label(self.t.frame1,text='秒',padx=10,pady=10,anchor=W)
        self.t.label2.grid(row=2,column=1,sticky=W)   
        self.t.button1 = Button(self.t.frame1,text='确定',command=self.mode1,padx=50,pady=5)
        self.t.button1.grid(row=3,column=2,padx=5,pady=5)
        self.color='black'
        self.t.button2=Button(self.t.frame1,text='字体颜色',command=self.coloradj)
        self.t.button2.grid(row=2,column=2,padx=5,pady=5)
    def coloradj(self):
        self.color=colorchooser.askcolor(title='来选择颜色呀！')
        self.color=self.color[1]
    def mode1(self):
        print('选择了模式1')
        self.time1 = int(self.t.entry1.get())
        self.startCount()

    def startCount(self):

        self.t.label1.grid_forget()
        self.t.entry1.grid_forget()
        self.t.label2.grid_forget()
        self.t.button1.grid_forget()
        self.t.button2.grid_forget()
        self.t.frame1 = Frame(self.t.root1,padx=20,pady=50)
        self.t.frame1.grid(row=0,column=0)
        self.time2 = IntVar()
        self.time2.set(self.time1+1)
        self.t.label1 = Label(self.t.frame1,textvariable = self.time2,pady=10,font=("Arial", 100),fg = self.color)
        self.t.label1.grid(row=1,column=0)      
        self.time_refresh()
    def time_refresh(self):
        
        if self.time2.get()>0:
            
            if self.time2.get()<6:
                self.t.label1 = Label(self.t.frame1,textvariable = self.time2,pady=10,font=("Arial", 100),fg='red')
            self.time2.set(self.time2.get()-1)
            self.t.label1.after(1000, self.time_refresh)
        else:
            print('over')
            self.t.frame1.grid_forget()
            self.t.frame1 = Frame(self.t.root1,padx=50,pady=50)
            self.t.frame1.grid(row=0,column=0)
            self.t.label3=Label(self.t.frame1,text='计时结束！')
            print("\b")
            self.t.label3.grid(row=1,column=1)
            self.t.button3 = Button(self.t.frame1,text="重新计时",padx=10,pady=10,command=self.inputtime)
            self.t.button3.grid(row=2,column=1)
