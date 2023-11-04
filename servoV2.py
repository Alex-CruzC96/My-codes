import tkinter as tk
import serial

arduino = serial.Serial('COM4', 9600)

def enviar_a_arduino(motor, val):
    arduino.write('{} {}\n'.format(motor, val).encode())

root = tk.Tk()

for i in range(4):
    scale = tk.Scale(root, from_=0, to=180, length=400, orient='horizontal', command=lambda val, i=i: enviar_a_arduino(i, val))
    scale.set(90)
    scale.pack()

root.mainloop()
