from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from PIL import ImageTk,Image
import datetime
from tkinter import messagebox

top=Tk()
top.geometry('600x400')
top.title("LOGIN GUI COLLEGE REGISTRATION FORM")

# homeimg=ImageTk.PhotoImage(file=r"D:\Python Codes\Python Projects\Student_Registration\images\v5.jpg") # Put Main Page Image
# L4=Label(top,image=homeimg)
# L4.pack()

def Login():
    import pymysql as sql
    db=sql.Connect(host='localhost',user='root',password='DBpath@9837.81',db='RegistrationForm')
    cur=db.cursor()
    cur.execute("select * from registered_form where Name=%s and Password=%s",(e1.get(),e2.get()))
    row=cur.fetchone()

    if row==None:
        messagebox.showerror("Error","Invalid UserName And Password")
    else:
        top.destroy()
        import Project_MainPage

def ShowPassword():
    if e2.cget('show')=="*":
        e2.config(show='')
    else:
        e2.config(show="*")

def Exit():
    top.destroy()

l=Label(top,text='LOGIN COLLEGE REGISTRATION FORM....',bg='yellow',fg='black',font=('Georgia 15 bold'),width=35)
l.place(x=50,y=50)

L1=Label(top,text='UserName : ',bg='white',fg='black',font=('Arial 15 bold'),width=10)
L1.place(x=50,y=150)
e1=Entry(top,font=('Arial 15 bold'),width=25)
e1.place(x=184,y=150)

L2=Label(top,text='Password : ',bg='White',fg='black',font=('Arial 15 bold'),width=10)
L2.place(x=50,y=200)
e2=Entry(top,font=('Arial 15 bold'),width=25,show="*")
e2.place(x=184,y=200)

c1=Checkbutton(top,command=ShowPassword)
c1.place(x=470,y=200)

b1=Button(top,text='LOGIN',font=('Arial 15 bold'),command=Login)
b1.place(x=305,y=250)

b2=Button(top,text='EXIT',font=('Arial 15 bold'),command=Exit)
b2.place(x=395,y=250)

top.config(bg='darkslategrey')
top.mainloop()