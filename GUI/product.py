from tkinter import *

class detail:
    def __init__(self):
        obj=Tk()
        obj.configure(bg="black")
        obj.geometry("700x700")
        obj.title("Product details")

        lbl_info=Label(obj,text="product information",bg="white",fg="black",font="Calibri")
        lbl_info.place(x=240,y=50)

        lbl_name=Label(obj,text="product name ",bg="white",fg="black",font="Calibri")
        lbl_name.place(x=100,y=100)

        txt_name=Entry(obj,width=40)
        txt_name.place(x=250,y=100)

        lbl_quantity=Label(obj,text="selet quantity ",bg="white",fg="black",font="Calibri")
        lbl_quantity.place(x=100,y=140)

        txt_quantity=Spinbox(obj,from_=0,to=1000000)
        txt_quantity.place(x=250,y=140)

        lbl_exdate=Label(obj,text="expire date ",bg="white",fg="black",font="Calibri")
        lbl_exdate.place(x=100,y=180)

        txt_exdate=Entry(obj,width=40)
        txt_exdate.place(x=250,y=180)

        lbl_mfdate=Label(obj,text="mf date ",bg="white",fg="black",font="Calibri")
        lbl_mfdate.place(x=100,y=220)

        txt_mfdate=Entry(obj,width=40)
        txt_mfdate.place(x=250,y=220)

        lbl_des=Label(obj,text="prod description",bg="white",fg="black",font="Calibri")
        lbl_des.place(x=100,y=260)

        txt_des=Text(obj,width=40,height=6)
        txt_des.place(x=250,y=260)

        lbl_spe=Label(obj,text="specification",bg="white",fg="black",font="Calibri")
        lbl_spe.place(x=100,y=380)

        txt_spe=Text(obj,width=40,height=6)
        txt_spe.place(x=250,y=380)

        btn_detail=Button(obj,text="Save",bg="white",fg="black",font="Calibri")
        btn_detail.place(x=240,y=500)


        obj.mainloop()

det=detail()
