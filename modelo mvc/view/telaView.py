from view.Tkfull import Janela
from controller.telaController import TelaController

class TelaView:

    titulo = [['Título']]
    objetos = [['Nome',input],
               [None,'*Ok']]

    def __init__(self):
        self.tela = Janela()
        self.tela.gerar(self.titulo)
        self.tela.gerar(self.objetos)
        self.tela.setEvento(4, self.evento)
        self.tela.start()

    def evento(self):
        obj = TelaController()
        msg = obj.pegarNome(self.tela)
        self.tela.mensagem(msg)
