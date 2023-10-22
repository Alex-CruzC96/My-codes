import tkinter as tk
import serial as ser

def ask_quit():
    root.destroy()
    conex.close()

def angle(int):
    angleData=str(control.get())
    conex.write((angleData+'\n').encode())

root=tk.Tk()
root.geometry("240x50")
root.title("Brazo robot")
root.protocol("WM_DELETE_WINDOW",)
conex=ser.Serial("COM3",9600)

control=tk.Scale(root,from_=0,to=180,orient="horizontal",command=angle,length=400)
control.pack()

root.mainloop()