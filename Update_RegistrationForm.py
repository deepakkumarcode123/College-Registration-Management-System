from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from tkcalendar import Calendar, DateEntry
import datetime

top2=Tk()
top2.geometry('1250x700')

top2.title("UPDATE GUI COLLEGE REGISTRATION FORM")

def Update():
    k=e.get()
    k2=e1.get()
    k3=e2.get()
    k4=int(e3.get())

    format='%m/%d/%y'
    k5=cal.get()
    date=datetime.datetime.strptime(str(k5),format)
    n=date.strftime('%Y-%m-%d')

    k6=e5.get()
    k7=cb.get()
    k8=var.get()
    k9=cb1.get()

    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='DBpath@9837.81',db='RegistrationForm')
    cur=db.cursor()
    s="update Registered_Form set Name=%s,LastName=%s,Contact=%s,Date=%s,Email=%s,City=%s,Gender=%s,Course=%s Where Password=%s"
    m=(k,k2,k4,n,k6,k7,k8,k9,k3)
    resutl=cur.execute(s,m)
    if(resutl>0):
        messagebox.showinfo("Result","Your Record has been Sucessfully! Updated [✔]")
    else:
        messagebox.showinfo("Result","Your Record has not been Updated [⨂]")

    db.commit()
    e.delete(0,"end")
    k2.delete(0,"end")
    k3.delete(0,"end")
    k4.delete(0,"end")
    n.delete(0,"end")
    k6.delete(0,"end")
    k7.delete(0,"end")
    k8.delete(0,"end")
    k9.delete(0,"end")

def Exit():
    top2.destroy()

def ShowPassword():
    if e2.cget('show')=="*":
        e2.config(show='')
    else:
        e2.config(show="*")

 
homeimg=ImageTk.PhotoImage(file=r"D:\Python Codes\Python Projects\Student_Registration\images\v1.jpg") # Put Main Page Image
L4=Label(top2,image=homeimg)
L4.pack()

var=StringVar() # For Radiobutton StringVar

list=['Select','Noida','Dehli','Mumbai','Bangalore','Pune','Hyderabad','Jaipur','Kolkata','Varanasi']
list1=['Select','Data Analyst','Data Science','Mern Full Stack','Web Designing','Java Developer']

L=Label(top2,text='UPDATE COLLEGE REGISTRATION FORM BASED ON PASSWORD',fg='Black',bg='lightcyan',font=('Georgia 25 bold'))
L.place(x=50,y=20)

l=Label(top2,text='Name :',fg='black',bg='lightcyan',font=('Arial 20 bold'))
l.place(x=50,y=145)
e=Entry(top2,font=('Arail 20 bold'))
e.place(x=210,y=145)

l1=Label(top2,text='LastName :',fg='black',bg='lightcyan',font=('Arial 20 bold'))
l1.place(x=50,y=195)
e1=Entry(top2,font=('Arail 20 bold'))
e1.place(x=210,y=195)

l2=Label(top2,text='Password :',fg='black',bg='lightcyan',font=('Arial 20 bold'))
l2.place(x=50,y=240)
e2=Entry(top2,font=('Arail 20 bold'),width=17,show="*")
e2.place(x=210,y=240)


l3=Label(top2,text='Contact :',fg='black',bg='lightcyan',font=('Arial 20 bold'))
l3.place(x=50,y=285)
e3=Entry(top2,font=('Arail 20 bold'))
e3.place(x=210,y=285)

l4=Label(top2,text='Date :',fg='black',bg='lightcyan',font=('Arial 20 bold'))
l4.place(x=50,y=330)
cal=DateEntry(top2,width=19,bg='lightcyan',fg='white',year=2010,font=('Arial 20 bold'))
cal.place(x=210,y=330)

l5=Label(top2,text='Email :',fg='black',bg='lightcyan',font=('Arial 20 bold'))
l5.place(x=50,y=375)
e5=Entry(top2,font=('Arail 20 bold'))
e5.place(x=211,y=375)


l6=Label(top2,text='City :',fg='black',bg='lightcyan',font=('Arial 20 bold'))
l6.place(x=50,y=420)
cb=ttk.Combobox(top2,value=list,font=('Arial 20 bold'),width=19)
cb.place(x=210,y=420)
cb.current(0)

l7=Label(top2,text='Gender :',fg='black',bg='lightcyan',font=('Arial 20 bold'))
l7.place(x=50,y=465)

l8=Label(top2,text='Course :',fg='black',bg='lightcyan',font=('Arial 20 bold'))
l8.place(x=50,y=520)
cb1=ttk.Combobox(top2,value=list1,font=('Arial 20 bold'),width=19)
cb1.place(x=210,y=520)
cb1.current(0)


r1=Radiobutton(top2,text="Male",variable=var,value='Male',font="Arial 18 bold")
r1.place(x=210,y=465)

r2=Radiobutton(top2,text="Femail",variable=var,value='Female',font="Arial 18 bold")
r2.place(x=303,y=465)

r3=Radiobutton(top2,text="Other",variable=var,value='Other',font="Arial 18 bold")
r3.place(x=419,y=465)
r1.select()

c1=Checkbutton(top2,font=('Arial 18 bold'),command=ShowPassword)
c1.place(x=480,y=240)
 
b=Button(top2,text='UPDATE',font=('Arial 20 bold'),command=Update) 
b.place(x=580,y=300)

b2=Button(top2,text='EXIT',font=('Arial 20 bold'),command=Exit) 
b2.place(x=600,y=370)

top2.config(bg='skyblue')
top2.mainloop()
 

