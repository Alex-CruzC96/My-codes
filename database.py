import mysql.connector
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import re

def evaluateInputs(model,name,marca,material,color,precio,costo):
    flotante=False
    try:
        float(precio)
        float(costo)
        flotante=True
    except ValueError:
        pass
    evaluateModel=(len(model)<=45)
    evaluateName=(len(name)<=45)
    evaluateMarca=(re.match("^[a-zA-Z\s]+$",marca) and len(marca)<=20)
    evaluateMaterial=(re.match("^[a-zA-Z\s]+$",material) and len(material)<=10)
    evaluateColor=(re.match("^[a-zA-Z\s]+$",color) and len(color)<=20)
    return(evaluateModel and evaluateName and evaluateMarca and evaluateMaterial and evaluateColor and flotante)

def addRegister(): #Agrega registro de product
    #función interna 2
    def reset(): #deja en blanco los inputs
        inputModel.delete(0,tk.END)
        inputName.delete(0,tk.END)
        selection.set("Seleccionar")
        inputMarca.delete(0,tk.END)
        inputMaterial.delete(0,tk.END)
        inputColor.delete(0,tk.END)
        inputPrecioVenta.delete(0,tk.END)
        inputCosto.delete(0,tk.END)
    #funcion interna 3
    def save(): #envia los datos
        try:
            nameCategory=selection.get()
            cursor.execute(f"SELECT Id_Categoria FROM Categoría WHERE Nombre_Categoria = '{nameCategory}' ")
            index=cursor.fetchone()
            if(index is not None):
                id_categoria=index[0]            
        except ValueError:
            pass
        if(evaluateInputs(inputModel.get(),inputName.get(),inputMarca.get(),inputMaterial.get(),inputColor.get(),inputPrecioVenta.get(),inputCosto.get())): #evalua los datos, pero falta verificar si el registro existe
            try:#intenta insertar
                precioValor=float(inputPrecioVenta.get())
                costoValor=float(inputCosto.get())
                cursor.execute(f"INSERT INTO Producto(Modelo,Nom_producto,Id_Categoria,Marca,Material,Color,Precio_venta,Costo_Adquisicion) VALUES('{inputModel.get()}','{inputName.get()}',{id_categoria},'{inputMarca.get()}','{inputMaterial.get()}','{inputColor.get()}',{precioValor},{costoValor})")
                conexion.commit()
                if(selection.get()=="Lentes de sol"): #si el registro a insertar pertenece a la categoria lentes de sol
                    def insertIntoGraduaciones():
                        flotante=False
                        try:
                            float(inputGraduacion.get())
                            
                            flotante=True
                        except ValueError:
                            pass
                        if(flotante):
                            cursor.execute(f"SELECT Id_Producto FROM Producto WHERE Nom_producto = '{inputName.get()}' AND Modelo= '{inputModel.get()}' AND Color='{inputColor.get()}'")
                            idP=cursor.fetchone()[0]
                            cursor.execute(f"INSERT INTO Graduaciones(Id_Producto,Graduacion,Color_Mica,Tratamiento_mica) VALUES({idP},'{inputGraduacion.get()}','{inputMica.get()}','{inputTratamiento.get()}')")
                            conexion.commit() 
                            extra.destroy()
                            reset()
                            actualizar()
                    extra=tk.Toplevel(ventana2)
                    extra.geometry("260x280")
                    extra.title("Define la graduación")
                    graduacion=tk.Label(extra,text="Gruaduación",font=("Calibri",12))
                    graduacion.pack()
                    inputGraduacion=tk.Entry(extra,width=20,justify='center')
                    inputGraduacion.pack(pady=(5,20))
                    colorMica=tk.Label(extra,text="Colo de mica",font=("Calibri",12))
                    colorMica.pack()
                    inputMica=tk.Entry(extra,width=20,justify='center')
                    inputMica.pack(pady=(5,20))
                    tratamiento=tk.Label(extra,text="Tratamiento de mica",font=("Calibri",12))
                    tratamiento.pack()
                    inputTratamiento=tk.Entry(extra,width=20,justify='center')
                    inputTratamiento.pack(pady=(5,20))
                    guardar=tk.Button(extra,text="Guardar",width=10,font=("Calibri",12),command=insertIntoGraduaciones)
                    guardar.pack()
                else:
                    confirm=tk.Toplevel(ventana2)
                    confirm.geometry("400x320")
                    confirm.title("Envío de datos exitoso!")
                    titulo=tk.Label(confirm,text="Los datos se han guardado con éxito!",font=("Arial",12))
                    titulo.pack()

                    contenedor=tk.Frame(confirm,width=295,height=160)
                    contenedor.pack(pady=20)
                    
                    cursor.execute(f"SELECT Id_Producto FROM Producto WHERE Nom_producto = '{inputName.get()}' AND Modelo= '{inputModel.get()}' AND Color='{inputColor.get()}'")
                    idP=cursor.fetchone()[0]
                    id_Producto=tk.Label(contenedor,text="Id del producto",font=("Calibri",12))
                    id_Producto.grid(row=0,column=0)
                    idShow=tk.Label(contenedor,text=idP,font=("Calibri",12))
                    idShow.grid(row=0,column=1,padx=(20,3),sticky='e')

                    modelo=tk.Label(contenedor,text="Modelo",font=("Calibri",12))
                    modelo.grid(row=1,column=0)
                    modeloShow=tk.Label(contenedor,text=inputModel.get(),font=("Calibri",12))
                    modeloShow.grid(row=1,column=1,padx=(20,3),sticky='e')

                    nombre=tk.Label(contenedor,text="Nombre",font=("Calibri",12))
                    nombre.grid(row=2,column=0)
                    nombreShow=tk.Label(contenedor,text=inputName.get(),font=("Calibri",12))
                    nombreShow.grid(row=2,column=1,padx=(20,3),sticky='e')

                    categoria=tk.Label(contenedor,text="Categoría",font=("Calibri",12))
                    categoria.grid(row=3,column=0)
                    categoriaShow=tk.Label(contenedor,text=selection.get(),font=("Calibri",12))
                    categoriaShow.grid(row=3,column=1,padx=(20,3),sticky='e')

                    marca=tk.Label(contenedor,text="Marca",font=("Calibri",12))
                    marca.grid(row=4,column=0)
                    marcaShow=tk.Label(contenedor,text=inputMarca.get(),font=("Calibri",12))
                    marcaShow.grid(row=4,column=1,padx=(20,3),sticky='e')

                    material=tk.Label(contenedor,text="Material",font=("Calibri",12))
                    material.grid(row=5,column=0)
                    materialShow=tk.Label(contenedor,text=inputMaterial.get(),font=("Calibri",12))
                    materialShow.grid(row=5,column=1,padx=(20,3),sticky='e')

                    color=tk.Label(contenedor,text="Color",font=("Calibri",12))
                    color.grid(row=6,column=0)
                    colorShow=tk.Label(contenedor,text=inputColor.get(),font=("Calibri",12))
                    colorShow.grid(row=6,column=1,padx=(20,3),sticky='e')

                    precio=tk.Label(contenedor,text="Precio de venta",font=("Calibri",12))
                    precio.grid(row=7,column=0)
                    precioShow=tk.Label(contenedor,text="$"+inputPrecioVenta.get(),font=("Calibri",12))
                    precioShow.grid(row=7,column=1,padx=(20,3),sticky='e')

                    costo=tk.Label(contenedor,text="Costo de adquisición",font=("Calibri",12))
                    costo.grid(row=8,column=0)
                    costoShow=tk.Label(contenedor,text="$"+inputCosto.get(),font=("Calibri",12))
                    costoShow.grid(row=8,column=1,padx=(20,3),sticky='e')
                    reset()
                    actualizar()
            except:
                messagebox.showerror("Error!","Ha ocurrido un error")

        else:
            messagebox.showerror("Error!","Por favor ingrese datos correctos en los campos")

    ventana2=tk.Toplevel(root)
    ventana2.geometry("550x300")
    ventana2.title("Agregar registro")

    #Modelo
    labelModel=tk.Label(ventana2,text="Modelo",font=("Calibri,14"),padx=20)
    labelModel.grid(row=0,column=0,sticky='w')
    inputModel=tk.Entry(ventana2,width=50,justify='left')
    inputModel.grid(row=0,column=1,padx=10)
    
    #Nombre
    labelName=tk.Label(ventana2,text="Nombre del producto",font=("Calibri",14),padx=20)
    labelName.grid(row=1,column=0,sticky='w')
    inputName=tk.Entry(ventana2,width=50,justify='left')
    inputName.grid(row=1,column=1)

    #categoría
    cursor.execute("SELECT * FROM Categoría")
    opciones=cursor.fetchall()
    options=[]
    for op in opciones:
        options.append(op[1])
    selection=tk.StringVar()
    selection.set("Seleccionar")
    labelCategory=tk.Label(ventana2,text="Categoría",font=("Calibri",14),padx=20)
    labelCategory.grid(row=2,column=0,sticky='w')
    menuCategory=tk.OptionMenu(ventana2,selection,*options) #modificar
    menuCategory.grid(row=2,column=1,sticky='w',padx=10)

    #Marca 
    marcaLabel=tk.Label(ventana2,text="Marca del producto",font=("Calibri",14),padx=20)
    marcaLabel.grid(row=3,column=0,sticky='w')
    inputMarca=tk.Entry(ventana2,width=50,justify='left')
    inputMarca.grid(row=3,column=1)

    #material
    materialLabel=tk.Label(ventana2,text="Material de fabricación",font=("Calibri",14),padx=20)
    materialLabel.grid(row=4,column=0)
    inputMaterial=tk.Entry(ventana2,width=50,justify='left')
    inputMaterial.grid(row=4,column=1)

    #Color
    colorLabel=tk.Label(ventana2,text="Color del producto",font=("Calibri",14),padx=20)
    colorLabel.grid(row=5,column=0,sticky='w')
    inputColor=tk.Entry(ventana2,width=50,justify='left')
    inputColor.grid(row=5,column=1)

    #Precio_Venta
    precioVentaLabel=tk.Label(ventana2,text="Precio de venta",font=("Calibri",14),padx=20)
    precioVentaLabel.grid(row=6,column=0,sticky='w')
    inputPrecioVenta=tk.Entry(ventana2,width=50,justify='left')
    inputPrecioVenta.grid(row=6,column=1)

    #Costo de aquisición
    costoLabel=tk.Label(ventana2,text="Costo de adquisición",font=("Calibri",14),padx=20)
    costoLabel.grid(row=7,column=0,sticky='w')
    inputCosto=tk.Entry(ventana2,width=50,justify='left')
    inputCosto.grid(row=7,column=1)

    #Enviar
    send=tk.Button(ventana2,text="Guardar",width=10,font=("Calibri",14),command=save)
    send.place(x=230,y=240)


def actualizar():   #Confirma que los datos se han enviado SE ELIMINARÁ 
    cursor.execute("SELECT * FROM Producto")
    datas=cursor.fetchall()
    for data in datas:
        print(data)

def exitFullScreen(event=None): #cambia el modo de pantalla completa
    root.attributes('-fullscreen',not root.attributes('-fullscreen'))

root=tk.Tk()
root.attributes('-fullscreen',True)
root.title("Servicio de inventario")
root.geometry("920x650")
root.bind("<Escape>",exitFullScreen)
conexion=mysql.connector.connect(host="localhost",user="root",passwd="10022004AlexCruz9669",database="optilent")

global cursor
cursor=conexion.cursor()


st = scrolledtext.ScrolledText(root, width=50, height=10)
st.pack()
#conexion.commit() #confirma la insercion 


salir=tk.Button(root,text="X",bg="red",font=("Arial",12),fg="white",height=0,command=root.destroy)
salir.place(x=1512,y=0)

minimize=tk.Button(root,text="-",bg="gray",font=("Arial",12),fg="black",height=0,width=2,command=root.iconify)
minimize.place(x=1484,y=0)

add=tk.Button(root,text="Agregar registro",command=addRegister)
add.pack()


root.mainloop()

