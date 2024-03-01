from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#Functionality Part
def clear():
    emailentry.delete(0,END)
    userentry.delete(0,END)
    passwordentry.delete(0,END)
    cpasswordentry.delete(0,END)
    check.set(0)

def connect_database():
    if emailentry.get()=='' or userentry.get()=='' or passwordentry.get()=='' or cpasswordentry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordentry.get() != cpasswordentry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Terms and Condition')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='password')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return

        try:
            query='create database user_data'
            mycursor.execute(query)
            query='use user_data'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(50))'
            mycursor.execute(query)
        except:
            mycursor.execute('use user_data')

        query='select * from data where username=%s'
        mycursor.execute(query,(userentry.get()))

        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','Username Already exists')
        else:
            query = 'insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query, (emailentry.get(), userentry.get(), passwordentry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            signup.destroy()
            import Login


def login_page():
    signup.destroy()
    import Login

#GUI Part
signup=Tk()
signup.geometry('1366x768+70+10')
signup.resizable(0,0)
signup.title('Signup')

bgImage=ImageTk.PhotoImage(file='E Mart2.png')
bgLabel=Label(signup,image=bgImage)
bgLabel.place(x=0,y=0)

email=Label(signup,text='Email',font=('Microsoft Yahei UI Light',16,'bold'),bg='white')
email.place(x=780,y=160)
emailentry=Entry(signup,width=30,font=('Microsoft Yahei UI Light',16,'bold'),fg='white',bg='#40A2D8')
emailentry.place(x=780,y=190)

user=Label(signup,text='Username',font=('Microsoft Yahei UI Light',16,'bold'),bg='white')
user.place(x=780,y=240)
userentry=Entry(signup,width=30,font=('Microsoft Yahei UI Light',16,'bold'),fg='white',bg='#40A2D8')
userentry.place(x=780,y=270)

password=Label(signup,text='Password',font=('Microsoft Yahei UI Light',16,'bold'),bg='white')
password.place(x=780,y=320)
passwordentry=Entry(signup,width=30,font=('Microsoft Yahei UI Light',16,'bold'),fg='white',bg='#40A2D8')
passwordentry.place(x=780,y=350)

cpassword=Label(signup,text='Confirm Password',font=('Microsoft Yahei UI Light',16,'bold'),bg='white')
cpassword.place(x=780,y=400)
cpasswordentry=Entry(signup,width=30,font=('Microsoft Yahei UI Light',16,'bold'),fg='white',bg='#40A2D8')
cpasswordentry.place(x=780,y=430)

check=IntVar()
termsandcond=Checkbutton(signup,text='I agree to the Terms and Conditions',font=('Microsoft Yahei UI Light',12,'bold'),bg='white',variable=check)
termsandcond.place(x=780,y=480)

signupButton=Button(signup,text='Sign Up',font=('Open Sans',19,'bold'),fg='white',bg='#FF6868',width=25,activebackground='white',activeforeground='white',cursor='hand2',bd=0,command=connect_database)
signupButton.place(x=785,y=550)

alreadyaccount=Label(signup,text="Don't have an account?",font=('Open Sans',12,'bold'),bg='white')
alreadyaccount.place(x=845,y=640)

loginButton=Button(signup,text='Log in',font=('Open Sans',12,'bold underline'),fg='blue',bg='white',activebackground='white',activeforeground='white',cursor='hand2',bd=0,command=login_page)
loginButton.place(x=1030,y=638)

signup.mainloop()