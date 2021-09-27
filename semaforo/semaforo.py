import tkinter as tk
import time as t
#import threading

cont = 0
while True:
    print("Olá...")
    t.sleep(5)

janela = tk.Tk()
f = tk.Frame(janela)



f.pack()
#threading.Thread(target=funcao, daemon=True).start()
janela.mainloop()
        
    
