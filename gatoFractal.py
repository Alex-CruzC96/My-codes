import tkinter as tk

root=tk.Tk()
root.geometry("690x690")

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

for rowOne in range(3):
    for columnOne in range(3):
        for row in range(3):
            for column in range(3):
                littleCats[rowOne][columnOne][row][column].grid(row=row,column=column)



for row in range(3):
    for column in range(3):
        cat[row][column].grid(row=row,column=column)

color_actual = '#B7B7B7'
def cambiar_color(event):                   
    global color_actual
    if color_actual == '#B7B7B7':
        event.config(bg='red')    
        event.config(state='disabled')
        color_actual = 'red'
        
        
    else:
        event.config(bg='#B7B7B7')
        color_actual = '#B7B7B7'
         

for rowOne in range(3):
    for columnOne in range(3):
        for row in range(3):
            for column in range(3):
                littleCats[rowOne][columnOne][row][column].bind("<Button-1>",lambda event,eve=littleCats[rowOne][columnOne][row][column]:cambiar_color(eve))                
                




root.mainloop()
