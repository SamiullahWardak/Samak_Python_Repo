from tkinter import messagebox

import pyautogui
from tkinter import *
import os
import fileinput


def take():
    sShot = pyautogui.screenshot()
    sShot.save('screenshot.JPG')


root = Tk()
root.title('Samak_Screenshot')
root.geometry("200x60+1050+400")
root.config(background='cyan')
root.resizable(FALSE,FALSE)

label = Label(text='Click the button to capture', font=40, background='cyan', foreground='#343434').pack()

btn = Button(text='Screenshot', font=40, background='#343434', foreground='#adadff', command=take).pack(anchor='center')

msg = messagebox.showinfo(title='Warning', message='1- (IMPORTANT) Check the folder must not have any file same as (screenshot.JPG)\n'
                                               '2- (IMPORTANT) After capturing every screenshot change the name of the captured screenshot')

root.mainloop()
