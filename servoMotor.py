import tkinter as tk
import serial as ser

def ask_quit():
    root.destroy()
    conex.close()

def angle(int):
    angleData=str(control.get())
    conex.write((angleData+'\n').encode())

def enviar_angulos(*args):
    # Lee los valores de los deslizadores
    angulo1 = control.get()
    angulo2 = control2.get()
    angulo3 = control3.get()
    # Crea una cadena con los ángulos separados por comas
    data = '{},{},{}\n'.format(angulo1, angulo2, angulo3)
    # Envía la cadena al Arduino
    conex.write(data.encode())


root=tk.Tk()
root.geometry("240x250")
root.title("Brazo robot")
root.protocol("WM_DELETE_WINDOW",)
conex=ser.Serial("COM4",9600)

control=tk.Scale(root,from_=0,to=180,orient="horizontal",command=enviar_angulos,length=400)
control.pack()

control2=tk.Scale(root,from_=0,to=180,orient="horizontal",command=enviar_angulos,length=400)
control2.pack()

control3=tk.Scale(root,from_=0,to=180,orient="horizontal",command=enviar_angulos,length=400)
control3.pack()

root.mainloop()