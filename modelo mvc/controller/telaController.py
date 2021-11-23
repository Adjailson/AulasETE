from model.telaModel import TelaModel

class TelaController:

    def __init__(self):
        pass

    def pegarNome(self, telaView):
        nome = telaView.getTexto(3)
        obj = TelaModel()
        obj.setNome(nome)
        return obj.getNome()
