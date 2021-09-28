import tkinter as tk
import time as t
import threading

def iniciar():
    while True:
        label['image'] = amarelo
        t.sleep(2)
        label['image'] = vermelho
        t.sleep(2)
        label['image'] = verde
        t.sleep(2)

janela = tk.Tk()
f = tk.Frame(janela)

amarelo = tk.PhotoImage(file='amarelo.png')
vermelho = tk.PhotoImage(file='vermelho.png')
verde = tk.PhotoImage(file='verde.png')

label = tk.Label(f,image=amarelo)
#label.bind("<Button-1>",iniciar)
label.grid(row=0, column=0)


f.pack()
threading.Thread(target=iniciar, daemon=True).start()
janela.mainloop()
        
    
