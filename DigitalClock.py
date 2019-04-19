"""
Project:A digital clock in Python using Tkinter.
Author:Nikhil Kumar
Roll:34
SEM:4th
Sec:'C'
REGD NO:201700467
"""
from tkinter import *
import time

def tick():
    # get the current local time from the PC
    time_string = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    clock.config(text=time_string)
    clock.after(200, tick)

root = Tk()
status = Label(root, text="Time Kharab Chal Raha", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=0, column=0)
clock = Label(root, font=('times', 60, 'bold'), bg='RED')
clock.grid(row=0, column=1) 
tick()
root.mainloop()