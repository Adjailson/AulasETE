
class Cadastro:
    def __init__(self):
        self.__nome = str
        self.__cpf = str
        self.__email = str
        self.__senha = str

    def setNome(self,nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome
    
    def setCpf(self,cpf):
        self.__cpf = cpf
    def getCpf(self):
        return self.__cpf

    def setEmail(self,email):
        self.__email = email
    def getEmail(self):
        return self.__email

    def setSenha(self,senha):
        self.__senha = senha
    def getSenha(self):
        return self.__senha

    def viewDados(self):
        dados = (self.getNome(),self.getCpf(),
                 self.getEmail(),self.getSenha())
        return dados
