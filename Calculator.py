#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     Calculator.py
   Description :
   Author :       yueyao
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""
__author__ = 'yueyao'

import tkinter
import os
from tkinter import *
import tkinter.font as tkfont

class Calculator(object):

    def __init__(self):
        self.tk = tkinter.Tk()
        self.tk.title("计算器")
        self.tk.minsize(370,460)
        self.tk.maxsize(400,400)
        self.tk.iconbitmap(os.getcwd()+"/favicon.ico")

        self.EntryFont=tkfont.Font(self.tk,size=13)
        self.ButtonFont=tkfont.Font(self.tk,size=12)
        #面板显示
        self.count=tkinter.StringVar()
        self.count.set('0')
        self.label=tkinter.Label(self.tk,bg='#EEE9E9',bd='3',fg='black',anchor='center',font=self.EntryFont,textvariable=self.count)
        self.label.place(y=10,width=380,height=40)

        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#EE6A50', text=self.ButtonList[0],
                                        font=self.ButtonFont, command=self.clear)
        self.NumButton.place(x=30, y=80, width=70, height=55)

        self.shiEntry = Entry(self.baoxianTk, validate='key', validatecommand=(self.checkNum, '%P'), font=self.EntryFont)
        self.shiEntry.place(x=190, y=80)

        self.checkNum = self.baoxianTk.register(self.validateNum)

        self.gerenEntry = Entry(self.baoxianTk, validate='key', validatecommand=(self.checkNum, '%P'), font=self.EntryFont)
        self.gerenEntry.place(x=190, y=190)

    def start(self):
        self.tk.mainloop()

    def checkList(self):
        result=0
        locate=-1
        listSum=0
        for length in range(0,len(self.inputlist)):
            if re.findall(r'[-+*/]',str(self.inputlist[length])):
                result=1
                if length>locate:
                    locate=length
            else:
                pass
        if result==1:
            for i in range(locate+1,len(self.inputlist)):
                listSum+=int(self.inputlist[i])*(10**(len(self.inputlist)-i-1))
        else:
            for j in range(0,len(self.inputlist)):
                listSum+=int(self.inputlist[j])*(10**(len(self.inputlist)-j-1))
        return listSum,locate
    #添加button
    def addButton(self,button):
        if button==self.ButtonList[18]:
            listSum,locate=self.checkList()
            if locate==-1:
                self.inputlist=[str(round(eval('1/'+str(listSum)),5))]
            else:
                for k in range(locate+1,len(self.inputlist)):
                    del self.inputlist[k]
                self.inputlist.append(str(round(eval('1/'+str(listSum)),5)))
        elif button==self.ButtonList[19]:
            pass
        elif button==self.ButtonList[20]:
            pass
        else:
            self.inputlist.append(button)
        self.count.set(self.inputlist)

    def validateNum(self,content):
        if content.isdigit() and int(content)>=0 or content=="":
            return True
        else:
            return False

if __name__ == '__main__':
    NewCalculator = Calculator()
    NewCalculator.start()
