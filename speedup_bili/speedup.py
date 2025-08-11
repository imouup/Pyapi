import time

import pyautogui as pg
from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, width=200, height=100)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.noticetext = StringVar()

        self.notice = Label(self, textvariable= self.noticetext, fg = 'black', font=('微软雅黑', 12), width=30, height=15)
        self.notice.pack()
        self.upButton = Button(self, text='加速>>>', command=speedup)
        self.upButton.pack()
        self.downButton = Button(self, text='不加速了', command=stop)
        self.downButton.pack()

A = True

def speedup():
    global A
    pg.keyDown('right')
    app.noticetext.set('正在加速')
    while A:
        time.sleep(1)
def stop():
    global A
    A = False
    pg.keyUp('right')

app = Application()
app.noticetext.set('加速')
app.master.title('加速')
app.mainloop()