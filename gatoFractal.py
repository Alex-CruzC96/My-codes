import tkinter as tk

root=tk.Tk()
root.geometry("750x750")

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
                tk.Frame(cat[0][0],bg="#FFE4D6",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][0],bg="#FFE4D6",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][0],bg="#FFE4D6",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[0][0],bg="#FFE4D6",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][0],bg="#FFE4D6",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][0],bg="#FFE4D6",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[0][0],bg="#FFE4D6",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][0],bg="#FFE4D6",width=75,height=75,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][0],bg="#FFE4D6",width=75,height=75,highlightbackground="purple",highlightthickness=2)
            ]
        ],
        [
            [
                tk.Frame(cat[0][1],bg="#FFE4D6",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][1],bg="#FFE4D6",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][1],bg="#FFE4D6",width=81,height=81,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[0][1],bg="#FFE4D6",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][1],bg="#FFE4D6",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][1],bg="#FFE4D6",width=81,height=81,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[0][1],bg="#FFE4D6",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][1],bg="#FFE4D6",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][1],bg="#FFE4D6",width=81,height=81,highlightbackground="purple",highlightthickness=2)
            ]
        ],
        [
            [
                tk.Frame(cat[0][2],bg="#FFE4D6",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][2],bg="#FFE4D6",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][2],bg="#7C96AB",width=81,height=81,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[0][2],bg="#7C96AB",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][2],bg="#7C96AB",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][2],bg="#7C96AB",width=81,height=81,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[0][2],bg="lightblue",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][2],bg="lightblue",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[0][2],bg="lightblue",width=81,height=81,highlightbackground="purple",highlightthickness=2)
            ]
        ]
    ],
        
    [
        [
            [
                tk.Frame(cat[1][0],bg="lightblue",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][0],bg="lightblue",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][0],bg="lightblue",width=81,height=81,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[1][0],bg="lightblue",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][0],bg="lightblue",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][0],bg="lightblue",width=81,height=81,highlightbackground="purple",highlightthickness=2)
            ],
            [
                tk.Frame(cat[1][0],bg="lightblue",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][0],bg="lightblue",width=81,height=81,highlightbackground="purple",highlightthickness=2),
                tk.Frame(cat[1][0],bg="lightblue",width=81,height=81,highlightbackground="purple",highlightthickness=2)
            ]
        ],
        [
            [
                tk.Frame(cat[1][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[1][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[1][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ],
            [
                tk.Frame(cat[1][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[1][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[1][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ],
            [
                tk.Frame(cat[1][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[1][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[1][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ]
        ],
        [
            [
                tk.Frame(cat[1][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[1][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[1][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ],
            [
                tk.Frame(cat[1][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[1][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[1][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ],
            [
                tk.Frame(cat[1][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[1][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[1][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ]
        ]
    ],

    [
        [
            [                
                tk.Frame(cat[2][0],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][0],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][0],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ],
            [
                tk.Frame(cat[2][0],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][0],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][0],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ],
            [
                tk.Frame(cat[2][0],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][0],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][0],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ]
        ],
        [
            [
                tk.Frame(cat[2][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ],
            [
                tk.Frame(cat[2][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ],
            [
                tk.Frame(cat[2][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][1],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ]
        ],
        [
            [
                tk.Frame(cat[2][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ],
            [
                tk.Frame(cat[2][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
            ],
            [
                tk.Frame(cat[2][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2),
                tk.Frame(cat[2][2],bg="lightblue",width=81,height=81,highlightbackground="white",highlightthickness=2)
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



littleCats[1][1][1][1].config(bg="purple")

root.mainloop()
