import tkinter as tk
from tkinter import messagebox
import re

def saveData():
    names=input_Name.get()
    lastNames=input_LastName.get()
    age=input_Age.get()
    height=input_Height.get()
    phone=input_Phone.get()
    genre=""
    if var_Genre.get()==1:
        genre="Hombre"
    elif var_Genre.get()==2:
        genre="Mujer"
    
    if(validateInteger(age) and validateDecimal(height) and validateLength(phone) and validateString(names) and validateString(lastNames)):
        datos=f"Nombres: {names}\nApellidos: {lastNames}\nEdad: {age} años\nAltura: {height}\nTeléfono: {phone}\nGénero: {genre}"

        with open("Datos.txt","a") as archivo:
            archivo.write(datos+"\n\n")

        messagebox.showinfo("Los datos han sido guardados con éxito!\n\n"+datos)

        input_Name.delete(0,tk.END)
        input_LastName.delete(0,tk.END)
        input_Age.delete(0,tk.END)
        input_Height.delete(0,tk.END)
        input_Phone.delete(0,tk.END)
        var_Genre.set(0)
    else:
        messagebox.showerror("Error","Ingrese datos validos en los campos")

def deleteInputs():
    input_Name.delete(0,tk.END)
    input_LastName.delete(0,tk.END)
    input_Age.delete(0,tk.END)
    input_Height.delete(0,tk.END)
    input_Phone.delete(0,tk.END)
    var_Genre.set(0)

def validateInteger(integer):
    try:
        int(integer)
        return True
    except ValueError:
        return False

def validateDecimal(decimal):
    try:
        float(decimal)
        return True
    except ValueError:
        return False
    
def validateLength(value):
    return value.isdigit() and len(value) == 10

def validateString(text):
    return bool(re.match("^[a-zA-Z\s]+$",text))

root=tk.Tk()
root.title("Formulario")
root.geometry("280x460")

var_Genre=tk.IntVar()

names=tk.Label(root,text="Nombres:",font=("Comic_Sans",14),fg="#B0578D")
names.pack()
input_Name=tk.Entry(root,background="#FFE4D6",width=30,justify='center')
input_Name.pack(pady=(0,10))

lastNames=tk.Label(root,text="Apellidos:",font=("Comic_Sans",14),fg="#B0578D")
lastNames.pack()
input_LastName=tk.Entry(root,background="#FFE4D6",width=30,justify='center')
input_LastName.pack(pady=(0,10))

age=tk.Label(root,text="Edad:",font=("Comic_Sans",14),fg="#B0578D")
age.pack()
input_Age=tk.Entry(root,background="#FFE4D6",width=30,justify='center')
input_Age.pack(pady=(0,10))

height=tk.Label(root,text="Estatura",font=("Comic_Sans",14),fg="#B0578D")
height.pack()
input_Height=tk.Entry(root,background="#FFE4D6",width=30,justify='center')
input_Height.pack(pady=(0,10))

phone=tk.Label(root,text="Teléfono",font=("Comic_Sans",14),fg="#B0578D")
phone.pack()
input_Phone=tk.Entry(root,background="#FFE4D6",width=30,justify='center')
input_Phone.pack(pady=(0,10))

genre=tk.Label(root,text="Género",font=("Comic_Sans",14),fg="#B0578D")
genre.pack()

rb_Man=tk.Radiobutton(root,text="Hombre",variable=var_Genre,value=1)
rb_Man.pack()

rb_Women=tk.Radiobutton(root,text="Mujer",variable=var_Genre,value=2)
rb_Women.pack(pady=(0,10))

button_Save=tk.Button(root,text="Guardar",font=("Comic_Sans",12),width=14,background="#FACBEA",fg="#B0578D",command=saveData)
button_Save.pack(pady=(0,10))

button_Delete=tk.Button(root,text="Borrar campos",font=("Comic_Sans",12),width=14,background="#FACBEA",fg="#B0578D",command=deleteInputs)
button_Delete.pack(pady=(0,10))


root.mainloop()






