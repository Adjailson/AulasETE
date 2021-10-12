import tkinter as tk
from Marcador import Marcador

class MarcadorTk:
    def __init__(self):
        '''Criar e configurar o objeto'''
        self.obj = Marcador()
        self.obj.setCor("Blue")#Verifique a tabela de cores
        self.obj.setLargura(10)
        self.obj.setAltura(20)
        self.obj.setTampa(True)
        self.obj.setMarca("Compactor")
        self.obj.setEspessuraPonta(1)

        '''Criar a janela'''
        self.jan = tk.Tk()

        self.desenharMarcadorTk()
        self.criarLinha(25,"H")
        
        self.jan.mainloop()

    '''Criar linha com Label do tkinter'''
    def criarLinha(self,tamanho,direcao):
        conf = self.obj.fazerLinha(tamanho,direcao)

        self.linha = tk.Label(self.jan,
                              bg=self.obj.getCor(),
                              width=conf[0],
                              height=conf[1])
        self.linha.grid(row=1,column=1,padx=10,pady=10)

    '''Desenhar o OBJETO com tkinter'''
    def desenharMarcadorTk(self):
        self.canudo = tk.Label(self.jan,
                            width=self.obj.getLargura(),
                            height=self.obj.getAltura(),
                            text=self.obj.getMarca(),
                            bg=self.obj.getCor(),
                            fg="#fff",
                            font=("Impact",14))
        self.canudo.grid(row=1,column=0,padx=10)
        if(self.obj.getTampa()):
            self.tampa = tk.Label(self.jan,
                            width=self.obj.getLargura()-1,
                            height=int(self.obj.getAltura()/3),
                            bg="#000")
            self.tampa.grid(row=0,column=0,padx=10)

MarcadorTk()
