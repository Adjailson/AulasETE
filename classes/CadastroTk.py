import tkinter as tk
from Cadastro import Cadastro

class CadastroTk:

    def __init__(self):
        self.janela = tk.Tk()
        self.f1 = tk.Frame(self.janela)
        self.f2 = tk.Frame(self.janela)

        self.titulo = tk.Label(self.f1,
                               font=("Arial",20),
                               text="Cadastro")
        self.titulo.grid(row=1, column=1)

        self.lnome = tk.Label(self.f2,text="Nome:",font=("Arial",12))
        self.lnome.grid(row=2, column=1,sticky="w")

        self.txtNome = tk.Entry(self.f2,font=("Arial",12))
        self.txtNome.grid(row=2, column=2)

        self.lcpf = tk.Label(self.f2,text="CPF:",font=("Arial",12))
        self.lcpf.grid(row=3, column=1,sticky="w")

        self.txtCpf = tk.Entry(self.f2,font=("Arial",12))
        self.txtCpf.grid(row=3, column=2)

        self.lemail = tk.Label(self.f2,
                               text="Digite seu e-mail:",
                               font=("Arial",12))
        self.lemail.grid(row=4, column=1,sticky="w")

        self.txtEmail = tk.Entry(self.f2,font=("Arial",12))
        self.txtEmail.grid(row=4, column=2)

        self.lsenha = tk.Label(self.f2,
                                 text="Gerar senha:",
                                 font=("Arial",12))
        self.lsenha.grid(row=5, column=1,sticky="w")

        self.txtSenha = tk.Entry(self.f2,show="*", font=("Arial",12))
        self.txtSenha.grid(row=5, column=2)

        self.btn = tk.Button(self.f2,text="Salvar",font=("Arial",13))
        self.btn.bind("<ButtonPress>",self.Cadastrar)
        self.btn.grid(row=6, column=2,sticky="e",pady=10,padx=10)

        self.f1.pack()
        self.f2.pack()
        self.janela.mainloop()
        
    def Cadastrar(self,object):
        objeto = Cadastro()
        objeto.setNome(self.txtNome.get())
        objeto.setCpf(self.txtCpf.get())
        objeto.setEmail(self.txtEmail.get())
        objeto.setSenha(self.txtSenha.get())

        print(objeto.viewDados())
        

CadastroTk()
