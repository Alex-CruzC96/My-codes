import mysql.connector
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

def addRegister():
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
    cursor.execute("SELECT * FROM Usuario")
    opciones=cursor.fetchall()
    options=[]
    for op in opciones:
        options.append(op[1])
    selection=tk.StringVar()
    selection.set("Seleccionar")
    labelCategory=tk.Label(ventana2,text="Categoría",font=("Calibri",14),padx=20)
    labelCategory.grid(row=2,column=0,sticky='w')
    menuCategory=tk.OptionMenu(ventana2,selection,*options)
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
    send=tk.Button(ventana2,text="Guardar",width=10,font=("Calibri",14))
    send.bind("<Button-1>",lambda model=inputModel.get(),name=inputName.get(),category=selection.get(),marca=inputMarca.get(),material=inputMaterial.get(),color=inputColor.get(),precio=inputPrecioVenta.get(),costo=inputCosto.get():save(model,name,category,marca,material,color,precio,costo))
    send.place(x=230,y=240)

def save(model,name,category,marca,material,color,precio,costo):
    cursor.execute(f"INSERT INTO Productos(Modelo,Nom_Producto,Categoria,Marca,Material,Color,Precio_Venta,Costo_Adquisicion) VALUES('{model}','{name}','{category}','{marca}','{material}','{color}','{float(precio)}','{float(costo)}')")
    actualizar()

def actualizar():
    cursor.execute("SELECT * FROM Productos")
    datas=cursor.fetchall()
    for data in datas:
        print(data)


root=tk.Tk()
root.attributes('-fullscreen',True)
root.title("Servicio de inventario")
conexion=mysql.connector.connect(host="localhost",user="root",passwd="10022004AlexCruz9669",database="formulario")

global cursor
cursor=conexion.cursor()


st = scrolledtext.ScrolledText(root, width=50, height=10)
st.pack()
#cursor.execute(f"INSERT INTO Usuario (Nombre,Apellidos,Telefono,Estatura,Genero) VALUES('{name}','{lastName}',{phone},{height},'{gender}')")
#conexion.commit() #confirma la insercion 
for i in range(20):
    cursor.execute(f"INSERT INTO Usuario(Nombre,Apellidos,Telefono,Estatura,Genero)VALUES('{'name'}','{'LastName'}','{9611111111}','{1.60}','{'Genero'}')")
cursor.execute("SELECT * FROM Usuario")
datas=cursor.fetchall()
nombres=[]
for data in datas:
    st.insert(tk.INSERT,data)
    nombres.append(data[1])

ejemplo=tk.Label(root,text=nombres[0],font=("Comic_Sans",24))
ejemplo.pack()


salir=tk.Button(root,text="X",bg="red",font=("Arial",12),fg="white",height=0,command=root.destroy)
salir.place(x=1512,y=0)

minimize=tk.Button(root,text="-",bg="gray",font=("Arial",12),fg="black",height=0,width=2,command=root.iconify)
minimize.place(x=1484,y=0)

add=tk.Button(root,text="Agregar registro",command=addRegister)
add.pack()



root.mainloop()

