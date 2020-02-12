# -*- coding: utf-8 -*-
"""
@author: dlnb5
"""
#选择功能
from tkinter import *
import reCount
import count
import show
import webbrowser
from tkinter import colorchooser
class Launcher():
    def __init__(self):
        
        #GUI设计
        self.root = Tk()
        self.root.title('Timer by dlnb526')
        
        #GUI设计-菜单部分
        self.menubar1 = Menu(self.root)
        self.menu1 = Menu()
        self.menu1.add_command(label='关于',command=self.about)
        self.menu1.add_command(label='更新',command=self.new_ver)
        self.menubar1.add_cascade(label="菜单", menu=self.menu1)
        self.menubar1.add_command(label='退出',command=self.root.destroy)
        
        self.root.config(menu=self.menubar1)
        
        #GUI设计-功能部分
        self.label1 = Label(self.root,text = '请选择您要实现的功能：',padx=10,pady=10)
        self.label1.grid(row = 0,column = 0)
        self.choicenum = IntVar()
        
        self.button1 = Radiobutton(self.root,text="正向计时",variable=self.choicenum,value=1).grid(row=0,column =1)
        self.button1 = Radiobutton(self.root,text="倒计时",variable=self.choicenum,value=2).grid(row=0,column =2)
        self.button1 = Radiobutton(self.root,text="系统时间",variable=self.choicenum,value=3).grid(row=0,column =3)
        self.button4 = Button(self.root,text='确定',command = self.choosed)
        self.button4.grid(row=1,column=3)
        mainloop()
    def new_ver(self):
        webbrowser.open('https://github.com/dlnb/python_exp/tree/master/desktop_clock')
    def about(self):
        print('点击了关于')
        self.top = Toplevel()
        self.top.title('关于')
        self.text = Text(self.top,width=50,height=30)
        self.text.grid(row=0,column=0)
        with open('ReadMe.txt',encoding='utf-8') as file1:
            self.content = file1.readlines()
            for lines in self.content:
                self.text.insert(END,lines)
    def choosed(self):
        print(self.choicenum.get())
        if self.choicenum.get()==1:
            print('您选择了正向计时')
            self.root.destroy()
            self.count=count.Count()
        if self.choicenum.get()==2:
            print('您选择了倒计时')
            self.root.destroy()
            self.recount=reCount.Recount()
        if self.choicenum.get()==3:
            print('您选择了系统时间')
            self.root.destroy()
            self.show=show.Show()
l = Launcher()