from tkinter import *
import time
from tkinter import messagebox

root = Tk()
root.title("Timer")


def timer():
    global min
    min_label.config(text=min)
    

    hour = time.strftime("%H")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    min_label.config(text =hour + ":"+min +":"+ sec)
    # min-=1
    
    if min ==0:
        messagebox.showinfo("Completed","Done")
        root.destroy()
    # min-=1
    min_label.after(1000,timer)

min_label = Label(root,text="",bg="black", fg ="white",font="Ubuntu 20 bold")
min_label.pack(pady=20)
timer()
root.mainloop()