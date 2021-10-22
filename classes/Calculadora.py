class Calculadora:

    def __init__(self):
        self.__botoes = list
        self.__altura = int
        self.__largura = int

    def setBotoes(self, botoes):
        self.__botoes = botoes
    def getBotoes(self):
        return self.__botoes

    def setAltura(self, altura):
        self.__altura = altura
    def getAltura(self):
        return self.__altura

    def setLargura(self, largura):
        self.__largura = largura
    def getLargura(self):
        return self.__largura
