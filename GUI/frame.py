#program 1
# from tkinter import *
# login=Tk()
# login.configure(bg="orange")
# login.geometry("600x600")
# login.title("Login From")
# login.mainloop()

#program 2-using constructor
from tkinter import *
class login:
    def __init__(self):
        login=Tk()
        login.configure(bg="orange")
        login.geometry("600x600")
        login.title("login from")
        login.mainloop()
log=login()