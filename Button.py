import tkinter as tk
estilos = {
    'text':'Meu Botão',#texto
    'bg':'#00FF7F',#cor botão
    'fg':'#fff',#cor letras
    'font':('Consolas Bold',20),#Fontes e tamanhos
    'width':'20',#Largura
    'height':'1',#Altura
    'relief':'flat',#tipos de relevo:(flat, groove, raised, ridge, solid, or sunken)
    'activebackground':'#fff',#cor quando clicado
    'padx':'10',#margin interna dos lados
    'pady':'10',#margin interna superior e inferior
    'anchor':'center'#Posição: n, ne, e, se, s, sw, w, nw, or center
    }
def evento():
    print(btn['text'])

janela = tk.Tk()
frame = tk.Frame()

btn = tk.Button(frame)
btn.config(estilos,command=evento)
btn.grid(row=0, column=0)

frame.pack()
janela.mainloop()
