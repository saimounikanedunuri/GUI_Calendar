from tkinter import *
from tkcalendar import Calendar
root=Tk()

def choice_date():
    present_date=display_cal.get_date()
    user_date=Label(text=present_date)
    user_date.pack(padx=2,pady=2)
    
display_cal=Calendar(root,setmode="day",date_pattern='m/d/yy')
display_cal.pack(padx=20,pady=20)

open_cal=Button(root,text="select date",command=choice_date)
open_cal.pack(padx=20,pady=20)

root.geometry('500x500')
root.title("GUI CALENDER")
root.configure(bg="purple")
root.mainloop()
