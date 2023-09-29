import PySimpleGUI as sg

def farToGrades(value1):
    return ((value1-32)*5)/9

def gradesToFar(value1):
    return (value1*9/5)+32

# Elementos de la ventana 
layout = [
    [sg.Text("Ingrese los datos",font=("Comic_Sans",20),size=(50,1),justification='center',text_color='#FE7BE5',background_color='#313866')],
    [
        sg.InputText(size=(15,2),pad=((80,0),(10)),justification='center',key="InputOne"),
        sg.Button("F to C ->",font=('Comic_Sans',10),size=(7,1),pad=((70,0),(20)),button_color='#974EC3',border_width=0,key="ButtonOne"),
        sg.InputText(size=(15,2),pad=((76,0),(10)),justification='center',key="InputTwo"),
    ],
    [sg.Button("<- C to F",size=(7,1),pad=((260),(12)),button_color='#974EC3',border_width=0,key="ButtonTwo")],
    [sg.Button("Clear",size=(7,1),pad=((260),(20)),button_color='#974EC3',border_width=0,key="ButtonThree")]
]

window = sg.Window("Convertidor de grados", layout, size=(600, 300),background_color='#313866',icon="calculadora.ico")

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break;
    
    if event == "ButtonOne":
        try:
            value1=float(values["InputOne"])
            window["InputTwo"].Update("{:.2f}".format(farToGrades(value1)))  
        
        except ValueError:
            sg.popup_error(
                "Por favor, ingrese un número válido en el campo.",
                title="Error",
                background_color='#504099',
                text_color='#FE7BE5'
            )

    if event == "ButtonTwo":
        try:
            value1=float(values["InputTwo"])
            window["InputOne"].Update("{:.2f}".format(gradesToFar(value1)))

        except ValueError:
             sg.popup_error(
                "Por favor, ingrese un número válido en el campo.",
                title="Error",
                background_color='#504099',
                text_color='#FE7BE5'
            )


    if event == "ButtonThree":
        try:
            window["InputOne"].update("")
            window["InputTwo"].update("")
        except ValueError:
             sg.popup_error(
                "Por favor, ingrese un número válido en el campo.",
                title="Error",
                background_color='#504099',
                text_color='#FE7BE5'
            )

# Cierra la ventana al salir del bucle
window.close()
