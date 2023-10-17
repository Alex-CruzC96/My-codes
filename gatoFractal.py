import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.geometry("690x690")
root.title("Gato Fractal!")

cat=[
    [
        tk.Frame(root,bg="purple",width=250,height=250,highlightbackground="white",highlightthickness=2),
        tk.Frame(root,bg="purple",width=250,height=250,highlightbackground="white",highlightthickness=2),
        tk.Frame(root,bg="purple",width=250,height=250,highlightbackground="white",highlightthickness=2)
    ],
    [
        tk.Frame(root,bg="purple",width=250,height=250,highlightbackground="white",highlightthickness=2),
        tk.Frame(root,bg="purple",width=250,height=250,highlightbackground="white",highlightthickness=2),
        tk.Frame(root,bg="purple",width=250,height=250,highlightbackground="white",highlightthickness=2)
    ],
    [
        tk.Frame(root,bg="purple",width=250,height=250,highlightbackground="white",highlightthickness=2),
        tk.Frame(root,bg="purple",width=250,height=250,highlightbackground="white",highlightthickness=2),
        tk.Frame(root,bg="purple",width=250,height=250,highlightbackground="white",highlightthickness=2)
    ]
]


littleCats=[

    [
        [
            [
                tk.Frame(cat[0][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[0][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[0][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ]
        ],
        [
            [
                tk.Frame(cat[0][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[0][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[0][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ]
        ],
        [
            [
                tk.Frame(cat[0][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[0][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[0][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ]
        ]
    ],
        
    [
        [
            [
                tk.Frame(cat[1][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[1][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[1][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ]
        ],
        [
            [
                tk.Frame(cat[1][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[1][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[1][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ]
        ],
        [
            [
                tk.Frame(cat[1][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[1][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[1][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ]
        ]
    ],

    [
        [
            [
                tk.Frame(cat[2][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[2][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[2][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][0],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ]
        ],
        [
            [
                tk.Frame(cat[2][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[2][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[2][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][1],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ]
        ],
        [
            [
                tk.Frame(cat[2][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[2][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[2][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[2][2],bg="#B7B7B7",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ]
        ]
    ]
]

labels=[
    [
        [
            [
                tk.Label(littleCats[0][0][0][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][0][0][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][0][0][2],text="",font=("Arial",32),bg="#B7B7B7"),
            ],
            [
                tk.Label(littleCats[0][0][1][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][0][1][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][0][1][2],text="",font=("Arial",32),bg="#B7B7B7"),
            ],
            [
                tk.Label(littleCats[0][0][2][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][0][2][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][0][2][2],text="",font=("Arial",32),bg="#B7B7B7"), 
            ]
        ],
        [
            [
                tk.Label(littleCats[0][1][0][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][1][0][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][1][0][2],text="",font=("Arial",32),bg="#B7B7B7"),
            ],
            [
                tk.Label(littleCats[0][1][1][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][1][1][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][1][1][2],text="",font=("Arial",32),bg="#B7B7B7"),
            ],
            [
                tk.Label(littleCats[0][1][2][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][1][2][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][1][2][2],text="",font=("Arial",32),bg="#B7B7B7"),
            ]
        ],
        [
            [
                tk.Label(littleCats[0][2][0][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][2][0][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][2][0][2],text="",font=("Arial",32),bg="#B7B7B7"),
            ],
            [
                tk.Label(littleCats[0][2][1][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][2][1][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][2][1][2],text="",font=("Arial",32),bg="#B7B7B7"),
            ],
            [
                tk.Label(littleCats[0][2][2][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][2][2][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[0][2][2][2],text="",font=("Arial",32),bg="#B7B7B7"),
            ]
        ]
    ],
    [
        [
            [
                tk.Label(littleCats[1][0][0][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][0][0][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][0][0][2],text="",font=("Arial",32),bg="#B7B7B7")
            ],
            [
                tk.Label(littleCats[1][0][1][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][0][1][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][0][1][2],text="",font=("Arial",32),bg="#B7B7B7")
            ],
            [
                tk.Label(littleCats[1][0][2][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][0][2][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][0][2][2],text="",font=("Arial",32),bg="#B7B7B7")
            ]
        ],
        [
            [
                tk.Label(littleCats[1][1][0][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][1][0][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][1][0][2],text="",font=("Arial",32),bg="#B7B7B7")
            ],
            [
                tk.Label(littleCats[1][1][1][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][1][1][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][1][1][2],text="",font=("Arial",32),bg="#B7B7B7")
            ],
            [
                tk.Label(littleCats[1][1][2][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][1][2][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][1][2][2],text="",font=("Arial",32),bg="#B7B7B7")
            ]
        ],
        [
            [
                tk.Label(littleCats[1][2][0][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][2][0][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][2][0][2],text="",font=("Arial",32),bg="#B7B7B7")
            ],
            [
                tk.Label(littleCats[1][2][1][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][2][1][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][2][1][2],text="",font=("Arial",32),bg="#B7B7B7")
            ],
            [
                tk.Label(littleCats[1][2][2][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][2][2][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[1][2][2][2],text="",font=("Arial",32),bg="#B7B7B7")
            ]
        ]
    ],
    [
        [
            [
                tk.Label(littleCats[2][0][0][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][0][0][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][0][0][2],text="",font=("Arial",32),bg="#B7B7B7")
            ],
            [
                tk.Label(littleCats[2][0][1][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][0][1][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][0][1][2],text="",font=("Arial",32),bg="#B7B7B7")
            ],
            [
                tk.Label(littleCats[2][0][2][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][0][2][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][0][2][2],text="",font=("Arial",32),bg="#B7B7B7")
            ]
        ],
        [
            [
                tk.Label(littleCats[2][1][0][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][1][0][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][1][0][2],text="",font=("Arial",32),bg="#B7B7B7")
            ],
            [
                tk.Label(littleCats[2][1][1][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][1][1][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][1][1][2],text="",font=("Arial",32),bg="#B7B7B7")
            ],
            [
                tk.Label(littleCats[2][1][2][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][1][2][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][1][2][2],text="",font=("Arial",32),bg="#B7B7B7")
            ]
        ],
        [
            [
                tk.Label(littleCats[2][2][0][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][2][0][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][2][0][2],text="",font=("Arial",32),bg="#B7B7B7")
            ],
            [
                tk.Label(littleCats[2][2][1][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][2][1][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][2][1][2],text="",font=("Arial",32),bg="#B7B7B7")
            ],
            [
                tk.Label(littleCats[2][2][2][0],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][2][2][1],text="",font=("Arial",32),bg="#B7B7B7"),
                tk.Label(littleCats[2][2][2][2],text="",font=("Arial",32),bg="#B7B7B7")
            ]
        ]
    ]
]

bigLabels=[
    [
        tk.Label(cat[0][0],text="",font=("Arial",120)),
        tk.Label(cat[0][1],text="",font=("Arial",120)),
        tk.Label(cat[0][2],text="",font=("Arial",120))
    ],
    [
        tk.Label(cat[1][0],text="",font=("Arial",120)),
        tk.Label(cat[1][1],text="",font=("Arial",120)),
        tk.Label(cat[1][2],text="",font=("Arial",120))
    ],
    [
        tk.Label(cat[2][0],text="",font=("Arial",120)),
        tk.Label(cat[2][1],text="",font=("Arial",120)),
        tk.Label(cat[2][2],text="",font=("Arial",120))
    ]
]


xActiva = False 
def principalEvent(event,rowOne,columnOne,row,column):
    global xActiva
    if(labels[rowOne][columnOne][row][column].cget("text")=="" and cat[rowOne][columnOne].cget("bg")!="red" and bigLabels[rowOne][columnOne].cget("text")==""):
        if (xActiva!=True):
            labels[rowOne][columnOne][row][column].config(text="X")      
            xActiva=True  
            evaluate(rowOne,columnOne)
            evaluate_bigLabels()
            blockingEvent(rowOne,columnOne,row,column)
        else:
            labels[rowOne][columnOne][row][column].config(text="O")
            xActiva=False
            
            evaluate(rowOne,columnOne)
            evaluate_bigLabels()
            blockingEvent(rowOne,columnOne,row,column)
    
def evaluate(rowOne,columnOne):
    combos=[
        #Combinaciones ganadoras horizontales
      [labels[rowOne][columnOne][0][0], labels[rowOne][columnOne][0][1], labels[rowOne][columnOne][0][2]],
      [labels[rowOne][columnOne][1][0], labels[rowOne][columnOne][1][1], labels[rowOne][columnOne][1][2]],
      [labels[rowOne][columnOne][2][0], labels[rowOne][columnOne][2][1], labels[rowOne][columnOne][2][2]],
        #Combinaciones ganadoras verticales
      [labels[rowOne][columnOne][0][0], labels[rowOne][columnOne][1][0], labels[rowOne][columnOne][2][0]],
      [labels[rowOne][columnOne][0][1], labels[rowOne][columnOne][1][1], labels[rowOne][columnOne][2][1]],
      [labels[rowOne][columnOne][0][2], labels[rowOne][columnOne][1][2], labels[rowOne][columnOne][2][2]],
        #Combinaciones ganadoras diagonales
      [labels[rowOne][columnOne][0][0], labels[rowOne][columnOne][1][1], labels[rowOne][columnOne][2][2]],
      [labels[rowOne][columnOne][0][2], labels[rowOne][columnOne][1][1], labels[rowOne][columnOne][2][0]]
    ]
    for combo in combos:
        a,b,c=combo
        if(a.cget("text")=="X" and b.cget("text")=="X" and c.cget("text")=="X"):
            messagebox.showinfo("Ganó X!","Felicidades, ganaste!")
            bigLabels[rowOne][columnOne].config(text="X")
            global xActiva
            xActiva= not xActiva
        if(a.cget("text")=="O" and b.cget("text")=="O" and c.cget("text")=="O"):
            messagebox.showinfo("Ganó O!","Felicidades, ganaste!")
            bigLabels[rowOne][columnOne].config(text="O")
            xActiva= not xActiva
        

def evaluate_bigLabels():
    combos=[
        #Combinaciones ganadoras horizontales
      [bigLabels[0][0], bigLabels[0][1], bigLabels[0][2]],
      [bigLabels[1][0], bigLabels[1][1], bigLabels[1][2]],
      [bigLabels[2][0], bigLabels[2][1], bigLabels[2][2]],
        #Combinaciones ganadoras verticales
      [bigLabels[0][0], bigLabels[1][0], bigLabels[2][0]],
      [bigLabels[0][1], bigLabels[1][1], bigLabels[2][1]],
      [bigLabels[0][2], bigLabels[1][2], bigLabels[2][2]],
        #Combinaciones ganadoras diagonales
      [bigLabels[0][2], bigLabels[1][1], bigLabels[2][0]],
      [bigLabels[0][0], bigLabels[1][1], bigLabels[2][2]]
    ]
    for combo in combos:
        a,b,c=combo
        if(a.cget("text")=="X" and b.cget("text")=="X" and c.cget("text")=="X"):
            messagebox.showinfo("Ganó X!","Felicidades, ganaste la partida!")            
            # global xActiva
            # xActiva= not xActiva
        if(a.cget("text")=="O" and b.cget("text")=="O" and c.cget("text")=="O"):
            messagebox.showinfo("Ganó O!","Felicidades, ganaste la partida!")
            #xActiva= not xActiva



def blockingEvent(rowOne,columnOne,row,column):
    for rowOne in range(3):
        for columnOne in range(3):
            if(cat[rowOne][columnOne]!=cat[row][column] and bigLabels[row][column].cget("text")==""):
                cat[rowOne][columnOne].config(bg="red")
                for r in range(3):
                    for c in range(3):
                        littleCats[rowOne][columnOne][r][c].config(bg="red")
                        labels[rowOne][columnOne][r][c].config(bg="red")
            else:
                cat[rowOne][columnOne].config(bg="purple")
                for r in range(3):
                    for c in range(3):
                        littleCats[rowOne][columnOne][r][c].config(bg="#B7B7B7")
                        labels[rowOne][columnOne][r][c].config(bg="#B7B7B7")

for row in range(3):
    for column in range(3):
        cat[row][column].grid(row=row,column=column)
        bigLabels[row][column].place(x=65,y=22)

for rowOne in range(3):
    for columnOne in range(3):
        for row in range(3):
            for column in range(3):
                littleCats[rowOne][columnOne][row][column].grid(row=row,column=column)
                littleCats[rowOne][columnOne][row][column].bind("<Button-1>",lambda eve=littleCats[rowOne][columnOne][row][column],one=rowOne,two=columnOne,three=row,four=column:principalEvent(eve,one,two,three,four))
                labels[rowOne][columnOne][row][column].place(x=19,y=10)


root.mainloop()
