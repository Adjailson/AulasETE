#classe Conta é back-end
class Conta:

    def __init__(self, limite):
        self.__saldo = 0
        self.__limite = limite

    def depositar(self, valor):
        '''Retorno Boolean,recomendado!'''
        if(valor >= 10 and valor <= self.getLimite()):
            self.__saldo = self.__saldo + valor
            return True#"Deposito realizado com sucesso!"
        return False#"Fora dos limites!"

    def saque(self, valor):
        '''
        Retorno String, não recomendado!
        Quem deve alterar a mensagem é o web-design
        pelo Front-End, minha opnião.
        '''
        if(self.__saldo >= valor):
            self.__saldo = self.__saldo - valor
            return "Saque realizado com sucesso!"
        return "Saldo insuficiente!"
    
    def emprestimo(self,parcelas,juros,iof):pass
    
    def getSaldo(self):
        return self.__saldo

    def getLimite(self):
        return self.__limite
