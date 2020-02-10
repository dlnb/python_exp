# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:09:39 2020

@author: dlnb5
"""
#账单主程序
from books_register import Login
from tkinter import *
import time
import json
from history_list import Historylist
import tkinter.filedialog
class MoneyBook():
    def __init__(self):
        login = Login()
        judge1 = 0
        try:
            self.Total = 0
            self.data = login.data1
            self.username = login.user_name
            print('您好：%s,欢迎使用账本！控制台将显示您的操作历史'%self.username)
            print('当前余额：%.2f'%self.data[-1]["Total"])
            self.Total = self.data[-1]["Total"]
            judge1 = 1

        except:
            print('处理错误,请重新注册！')
        if judge1 == 1:  
            self.bookGui()
    #检测输入框里是否输入数字
    
    def inputwindow(self,select):
        print('%s'%select)
        self.labelframe2.grid_forget()
        self.labelframe2 = LabelFrame(self.root,text='%s'%select,labelanchor=N,padx=80,pady=50)
        self.labelframe2.grid(row=1,column=1,padx=5,pady=10)
        self.label_item = Label(self.labelframe2,text = '%s项目：'%select,padx=5,pady=5)
        self.label_item.grid(row=2,column=1)
        self.label_price = Label(self.labelframe2,text = '金额：',padx=5,pady=5)
        self.label_price.grid(row=3,column=1)
        self.entry_item = Entry(self.labelframe2)
        self.entry_item.grid(row=2,column=2,padx=10,pady=5)
        self.entry_price = Entry(self.labelframe2)
        self.entry_price.grid(row=3,column=2,padx=10,pady=5)
        self.savebutton =Button(self.labelframe2,text='保存',command = self.save)
        self.savebutton.grid(row=4, column=3)
        
    def income(self):
        self.inputwindow('收入')
        self.choice = 1
    def outcome(self):
        self.inputwindow('支出') 
        self.choice = 2
   #保存数据
    def save(self):
        if self.choice == 1:
            print('正在执行保存收入操作')

            
            try:
                self.price_input = self.entry_price.get()
                self.item = self.entry_item.get()
                self.price_input=float(self.price_input)
                self.atime=time.localtime()
                self.timstr='%d%02d%02d%02d%02d%02d'%(self.atime[0],self.atime[1],self.atime[2],self.atime[3],self.atime[4],self.atime[5])
                print('-------当前时间为：%s-------'%self.timstr)
                self.Total = self.Total + self.price_input
                self.dict_temp = {"Time":self.timstr,"Item":self.item,"Exp":self.price_input,"Total":self.Total}

                self.data.append(self.dict_temp)
                with open('user_data\%s_file.json'%self.username,'w', encoding='utf-8') as file2:
                    json.dump(self.data, file2, indent=4)
                self.label3.grid_forget()
                self.label3 = Label(self.root,text='%02d:%02d:%02d  保存成功！收入%.2f元，余额%.2f元'%(self.atime[3],self.atime[4],self.atime[5],self.price_input,self.Total),padx=5)
                self.label3.grid(row =4,column=1,padx=5,pady=1)                
            except:
                print('输入有误！')
                self.label3.grid_forget()
                self.label3 = Label(self.root,text='金额处请输入数字！',padx=5,fg='red')
                self.label3.grid(row =4,column=1,padx=5,pady=1)    
        elif self.choice == 2:
            print('正在执行保存支出')
            try:
                self.price_input = self.entry_price.get()
                self.item = self.entry_item.get()
                self.price_input=-float(self.price_input)
                self.atime=time.localtime()
                self.timstr='%d%02d%02d%02d%02d%02d'%(self.atime[0],self.atime[1],self.atime[2],self.atime[3],self.atime[4],self.atime[5])
                print('-------当前时间为：%s-------'%self.timstr)
                self.Total = self.Total + self.price_input
                self.dict_temp = {"Time":self.timstr,"Item":self.item,"Exp":self.price_input,"Total":self.Total}
                self.data.append(self.dict_temp)
                with open('user_data\%s_file.json'%self.username,'w', encoding='utf-8') as file2:
                    json.dump(self.data, file2, indent=4)
                self.label3.grid_forget()
                self.label3 = Label(self.root,text='%02d:%02d:%02d  保存成功！支出%.2f元，余额%.2f元'%(self.atime[3],self.atime[4],self.atime[5],-self.price_input,self.Total),padx=5)
                self.label3.grid(row =4,column=1,padx=5,pady=1) 
            except:
                print('输入有误！')
                self.label3.grid_forget()
                self.label3 = Label(self.root,text='金额处请输入数字！',padx=5,fg='red')
                self.label3.grid(row =4,column=1,padx=5,pady=1)   
    def history(self):
        Historylist(self.username)
        #设计账本的图形界面
    def bookGui(self):
        self.root = Tk()
        self.root.title('%s的账本 by dlnb526'%self.username)
   
        self.labelframe1 = LabelFrame(self.root,text="记录",labelanchor=N,padx=30,pady=20)
        self.labelframe1.grid(row=1,column=0,padx=5,pady=10)
        self.button1 = Button(self.labelframe1,text='收入',command = self.income)
        self.button1.grid(row=2,column=0,padx=5,pady=10)
        self.button2 = Button(self.labelframe1,text='支出',command=self.outcome)
        self.button2.grid(row=3,column=0,padx=5,pady=10)        
        self.labelframe2 = LabelFrame(self.root,text="请选择",labelanchor=N,padx=80,pady=50)
        self.labelframe2.grid(row=1,column=1,padx=5,pady=10)
        self.label2 = Label(self.labelframe2,text='请在左侧选择内容',padx=20,pady=20)
        self.label2.grid(row=1,column=4,padx=5,pady=5)
        self.result=StringVar()
        self.result.set('当前总计余额%.2f'%self.Total)
        self.label3 = Label(self.root,textvariable=self.result,padx=5)
        self.label3.grid(row =4,column=1,padx=5,pady=1)
        self.button3 = Button(self.root,text='查看历史账单',command=self.history)
        self.button3.grid(row =5,column=1,padx=5,pady=5)
        mainloop()
        

        
moneybook = MoneyBook()