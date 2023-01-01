#program 1
# from tkinter import *
# class login:
#     def __init__(self):
#         login=Tk()
#         login.configure(bg="orange")
#         login.geometry("600x600")
#         login.title("Login From")
#
#         lbl_name=Label(login,font="Corbel,20",text="Enter name",bg="blue",fg="white")
#         lbl_name.place(x=100,y=100)
#         txt_name=Entry(login,width=40)
#         txt_name.place(x=250,y=100)
#
#         lbl_password= Label(login,font="Corbel,20",text="Enter password", bg="blue", fg="white")
#         lbl_password.place(x=100, y=140)
#         txt_pass = Entry(login, width=40)
#         txt_pass.place(x=250, y=140)
#
#         login.mainloop()
# log=login()

#program 2
from tkinter import *
class login:
    def __init__(self):
        login=Tk()
        login.configure(bg="black")
        login.geometry("600x600")
        login.title("Login from")

        lbl_name=Label(login,font="Arial",text="Enter name",bg="White",fg="black")
        lbl_name.place(x=100,y=100)
        txt_name=Entry(login,width=40)
        txt_name.place(x=280,y=100)

        lbl_password = Label(login,font="Arial",text="Enter password", bg="white", fg="black")
        lbl_password.place(x=100, y=140)
        txt_pass= Entry(login, width=40)
        txt_pass.place(x=280,y=140)

        lbl_subject = Label(login,font="Arial",text="Subject",bg="white",fg="black")
        lbl_subject.place(x=100,y=180)

        che_button=Checkbutton(login,text="python")
        che_button1=Checkbutton(login,text="java")
        che_button2=Checkbutton(login,text="css")
        che_button.place(x=280,y=180)
        che_button1.place(x=360,y=180)
        che_button2.place(x=420, y=180)

        lbl_text = Label(login, font="Arial", text="Enter address", bg="white", fg="black")
        lbl_text.place(x=100, y=220)

        txt_text=Text(login,width=40,height=5)
        txt_text.place(x=280,y=220)

        lbl_gender=Label(login,font="Arial", text="selet Gender", bg="white", fg="black")
        lbl_gender.place(x=100,y=340)

        txt_male=Radiobutton(login,text="male",value=1)
        txt_male.place(x=280,y=340)
        txt_female = Radiobutton(login, text="female",value=2)
        txt_female.place(x=340, y=340)

        lbl_subject = Label(login, font="Arial", text="selet subject", bg="white", fg="black")
        lbl_subject.place(x=100, y=400)

        txt_subject=Listbox(login,width=40)
        txt_subject.insert(1,"python")
        txt_subject.insert(2, "java")
        txt_subject.insert(3, "javascript")
        txt_subject.insert(4, "php")
        txt_subject.insert(5, "eti")
        txt_subject.insert(6, "mad")
        txt_subject.insert(7, "html")
        txt_subject.insert(8, "css")
        txt_subject.insert(9, "cpp")
        txt_subject.insert(10, "oop")
        txt_subject.place(x=280,y=400)

        lbl_number = Label(login, font="Arial", text="selet number", bg="white", fg="black")
        lbl_number.place(x=100, y=600)

        txt_number=Spinbox(login,from_=0,to=150)
        txt_number.place(x=280,y=600)

        lbl_option=Label(login,font="Arial",text="selet Subject",bg="white",fg="black")
        lbl_option.place(x=100,y=640)

        txt_option=OptionMenu(login, "c","Python","Java")
        txt_option.place(x=280,y=640)

        menubar=Menu(login)
        menubar.add_command(label="Edit")
        menubar.add_command(label="Run")
        menubar.add_command(label="View")
        menubar.add_command(label="Tool")
        menubar.add_command(label="File")
        login.config(menu=menubar)

        btn_login = Button(login, font="Arial", text="login", bg="white", fg="black")
        btn_login.place(x=240, y=1000)

        login.mainloop()

log=login()

