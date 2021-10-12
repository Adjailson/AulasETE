class Marcador:
    '''
    Criar o método construtor
    Depois declaramos nossos atributos dentro dele
    '''
    def __init__(self):
        '''Atributos de um marcador
        coloque em modo privado usando __'''
        self.__cor = str
        self.__tampa = bool
        self.__largura = int
        self.__altura = int
        self.__marca = str
        self.__espessuraPonta = int
    '''Você pode fazer um comportamento:'''
    def fazerLinha(self,tamanhoLinha,direcao):
        largura = 0
        altura = 0
        if(direcao == 'V'):#Vertical
            largura = self.getEspessuraPonta()
            altura = tamanhoLinha
            return [largura,altura]
        else:#Horizontal
            largura = tamanhoLinha
            altura = self.getEspessuraPonta()
            return [largura,altura]
            
    '''Agora configure os sets e gets'''
    def setCor(self,cor):
        self.__cor = cor
    def getCor(self):
        return self.__cor

    def setTampa(self,tampa):
        self.__tampa = tampa
    def getTampa(self):
        return self.__tampa

    def setLargura(self,largura):
        self.__largura = largura
    def getLargura(self):
        return self.__largura

    def setAltura(self,altura):
        self.__altura = altura
    def getAltura(self):
        return self.__altura

    def setMarca(self,marca):
        self.__marca = marca
    def getMarca(self):
        return self.__marca

    def setEspessuraPonta(self,espessura):
        self.__espessuraPonta = espessura
    def getEspessuraPonta(self):
        return self.__espessuraPonta
