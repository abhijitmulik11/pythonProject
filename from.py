from tkinter import *

class register:
    def __init__(self):
        obj=Tk()
        obj.configure(bg="black")
        obj.geometry("800x800")
        obj.title("from")

        lbl_title=Label(obj,text="login from",bg="white",fg="black",font="calibri")
        lbl_title.place(x=250,y=30)

        lbl_username=Label(obj,text="Enter username",bg="white",fg="black",font="Calibri")
        lbl_username.place(x=100,y=100)

        txt_username=Entry(obj,width=40)
        txt_username.place(x=250,y=100)

        lbl_password = Label(obj, text="Enter password", bg="white", fg="black", font="Calibri")
        lbl_password.place(x=100, y=140)

        txt_password = Entry(obj, width=40)
        txt_password.place(x=250, y=140)

        btn_register=Button(obj,text="Login",bg="white",fg="black",font="Calibri")
        btn_register.place(x=250,y=200)

        obj.mainloop()

reg=register()