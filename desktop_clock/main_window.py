# -*- coding: utf-8 -*-
"""
@author: dlnb5
"""
#时间的窗口样式
from tkinter import *
from tkinter import colorchooser
class Time_window():
    def __init__(self):
        self.root1 = Tk()

         
        #GUI设计-菜单部分
        self.menubar1 = Menu(self.root1)
        self.menu1 = Menu()
        self.topVar = IntVar()
        self.menu1.add_checkbutton(label='置顶',command=self.to_top,variable=self.topVar)

        self.menubar1.add_cascade(label="置顶设置", menu=self.menu1)
        self.menubar1.add_command(label='窗口透明度',command=self.alpha)
        self.menubar1.add_command(label='退出',command=self.root1.destroy)
        self.root1.config(menu=self.menubar1)
    
    def to_top(self):
        if self.topVar.get()==1:
            self.root1.attributes("-topmost",True)
            print(self.topVar.get())
        if self.topVar.get()==0:
            self.root1.attributes("-topmost",False)
            print(self.topVar.get())
    
    def alpha(self):
        print('透明度')
        top1 = Tk()
        top1.title=('窗口透明度')
        top1.attributes("-topmost",True)
        msg = Label(top1,text="请滑动滑块调节透明度",padx=10,pady=10).grid(row=0,column=0)

        self.scale=Scale(top1,from_=0,to=1,resolution = 0.1,length=100,showvalue=False,orient=HORIZONTAL,\
                         sliderrelief=FLAT,command=self.alpha1).grid(row=1,column=0)
    def alpha1(self,pos):
        self.pos = pos
        self.num = 1-float(self.pos)
        self.root1.attributes("-alpha",self.num)
        

