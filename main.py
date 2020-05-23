# -*- coding: utf-8 -*-
# @time:2020/5/22 8:15
# @author: 垃圾小邓
import PyQt5.sip
import time
import pyautogui as pag
from tkinter import *


def get():
    po.delete(0, END)
    time.sleep(1) #几秒后返回位置
    x, y = pag.position()

    po.insert(0, str(x) + ',' + str(y))


root = Tk()



tip = Label(root, text="1s后的光标位置")
tip.grid(row=0)
po = Entry(root)
po.grid(row=1)
do = Button(root, text="获取", command=get)  # 点击获取位置
do.grid(row=2)

mouse= IntVar(value=0)
print(str(mouse))

mainloop()
