import tkinter as tk

janela = tk.Tk()
frame = tk.Frame(janela)
frame.config(padx=10,pady=10,bg="#999")

img1 = tk.PhotoImage(file="usuarios.png")
img2 = tk.PhotoImage(file="salve.png")

btn1 = tk.Button(frame,
                text="Cadastrar",
                image = img1,
                font=("Arial",17),
                padx=10,
                compound=tk.LEFT)
btn1.grid(row=0,column=0)

btn2 = tk.Button(frame,
                text="Salvar",
                image = img2,
                font=("Arial",17),
                padx=10,
                compound=tk.LEFT)
btn2.grid(row=0,column=1)
'''
compound = LEFT -> image esquerda
compound = RIGHT -> image direita
compound = TOP -> image topo
compound = BOTTOM -> image abaixo

baixe icones em https://www.flaticon.com/ nos
tamanhos 32x32
'''
frame.pack()
janela.mainloop()
