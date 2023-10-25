import mysql.connector as my
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import re

def reset(): #deja en blanco los inputs
        inputModel.delete(0,tk.END)
        inputName.delete(0,tk.END)
        selection.set("Seleccionar")
        inputMarca.delete(0,tk.END)
        inputMaterial.delete(0,tk.END)
        inputColor.delete(0,tk.END)
        inputPrecio.delete(0,tk.END)
        inputCosto.delete(0,tk.END)
 
def retornarId():
    task.execute(f"SELECT Id_Producto FROM Producto WHERE Nom_producto = '{inputName.get()}' AND Modelo = '{inputModel.get()}' AND Color = '{inputColor.get()}'")
    temp=task.fetchone()
    if temp is not None:
        id_Producto=temp[0]
    else:
        id_Producto=0
    return id_Producto

def evaluarSiExiste(): #evalua si el registro a ingresar ya existe
    try:
        task.execute(f"SELECT 1 FROM Producto WHERE Nom_Producto = '{inputName.get()}' AND Modelo = '{inputModel.get()}' AND Color = '{inputColor.get()}'")
        data=task.fetchone()
        return data is None
    except ValueError:
        messagebox.showerror("Error","Ha ocurrido un error inesperado.")
    
def evaluarSiExisteConMismaGraduacion():
    booleano =False
    id_Producto=retornarId()
    try:
        task.execute(f"SELECT 1 FROM Graduaciones WHERE Id_Producto = {id_Producto}")
        temp=task.fetchone()
        if temp is not None:
            booleano=True
    except:
        pass
    #Me quedé aquí, no puedo evaluar porque no me deja hacer dos inserciones en la tabla graduaciones!!!!!!!!
    return booleano

def evaluarSolucionValue(): #pendiente
    booleano=False
    if(len(inputContenido.get()) < 15 and len(inputEmpleo.get()) < 45 and len(inputDetalles.get()) < 150):
        booleano=True
    return booleano

def evaluarGraduacionValue():
    booleano = False
    try:
        float(inputGraduacion.get())
        if(len(inputMica.get()) < 45 and len(inputTratamiento.get()) < 45):
            booleano=True
    except:
        pass
    return booleano 
        

def definirGraduacion(): #funciona solo para los productos que poseen graduacion 
    def insertarGraduacion():#inserta los valores de las graduaciones, color de mica, etc.
        try:
            if(evaluarSiExisteConMismaGraduacion()==False):
                if(evaluarGraduacionValue()):
                    task.execute(f"INSERT INTO Graduaciones(Id_Producto,Graduacion,Color_mica,Tratamiento_mica) VALUES({id_producto},'{inputGraduacion.get()}','{inputMica.get()}','{inputTratamiento.get()}')")
                    conexion.commit() #confirma la inserción a la base de datos
                    messagebox.showinfo("Datos guardados!","Los datos se han guardado con éxito.")
                    extra.destroy()
                    reset()
                else:
                    messagebox.showwarning("Datos incorrectos","Ingrese datos correctos en los campos.")
            else:
                messagebox.showwarning("Dato ya agregado","El producto ya está relacionado con una graduación") #se debe arreglar la relación de las tablas
        except ValueError:
            messagebox.showerror("Error","Ha ocurrido un error inesperado.")

    if(evaluarSiExiste()):
        task.execute(f"INSERT INTO Producto(Modelo,Nom_producto,Id_Categoria,Marca,Material,Color,Precio_venta,Costo_Adquisicion) VALUES('{inputModel.get()}','{inputName.get()}',{id_Categoria},'{inputMarca.get()}','{inputMaterial.get()}','{inputColor.get()}',{float(inputPrecio.get())},{float(inputCosto.get())})")
        conexion.commit()
    id_producto=retornarId()

    extra=tk.Toplevel(registro)
    extra.geometry("260x280")
    extra.title("Define la graduación")
    graduacion=tk.Label(extra,text="Gruaduación",font=("Calibri",12))
    graduacion.pack()
    global inputGraduacion
    inputGraduacion=tk.Entry(extra,width=20,justify='center')
    inputGraduacion.pack(pady=(5,20))
    colorMica=tk.Label(extra,text="Colo de mica",font=("Calibri",12))
    colorMica.pack()
    global inputMica
    inputMica=tk.Entry(extra,width=20,justify='center')
    inputMica.pack(pady=(5,20))
    tratamiento=tk.Label(extra,text="Tratamiento de mica",font=("Calibri",12))
    tratamiento.pack()
    global inputTratamiento
    inputTratamiento=tk.Entry(extra,width=20,justify='center')
    inputTratamiento.pack(pady=(5,20))
    guardar=tk.Button(extra,text="Guardar",width=10,font=("Calibri",12),command=insertarGraduacion)
    guardar.pack()

def insertarSolucion():
    def solucionMathEval():
        booleano =False
        id_Producto=retornarId()
        try:
            task.execute(f"SELECT 1 FROM Soluciones_aplicables WHERE Id_Producto = {id_Producto}")
            temp=task.fetchone()
            if temp is not None:
                booleano=True
        except:
            pass
        return booleano

    if(evaluarSolucionValue()):
        if(evaluarSiExiste()):
            try:
                task.execute(f"INSERT INTO Producto(Modelo,Nom_producto,Id_Categoria,Marca,Material,Color,Precio_venta,Costo_Adquisicion) VALUES('{inputModel.get()}','{inputName.get()}',{id_Categoria},'{inputMarca.get()}','{inputMaterial.get()}','{inputColor.get()}',{float(inputPrecio.get())},{float(inputCosto.get())})")
                conexion.commit()
            except ValueError:
                messagebox.showerror("Ha ocurrido un error inesperado")
        if(solucionMathEval()==False):
            task.execute(f"INSERT INTO Soluciones_aplicables(Id_Producto,Contenido_producto,Modo_empleo,Detalles) VALUES({retornarId()},'{inputContenido.get()}','{inputEmpleo.get()}','{inputDetalles.get()}')")
            conexion.commit()
            messagebox.showinfo("Inserción exitosa","Los datos se han insertado correctamente")
        else:
            messagebox.showerror("Error","El producto ya está asociado a un registro")
    else:
        messagebox.showerror("Error","Ingrese datos correctos en los campos")

def definirSolucion(): #terminar
    contenidoWindow=tk.Toplevel(registro)
    contenidoWindow.geometry("260x280")
    contenidoWindow.title("Ingresa el contenido del producto")
    contenido=tk.Label(contenidoWindow,text="Cantidad de contenido",font=("Calibri",12))
    contenido.pack()
    global inputContenido
    inputContenido=tk.Entry(contenidoWindow,width=20,justify='center')
    inputContenido.pack(pady=(5,20))
    modoEmpleo=tk.Label(contenidoWindow,text="Modo de empleo",font=("Calibri",12))
    modoEmpleo.pack()
    global inputEmpleo
    inputEmpleo=tk.Entry(contenidoWindow,width=20,justify='center')
    inputEmpleo.pack(pady=(5,20))
    detalles=tk.Label(contenidoWindow,text="Detalles a mencionar",font=("Calibri",12))
    detalles.pack()
    global inputDetalles
    inputDetalles=tk.Entry(contenidoWindow,width=100,justify='center')
    inputDetalles.pack(pady=(5,20))
    guardarContenido=tk.Button(contenidoWindow,text="Guardar",width=10,font=("Calibri",12),command=insertarSolucion)
    guardarContenido.pack()

def insertarRegistros(): #Inserta registros sencillos
    if(extra.get()==""): #si no posee ningún dato extra en el producto
        if(evaluarSiExiste()): #Evalua que el registro no exista si existe no tiene caso volver a agregarlo
            try:#intenta hacer la inserción
                task.execute(f"INSERT INTO Producto(Modelo,Nom_producto,Id_Categoria,Marca,Material,Color,Precio_venta,Costo_Adquisicion) VALUES('{inputModel.get()}','{inputName.get()}',{id_Categoria},'{inputMarca.get()}','{inputMaterial.get()}','{inputColor.get()}',{float(inputPrecio.get())},{float(inputCosto.get())})")   
                conexion.commit()
                messagebox.showinfo("Datos guardados!","Los datos se han guardado con éxito.")
                reset()
            except ValueError:#error de conexión o inserción por algún motivo
                    messagebox.showerror("Error","Ha ocurrido un error inesperado")#envia el mensaje de error
        else:
            messagebox.showinfo("Ya agregado","El registro ya existe.")
    elif(extra.get()=="graduacion"):
        definirGraduacion()
    elif(extra.get()=="liquido"):       #si necesita insertar datos de soluciones entraría aquí
        definirSolucion()

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
    global registro
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

add=tk.Button(root,text="Agregar registro",command=ingresarRegistro) #evento principal, se modificará 
add.pack()

root.mainloop()
