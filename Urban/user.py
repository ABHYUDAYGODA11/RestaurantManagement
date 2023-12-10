import tkinter
from tkinter import *
from tkinter import PhotoImage
import qrcode
a=tkinter.Tk()
a.geometry('600x600')
a.configure(bg="goldenrod2")
v=qrcode.QRCode()
def action():
    #used for veg menu
    b=Toplevel(a)
    b.title("Veg Menu")
    b.geometry("600x600")
    b.configure(bg="black")
    lb=Label(b,text="Welcome To Veg Menu",font=("arial bold",25),bg="black",fg="cyan3").pack()
    lb2=Label(b,text="***Scan This QR code to get veg menu**",font=("herald",15),bg="black",fg="cyan3").pack()
    image_path = r"C:\Users\MR SLAYER\Desktop\Urban\qr-img1.png"
    img = PhotoImage(file=image_path)
    li =Label(b, image=img,bg="black").pack()
    b.mainloop()
def action2():
    #used for n-veg menu
    b=Toplevel(a)
    b.title("Non-Veg Menu")
    b.geometry("600x600")
    b.configure(bg="black")
    lb1=Label(b,text="Welcome To Non-Veg Menu",font=("arial bold",25),bg="black",fg="cyan3").pack()
    lb2=Label(b,text="***Scan This QR code to get non-veg menu**",font=("herald",15),bg="black",fg="cyan3").pack()
    image_path = r"C:\Users\MR SLAYER\Desktop\Urban\nonveg.png"
    img = PhotoImage(file=image_path)
    li =Label(b, image=img,bg="black").pack()
    b.mainloop()
a.title("Hello")
l1=Label(a,text="Hello Welcome To Urban Chowk",font=("arial bold",25),fg="darkorchid2",bg="goldenrod2",anchor="center").pack()
l2=Label(a,text="**TO GET VEG MENU CLICK 'Veg Menu' BUTTON**",font=("herald",15),bg="goldenrod2").pack()
l3=Label(a,text="**TO GET NON-VEG MENU CLICK 'Non-Veg Menu' BUTTON**",font=("herald",15),bg="goldenrod2").pack()

b1=Button(a,text="Veg Menu",bg="blue",fg="white",font=("Verdana"),command=action).pack(side=RIGHT)
b2=Button(a,text="Non-Veg Menu",bg="blue",fg="white",font=("Verdana"),command=action2).pack(side=LEFT)
a.mainloop()
