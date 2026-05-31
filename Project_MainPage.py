from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from PIL import ImageTk,Image
import datetime
from tkinter import messagebox

top=Tk()
top.geometry('1450x700')
top.title("GUI COLLEGE REGISTRATION FORM")

def Insert():
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
    s="insert into Registered_Form values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(k,k2,k3,k4,n,k6,k7,k8,k9)
    resutl=cur.execute(s)
    if(resutl>0):
        messagebox.showinfo("Result","Your Record has been Sucessfully! Inserted [✔]")
    else:
        messagebox.showinfo("Result","Your Record has not been Inserted [⨂]")
    db.commit()
    e.delete(0,"end")
    e1.delete(0,"end")
    e2.delete(0,"end")
    e3.delete(0,"end")
    cal.delete(0,"end")
    e5.delete(0,"end")
    cb.delete(0,"end")
    var.delete(0,"end")
    cb1.delete(0,"end")


def ShowPassword():
    if e2.cget('show')=="*":
        e2.config(show='')
    else:
        e2.config(show="*")

 
homeimg=ImageTk.PhotoImage(file=r"D:\Python Codes\Python Projects\Student_Registration\images\v3.jpg") # Put Main Page Image
L4=Label(top,image=homeimg)
L4.pack()

var=StringVar() # For Radiobutton StringVar

def Update():
    top.destroy()
    import Update_RegistrationForm
 
# Delete Record based on Name column
def delete():
    k=e.get()
    if k=="":
        messagebox.showerror("Error","Please Enter an Name! [👈✍] ")
    import pymysql as sql
    db=sql.Connect(host='localhost',user='root',password='DBpath@9837.81',db='RegistrationForm')
    cur=db.cursor()
    s="delete from registered_form where name=%s"
    result=cur.execute(s,k)
    if(result>0):
        messagebox.showinfo("Result","Your record has been sucessfully! deleted [✔]")
    else:
        messagebox.showinfo("Result","Your record has not been deleted [⨂]")
    db.commit()
    e.delete(0,"end")

def Exit():
    top.destroy()

# Search Data Based on Name
def Search():
    k=e.get()
    for i in tv.get_children():
        tv.delete(i)
    import pymysql as sql
    db=sql.Connect(host='localhost',user='root',password='DBpath@9837.81',db='RegistrationForm')
    cur=db.cursor()
    s="select * from registered_form where Name=%s"
    cur.execute(s,k)
    result=cur.fetchall()
    for col in result:
        Name=col[0]
        LastName=col[1]
        Password=col[2]
        Contact=col[3]
        Date=col[4]
        Email=col[5]
        City=col[6]
        Gender=col[7]
        Course=col[8]
        tv.insert("",'end',values=(Name,LastName,Password,Contact,Date,Email,City,Gender,Course))
    db.commit()
    e1.delete(0,"end")

def Show():
    for i in tv.get_children():
        tv.delete(i)
    import pymysql as sql
    db=sql.Connect(host='localhost',user='root',password='DBpath@9837.81',db='RegistrationForm')
    cur=db.cursor()
    s="select * from Registered_form"
    cur.execute(s)
    result=cur.fetchall()
    for col in result:
        Name=col[0]
        LastName=col[1]
        Password=col[2]
        Contact=col[3]
        Date=col[4]
        Email=col[5]
        City=col[6]
        Gender=col[7]
        Course=col[8]
        tv.insert("",'end',values=(Name,LastName,Password,Contact,Date,Email,City,Gender,Course))
         

tv = ttk.Treeview(top,height=19)
tv['columns']=('Name','LastName','Password','Contact','Date','Email','City','Gender','Course')
tv.column('#0', width=0, stretch=NO)

tv.column('Name', anchor=CENTER, width=100)
tv.column('LastName',anchor=CENTER, width=100)
tv.column('Password', anchor=CENTER, width=100)
tv.column('Contact', anchor=CENTER, width=100)
tv.column('Date', anchor=CENTER, width=100)
tv.column('Email', anchor=CENTER, width=120)
tv.column('City', anchor=CENTER, width=100)
tv.column('Gender', anchor=CENTER, width=75)
tv.column('Course', anchor=CENTER, width=120)



tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('LastName', text='LastName', anchor=CENTER)
tv.heading('Password', text='Password', anchor=CENTER)
tv.heading('Contact', text='Contact', anchor=CENTER)
tv.heading('Date', text='Date',anchor=CENTER)
tv.heading('Email', text='Email',anchor=CENTER)
tv.heading('City', text='City',anchor=CENTER)
tv.heading('Gender', text='Gender',anchor=CENTER)
tv.heading('Course', text='Course',anchor=CENTER)
tv.place(x=515,y=145)

list=['Select','Noida','Dehli','Mumbai','Bangalore','Pune','Hyderabad','Jaipur','Kolkata','Varanasi']
list1=['Select','Data Analyst','Data Science','Mern Full Stack','Web Designing','Java Developer']

L=Label(top,text='COLLEGE REGISTRATION FORM',fg='Black',bg='skyblue',font=('Georgia 25 bold'))
L.place(x=425,y=20)

l=Label(top,text='Name :',fg='black',bg='skyblue',font=('Arial 20 bold'))
l.place(x=30,y=145)
e=Entry(top,font=('Arail 20 bold'))
e.place(x=190,y=145)

l1=Label(top,text='LastName :',fg='black',bg='skyblue',font=('Arial 20 bold'))
l1.place(x=30,y=195)
e1=Entry(top,font=('Arail 20 bold'))
e1.place(x=190,y=195)

l2=Label(top,text='Password :',fg='black',bg='skyblue',font=('Arial 20 bold'))
l2.place(x=30,y=240)
e2=Entry(top,font=('Arail 20 bold'),width=17,show="*")
e2.place(x=190,y=240)


l3=Label(top,text='Contact :',fg='black',bg='skyblue',font=('Arial 20 bold'))
l3.place(x=30,y=285)
e3=Entry(top,font=('Arail 20 bold'))
e3.place(x=190,y=285)

l4=Label(top,text='Date :',fg='black',bg='skyblue',font=('Arial 20 bold'))
l4.place(x=30,y=330)
cal=DateEntry(top,width=19,bg='darkblue',fg='white',year=2010,font=('Arial 20 bold'))
cal.place(x=190,y=330)

l5=Label(top,text='Email :',fg='black',bg='skyblue',font=('Arial 20 bold'))
l5.place(x=30,y=375)
e5=Entry(top,font=('Arail 20 bold'))
e5.place(x=190,y=375)


l6=Label(top,text='City :',fg='black',bg='skyblue',font=('Arial 20 bold'))
l6.place(x=30,y=420)
cb=ttk.Combobox(top,value=list,font=('Arial 20 bold'),width=19)
cb.place(x=190,y=420)
cb.current(0)

l7=Label(top,text='Gender :',fg='black',bg='skyblue',font=('Arial 20 bold'))
l7.place(x=30,y=465)

l8=Label(top,text='Course :',fg='black',bg='skyblue',font=('Arial 20 bold'))
l8.place(x=30,y=520)
cb1=ttk.Combobox(top,value=list1,font=('Arial 20 bold'),width=19)
cb1.place(x=190,y=520)
cb1.current(0)


r1=Radiobutton(top,text="Male",variable=var,value='Male',font="Arial 18 bold")
r1.place(x=190,y=465)

r2=Radiobutton(top,text="Femail",variable=var,value='Female',font="Arial 18 bold")
r2.place(x=283,y=465)

r3=Radiobutton(top,text="Other",variable=var,value='Other',font="Arial 18 bold")
r3.place(x=399,y=465)
r1.select()

c1=Checkbutton(top,font=('Arial 18 bold'),command=ShowPassword)
c1.place(x=460,y=240)
 
b=Button(top,text='SUBMIT',font=('Arial 20 bold'),command=Insert) #130
b.place(x=190,y=600)

b1=Button(top,text='UPDATE',font=('Arial 20 bold'),command=Update)
b1.place(x=330,y=600)

b2=Button(top,text='DELETE',font=('Arial 20 bold'),command=delete)
b2.place(x=480,y=600)

b3=Button(top,text='SEARCH',font=('Arial 20 bold'),command=Search)
b3.place(x=625,y=600)

b4=Button(top,text='DESPLAY',font=('Arial 20 bold'),command=Show)
b4.place(x=775,y=600)

b5=Button(top,text='LOGIN',font=('Arial 20 bold'))
b5.place(x=938,y=600)

b6=Button(top,text='EXIT',font=('Arial 20 bold'),command=Exit)
b6.place(x=1065,y=600)



top.config(bg='skyblue')
top.mainloop()
