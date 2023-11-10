import tkinter as tk
from tkinter import filedialog
import shutil
import os
import cv2

def upload_image():
    file_path=filedialog.askopenfilename(filetypes=[("Image files","*.jpg;*.png")])
    if file_path:
        new_path="C:\\Users\\alexc\\Desktop\\Formularios"
        file_name = os.path.basename(file_path)
        
        # Combina la nueva ruta con el nombre del archivo
        new_file_path = os.path.join(new_path, file_name)
        
        # Copia el archivo a la nueva ubicación
        shutil.copy(file_path, new_file_path)
def take_photo():
    # Inicia la cámara
    cap = cv2.VideoCapture(0)

    while True:
        # Muestra la imagen de la cámara en una ventana
        ret, frame = cap.read()
        cv2.imshow('Presiona la tecla "s" para tomar una foto', frame)

        # Espera a que se presione la tecla 's' para tomar una foto
        if cv2.waitKey(1) & 0xFF == ord('s'):
            # Guarda la foto
            new_path = "C:\\Users\\alexc\\Desktop\\Formularios\\photo.jpg"
            cv2.imwrite(new_path, frame)
            break

    # Espera un momento antes de cerrar la ventana
    cv2.waitKey(1)
    # Cierra la ventana
    cv2.destroyAllWindows()

    # Libera la cámara
    cap.release()


root = tk.Tk()
button1 = tk.Button(root, text="Subir imagen", command=upload_image)
button1.pack()
button2 = tk.Button(root, text="Tomar foto", command=take_photo)
button2.pack()
root.mainloop()