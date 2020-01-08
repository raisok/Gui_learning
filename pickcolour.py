#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     pickcolour.py
   Description :
   Author :       yueyao
   date：          2020/1/7
-------------------------------------------------
   Change Activity:
                   2020/1/7:
-------------------------------------------------
"""
__author__ = 'yueyao'

import os
from time import sleep
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from PIL import ImageGrab, Image,ImageTk

#创建主程序，铺满整个屏幕并删除标题栏
root = tkinter.Tk()
screenWidth=root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry(str(screenWidth)+"x"+str(screenHeight)+'+0+0')
root.overrideredirect(True)
#不允许改变窗体大小
root.resizable(False, False)

#创建画布
canvas = tkinter.Canvas(root,bg='white',width=screenWidth,height=screenHeight)
image = ImageTk.PhotoImage(ImageGrab.grab())
canvas.create_image(screenWidth//2,screenHeight//2,image=image)

def onMouseRightClick(event):
    root.destroy()
canvas.bind('<Button-3>',onMouseRightClick)

radius = 20
def onMouseMove(event):
    global lastIm
    try:
        canvas.delete(lastIm)
    except:
        pass
    #获取鼠标的位置
    x=event.x
    y=event.y
    # im = Image.open(png)
    # color = im.getpixel(x,y)[:3]
    # color = [hex(n)[2:] for n in color]
    # color = map(lambda x:x if len(x)==2 else '0'+x, color)
    # color = "#".join(color)
    # tkinter.messagebox.showinfo("",str(color))
    #二次截图，放大3倍，在鼠标当前位置左上方显示
    subIm = ImageGrab.grab((x-radius,y-radius,x+radius,y+radius))
    subIm = subIm.resize(radius*6,radius*6)
    subIm = ImageTk.PhotoImage(subIm)
    lastIm = canvas.create_image(x-70,y-70,image=subIm)
    canvas.update()

canvas.bind('<Motion>',onMouseMove)
canvas.pack(fill=tkinter.BOTH,expand=tkinter.YES)

# 启动消息主循环
if __name__ == '__main__':
    root.mainloop()
