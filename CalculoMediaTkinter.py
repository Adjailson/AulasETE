'''
Conceito utilizado: Classes e funções
Acompanhar as aulas presenciais para
explicações dos widgets e atributos
'''
import tkinter as tk
from tkinter import messagebox

class CalculoMediaTk:
    janela = tk.Tk()
    def __init__(self):
        self.layout = tk.Frame(self.janela,padx=20,pady=20)

        self.lb1 = tk.Label(self.layout)
        self.lb1.config(text="Digite valor 1:",
                        font=("Courier New",17))
        self.lb1.grid(row=0,column=0)
        
        self.v1 = tk.Entry(self.layout)
        self.v1.config(width=15,font=("Courier New",17))
        self.v1.insert(0,"0")
        self.v1.grid(row=1,column=0)

        self.lb2 = tk.Label(self.layout)
        self.lb2.config(text="Digite valor 2:",font=("Courier New",17))
        self.lb2.grid(row=2,column=0)

        self.v2 = tk.Entry(self.layout)
        self.v2.config(width=15,font=("Courier New",17))
        self.v2.insert(0,"0")
        self.v2.grid(row=3,column=0)

        self.btn = tk.Button(self.layout,command=self.media)
        self.btn.config(text="Calcular Média",font=("Courier New",17))
        self.btn.grid(row=4,column=0)
        
        self.layout.pack()
        self.janela.mainloop()

    def media(self):
        return
    
obj = CalculoMediaTk()
