from tkinter import *
from tkinter import messagebox

class personal:
    def __init__(self):
        obj=Tk()
        obj.configure(bg="blue")
        obj.geometry("700x700")
        obj.title("personal detail")

        self.name=StringVar()
        self.contno=StringVar()
        self.email=StringVar()
        self.age=StringVar()
        self.birth=StringVar()
        self.address=StringVar()
        self.gender=StringVar()


        lbl_title=Label(obj,text="Personal Detail",bg="black",fg="white",font="Arial")
        lbl_title.place(x=250,y=50)

        lbl_name=Label(obj,text="Enter Name",bg="black",fg="white",font="Arial")
        lbl_name.place(x=100,y=100)

        txt_name=Entry(obj,width=40,textvariable=self.name)
        txt_name.place(x=260,y=105)

        lbl_contno = Label(obj, text="Contact no", bg="black", fg="white", font="Arial")
        lbl_contno.place(x=100, y=140)

        txt_contno = Entry(obj, width=40,textvariable=self.contno)
        txt_contno.place(x=260, y=145)

        lbl_email=Label(obj,text="Enter email",bg="black",fg="white",font="Arial")
        lbl_email.place(x=100,y=185)

        txt_email = Entry(obj, width=40,textvariable=self.email)
        txt_email.place(x=260, y=190)

        lbl_age= Label(obj, text="Select age", bg="black", fg="white", font="Arial")
        lbl_age.place(x=100, y=225)

        txt_age = Spinbox(obj,from_=0,to=150,textvariable=self.age)
        txt_age.place(x=260, y=230)

        lbl_birth= Label(obj, text="birth date", bg="black", fg="white", font="Arial")
        lbl_birth.place(x=100, y=270)

        txt_birth = Spinbox(obj,from_=0,to=150,textvariable=self.birth)
        txt_birth.place(x=260, y=275)

        lbl_address=Label(obj,text="Enter Address",bg="black",fg="white",font="Arial")
        lbl_address.place(x=100,y=320)

        txt_address=Text(obj, width=40, height=6)
        txt_address.place(x=260,y=320)

        lbl_gender = Label(obj, font="Arial", text="selet Gender", bg="black", fg="white")
        lbl_gender.place(x=100, y=440)
        txt_male = Radiobutton(obj, text="male", value=1)
        txt_male.place(x=260, y=440)
        txt_female = Radiobutton(obj, text="female", value=2)
        txt_female.place(x=340, y=440)

        btn_detail = Button(obj, text="Save", bg="white", fg="black", font="Arial",command=self.show)
        btn_detail.place(x=240, y=500)

        obj.mainloop()

    def show(self):
        print("Name is:", self.name.get())
        print("Address is:", self.contno.get())
        print("Contact is:", self.email.get())
        print("email is:", self.age.get())
        print("birt date is:", self.birth.get())


per=personal()