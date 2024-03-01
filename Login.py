from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#Functionality Part
def forget_pass():
    def change_pass():
        if userentry.get()=='' or newpassentry.get()=='' or cnewpassentry.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=window)
        elif newpassentry.get() != cnewpassentry.get():
            messagebox.showerror('Error','Password Mismatch',parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='password',database='user_data')
            mycursor = con.cursor()
            query='select * from data where username=%s'
            mycursor.execute(query,(userentry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(newpassentry.get(),userentry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, please login with new password',parent=window)
                window.destroy()

    window = Toplevel()
    window.geometry('1366x768+70+10')
    window.resizable(0, 0)
    window.title('Change Password')

    bgPic=ImageTk.PhotoImage(file='E Mart3.png')
    bgLabel=Label(window,image=bgPic)
    bgLabel.place(x=0, y=0)

    userLabel=Label(window,text='Username',font=('Microsoft Yahei UI Light',18,'bold'),bg='white')
    userLabel.place(x=780,y=190)
    userentry=Entry(window,width=30,font=('Microsoft Yahei UI Light',18,'bold'),fg='black',bd=0)
    userentry.place(x=780,y=240)

    Frame(window, width=380, height=2, bg='black').place(x=782, y=280)

    passLabel = Label(window, text='Password', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white')
    passLabel.place(x=780, y=320)
    newpassentry = Entry(window, width=30, font=('Microsoft Yahei UI Light', 18, 'bold'), fg='black', bd=0)
    newpassentry.place(x=780, y=370)

    Frame(window, width=380, height=2, bg='black').place(x=782, y=410)

    cpassLabel = Label(window, text='Confirm Password', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white')
    cpassLabel.place(x=780, y=450)
    cnewpassentry = Entry(window, width=30, font=('Microsoft Yahei UI Light', 18, 'bold'), fg='black', bd=0)
    cnewpassentry.place(x=780, y=500)

    Frame(window, width=380, height=2, bg='black').place(x=782, y=540)

    submitButton = Button(window, text='Submit', font=('Open Sans', 19, 'bold'), fg='white', bg='#FF6868', width=25,
                          activebackground='white', activeforeground='white', cursor='hand2', bd=0,command=change_pass)
    submitButton.place(x=785, y=600)

    window.mainloop()


def login_user():
    if username.get()=='' or password.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='password')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return

        query = 'use user_data'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(username.get(),password.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is successful')

def signup_page():
    login.destroy()
    import Signup

def hide():
    openeye.config(file='crossed-eye.png')
    password.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='eye.png')
    password.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if username.get()=='Username':
        username.delete(0,END)

def pass_enter(event):
    if password.get()=='Password':
        password.delete(0,END)

#GUI Part
login=Tk()
login.geometry('1366x768+70+10')
login.resizable(0,0)
login.title('Login')

bgImage=ImageTk.PhotoImage(file='E Mart1.png')
bgLabel=Label(login,image=bgImage)
bgLabel.place(x=0,y=0)

username=Entry(login,width=25,font=('Microsoft Yahei UI Light',20,'bold'),bd=0)
username.place(x=780,y=320)
username.insert(0,'Username')
username.bind('<FocusIn>',user_enter)

Frame(login,width=380,height=2,bg='black').place(x=783,y=360)

password=Entry(login,width=25,font=('Microsoft Yahei UI Light',20,'bold'),bd=0)
password.place(x=780,y=400)
password.insert(0,'Password')
password.bind('<FocusIn>',pass_enter)

Frame(login,width=380,height=2,bg='black').place(x=783,y=440)

openeye=PhotoImage(file='eye.png')
eyeButton=Button(login,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=1130,y=400)

forgetButton=Button(login,text='Forget Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',11,'bold'),command=forget_pass)
forgetButton.place(x=1030,y=455)

loginButton=Button(login,text='Login',font=('Open Sans',19,'bold'),fg='white',bg='#40A2D8',width=25,activebackground='white',activeforeground='white',cursor='hand2',bd=0,command=login_user)
loginButton.place(x=780,y=500)

orLabel=Label(login,text='---------------------- OR ----------------------',font=('Open Sans',16),fg='black',bg='white')
orLabel.place(x=790,y=560)

facebook=PhotoImage(file='facebook.png')
fbLabel=Label(login,image=facebook,bg='white',)
fbLabel.place(x=870,y=595)

google=PhotoImage(file='google.png')
gogLabel=Label(login,image=google,bg='white',)
gogLabel.place(x=1000,y=595)

signupLabel=Label(login,text='Dont have an account?',font=('Open Sans',11,'bold'),fg='black',bg='white')
signupLabel.place(x=820,y=670)

newaccButton=Button(login,text='Create new one',font=('Open Sans',11,'bold underline'),fg='blue',bg='white',activebackground='white',activeforeground='white',cursor='hand2',bd=0,command=signup_page)
newaccButton.place(x=990,y=665)

login.mainloop()

