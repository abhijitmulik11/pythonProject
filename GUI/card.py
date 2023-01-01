from tkinter import *

class card:
    def __init__(self):
        obj=Tk()
        obj.configure(bg="black")
        obj.geometry("800x800")
        obj.title("from")

        lbl_title=Label(obj,text="card info",bg="white",fg="black",font="calibri")
        lbl_title.place(x=250,y=30)

        lbl_cardno=Label(obj,text="Enter cardno",bg="white",fg="black",font="Calibri")
        lbl_cardno.place(x=100,y=100)

        txt_username=Entry(obj,width=40)
        txt_username.place(x=250,y=100)

        lbl_valid = Label(obj, text="valid from", bg="white", fg="black", font="Calibri")
        lbl_valid.place(x=100, y=140)

        txt_valid = Entry(obj, width=40)
        txt_valid.place(x=250, y=140)

        lbl_validfr = Label(obj, text="valid from", bg="white", fg="black", font="Calibri")
        lbl_validfr.place(x=100, y=140)

        txt_validfr = Entry(obj, width=40)
        txt_validfr.place(x=250, y=140)

        lbl_validto = Label(obj, text="valid thru", bg="white", fg="black", font="Calibri")
        lbl_validto.place(x=100, y=180)

        txt_validto = Entry(obj, width=40)
        txt_validto.place(x=250, y=180)

        lbl_cvv = Label(obj, text="cvv no", bg="white", fg="black", font="Calibri")
        lbl_cvv.place(x=100, y=220)

        txt_cvv = Entry(obj, width=40)
        txt_cvv.place(x=250, y=220)

        lbl_amount = Label(obj, text="Amount", bg="white", fg="black", font="Calibri")
        lbl_amount.place(x=100, y=260)

        txt_cvv = Entry(obj, width=40)
        txt_cvv.place(x=250, y=260)

        btn_detail = Button(obj, text="process", bg="white", fg="black", font="Calibri")
        btn_detail.place(x=250, y=300)


        obj.mainloop()

reg=card()