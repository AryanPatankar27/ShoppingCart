import tkinter
from tkinter import font
from tkinter import messagebox


window=tkinter.Tk()
window.title("Login form")
window.geometry("340x440")
window.configure(bg='#333333')
roboto_font = font.Font(family="Roboto", size=16, weight="normal")

def login():
    username_entry="aryan"
    password_entry="12345"

    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(Title="Login Success",message="You successfully logged in.")
    else:
       messagebox.showerror(title="Error",message="Invalid login")

frame=tkinter.Frame(bg='#333333')

#Creating widgets(labels,entry,grid)
login_label=tkinter.Label(frame,text="Login",bg='#333333',fg='#FFFFFF',font=roboto_font)
username_label=tkinter.Label(frame,text="Username",bg='#333333',fg='#FFFFFF',font=roboto_font)
username_entry=tkinter.Entry(frame,font="Roboto")
password_entry=tkinter.Entry(frame,show="*",font="Roboto")
password_label=tkinter.Label(frame,text="Password",bg='#333333',fg='#FFFFFF',font=roboto_font)
login_button=tkinter.Button(frame,text="Login",bg="blue",fg='#FFFFFF',command=login)

#placing the widget on the screen
login_label.grid(row=0,column=0,columnspan=2,pady=40)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1,pady=20)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1,pady=20)
login_button.grid(row=3,column=0,columnspan=2,pady=30)


#label is a plain text on the screen

#pack,place and grid(.pack centres the login form)
frame.pack()

window.mainloop()
