#program 1
from tkinter import *
class login:
    def __init__(self):
        login=Tk()
        login.configure(bg="orange")
        login.geometry("600x600")
        login.title("Login From")

        lbl_name=Label(login,text="Enter name",bg="blue",fg="white")
        lbl_name.place(x=100,y=100)
        txt_name=Entry(login,width=40)
        txt_name.place(x=200,y=100)

        lbl_password= Label(login, text="Enter password", bg="blue", fg="white")
        lbl_password.place(x=100, y=140)
        txt_pass = Entry(login, width=40)
        txt_pass.place(x=200, y=140)

        login.mainloop()
log=login()