#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     Canvas.py
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
root = Tk()
root.title('Canvas draw tool')

w = Canvas(root, width=400, height=200, background='white')
w.pack()

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill='yellow')

w.bind('<B1-Motion>', paint)
Label(root, text='按住鼠标左键并移动，开始绘制吧！~~').pack(side=BOTTOM)

mainloop()
