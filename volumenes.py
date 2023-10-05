import tkinter as tk
from tkinter import messagebox
import math 

def volumenCil():
    try:
        radio=float(inputRad.get())
        altura=float(inputAlt.get())
        volu=math.pi*math.pow(radio,2)*altura
        text="{:.2f}".format(volu)
        vol.config(text=text)
    except ValueError:
        messagebox.showerror("Error","Ingrese unicamente valores flotantes")

def volumenPrisma():
    try:
        lad=float(inputLado.get())
        var2=float(inputAp.get())
        altura=float(inputH.get())
        volu=3*lad*var2*altura
        text="{:.2f}".format(volu)
        volumen2.config(text=text)
    except ValueError:
        messagebox.showerror("Error","Ingrese unicamente valores flotantes")


root=tk.Tk()
root.geometry("380x230")
root.title("Calculadora de volumenes")

titulo1=tk.Label(root,text="Cilindro",font=("Comic_Sans",15))
titulo1.grid(row=0,column=0)

rad=tk.Label(root,text="Radio",font=("Arial",12))
rad.grid(row=1,column=0)
inputRad=tk.Entry(root,bg="lightgray",width=15,justify='center')
inputRad.grid(row=1,column=1)

alt=tk.Label(root,text="Altura",font=("Arial",12))
alt.grid(row=2,column=0)
inputAlt=tk.Entry(root,bg="lightgray",width=15,justify='center')
inputAlt.grid(row=2,column=1)

volumen=tk.Label(root,text="Volumen",font=("Comic_Sans",15))
volumen.grid(row=4,column=0)
vol=tk.Label(root,text="0",font=("Arial",14))
vol.grid(row=4,column=1)

titulo2=tk.Label(root,text="Prisma",font=("Comic_Sans",15),padx=20)
titulo2.grid(row=0,column=2)

lado=tk.Label(root,text="Lado",font=("Arial",12))
lado.grid(row=1,column=2)
inputLado=tk.Entry(root,bg="lightgray",width=15,justify='center')
inputLado.grid(row=1,column=3)

ap=tk.Label(root,text="ap",font=("Arial",12))
ap.grid(row=2,column=2)
inputAp=tk.Entry(root,bg="lightgray",width=15,justify='center')
inputAp.grid(row=2,column=3)

h=tk.Label(root,text="h",font=("Arial",12))
h.grid(row=3,column=2)
inputH=tk.Entry(root,bg="lightgray",width=15,justify='center')
inputH.grid(row=3,column=3)

vol2=tk.Label(root,text="Volumen",font=("Comic_Sans",15))
vol2.grid(row=4,column=2)
volumen2=tk.Label(root,text="0",font=("Arial",14))
volumen2.grid(row=4,column=3)

buttonOne=tk.Button(root,text="Evaluar",font=("Arial",14),width=8,bg="lightgray",command=volumenCil)
buttonOne.place(x=20,y=140)

buttonTwo=tk.Button(root,text="Evaluar",font=("Arial",14),width=8,bg="lightgray",command=volumenPrisma)
buttonTwo.place(x=240,y=140)

root.mainloop()
