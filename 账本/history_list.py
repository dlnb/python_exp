# -*- coding: utf-8 -*-
"""
Created on Sun Feb 2020

@author: dlnb5
"""
#账单历史的程序
from tkinter import *
import json
from tkinter import filedialog

class Historylist():
    def __init__(self,username):
        print(username)
        self.username = username
        print(' 您打开了账单历史页面,正在写入文件')
        with open('user_data\%s_file.json'%self.username,'r') as file1:
            self.data1 = json.loads(file1.read())
        self.hlwindow()
    def search(self):
        print('正在载入搜索功能')
        print(self.entry1.get())
        self.text.delete(1.0,END)
        self.searchcontent = self.entry1.get()
        self.text.insert(END,'搜索结果如下！\n')
        self.count=0
        for eachdict in self.data1:
            temp_data = eachdict["Time"]

            if self.searchcontent in temp_data:
                self.count=1
                try:
                    self.text.insert(END,'您在%s 收支了%.2f元，\n项目是%s\n'%(eachdict["Time"],eachdict["Exp"],eachdict["Item"]))
                except:
                    self.text.insert(END,'\n%s缺少项目无法展示\n'%eachdict["Time"])
        if self.count == 0:
            self.text.insert(END,'没有搜索结果')
        self.text.insert(END,'\n-------\n搜索结束')
    def saveas(self):
        print('正在载入另存为~')
        
        filename = filedialog.asksaveasfilename(title='选择要保存账单的位置', filetypes=[('All Files', '*.txt')])
        print(filename)
        with open(filename,'w') as file2:
            file2.write('\n欢迎使用账单程序 by dlnb526\n')
            for eachdict in self.data1:
                try:
                    file2.write('-----------------------------\n时间 %s\n项目 %s \n收支 %.2f元\n余额 %.2f元\n'%\
                        (eachdict['Time'],eachdict['Item'],eachdict['Exp'],eachdict['Total']))

                except:
                    file2.write('\n%s缺少项目无法展示\n'%eachdict["Time"])

    def datapro(self):
        self.text.delete(1.0,END)
        self.text.insert(END,'****%s,您的历史账单如下:****\n'%self.username)
        for eachdict in self.data1:
            try:
                self.hisstr =  '-----------------------------\n时间 %s\n项目 %s \n收支 %.2f元\n余额 %.2f元\n'%\
                    (eachdict['Time'],eachdict['Item'],eachdict['Exp'],eachdict['Total'])
                self.text.insert(INSERT,self.hisstr)
            except:
                print('emmm已经录入数据')
        self.text.insert(END,'---------\n感谢使用本程序！')
    def back(self):
        self.datapro()
#账单历史的界面
    def hlwindow(self):
        self.root=Tk()
        self.root.title("历史账单 by dlnb526")
        
        self.labelframe = LabelFrame(self.root,text="历史账单如下",labelanchor=N)
        self.labelframe.grid(padx=10,pady=10,columnspan=4)
        self.sb_text = Scrollbar(self.labelframe)
        self.sb_text.grid(row=2,column=4,sticky=N+S)
        self.text = Text(self.labelframe,width=50, height=30,yscrollcommand =self.sb_text.set)
        self.text.grid(row=2,column=1,columnspan=3,padx=10,pady=10,sticky=W)
        self.datapro()
        self.label1 = Label(self.root,text="请输入要搜索的日期")
        self.label1.grid(row=3,column=0,sticky=W,padx=5)
        self.entry1 = Entry(self.root)
        self.entry1.grid(row=3,column=1)

        self.button2 = Button(self.root,text = "另存为",command=self.saveas)
        self.button2.grid(padx=30,pady=30,row=4,column=1,columnspan=3,sticky=W+E)
        self.button1 = Button(self.root,text = "搜索",command=self.search)
        self.button1.grid(row=3,column=2,padx=10,pady=10,sticky=W)
        self.button3 = Button(self.root,text = "刷新账单",command=self.back)
        self.button3.grid(row=3,column=3,padx=10,pady=10,sticky=E)
        
        self.sb_text.config(command=self.text.yview)
        
        
        
        
        mainloop()
