#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     messagebox.py
   Description :
   Author :       yueyao
   date：          2020/1/7
-------------------------------------------------
   Change Activity:
                   2020/1/7:
-------------------------------------------------
"""
__author__ = 'yueyao'

from tkinter import *
from tkinter import messagebox #messagebox()需要单独导入
from tkinter import filedialog #filedialog()需要单独导入
from tkinter import colorchooser #colorchooser()需要单独导入
from tkinter.messagebox import * #用户使用showinfo()

showinfo(title='test',message='警告')

result = messagebox.askokcancel('demo','发射核弹？')
print(result)

root=Tk()
def callback1():
    filename = filedialog.askopenfilename(defaultextension='.py')
    print(filename)

Button(root,text='打开文件',command=callback1).pack()

def callback2():
    color_data = colorchooser.askcolor()  #调用windows的颜色选择器
    print(color_data)

Button(root,text='选择颜色',command=callback2).pack()

mainloop()