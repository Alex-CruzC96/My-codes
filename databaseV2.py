import mysql.connector as my
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import messagebox
import re
from PIL import Image,ImageTk

def reset(): #deja en blanco los inputs
        inputModel.delete(0,tk.END)
        inputName.delete(0,tk.END)
        selection.set("Seleccionar")
        inputMarca.delete(0,tk.END)
        inputMaterial.delete(0,tk.END)
        inputColor.delete(0,tk.END)
        inputPrecio.delete(0,tk.END)
        inputCosto.delete(0,tk.END)
        dateInput.delete(0,tk.END)
        dateInput.insert(0,"yyyy/mm/dd")
        stockInput.delete(0,tk.END)
 
def retornarId():
    task.execute(f"SELECT Id_Producto FROM Producto WHERE Nom_producto = '{inputName.get()}' AND Modelo = '{inputModel.get()}' AND Color = '{inputColor.get()}'")
    temp=task.fetchone()
    if temp is not None:
        id_Producto=temp[0]
    else:
        id_Producto=0
    return id_Producto

def retornarIdCategoria():
    task.execute(f"SELECT Id_Categoria FROM Categoría WHERE Nombre_Categoria = '{selection.get()}'")
    temp=task.fetchone()
    if temp is not None:
        id_Categoria=temp[0]
    else:
        id_Categoria=0
    return id_Categoria

def retornarIdProveedor():
    task.execute(f"SELECT Id_Proveedor FROM Proveedor WHERE Nombre_proveedor = '{selection2.get()}'")
    temp=task.fetchone()
    if temp is not None:
        id_Proveedor=temp[0]
    else:
        id_Proveedor=0
    return id_Proveedor

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
        task.execute(f"INSERT INTO Inventario(Id_Producto,Id_Proveedor,Stock_Producto,Fecha_Adquisicion) VALUES('{retornarId()}','{retornarIdProveedor()}','{stockInput.get()}','{dateInput.get()}')")
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
                task.execute(f"INSERT INTO Inventario(Id_Producto,Id_Proveedor,Stock_Producto,Fecha_Adquisicion) VALUES('{retornarId()}','{retornarIdProveedor()}','{stockInput.get()}','{dateInput.get()}')")
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
    inputDetalles=tk.Entry(contenidoWindow,width=40,justify='center')
    inputDetalles.pack(pady=(5,20))
    guardarContenido=tk.Button(contenidoWindow,text="Guardar",width=10,font=("Calibri",12),command=insertarSolucion)
    guardarContenido.pack()

def insertarRegistros(): #Inserta registros sencillos
    if(extra.get()==""): #si no posee ningún dato extra en el producto
        if(evaluarSiExiste()): #Evalua que el registro no exista si existe no tiene caso volver a agregarlo
            try:#intenta hacer la inserción
                task.execute(f"INSERT INTO Producto(Modelo,Nom_producto,Id_Categoria,Marca,Material,Color,Precio_venta,Costo_Adquisicion) VALUES('{inputModel.get()}','{inputName.get()}',{retornarIdCategoria()},'{inputMarca.get()}','{inputMaterial.get()}','{inputColor.get()}',{float(inputPrecio.get())},{float(inputCosto.get())})")   
                conexion.commit()
                task.execute(f"INSERT INTO Inventario(Id_Producto,Id_Proveedor,Stock_Producto,Fecha_Adquisicion) VALUES('{retornarId()}','{retornarIdProveedor()}','{stockInput.get()}','{dateInput.get()}')")
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
        int(stockInput.get()) ### Me quedé aquí ### 
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
    task.execute(f"SELECT Id_Proveedor FROM Proveedor WHERE Nombre_proveedor = '{selection2.get()}'")
    result2=task.fetchone()
    if result2 is None:
        flotante=False
    else:
        flotante=True
    evaluateModel=(len(inputModel.get())<=45)
    evaluateName=(len(inputName.get())<=45)
    evaluateMarca=(re.match("^[a-zA-Z\s]+$",inputMarca.get()) and len(inputMarca.get())<=20)
    evaluateMaterial=(re.match("^[a-zA-Z\s]+$",inputMaterial.get()) and len(inputMaterial.get())<=10)
    evaluateColor=(re.match("^[a-zA-Z\s]+$",inputColor.get()) and len(inputColor.get())<=20)
    evaluarFecha=True if ("/" in dateInput.get() or "-" in dateInput.get() and re.match(r"^([0-9]{4})(-|/)([0-9]{1,2})(-|/)([0-9]{1,2})$",dateInput.get()) is not None) else False
    if(len(dateInput.get())==10):
        evaluarFecha=True
    else:
        evaluarFecha=False
        print("falso")
    if(evaluateModel and evaluateName and evaluateMarca and evaluateMaterial and evaluateColor and flotante and evaluarFecha):
        insertarRegistros()
    else:
        messagebox.showerror("Entradas incorrectas","Por favor, ingrese datos correctos.")

def ingresarRegistro(event): #genera una ventana para ingresar datos en producto
    global registro
    registro=tk.Toplevel(root)
    registro.geometry("680x460")
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
    options=[]
    try:
        task.execute("SELECT * FROM Categoría")
        temp1=task.fetchall()
        for op in temp1:
            options.append(op[1])
    except ValueError:
        pass
    global selection
    selection=tk.StringVar()
    selection.set("Seleccionar")
    if(len(options) != 0):
        menuCategory=tk.OptionMenu(registro,selection,*options) #modificar
        menuCategory.grid(row=2,column=1,sticky='w',padx=10)
    else:
        menuCategory=tk.OptionMenu(registro,selection,"") #modificar
        menuCategory.grid(row=2,column=1,sticky='w',padx=10)
    labelCategory=tk.Label(registro,text="Categoría",font=("Calibri",14),padx=20)
    labelCategory.grid(row=2,column=0,sticky='w')

    #Marca 
    marcaLabel=tk.Label(registro,text="Marca del producto",font=("Calibri",14),padx=20)
    marcaLabel.grid(row=3,column=0,sticky='w')
    global inputMarca
    inputMarca=tk.Entry(registro,width=50,justify='left')
    inputMarca.grid(row=3,column=1)

    #material
    materialLabel=tk.Label(registro,text="Material de fabricación",font=("Calibri",14),padx=20)
    materialLabel.grid(row=4,column=0,sticky='w')
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
    option0.place(x=20,y=330)
    option1=tk.Radiobutton(registro,text="Posee graduación",variable=extra,value="graduacion")
    option1.place(x=180,y=330)
    option2=tk.Radiobutton(registro,text="Posee líquido",variable=extra,value="liquido")
    option2.place(x=360,y=330)

    #Agregar a inventario
    opciones=[]
    global selection2
    selection2=tk.StringVar()
    selection2.set("Seleccionar")
    proveedor=tk.Label(registro,text="Proveedor del producto",font=("Calibri",14),padx=20)
    proveedor.grid(row=8,column=0,sticky='w')
    try:
        task.execute("SELECT * FROM Proveedor")
        temp=task.fetchall()
        for op2 in temp:
            opciones.append(op2[1])
    except:
        pass
    if(len(opciones)!=0):
        menuProveedor=tk.OptionMenu(registro,selection2,*opciones) #modificar
        menuProveedor.grid(row=8,column=1,sticky='w',padx=10)
    else:
        menuProveedor=tk.OptionMenu(registro,selection2,"") #modificar
        menuProveedor.grid(row=8,column=1,sticky='w',padx=10)

    #stock
    global stockInput
    stock=tk.Label(registro,text="Cantidad de stock disponible",font=("Calibri",14),padx=20)
    stock.grid(row=9,column=0,sticky='w')
    stockInput=tk.Entry(registro,width=50,justify='left')
    stockInput.grid(row=9,column=1)

    #fecha de adquisición
    global dateInput
    date=tk.Label(registro,text="Fecha en la que se adquirió el producto",font=("Calibri",14),padx=20)
    date.grid(row=10,column=0,sticky='w')
    dateInput=tk.Entry(registro,width=50,justify='left')
    dateInput.insert(0,"yyyy/mm/dd")
    dateInput.grid(row=10,column=1)

    #Enviar
    send=tk.Button(registro,text="Guardar",width=10,font=("Calibri",14),command=evaluarRegistros)
    send.place(x=230,y=360)


#función para agregar proveedores
def addSeller(event):
    def resetValues():
        nameInput.delete(0,tk.END)
        nombreInput.delete(0,tk.END)
        pInput.delete(0,tk.END)
        mInput.delete(0,tk.END)
        addresInput.delete(0,tk.END)
        phoneInput.delete(0,tk.END)
        mailInput.delete(0,tk.END)
        webSiteInput.delete(0,tk.END)
    def returnValues():
        name=nameInput.get()
        nombre=nombreInput.get()
        paterno=pInput.get()
        materno=mInput.get()
        addres=addresInput.get()
        phone=phoneInput.get()
        mail=mailInput.get()
        webSite=webSiteInput.get()
        value(name,nombre,paterno,materno,addres,phone,mail,webSite)

    def value(name,nombre,paterno,materno,addres,phone,mail,webSite):
        if(len(name) <= 45 and name!="" and len(nombre) <= 45 and nombre!="" and len(paterno) <= 45 and paterno!="" and len(materno) <= 45 and len(addres) <= 100 and addres!="" and len(phone) == 10 and phone.isdigit() and len(mail) <= 70 and mail!="" and len(webSite) <= 200):
            try:
                task.execute(f"SELECT 1 FROM Proveedor WHERE Nombre_proveedor = '{name}' AND Sitio_web = '{webSite}'")
                temp=task.fetchone()
                if temp is not None:
                    result=True
                else:
                    result=False
            except ValueError:
                messagebox.showerror("Error","Ha ocurrido un error inesperado.")
            if(result==False):
                insertProveedor(name,nombre,paterno,materno,addres,phone,mail,webSite)
            else:
                messagebox.showwarning("Dato ya ingresado","El registro ya existe.")
        else:
            messagebox.showwarning("Datos incorrectos","Por favor, ingrese datos correctos en los campos")

    def insertProveedor(name,nombre,paterno,materno,addres,phone,mail,webSite):
        try:
            task.execute(f"INSERT INTO Proveedor(Nombre_proveedor,Nombre_representante,Paterno_representante,Materno_representante,Direccion,Telefono,Correo,Sitio_web) VALUES('{name}','{nombre}','{paterno}','{materno}','{addres}','{phone}','{mail}','{webSite}')")
            conexion.commit()
            messagebox.showinfo("Datos insertado con éxito!","Los datos han sido guardados exitosamente.")
            resetValues()
        except ValueError:
            messagebox.showerror("Error","Ha ocurrido un error inesperado.")

    seller=tk.Toplevel(root)
    seller.geometry("580x330")
    seller.title("Agregar proveedor")
    #me quedé aquí!!!!
    name=tk.Label(seller,text="Nombre del proveedor",font=("Calibri",12))
    name.grid(row=0,column=0,sticky='w',padx=(5,50),pady=4)
    nameInput=tk.Entry(seller,width=50,justify='left')
    nameInput.grid(row=0,column=1)

    nombre=tk.Label(seller,text="Nombre del representante",font=("Calibri",12))
    nombre.grid(row=1,column=0,sticky='w',padx=(5,50),pady=4)
    nombreInput=tk.Entry(seller,width=50,justify='left')
    nombreInput.grid(row=1,column=1)

    apellidoP=tk.Label(seller,text="Apellido paterno del representante",font=("Calibri",12))
    apellidoP.grid(row=2,column=0,sticky='w',padx=(5,20),pady=4)
    pInput=tk.Entry(seller,width=50,justify='left')
    pInput.grid(row=2,column=1)

    apellidoM=tk.Label(seller,text="Apellido materno del representante",font=("Calibri",12))
    apellidoM.grid(row=3,column=0,sticky='w',padx=(5,20),pady=4)
    mInput=tk.Entry(seller,width=50,justify='left')
    mInput.grid(row=3,column=1)

    addres=tk.Label(seller,text="Dirección",font=("Calibri",12))
    addres.grid(row=4,column=0,sticky='w',padx=(5,20),pady=4)
    addresInput=tk.Entry(seller,width=50,justify='left')
    addresInput.grid(row=4,column=1)

    phone=tk.Label(seller,text="Teléfono de contacto",font=("Calibri",12))
    phone.grid(row=5,column=0,sticky='w',padx=(5,20),pady=4)
    phoneInput=tk.Entry(seller,width=50,justify='left')
    phoneInput.grid(row=5,column=1)

    mail=tk.Label(seller,text="Correo de contacto",font=("Calibri",12))
    mail.grid(row=6,column=0,sticky='w',padx=(5,20),pady=4)
    mailInput=tk.Entry(seller,width=50,justify='left')
    mailInput.grid(row=6,column=1)

    webSite=tk.Label(seller,text="Sitio web de contacto",font=("Calibri",12))
    webSite.grid(row=7,column=0,sticky='w',padx=(5,20),pady=4)
    webSiteInput=tk.Entry(seller,width=50,justify='left')
    webSiteInput.grid(row=7,column=1)

    save=tk.Button(seller,text="Guardar",font=("Arial",12),width=10,command=returnValues)
    save.place(x=260,y=280)

def guardarEvento(evento):
    messagebox.showinfo("Funciona","El evento funcionó!")

def visualizarInv(): #Por el momento queda así  
    visualizacion=tk.Toplevel(root)
    visualizacion.geometry("950x400")
    visualizacion.config(bg="#D9E2F3")
    visualizacion.title("Productos en inventario")
    producto=ttk.Treeview(visualizacion,columns=('Id_Producto','Modelo','Nom_Producto','Categoría','Marca','Material','Color','Precio_De_Venta','Costo_De_Adquisición','Proveedor','Stock','Fecha_Adquisicion'),show='headings')
    producto.place(x=24,y=20,width=890,height=350)
    producto.heading('Id_Producto',text='Id_Producto')
    producto.heading('Modelo',text='Modelo')
    producto.heading('Nom_Producto',text='Nombre del producto')
    producto.heading('Categoría',text='Categoría')
    producto.heading('Marca',text='Marca')
    producto.heading('Material',text='Material')
    producto.heading('Color',text='Color')
    producto.heading('Precio_De_Venta',text='Precio de venta')
    producto.heading('Costo_De_Adquisición',text='Costo de adquisición')
    producto.heading('Proveedor',text='Proveedor')
    producto.heading('Stock',text='Existencia de producto')
    producto.heading('Fecha_Adquisicion',text='Fecha de aquisición')
    producto.column('Id_Producto',anchor='center')
    producto.column('Modelo',anchor='center')
    producto.column('Nom_Producto',anchor='center')
    producto.column('Categoría',anchor='center')
    producto.column('Marca',anchor='center')
    producto.column('Material',anchor='center')
    producto.column('Color',anchor='center')
    producto.column('Precio_De_Venta',anchor='center')
    producto.column('Costo_De_Adquisición',anchor='center')
    producto.column('Proveedor',anchor='center')
    producto.column('Stock',anchor='center')
    producto.column('Fecha_Adquisicion',anchor='center')
    scrolledBar=ttk.Scrollbar(visualizacion,orient='horizontal',command=producto.xview)
    scrolledBar.pack(side='bottom',fill='x',pady=5,padx=20)
    producto.configure(yscrollcommand=scrolledBar.set)
    task.execute("SELECT * FROM Producto")
    datos=task.fetchall()
    for dato in datos:
        insercion=list(dato)
        if dato is not None:
            try:
                task.execute(f"SELECT Nombre_Categoria FROM Categoría WHERE Id_Categoria = {dato[3]}")
                temp=task.fetchone()
                insercion[3]=temp
                task.execute(f"SELECT Id_Proveedor FROM Inventario WHERE Id_Producto = {dato[0]}")
                temp=task.fetchone()
                task.execute(f"SELECT Nombre_proveedor FROM Proveedor WHERE Id_Proveedor = {temp[0]}")
                temp=task.fetchone()
                insercion.append(temp[0])
                task.execute(f"SELECT Stock_Producto FROM Inventario WHERE Id_Producto = {dato[0]}")
                temp=task.fetchone()
                insercion.append(temp[0])
                task.execute(f"SELECT Fecha_Adquisicion FROM Inventario WHERE Id_Producto = {dato[0]}")
                temp=task.fetchone()
                insercion.append(temp[0])
            except:
                pass
        producto.insert('','end',values=insercion)

def visualizarProveedores():
    visualizacion=tk.Toplevel(root)
    visualizacion.geometry("950x400")
    visualizacion.config(bg="#D9E2F3")
    visualizacion.title("Proveedores")
    tabla=ttk.Treeview(visualizacion,columns=('Id_Proveedor','Nombre_Proveedor','Nombre_Representante','Paterno_Representante','Materno_Representante','Direccion','Telefono','Correo','Sitio_Web'),show='headings')
    tabla.place(x=24,y=20,width=890,height=350)
    tabla.heading('Id_Proveedor',text='Id del proveedor')
    tabla.heading('Nombre_Proveedor',text='Nombre de la empresa')
    tabla.heading('Nombre_Representante',text='Nombres del representante')
    tabla.heading('Paterno_Representante',text='Apellido paterno del representante')
    tabla.heading('Materno_Representante',text='Apellido materno del representante')
    tabla.heading('Direccion',text='Direccion de la empresa')
    tabla.heading('Telefono',text='Telefono de contacto')
    tabla.heading('Correo',text='Correo de contacto')
    tabla.heading('Sitio_Web',text='Página de contacto')
    tabla.column('Id_Proveedor',anchor='center')
    tabla.column('Nombre_Proveedor',anchor='center')
    tabla.column('Nombre_Representante',anchor='center')
    tabla.column('Paterno_Representante',anchor='center')
    tabla.column('Materno_Representante',anchor='center')
    tabla.column('Direccion',anchor='center')
    tabla.column('Telefono',anchor='center')
    tabla.column('Correo',anchor='center')
    tabla.column('Sitio_Web',anchor='center')
    scrolledBar=ttk.Scrollbar(visualizacion,orient='horizontal',command=tabla.xview)
    scrolledBar.pack(side='bottom',fill='x',pady=5,padx=20)
    tabla.configure(yscrollcommand=scrolledBar.set)
    try:
        task.execute("SELECT * FROM Proveedor")
        datos=task.fetchall()
        for dato in datos:
            tabla.insert('','end',values=dato)
    except:
        messagebox.showerror("Error en la consulta","Ha ocurrido un error inesperado")
    
def updateInv():
    def busquedas(*args):
        texto=busqueda.get()
        task.execute(f"SELECT Nom_Producto FROM Producto WHERE Nom_Producto LIKE '%{texto}%'")
        temp=task.fetchall()
        for i in produc.get_children():
            produc.delete(i)
        for data in temp:
            produc.insert('','end',values=data)
    def seleccion(event):
        selecc=produc.selection()
        datos=produc.item(selecc,'values')[0]
        print(datos)

    visualizacion=tk.Toplevel(root)
    visualizacion.geometry("950x600")
    visualizacion.config(bg="#D9E2F3")
    visualizacion.title("Inventario")
    textOne=tk.Label(visualizacion,text="Elija un producto",font=("Arial",16),justify='center',bg="#D9E2F3")
    textOne.pack(pady=(10,0))
    #Contenedor
    container=tk.Frame(visualizacion,width=940,height=540,bg='lightblue')
    container.pack()
    container.grid_propagate(False)
    #Scroll text que contiene todos los productos
    produc=ttk.Treeview(container,columns=('Productos'),show='headings')
    produc.place(x=0,y=50,width=305,height=490)
    produc.heading('Productos',text='Productos')
    produc.column('Productos',anchor='center')
    produc.bind('<<TreeviewSelect>>',seleccion)
    try:
        task.execute("SELECT Nom_Producto FROM Producto")
        temp=task.fetchall()
        for data in temp:
            produc.insert('','end',values=data)
    except ValueError:
        messagebox.showerror("Error","Ha ocurrido un error inesperado")
    #Input de busqueda
    busqueda=tk.StringVar()
    busqueda.trace('w',busquedas)
    entrada=tk.Entry(container,width=23,justify='left',font=("Arial",18),textvariable=busqueda)
    entrada.grid(row=0,column=0,pady=(10,0))
    #datos a cambiar


#establece la conexion a la base de datos y se crea la variable que ejecuta los comandos SQL
conexion=my.connect(host="localhost",user="root",passwd="10022004AlexCruz9669",database="optilent")
task=conexion.cursor()

#se crea la ventana principal
root=tk.Tk()
root.title("Servicio de inventario")
root.geometry("920x650")
root.config(bg="#D9E2F3")

#Cabezal
head=tk.Frame(root,width=830,height=100,bg="#4472C4")
head.pack(pady=20)
head.propagate(False)
titular=tk.Label(head,text="OPTILENT",font=("Times",55),bg="#4472C4")
titular.pack()
imagen=Image.open("lentes.png")
imagen=imagen.resize((170,170))
photo=ImageTk.PhotoImage(imagen)
lentes=tk.Label(head,image=photo,bg="#4472C4")
lentes.place(x=60,y=-40)

#Bienvenido
welcome=tk.Label(root,text="¡Bienvenido!",font=("Arial",36),justify='center',bg="#D9E2F3")
welcome.pack()

#Main
main=tk.Frame(root,width=790,height=420,bg="#FFD966")
main.pack()
main.propagate(False)
#Texto de selección
cuadro1=tk.Frame(main,width=600,height=40,bg='white',highlightbackground="black",highlightthickness=2)
cuadro1.pack(pady=(30,0))
cuadro1.grid_propagate(False)
textInicio=tk.Label(cuadro1,text="SELECCIONE SU OPCION",font=("Arial",18),bg="white",justify='left')
textInicio.grid(row=0,column=0,sticky='w')
#contenido
cuadro2=tk.Frame(main,width=600,height=200,bg="white",highlightbackground="black",highlightthickness=2)
cuadro2.pack(pady=(20,0))
cuadro2.propagate(False)
#inventario (EN REMODELACIÓN)
updateInventory=tk.Button(cuadro2,text="Actualizar datos en inventario",font=("Arial",16),justify='center',command=updateInv)
updateInventory.config(bg='White',relief='flat',width=600)
updateInventory.pack(pady=(5,0))
#Proveedores (EN REMODELACIÓN)
updateProveedor=tk.Button(cuadro2,text="Actualizar datos de proveedor",font=("Arial",16),justify='center')
updateProveedor.config(bg='White',relief='flat',width=600)
updateProveedor.pack(pady=(5,0))
#visualizacion inventario
visualizarInventario=tk.Button(cuadro2,text="VISUALIZAR INVENTARIO",command=visualizarInv)
visualizarInventario.config(bg="white",relief='flat',width=600,font=("Arial",16))
visualizarInventario.pack(pady=(5,0))
#visualizar proveedores
visualizarProveedores=tk.Button(cuadro2,text="VISUALIZAR PROVEEDORES",command=visualizarProveedores)
visualizarProveedores.config(bg="white",relief='flat',width=600,font=("Arial",16))
visualizarProveedores.pack(pady=(5,0))
#boton de guardar
guardar=tk.Canvas(main,width=200,height=150,bg="#FFD966",highlightbackground="#FFD966")
guardar.place(x=60,y=290)
guardar.propagate(False)
labelG=tk.Label(guardar,text="AGREGAR REGISTRO",font=("Arial",12),justify='center',bg="#323f4f",fg="white")
labelG.place(x=20,y=45)
labelG.bind('<Button-1>',ingresarRegistro)
circle=guardar.create_oval(10,10,200,110,fill='#323f4f')

agregarProv=tk.Canvas(main,width=200,height=150,bg="#FFD966",highlightbackground="#FFD966")
agregarProv.place(x=520,y=290)
agregarProv.propagate(False)
labelA=tk.Label(agregarProv,text="AGREGAR PROVEEDOR",font=("Arial",11),justify='center',bg="#323f4f",fg='white')
labelA.place(x=15,y=45)
labelA.bind('<Button-1>',addSeller)
circle2=agregarProv.create_oval(10,10,200,110,fill='#323f4f')


# add=tk.Button(main,text="Agregar registro",command=ingresarRegistro) #evento principal, se modificará 
# add.place(x=100,y=50)

# addProveedor=tk.Button(main,text="Agregar proveedor",command=addSeller)
# addProveedor.pack(pady=40)

root.mainloop()
