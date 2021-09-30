import tkinter as tk

'''Faça o uso do objeto.delete(parametro,*parametro)'''
def limparTudo():
    '''x = apenas um valor menor que 1'''
    txt.delete(0,tk.END)
def limparEsqDir():#Limpar Esquerda/Direita
    '''Apenas um valor inteiro 0'''
    txt.delete(0)
def limparDirEsq():#Limpar Direita/Esquerda
    '''x = Quantidade de caracteres -1'''
    txt.delete(len(txt.get())-1,tk.END)

#botão pronto  
def Botao(frame,texto,posicao):
    b = tk.Button(frame,text=texto,font=("Arial",14))
    b.grid(row=posicao[0],column=posicao[2])
    return b

janela = tk.Tk()
f = tk.Frame(janela,padx=10,pady=10)

#Uma label com o texto "Nome:" Label
label = tk.Label(f,text="Nome:",font=("Arial",14))
label.grid(row=0,column=0)

#Uma estrada de texto, para inserir seu nome
txt = tk.Entry(f)
txt.insert(0,"Adjailson")
txt.grid(row=0,column=1)

#Três botões ("Limpar")
b1 = Botao(f,"Limpar","1,0")
b1.config(command=limparTudo)

b2 = Botao(f,"L. EsqDir","1,1")
b2.config(command=limparEsqDir)

b3 = Botao(f,"L. DirEsq","1,2")
b3.config(command=limparDirEsq)

f.pack()
janela.mainloop()
