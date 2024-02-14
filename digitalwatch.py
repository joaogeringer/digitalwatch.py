from tkinter import *
import tkinter
from datetime import datetime


## colors
color1 = "black" 
color2 = "white" 
color3 = "green" 


background = color1
color = color3

window = Tk()
window.title("DigitalWatch!")
window.geometry("440x190")
window.resizable(width=FALSE, height=FALSE)
window.configure(bg=background)

def watch():

    time = datetime.now()

    hour = time.strftime("%H:%M:%S")
    week_day = time.strftime("%A")
    day=time.day
    month=time.strftime("%B")
    year=time.strftime("%Y")

    label1.config(text=hour)
    label1.after(100, watch)
    label2.config(text=week_day + str(day) + "/" + str(month) + str(year))

label1=Label(window, text="", font=("Arial 80"), bg=background, fg=color)
label1.grid(row=0, column=0, sticky=NW, padx=5)

label2=Label(window, text="", font=("Arial 20"), bg=background, fg=color)
label2.grid(row=1, column=0, sticky=NW, padx=5)


watch()

window.mainloop()
