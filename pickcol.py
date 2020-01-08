#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     pickcol.py
   Description :
   Author :       yueyao
   date：          2020/1/7
-------------------------------------------------
   Change Activity:
                   2020/1/7:
-------------------------------------------------
"""
__author__ = 'yueyao'

import tkinter.filedialog
from PIL import ImageGrab, Image,ImageTk
# import cv2


def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    print(size)
    root.geometry(size)


root = tkinter.Tk()
root.title("Color Picker")
# 设置窗口大小与位置
center_window(root,300,240)
# 设置窗口大小不可改变
root.maxsize(600,400)
root.minsize(300,240)
#不允许改变窗体大小
root.resizable(False, False)
#设置标签
theLabel = tkinter.Label(root,text="Please press blank to select color")
theLabel.pack()

#一个窗口显示指针所在位置的颜色


#
screenWidth=root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
print(screenWidth)
print(screenHeight)

canvas = tkinter.Canvas(root,bg='red')
lastIm = ImageTk.PhotoImage(ImageGrab.grab())
lastIm
# canvas.create_image(5,5,image=image)

def onMouseRightClick(event):
    root.destroy()
canvas.bind('<Button-3>',onMouseRightClick)


def onMouseMove(event):
    global lastIm
    try:
        canvas.delete(lastIm)
    except:
        pass
    #获取鼠标的位置
    x=event.x
    y=event.y
    im = Image.open(lastIm)
    color = im.getpixel(x,y)[:3]
    color = [hex(n)[2:] for n in color]
    color = map(lambda x:x if len(x)==2 else '0'+x, color)
    color = "#".join(color)
    print(color)

canvas.bind('<Motion>',onMouseMove)
canvas.pack()

#一个list显示以经保存的颜色
listbox = tkinter.Listbox(root)
listbox.pack()
listbox.insert(0,"a list entry")


root.mainloop()

