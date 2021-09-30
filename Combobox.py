import tkinter as tk
from tkinter import ttk,messagebox

def funcao(self):
    if(box.get()=="Sair"):print(exit(0))
    else:messagebox.showinfo("Título Macho",box.get())

jan = tk.Tk()
f = tk.Frame(jan,padx=10,pady=10)

#box
box = ttk.Combobox(f,
                   values=["Masculino","Feminino","Sair"],
                   font=("Arial",14),
                   state = "readonly")
box.set("--selecione--")
box.bind("<<ComboboxSelected>>",funcao)#Evento selecionar
box.grid(row=0,column=0)

f.pack()
jan.mainloop()
