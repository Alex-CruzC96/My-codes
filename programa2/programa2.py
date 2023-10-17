import tkinter as tk

root=tk.Tk()
root.geometry("300x360")
root.title("Formulario")

label1=tk.Label(root,text="Nombre",font=("Comic_Sans",12),padx=20)
label1.grid(row=0,column=0)

input1=tk.Entry(root,background="#7C81AD",width=30,justify='center')
input1.grid(row=0,column=1)

label2=tk.Label(root,text="Apellidos",font=("Comic_Sans",12))
label2.grid(row=1,column=0)

input2=tk.Entry(root,background="#7C81AD",width=30,justify='center')
input2.grid(row=1,column=1)

label3=tk.Label(root,text="Telefono",font=("Comic_Sans",12))
label3.grid(row=2,column=0)

input3=tk.Entry(root,background="#7C81AD",width=30,justify='center')
input3.grid(row=2,column=1)

label4=tk.Label(root,text="Estatura",font=("Comic_Sans",12))
label4.grid(row=3,column=0)

input4=tk.Entry(root,background="#7C81AD",width=30,justify='center')
input4.grid(row=3,column=1)

label5=tk.Label(root,text="Edad",font=("Comic_Sans",12),pady=10)
label5.grid(row=4,column=0)

input5=tk.Entry(root,background="#7C81AD",width=30,justify='center')
input5.grid(row=4,column=1)

label6=tk.Label(root,text="Género",font=("Comic_Sans",12),pady=5)
label6.grid(row=5,column=0)

button1=tk.Radiobutton(root,text="Hombre")
button1.grid(row=6,column=0)

button2=tk.Radiobutton(root,text="Mujer")
button2.grid(row=6,column=1)

button3=tk.Button(root,text="Guardar",width=20,height=3,font=("Comic_Sans",12))
button3.place(x=55,y=210)

button4=tk.Button(root,text="Cancelar",width=20,height=3,font=("Comic_Sans",12))
button4.place(x=55,y=290)



root.mainloop()