from tkinter import*
import random
from datetime import date
from datetime import datetime
from datetime import timedelta
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
class tk:
#main page
    def main_page(self):
        global root
        root=Tk()
        root.geometry('925x500+200+100')
        root.configure(bg='#fff')
        root.resizable(False,False)

        img=Image.open('mr.png')
        img=ImageTk.PhotoImage(img)
        t=Label(root,image=img,bg='white')
        t.place(x=50,y=50)

        frame=Frame(root,width=350,height=350,bg='white')
        frame.place(x=480,y=70)

        heading=Label(frame,text='Passport system',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=70,y=5)
        newus=Button(frame,width=45,height=2,text='New User Registration',bg='#57a1f8',fg='white',border=0,command=self.new).place(x=30,y=90)
        exus=Button(frame,width=45,height=2,text='Existing User Login',command=self.existing,bg='#57a1f8',fg='white',border=0).place(x=30,y=150)
        che=Button(frame,width=45,height=2,text='Check Appoinment availability',command=self.appoinment,bg='#57a1f8',fg='white',border=0).place(x=30,y=210)
        track=Button(frame,width=45,height=2,text='Track Application Status',command= self.track,bg='#57a1f8',fg='white',border=0).place(x=30,y=270)

        root.mainloop()


    #registration process
    def get_data(self):
        if office.get()=='' or name.get()=='' or Aadhar.get()=='' or Dob.get()=='' or username.get()=='' or cpassword.get()=='' or rpassword.get()=='':
            messagebox.showerror('Error','Enter all input')
        elif cpassword.get()!=rpassword.get():
            messagebox.showerror('Error','Reenter confirm password')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='')
                cursor=conn.cursor()
            except:
                messagebox.showerror('Error','database connnection error')
                return
            try:
                query='create database userdata'
                cursor.execute(query)
                query='use userdata'
                cursor.execute(query)
                query='create table data(office varchar(20),name varchar(20),Aadhar_number varchar(20) UNIQUE,Dob varchar(15),username varchar(20) UNIQUE,cpassword varchar(20),rpassword varchar(20))'
                cursor.execute(query)
            except:
                cursor.execute('use userdata')

                
            try:
                query='insert into data(office,name,Aadhar_number,Dob,username,cpassword,rpassword) values(%s,%s,%s,%s,%s,%s,%s)'
                cursor.execute(query,(office.get(),name.get(),Aadhar.get(),Dob.get(),username.get(),cpassword.get(),rpassword.get()))
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo('success','registered successfully')
            except:
                messagebox.showerror('Error','Username already exists')
                return
            

    #signup process
    def signin(self):
        if user.get()=='' or password.get()=='':
            messagebox.showerror('Error','All entries are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='')
                cursor=conn.cursor()
            except:
                messagebox.showerror('Error','database connnection error')
                return
            query='use userdata'
            cursor.execute(query)
            query='select office,name,Aadhar_number,Dob,username,cpassword from data where username=%s and cpassword=%s'
            cursor.execute(query,(user.get(),password.get()))
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid username or password')
            else:
                messagebox.showinfo('welcome','Login Successfully')
                print('''your details:
                      ''')
                for x in row:
                    print(x)
                


    #registration page            
    def new(self):
        root.destroy()
        global dv
        dv=Tk()
        dv.geometry('925x500+200+100')
        dv.configure(bg='#fff')
        dv.resizable(False,False)

        img1=Image.open('R.png')
        img1=ImageTk.PhotoImage(img1)
        a=Label(dv,image=img1,bg='white')
        a.place(x=50,y=50)
        
        rock=Frame(dv,width=400,height=500,bg='white')
        rock.place(x=500,y=10)
        heading=Label(rock,text='Registration',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=100,y=2)
        
        global username
        global cpassword
        global rpassword
        global office
        global Aadhar
        global name
        global Dob
        
        office=StringVar()
        name=StringVar()
        Aadhar=StringVar()
        Dob=StringVar()
        login=StringVar()
        cpassword=StringVar()
        rpassword=StringVar()

        
        Label(rock,text='Passport Office',bg='white',font=('calabri',12)).place(x=30,y=80)
        option=['Delhi','Madurai','Mumbai','Trivandram','Trichy','Chennai']
        office=StringVar()
        office.set('--select--')
        
        passport=OptionMenu(rock,office,*option)
        passport.configure(font=('calabri',12),width=15)
        passport.place(x=180,y=82)
        Label(rock,text='Name',bg='white',font=('calabri',12)).place(x=30,y=130)
        name=Entry(rock,textvariable='name',width=23,font=('calabri',12),bg='#d3d3d3')
        name.place(x=180,y=135)
        Label(rock,text='Aadhar number',bg='white',font=('calabri',12)).place(x=30,y=180)
        Aadhar=Entry(rock,textvariable='Aadhar',width=23,font=('calabri',12),bg='#d3d3d3')
        Aadhar.place(x=180,y=180)
        Label(rock,text='Date of Birth',bg='white',font=('calabri',12)).place(x=30,y=230)
        Dob=DateEntry(rock,selectmode='day',width=20,font=('calabri',12))
        Dob.place(x=180,y=230)
        Label(rock,text='login Id',bg='white',font=('calabri',12)).place(x=30,y=280)
        username=Entry(rock,width=23,font=('calabri',12),bg='#d3d3d3')
        username.place(x=180,y=280)
        Label(rock,text='password',bg='white',font=('calabri',12)).place(x=30,y=330)
        cpassword=Entry(rock,width=23,font=('calabri',12),bg='#d3d3d3')
        cpassword.place(x=180,y=330)
        Label(rock,text='Confirm Password',bg='white',font=('calabri',12)).place(x=30,y=380)
        rpassword=Entry(rock,show='*',width=23,font=('calabri',12),bg='#d3d3d3')
        rpassword.place(x=180,y=380)
        Button(rock,width=25,pady=7,text='Register',bg='#57a1f8',fg='white',border=0,command=self.get_data).place(x=200,y=430)
        Button(rock,width=25,pady=7,text='Back',bg='#57a1f8',fg='white',border=0,command=self.back1).place(x=10,y=430)

        dv.mainloop()

    #track application page
    def track(self):
        root.destroy()
        global md
        md=Tk()
        md.geometry('925x500+200+100')
        md.configure(bg='#fff')
        md.resizable(False,False)



        
        heading=Label(md,text='Track Application Status',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=305,y=60)

        global fileno
        global Dob1
        fileno=StringVar()
        Dob1=StringVar()


        Label(md,text='Aadhar Number ',bg='white',font=('calabri',15)).place(x=150,y=150)
        fileno=Entry(md,textvariable=fileno,width=30,font=('ariel',15),bg='#d3d3d3')
        fileno.place(x=390,y=150)
        Label(md,text='Date of birth',bg='white',font=('calabri',15)).place(x=150,y=220)
        Dob1=DateEntry(md,Selectmode='day',font=('calabri',15),width=25)
        Dob1.place(x=390,y=220)
        Button(md,text='Track Status',width=30,pady=7,bg='#57a1f8',fg='white',border=0,font=('ariel',10),command=self.check_status).place(x=500,y=300)
        Button(md,width=30,pady=7,text='Back',bg='#57a1f8',fg='white',font=('ariel',10),border=0,command=self.back2).place(x=150,y=300)

        md.mainloop()


    def check_status(self):
        try:
            conn=mysql.connector.connect(host='localhost',username='root',password='')
            cursor=conn.cursor()
        except:
            messagebox.showerror('Error','database connnection error')
            return
        query='use userdata'
        cursor.execute(query)
        query='select *from data where Aadhar_number=%s and Dob=%s'
        cursor.execute(query,(fileno.get(),Dob1.get()))
        row=cursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Account not found')
        else:
            a=['Processing police verification','Status bending','Your Passport is dispatched']
            b=random.choice(a)
            messagebox.showinfo('welcome',b)


    def check_app(self):
        if var.get()=='Delhi':
            mr=date.today()+timedelta(days=5)
            messagebox.showinfo('Appoinment','Your appoinment available on {}'.format(mr))
        elif var.get()=='Madurai':
            m=date.today()+timedelta(days=2)
            messagebox.showinfo('Appoinment','Your appoinment available on {}'.format(m))
        elif var.get()=='Mumbai':
            r=date.today()+timedelta(days=7)
            messagebox.showinfo('Appoinment','Your appoinment available on {}'.format(r))
        elif var.get()=='Trivandram':
            b=date.today()+timedelta(days=6)
            messagebox.showinfo('Appoinment','Your appoinment available on {}'.format(b))
        elif var.get()=='Trichy':
            n=date.today()+timedelta(days=3)
            messagebox.showinfo('Appoinment','Your appoinment available on {}'.format(n))
        elif var.get()=='Chennai':
            j=date.today()+timedelta(days=3)
            messagebox.showinfo('Appoinment','Your appoinment available on {}'.format(j))
        else:
            messagebox.showerror('Error','Invalid Input')
           

            
    #appoinment page
    def appoinment(self):
        root.destroy()
        global app
        app=Tk()
        app.geometry('925x500+200+100')
        app.configure(bg='#fff')
        app.resizable(False,False)    
        img4=Image.open('check.png')
        img4=ImageTk.PhotoImage(img4)
        a=Label(app,image=img4,bg='white')
        a.place(x=50,y=50)
        rx=Frame(app,width=400,height=400,bg='white')
        rx.place(x=480,y=70)
        heading=Label(rx,text='Appoinment Availability',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=5,y=5)
        Label(rx,text='passport office',bg='white',font=('calabri',15)).place(x=2,y=150)
        global var
        option=['Delhi','Madurai','Mumbai','Trivandram','Trichy','Chennai']
        var=StringVar()
        var.set('--select--')
        
        passport=OptionMenu(rx,var,*option)
        passport.configure(font=('calabri',12),width=15)
        passport.place(x=150,y=152)
        Button(rx,text='Check appoinment',bg='#57a1f8',fg='white',border=0,width=25,height=2,command=self.check_app).place(x=200,y=250)
        Button(rx,text='Back',bg='#57a1f8',fg='white',border=0,width=25,height=2,command=self.back3).place(x=1,y=250)
        app.mainloop()

    #login page
    def existing(self):
        root.destroy()
        global screen
        screen=Tk()
        screen.geometry('925x500+200+100')
        screen.configure(bg='#fff')
        screen.resizable(False,False)
        
        img0=Image.open('login.png')
        img0=ImageTk.PhotoImage(img0)
        a=Label(screen,image=img0,bg='white')
        a.place(x=50,y=50)
        rdj=Frame(screen,width=350,height=350,bg='white')
        rdj.place(x=480,y=70)
        heading=Label(rdj,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=100,y=5)

        global user
        global password

        def on_enter(e):
            user.delete(0, 'end')
        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'username')

                
        UserEntry=StringVar()
        passEntry=StringVar()
        
        user=Entry(rdj,width=25,textvariable=UserEntry,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        user.place(x=30,y=80)
        user.insert(0,'username')
        user.bind('<FocusIn>',on_enter)
        user.bind('<FocusOut>',on_leave)
        Frame(rdj,width=295,height=2,bg='black').place(x=25,y=107)

        def on_enter(e):
            password.delete(0, 'end')
        def on_leave(e):
            p=password.get()
            if p=='':
                password.insert(0,'password')


        password=Entry(rdj,width=25,textvariable=passEntry,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        password.place(x=30,y=140)
        password.insert(0,'password')
        password.bind('<FocusIn>',on_enter)
        password.bind('<FocusOut>',on_leave)


        Frame(rdj,width=295,height=2,bg='black').place(x=25,y=170)
        Button(rdj,width=20,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=self.signin).place(x=180,y=200)
        Button(rdj,width=20,pady=7,text='back',bg='#57a1f8',fg='white',border=0,command=self.back).place(x=5,y=200)
        a=Label(rdj,text="Don't have an account ?",fg='black',bg='white',font=('Microsoft YaHei UI Light',10,'bold'))
        a.place(x=25,y=300)
        sign=Button(rdj,width=6,text='Sign up',command=self.new, border=0,bg='white',fg='green')
        sign.place(x=200,y=302)
        screen.mainloop()

    def back(self):
        screen.destroy()
        self.main_page()

    def back1(self):
        dv.destroy()
        self.main_page()

    def back2(self):
        md.destroy()
        self.main_page()

    def back3(self):
        app.destroy()
        self.main_page()
    
o = tk()
o.main_page()

