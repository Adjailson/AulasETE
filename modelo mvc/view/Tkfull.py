#version-0.0.5
import tkinter as tk
from tkinter import ttk, messagebox

class Janela:

    __estilo = {'font':('Arial',14)}
    __arrayObjetos = [tk.Button]

    def __init__(self):
        self.__janela = tk.Tk()
        
    def start(self):
        return self.__janela.mainloop()

    def gerar(self,objetos):
        frame = tk.Frame(self.__janela)
        for l in range(len(objetos)):
            for c in range(len(objetos[l])):
                oQueE = objetos[l][c]
                if(oQueE == input):#Campo de texto
                    campo = tk.Entry(frame)
                    campo.config(self.__estilo)
                    campo.grid(row=l,column=c)
                    self.__arrayObjetos.append(campo)
                if(oQueE == complex):#Campo de senha
                    senha = tk.Entry(frame,show="*")
                    senha.config(self.__estilo)
                    senha.grid(row=l,column=c)
                    self.__arrayObjetos.append(senha)
                if(type(oQueE) == str):#Achei Label ou Button
                    if("*" in oQueE):#Botao
                        btn = tk.Button(frame,
                                        text=oQueE[1:len(oQueE)])
                        btn.config(self.__estilo)
                        btn.grid(row=l,column=c)
                        self.__arrayObjetos.append(btn)
                    if(not("*" in oQueE)):#Label
                        label = tk.Label(frame,text=oQueE)
                        label.config(self.__estilo)
                        label.grid(row=l,column=c)
                        self.__arrayObjetos.append(label)
                        
                if(type(oQueE) == tuple):#Select
                    box = ttk.Combobox(frame,
                                       values=oQueE,
                                       font=("Arial",13),
                                       state="readonly")
                    box.set("Selecione")
                    box.grid(row=l,column=c)
                    self.__arrayObjetos.append(box)

                if(type(oQueE) == dict):#Button imagen
                    texto = str
                    url = str
                    for i in oQueE:
                        texto = i
                        url = oQueE.get(i)
                    if("*" in texto):
                        self.__imgButton = tk.PhotoImage(file=url)
                        btnImg = tk.Button(frame,
                                           text=texto[1:len(texto)],
                                           image=self.__imgButton,
                                           compound=tk.LEFT)
                        btnImg.config(self.__estilo)
                        btnImg.grid(row=l,column=c)
                        self.__arrayObjetos.append(btnImg)
                    else:
                        self.__imgLabel = tk.PhotoImage(file=url)
                        labelImg = tk.Label(frame,
                                           text=texto,
                                           image=self.__imgLabel,
                                           compound=tk.TOP)
                        labelImg.config(self.__estilo)
                        labelImg.grid(row=l,column=c)
                        self.__arrayObjetos.append(labelImg)
                    
        frame.pack()
        
    def mensagem(self,msg,tipo=None):
        if(tipo == None):
            messagebox.showinfo("Tkfull",msg)
        elif(tipo == 1):
            messagebox.showwarning("Tkfull",msg)
        elif(tipo == 2):
            messagebox.showerror("Tkfull",msg)
            
    def pergunta(self,msg):
        YesNo = messagebox.askyesno("Tkfull",msg)
        if YesNo:
            return True
        return False
    
    def setEvento(self,posicao,funcao):
        if(type(self.__arrayObjetos[posicao]) == tk.Button):
            for b in self.__arrayObjetos:
                if(b == self.__arrayObjetos[posicao]):
                    b.config(command=funcao)
        if(type(self.__arrayObjetos[posicao]) == ttk.Combobox):
            for c in self.__arrayObjetos:
                if(c == self.__arrayObjetos[posicao]):
                    c.bind("<<ComboboxSelected>>",funcao)

    def setTexto(self,posicao,texto):
        if(type(self.__arrayObjetos[posicao]) == tk.Entry):
            tamanho = len(self.getTexto(posicao))
            self.__arrayObjetos[posicao].insert(tamanho,texto)
        elif(type(self.__arrayObjetos[posicao]) == tk.Button or
             type(self.__arrayObjetos[posicao]) == tk.Label):
            self.__arrayObjetos[posicao]['text'] = texto
        elif(type(self.__arrayObjetos[posicao]) == ttk.Combobox):
            pass

    def setEstilo(self, posicao, estilo):
        self.__arrayObjetos[posicao].config(estilo)
    
    def getTexto(self,posicao):
        try:
            if(type(self.__arrayObjetos[posicao]) == tk.Entry):
                return self.__arrayObjetos[posicao].get()
            elif(type(self.__arrayObjetos[posicao]) == tk.Button or
                 type(self.__arrayObjetos[posicao]) == tk.Label):
                return self.__arrayObjetos[posicao]['text']
            elif(type(self.__arrayObjetos[posicao]) == ttk.Combobox):
                return self.__arrayObjetos[posicao].get()
            return None
        except IndexError:
            print(f"Erro! -Posição '{posicao}' do array inválida.")
        except TypeError:
            print(f"Erro! -Tipo '{posicao}' é uma String.")
        except NameError:
            print(f"Erro! -Variável '{posicao}' não definida.")
            
    def getObjetos(self):
        return self.__arrayObjetos
    
    def apagarTexto(self,posicao,acao=None):
        if(type(self.__arrayObjetos[posicao]) == tk.Entry):
            if(acao == None):
                self.__arrayObjetos[posicao].delete(0,tk.END)
            elif(acao == -1):
                self.__arrayObjetos[posicao].delete(0)
            elif(acao == 1):
                tamanho = len(self.getTexto(posicao))
                self.__arrayObjetos[posicao].delete(tamanho-1,tk.END)

    def verPosicoes(self):
        view = ""
        for i in range(1,len(self.getObjetos())):
            if(type(self.__arrayObjetos[i]) == tk.Button):
                view = view+str(i)+"-> Button:"+self.getObjetos()[i]['text']+"\n"
            elif(type(self.__arrayObjetos[i]) == tk.Entry):
                view = view+str(i)+"-> Entry\n"
            elif(type(self.__arrayObjetos[i]) == ttk.Combobox):
                view = view+str(i)+"-> Combobox\n"
            elif(type(self.__arrayObjetos[i]) == tk.Label):
                view = view+str(i)+"-> Label:"+self.getObjetos()[i]['text']+"\n"
        return view

    #Configurações da janela
    def titulo(self,titulo):self.__janela.title(titulo)
    def tamanho(self, dimensoes):self.__janela.geometry(dimensoes)
    def maximize(self, boolean):self.__janela.resizable(0,boolean)
    def icone(self, local,todas=False):
        try:
            icon = tk.PhotoImage(file=local)
            self.__janela.iconphoto(todas, icon)
        except:
            print("Verifique nome, local, extensão .png e tamanho da imagem!")
    def fechar(self):
        self.__janela.destroy()
    def limparObjetos(self):
        self.__arrayObjetos.clear()
        self.__arrayObjetos.append(tk.Button)
                
