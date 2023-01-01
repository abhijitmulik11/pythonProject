from tkinter import *
from tkinter import messagebox

class register:
    def __init__(self):
        obj=Tk()
        obj.configure(bg="black")
        obj.geometry("700x700")
        obj.title("Register")

        self.name=StringVar()
        self.address=StringVar()
        self.contact=StringVar()
        self.email=StringVar()
        self.password=StringVar()

        lbl_title=Label(obj, text="Reister from", bg="black", fg="white", font="calibri")
        lbl_title.place(x=250,y=50)

        lbl_name=Label(obj,text="Enter name",bg="black",fg="white",font="Calibri")
        lbl_name.place(x=100,y=100)
        txt_name=Entry(obj,width=30,textvariable=self.name)
        txt_name.place(x=240,y=100)

        lbl_address=Label(obj,text="Enter address",bg="black",fg="white",font="Calibri")
        lbl_address.place(x=100,y=140)

        txt_name=Entry(obj,width=30,textvariable=self.address)
        txt_name.place(x=240,y=140)

        lbl_contact=Label(obj,text="Enter contact",bg="black",fg="white",font="Calibri")
        lbl_contact.place(x=100,y=180)

        txt_contact=Entry(obj,width=30,textvariable=self.contact)
        txt_contact.place(x=240,y=180)

        lbl_email=Label(obj,text="Enter email",bg="black",fg="white",font="Calibri")
        lbl_email.place(x=100,y=220)

        txt_email=Entry(obj,width=30,textvariable=self.email)
        txt_email.place(x=240,y=220)

        lbl_password=Label(obj,text="Enter Password",bg="black",fg="white",font="Calibri")
        lbl_password.place(x=100,y=260)

        txt_password=Entry(obj,width=30,textvariable=self.password)
        txt_password.place(x=240,y=260)

        btn_sigup=Button(obj,text="Registerr",bg="black",fg="white",command=self.show)
        btn_sigup.place(x=250,y=300)

        obj.mainloop()

    def show(self):
        print("Name is:",self.name.get())
        print("Address is:", self.address.get())
        print("Contact is:", self.contact.get())
        print("email is:", self.email.get())
        print("password is:", self.password.get())

reg=register()