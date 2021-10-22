import tkinter as tk
from Calculadora import Calculadora

class CalculadoraTk:

    cal = Calculadora()
    cal.setBotoes([["8","9","3","+"],
                   ["7","6",".","x"]
                   ])
    cal.setAltura(150)
    cal.setLargura(150)

    def __init__(self):
        self.jan = tk.Tk()
        self.jan.geometry(str(self.cal.getLargura())+"x"+
                          str(self.cal.getAltura()))
        self.jan.resizable(False,False)

        self.f1 = tk.Frame(self.jan)
        self.f2 = tk.Frame(self.jan)

        self.visor = tk.Entry(self.f1,width=11,
                              justify="right",
                              font=("",17))
        self.visor.insert(0,"0")
        self.visor.grid(row=0, column=0)

        self.gerarBotoes()

        self.f1.pack()
        self.f2.pack()
        self.jan.mainloop()

    def gerarBotoes(self):
        for linha in range(len(self.cal.getBotoes())):
            for coluna in range(len(self.cal.getBotoes()[linha])):
                texto = self.cal.getBotoes()[linha][coluna]
                btn = tk.Button(self.f2,text=texto,
                                font=("Arial",17),
                                width=2)
                btn.grid(row=linha, column=coluna)

CalculadoraTk()
