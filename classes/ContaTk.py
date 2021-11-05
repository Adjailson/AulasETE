import tkinter as tk
from tkinter import messagebox
from Conta import Conta

#classe ContaTk é front-end
class ContaTk:

    c = Conta(1000)
    
    def __init__(self):
        self.jan = tk.Tk()
        self.f1 = tk.Frame(self.jan)
        self.f2 = tk.Frame(self.jan)

        #Fazendo o objeto sem função
        titulo = tk.Label(self.f1,
                          text="Bem Vindo a Conta XY",
                          font=("Arial",25))
        titulo.grid(row=0, column=0)

        #Fazendo com o uso da função
        self.inf = self.Texto("Saldo Conta R$ "+str(self.c.getSaldo()),"00","green")
        btnDeposito = self.Botao("Depositar","10",self.deposito)
        btnSaque = self.Botao("Saque","11",self.saque)
        self.valor = self.TextoCampoCompleto("Valor R$","20","0")

        self.f1.pack()
        self.f2.pack()
        self.jan.geometry("450x200")
        self.jan.resizable(0,0)
        self.jan.mainloop()

    #Manipulação do back-end pelo front-end
    def deposito(self):
        if(self.c.depositar(float(self.valor.get()))):
            messagebox.showinfo("Sistema", "Deposito realizado com sucesso!")
        else:
            messagebox.showinfo("Sistema", "Limites excedidos!")
        self.atualizarSaldo()
        
    def saque(self):
        msg = self.c.saque(float(self.valor.get()))
        messagebox.showinfo("Sistema", msg)
        self.atualizarSaldo()
        
    def atualizarSaldo(self):
        self.inf['text'] = "Saldo Conta R$ "+str(self.c.getSaldo())

    #Funções para gerar interface gráfica
    '''@return Label'''
    def Texto(self,texto,posicao,cor=str):
        objeto = tk.Label(self.f2,text=texto,
                          fg=cor,
                          font=("Arial",17))
        objeto.grid(row=posicao[0],column=posicao[1])
        return objeto
    
    '''@return Button'''
    def Botao(self,texto,posicao,evento=object):
        objeto = tk.Button(self.f2,text=texto,
                           font=("Arial",17),
                           width=10,
                           command=evento)
        objeto.grid(row=posicao[0], column=posicao[1])
        return objeto
    
    '''@return Entry'''
    def CampoTexto(self,posicao):
        objeto = tk.Entry(self.f2,
                          font=("Arial",17))
        objeto.grid(row=posicao[0],column=posicao[1])
        return objeto
    
    '''@return Entry acompanhado de Label'''
    def TextoCampoCompleto(self,texto,posicao,infor=""):
        label = tk.Label(self.f2,text=texto,
                         font=("Arial",17))
        label.grid(row=posicao[0], column=posicao[1])

        proxima = (int(posicao[1]))+1
        objeto = tk.Entry(self.f2,
                          font=("Arial",17))
        objeto.insert(0,infor)
        objeto.grid(row=posicao[0],column=proxima, pady=10)
        return objeto
    
ContaTk()
