# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:14:34 2020

@author: dlnb5
"""
#利用tkinter实现登陆程序界面for账单
from tkinter import *
import tkinter.messagebox
import webbrowser
import pickle
import os
import os.path
import json

class Login:
    def __init__(self): 
        print('您已载入登陆程序')
        #首先进行相关文件处理
        if os.path.exists('User_dict.pkl'):
            file1 = open('User_dict.pkl','rb')
            self.temp_dict = pickle.load(file1)
            file1.close()
        elif not os.path.exists('User_dict.pkl'):
            self.temp_dict={'username':'password'}
            file1 = open('User_dict.pkl','wb')
            pickle.dump(self.temp_dict,file1)
            file1.close()
        self.judgeframe3 = 0

        #然后生成图形界面
        self.root = Tk()
        self.root.title('登陆 by dlnb526')
        self.labelframe1 = LabelFrame(self.root,text='欢迎！',padx=5,pady=5,\
                                 labelanchor = N)
        
        self.labelframe1.grid(row=0,column=0,padx=10,pady=10)
        self.label1 = Label(self.labelframe1,text = "欢迎来到本程序!\n注意本程序密码明文保存，注意隐私安全",padx=5,pady=5)
        self.label1.grid(row = 0,column=0,padx=5,pady=5)
        self.anoutME = Button(self.labelframe1,text = '关于我',command = self.about_me)
        self.anoutME.grid(row=1,column=1)
        
        self.labelframe2 = LabelFrame(self.root,text="登录程序",padx=30,pady=30)
        self.labelframe2.grid(row=0,column=1,padx=10,pady=10)
        self.label2 = Label(self.labelframe2,text = "这是一个登录程序的演示!",padx=5,pady=5)
        self.label2.grid(row = 0,column=1,padx=5,pady=5)
        self.button1 = Button(self.labelframe2,text = '新建账户',command = self.newAccount)
        self.button1.grid(row=1,column=1)
        self.button2 = Button(self.labelframe2,text = '已有帐户登录',command = self.hadAccount)
        self.button2.grid(row=1,column=2)
        mainloop()
        
#---------------------------------新建账户后的行为----------------------------------------
    def newAccount(self):
        self.creatAccount()
    def creatAccount(self): 
        if self.judgeframe3 == 1:
            self.labelframe3.grid_forget()
            self.judgeframe3 = 0
        self.labelframe3 = LabelFrame(self.root,text="注册登录",padx=30,pady=30)
        self.labelframe3.grid(row=2,column=1,padx=10,pady=10)
        self.judgeframe3 = 1
        self.label_username = Label(self.labelframe3,text = '用户名：',padx=5,pady=5)
        self.label_username.grid(row=2,column=1)
        self.label_password1 = Label(self.labelframe3,text = '请输入密码：',padx=5,pady=5)
        self.label_password1.grid(row=3,column=1)
        self.label_password2 = Label(self.labelframe3,text = '请再次输入密码：',padx=5,pady=5)
        self.label_password2.grid(row=4,column=1)

        self.entry_username = Entry(self.labelframe3)
        self.entry_username.grid(row=2,column=2,padx=10,pady=5)
        self.entry_password1 = Entry(self.labelframe3,show='*')
        self.entry_password1.grid(row=3,column=2,padx=10,pady=5)
        self.entry_password2 = Entry(self.labelframe3,show='*')
        self.entry_password2.grid(row=4,column=2,padx=10,pady=5)
        self.regist_button = Button(self.labelframe3,text = '注册',command = self.regist_new_Account)
        self.regist_button.grid(row=5,column=2,padx=10,pady=5)

    #点击注册后的行为
    def regist_new_Account(self):
        
        self.user_name = self.entry_username.get()
        self.password1 = self.entry_password1.get()
        self.password2 = self.entry_password2.get()
        if self.user_name in self.temp_dict:
            self.label3 = Label(self.labelframe3,text = "账号已存在",padx=5,pady=5,fg='red')
            self.label3.grid(row = 5,column=1,padx=5,pady=5)
        else:
            if self.password1==self.password2:
                self.password = self.password1
                if  self.password:
                    self.dict1 = {self.user_name:self.password}
                    self.temp_dict.update(self.dict1)
                    file1 = open('User_dict.pkl','wb')
                    pickle.dump(self.temp_dict,file1)
                    file1.close()
                    self.file_creat()
                    self.label3 = Label(self.labelframe3,text = "注册成功！\n请返回登陆",padx=5,pady=5,fg='red')
                    self.label3.grid(row = 5,column=1,padx=5,pady=5)
                else:
                    self.label3 = Label(self.labelframe3,text = "密码不能为空！",padx=5,pady=5,fg='red')
                    self.label3.grid(row = 5,column=1,padx=5,pady=5)
                    
            else:
                self.label3 = Label(self.labelframe3,text = "前后两次密码输入不一致",padx=5,pady=5,fg='red')
                self.label3.grid(row = 5,column=1,padx=5,pady=5)
    def file_creat(self):
        if os.path.exists('user_data'):

            dict_list = [{"Total":0,"Time": '00000000000000',"Item":'BLANK',"Exp":0}]

            with open('user_data\%s_file.json'%self.user_name,'w', encoding='utf-8') as file2:
                json.dump(dict_list, file2, indent=4)
                
                
        if not os.path.exists('user_data'):
            os.mkdir('user_data')
            dict_list = [{"Total":0,"Time": '00000000000000',"Item":'BLANK',"Exp":0}]

            with open('user_data\%s_file.json'%self.user_name,'w', encoding='utf-8') as file2:
                json.dump(dict_list, file2, indent=4)
                
            
#------------------------------------点击登陆后的行为--------------------------------------------------                
    def hadAccount(self):
        if self.judgeframe3 == 1:
            self.labelframe3.grid_forget()
            self.judgeframe3 = 0
        self.labelframe3 = LabelFrame(self.root,text="登录",padx=30,pady=50)
        self.labelframe3.grid(row=2,column=1,padx=10,pady=10)
        self.label_username0 = Label(self.labelframe3,text = '用户名：',padx=5,pady=5)
        self.label_username0.grid(row=2,column=1)
        self.label_password0 = Label(self.labelframe3,text = '请输入密码：',padx=5,pady=5)
        self.label_password0.grid(row=3,column=1)
        self.entry_username_0 = Entry(self.labelframe3)
        self.entry_username_0.grid(row=2,column=2,padx=10,pady=5)
        self.entry_password_0 = Entry(self.labelframe3,show='*')
        self.entry_password_0.grid(row=3,column=2,padx=10,pady=5)
        self.judgeframe3 = 1
        self.regist_button = Button(self.labelframe3,text = '登录',command = self.check_login)
        self.regist_button.grid(row=5,column=2,padx=10,pady=5)
        
        
    def check_login(self):
        self.user_name = self.entry_username_0.get()
        self.input_password = self.entry_password_0.get()
        if self.user_name in self.temp_dict:
            if self.temp_dict[self.user_name] == self.input_password:
                self.label3 = Label(self.labelframe3,text = "登陆成功~\n正在加载程序",padx=5,pady=5,fg='red')
                self.label3.grid(row = 5,column=1,padx=5,pady=5)
                self.file_import()
                print('登陆成功！正在载入数据……')
            else:
                self.label3 = Label(self.labelframe3,text = "密码错误！",padx=5,pady=5,fg='red')
                self.label3.grid(row = 5,column=1,padx=5,pady=5)
        else:
            self.label3 = Label(self.labelframe3,text = "用户名不存在！",padx=5,pady=5,fg='red')
            self.label3.grid(row = 5,column=1,padx=5,pady=5)
                     
        
        
    def file_import(self):
        try:
            with open('user_data\%s_file.json'%self.user_name,'r') as file2:
                self.data1 = json.loads(file2.read())
            print('数据加载成功')
            #关闭窗口
            self.root.destroy()
            print('登陆成功，已经打开账本程序')
        except:
            tkinter.messagebox.showerror('错误','数据读取错误')
        
    def about_me(self):
        webbrowser.open('https://fishc.com.cn/space-uid-783916.html')
    
