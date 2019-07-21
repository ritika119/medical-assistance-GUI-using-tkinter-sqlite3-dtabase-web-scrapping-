from tkinter import *
import sqlite3 as s
from tkinter import messagebox
import requests as r
import bs4
global client,cu
try:
    client=s.connect("E://abc.db")
    cu=client.cursor()
    cu.execute("create table screen(name varchar(50),username varchar(50),email varchar(50),pass varchar(50),cnfpass varchar(50),phone int)")
except:
    pass

def fun():
    global e1,e2,e3,e4,e5,e6,client,cu
    cu.execute("insert into screen(name,username,email,pass,cnfpass,phone) values(%r,%r,%r,%r,%r,%d)"%(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),int(e6.get())))
    #cu.execute("insert into screen(name,username,email,pass,cnfpass,phone) values(%r,%r,%r,%r,%r,%d)"%(e1.get(),e2.get(),e3.get,e4.get(),e5.get(),int(e6.get())))
    client.commit()
    messagebox.showinfo("Register","registration successful")
    login()

def login():
    try:
        global scr1
        scr1.destroy()
    except:
        pass
    
    try:
        global scr2
        scr2.destroy()
    except:
        pass
    
    global scr
    scr=Tk()
    scr.geometry('500x450')
    scr.title('Account login')
    l2=Label(scr,text='Please enter the details below to login',bg='blue',justify='center',width=100,height=2,font=('calibri',20))
    l2.pack(side=TOP,fill=X)
    l1=Label(scr,text=" ")
    l1.pack()
    userverify = StringVar()
    passverify = StringVar()
    userlabel=Label(scr,text="  USERNAME  ",justify='center',width=30,height=2,font=('calibri',20))
    userlabel.pack()
    e=Entry(scr)
    e.pack()
    e.config(bg='light yellow',highlightcolor='grey21',relief='raised',width=50,textvariable=userverify)
    passlabel=Label(scr,text="  PASSWORD  ",justify='center',width=30,height=2,font=('calibri',20))
    passlabel.pack()
    e1=Entry(scr)
    e1.pack()
    e1.config(bg='light yellow',highlightcolor='grey21',relief='raised',show="*",width=50,textvariable=passverify)
    e1.get()
    l3=Label(scr,text=" ")
    l3.pack()
    b1=Button(scr,text='login',height='2',width='30',activebackground="cyan",activeforeground="green",bd=3,bg="lavender",fg="blue",justify="right",relief="raised",command=main)
    b1.pack()
    l4=Label(scr,text=" ")
    l4.pack()
    b2=Button(scr,text='Register',height='2',width='30',activebackground="cyan",activeforeground="green",bd=3,bg="lavender",fg="blue",justify="right",relief="raised",command=register)
    b2.pack()
    scr.mainloop()


def scrap():
    global lst,eee
    lst=[]
    dt=r.request('get','https://www.1mg.com/search/all?name=%r'%(eee.get()))
    s=bs4.BeautifulSoup(dt.text,'html.parser')
    for i in s.findAll('div'):
        if i.get('class'):
            if len([x for x in i.get('class') if 'style__container__' in x])>0:
                if i.find('a'):
                    x=i.find('a')
                    try:
                        dts=r.request('get','https://www.1mg.com'+x.get('href'))
                        s1=bs4.BeautifulSoup(dts.text,'html.parser')
                        for j in s1.findAll('div'):
                            if j.get('class'):
                                if len([x for x in j.get('class') if '_product-description' in x])>0:
                                    try:
                                        lst.append(j.text)
                                    except:
                                            pass
                                elif  len([x for x in j.get('class') if 'DrugOverview__container' in x])>0:
                                            try:
                                                lst.append(j.text)
                                            except:
                                                    pass
                    except:
                        pass
    global data
    data=iter(lst)


def nxt():
    global data,m
    try:
        m.config(text=next(data))
    except:
        m.config(text='The End')


def main():
    try:
        global scr
        scr.destroy()
    except:
            pass
    global scr1
    scr1=Tk()
    scr1.geometry('300x300')
    l=Label(scr1,text='MAINPAGE',bg='blue',justify='center',width=100,height=2,font=('calibri',20))
    l.pack(side=TOP,fill=X)
    l1=Label(scr1,text=" ")
    l1.pack()
    medicine=StringVar()
    global eee,m
    eee=Entry(scr1,bg='light yellow',highlightcolor='grey21',relief='raised',width=50)
    eee.pack()
    l2=Label(scr1,text=" ")
    l2.pack()
    b=Button(scr1,text='GO',height='2',width='30',activebackground="cyan",activeforeground="green",bd=3,bg="lavender",fg="blue",justify="right",relief="raised",command=scrap)
    b.pack()
    l4=Label(scr1,text=" ")
    l4.pack()
    m=Message(scr1)
    m.pack()
    b3=Button(scr1,text='NEXT',height='2',width='30',activebackground="cyan",activeforeground="green",bd=3,bg="lavender",fg="blue",justify="right",relief="raised",command=nxt)
    b3.pack()
    scr1.mainloop()

def register():
    try:
        global scr
        scr.destroy()
    except:
        pass
    global scr2,e1,e2,e3,e4,e5,e6
            
    scr2=Tk()
    scr2.title('Register')
    scr2.geometry('800x700')
    username=StringVar()
    password=StringVar()
    email=StringVar()
    name=StringVar()
    confirm=StringVar()
    user=StringVar()
    phone=IntVar()
    l=Label(scr2,text='PLEASE ENTER DETAILS BELOW',bg='blue',justify='center',width=20,height=2,font=('calibri',20))
    l.pack(side=TOP,fill=X)
    namelabel=Label(scr2,text=' NAME ',width=20,font=('calibri',20))
    namelabel.pack()
    e1=Entry(scr2)
    e1.pack()
    e1.config(textvariable=name)
    e1.get()
    l1=Label(scr2,text=" ")
    l1.pack()
    userlabel=Label(scr2,text=' USERNAME ',width=20,font=('calibri',20))
    userlabel.pack()
    e2=Entry(scr2)
    e2.pack()
    e2.config(textvariable=user)
    e2.get()
    l7=Label(scr2,text=" ")
    l7.pack()
    emlable=Label(scr2,text='  EMAIL_ID ',justify='center',width=30,height=2,font=('calibri',20))
    emlable.pack()
    e3=Entry(scr2)
    e3.pack()
    e3.get()
    l2=Label(scr2,text=" ")
    l2.pack()
    passlabel=Label(scr2,text="  PASSWORD  ",justify='center',width=30,height=2,font=('calibri',20))
    passlabel.pack()
    e4=Entry(scr2)
    e4.pack()
    e4.config(textvariable=username)
    e4.get()
    l3=Label(scr2,text=" ")
    l3.pack()
    confirmlabel=Label(scr2,text="  CONFIRM PASSWORD  ",justify='center',width=30,height=2,font=('calibri',20))
    confirmlabel.pack()
    e5=Entry(scr2)
    e5.pack()
    e5.config(textvariable=confirm)
    e5.get()
    l4=Label(scr2,text=" ")
    l4.pack()
    phonelabel=Label(scr2,text="  PHONE NUMBER  ",justify='center',width=30,height=2,font=('calibri',20))
    phonelabel.pack()
    e6=Entry(scr2)
    e6.pack()
    e6.config(textvariable=phone)
    e6.get()
    l5=Label(scr2,text=" ")
    l5.pack()
    var=IntVar()
    r1=Radiobutton(scr2, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
    r2=Radiobutton(scr2, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
    b=Button(scr2,text='SUBMIT',height='2',width='30',activebackground="cyan",activeforeground="green",bd=3,bg="lavender",fg="blue",justify="right",relief="raised",command=fun)
    b.pack()
    scr2.mainloop()




login()



    
        

    
        
             
