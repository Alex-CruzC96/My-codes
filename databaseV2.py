import mysql.connector as my
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import re

def insertarRegistros():
    if(extra.get()==""): #si no posee ningún dato extra en el producto
        try:#intenta hacer la inserción
            task.execute("ALTER TABLE Producto AUTO_INCREMENT=1")#borrar
            task.execute(f"INSERT INTO Producto(Modelo,Nom_producto,Id_Categoria,Marca,Material,Color,Precio_venta,Costo_Adquisicion) VALUES('{inputModel.get()}','{inputName.get()}',{id_Categoria},'{inputMarca.get()}','{inputMaterial.get()}','{inputColor.get()}',{float(inputPrecio.get())},{float(inputCosto.get())})")   
            messagebox.showinfo("Datos guardados!","Los datos se han guardado con éxito.")

            task.execute("SELECT * FROM Producto")#borrar
            datos=task.fetchall()
            for data in datos:
                print(data)#hasta aqui se debe borrar

        except ValueError:#error de conexión o inserción por algún motivo
            messagebox.showerror("Error","Ha ocurrido un error inesperado")#envia el mensaje de error
    elif(extra.get()=="graduacion"):
        print("graduacion")
    elif(extra.get()=="liquido"):
        print("liquido")

def evaluarRegistros(): #evalua las entradas de la ventana para producto
    flotante=False
    try:
        float(inputPrecio.get())
        float(inputCosto.get())
        flotante=True
    except ValueError:
        pass
    task.execute(f"SELECT Id_Categoria FROM Categoría WHERE Nombre_Categoria = '{selection.get()}'")
    result=task.fetchone()
    if result is None:
        flotante=False
    else:
        global id_Categoria
        id_Categoria=result[0]
    evaluateModel=(len(inputModel.get())<=45)
    evaluateName=(len(inputName.get())<=45)
    evaluateMarca=(re.match("^[a-zA-Z\s]+$",inputMarca.get()) and len(inputMarca.get())<=20)
    evaluateMaterial=(re.match("^[a-zA-Z\s]+$",inputMaterial.get()) and len(inputMaterial.get())<=10)
    evaluateColor=(re.match("^[a-zA-Z\s]+$",inputColor.get()) and len(inputColor.get())<=20)
    if(evaluateModel and evaluateName and evaluateMarca and evaluateMaterial and evaluateColor and flotante):
        insertarRegistros()
    else:
        messagebox.showerror("Entradas incorrectas","Por favor, ingrese datos correctos.")

def ingresarRegistro(): #genera una ventana para ingresar datos en producto
    registro=tk.Toplevel(root)
    registro.geometry("550x330")
    registro.title("Agregar registro")
    #Modelo
    labelModel=tk.Label(registro,text="Modelo",font=("Calibri,14"),padx=20)
    labelModel.grid(row=0,column=0,sticky='w')
    global inputModel
    inputModel=tk.Entry(registro,width=50,justify='left')
    inputModel.grid(row=0,column=1,padx=10)
    
    #Nombre
    labelName=tk.Label(registro,text="Nombre del producto",font=("Calibri",14),padx=20)
    labelName.grid(row=1,column=0,sticky='w')
    global inputName
    inputName=tk.Entry(registro,width=50,justify='left')
    inputName.grid(row=1,column=1)

    #categoría
    task.execute("SELECT * FROM Categoría")
    opciones=task.fetchall()
    options=[]
    for op in opciones:
        options.append(op[1])
    global selection
    selection=tk.StringVar()
    selection.set("Seleccionar")
    labelCategory=tk.Label(registro,text="Categoría",font=("Calibri",14),padx=20)
    labelCategory.grid(row=2,column=0,sticky='w')
    menuCategory=tk.OptionMenu(registro,selection,*options) #modificar
    menuCategory.grid(row=2,column=1,sticky='w',padx=10)

    #Marca 
    marcaLabel=tk.Label(registro,text="Marca del producto",font=("Calibri",14),padx=20)
    marcaLabel.grid(row=3,column=0,sticky='w')
    global inputMarca
    inputMarca=tk.Entry(registro,width=50,justify='left')
    inputMarca.grid(row=3,column=1)

    #material
    materialLabel=tk.Label(registro,text="Material de fabricación",font=("Calibri",14),padx=20)
    materialLabel.grid(row=4,column=0)
    global inputMaterial
    inputMaterial=tk.Entry(registro,width=50,justify='left')
    inputMaterial.grid(row=4,column=1)

    #Color
    colorLabel=tk.Label(registro,text="Color del producto",font=("Calibri",14),padx=20)
    colorLabel.grid(row=5,column=0,sticky='w')
    global inputColor
    inputColor=tk.Entry(registro,width=50,justify='left')
    inputColor.grid(row=5,column=1)

    #Precio_Venta
    precioVentaLabel=tk.Label(registro,text="Precio de venta",font=("Calibri",14),padx=20)
    precioVentaLabel.grid(row=6,column=0,sticky='w')
    global inputPrecio
    inputPrecio=tk.Entry(registro,width=50,justify='left')
    inputPrecio.grid(row=6,column=1)

    #Costo de aquisición
    costoLabel=tk.Label(registro,text="Costo de adquisición",font=("Calibri",14),padx=20)
    costoLabel.grid(row=7,column=0,sticky='w')
    global inputCosto
    inputCosto=tk.Entry(registro,width=50,justify='left')
    inputCosto.grid(row=7,column=1)

    #Extras
    global extra
    extra=tk.StringVar()
    extra.set("")
    option0=tk.Radiobutton(registro,text="Ninguno",variable=extra,value="")
    option0.place(x=20,y=230)
    option1=tk.Radiobutton(registro,text="Posee graduación",variable=extra,value="graduacion")
    option1.place(x=180,y=230)
    option2=tk.Radiobutton(registro,text="Posee líquido",variable=extra,value="liquido")
    option2.place(x=360,y=230)
    #Enviar
    send=tk.Button(registro,text="Guardar",width=10,font=("Calibri",14),command=evaluarRegistros)
    send.place(x=230,y=260)


#establece la conexion a la base de datos y se crea la variable que ejecuta los comandos SQL
conexion=my.connect(host="localhost",user="root",passwd="10022004AlexCruz9669",database="optilent")
task=conexion.cursor()

#se crea la ventana principal
root=tk.Tk()
root.title("Servicio de inventario")
root.geometry("920x650")

add=tk.Button(root,text="Agregar registro",command=ingresarRegistro)
add.pack()

root.mainloop()
