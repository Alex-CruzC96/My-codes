import tkinter as tk

def farToGrades():
    try:
        far=float(input1.get())
        cel=(far-32)*5/9
        input2.delete(0,tk.END)
        input2.insert(0,"{:.2f}".format(cel))
    except ValueError:
        pass

def gradesToFar():
    try:
        cel=float(input2.get())
        far=(cel*9/5)+32
        input1.delete(0,tk.END)
        input1.insert(0,"{:.2f}".format(far))
    except ValueError:
        pass

def reset():
    input1.delete(0,tk.END)
    input2.delete(0,tk.END)

pantalla=tk.Tk()
pantalla.title("Convertidor de grados")

label1=tk.Label(pantalla,text="Fahrentheit",font=("Comic_Sans",15),pady=(10),padx=(10))
label1.grid(row=0,column=0)

input1=tk.Entry(pantalla,background="lightblue",name="input1",width=35,justify='center')
input1.grid(row=0,column=1)

button=tk.Button(pantalla,text="F -> C",background="purple",font=("Comic_Sans",10),fg="white",justify='center',width=5,height=1,command=farToGrades)
button.grid(row=0,column=2)

label2=tk.Label(pantalla,text="Celsius",font=("Comic_Sans",15))
label2.grid(row=1,column=0)

input2=tk.Entry(pantalla,background="lightblue",name="input2",width=35,justify='center')
input2.grid(row=1,column=1)

button2=tk.Button(pantalla,text="F <- C",background="purple",font=("Comic_Sans",10),fg="white",justify='center',width=5,height=1,command=gradesToFar)
button2.grid(row=1,column=2)

button3=tk.Button(pantalla,text="Restablecer",background="purple",font=("Comic_Sans",10),fg="white",justify='center',pady=10,command=reset)
button3.grid(row=2,column=1)

pantalla.mainloop()