class ContaCorrente:
    def __init__(self, numero, saldo = 0):
        self.__numero = numero
        self.__saldo = saldo

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self):
        pass

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novoSaldo):
        self.__saldo = novoSaldo

    def creditar(self, valor):
        self.__saldo += valor

    def debitar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente!')
    
    def transferir(self, conta, valor):
        self.debitar(valor)
        conta.creditar(valor)

    def __str__(self):
        return f'''
        -----Conta Corrente-----
        Numero: {self.__numero:}
        Saldo: R${self.__saldo:,.2f}'''

class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, saldo = 0, taxaJuros = 0.05):
        super().__init__(numero, saldo)
        self.__taxaJuros = taxaJuros

    @property
    def taxaJuros(self):
        return self.__taxaJuros
    
    @taxaJuros.setter
    def taxaJuros(self, novaTaxa):
         self.__taxaJuros = novaTaxa


    def renderJuros(self):
        self.saldo += self.saldo * self.taxaJuros
    
    def __str__(self):
        return  f'''
        -----Conta Poupança-----
        Numero: {self.numero}
        Saldo: R${self.saldo:,.2f}
        Taxa de Juros: {self.taxaJuros}%a.m''' #super().__str__() +
    
def main():
    cc1 = ContaCorrente(1)
    cp1 = ContaPoupanca(2)
    cp1.creditar(1500.00)
    print(f'{cp1.saldo:,.2f}')
    cp1.debitar(25.50)
    print(f'{cp1.saldo:,.2f}')
    cp1.transferir(cc1, 220.00)
    print(f'{cp1.saldo:,.2f}')
    cp1.renderJuros()
    print(f'{cp1.saldo:,.2f}')
    print(f'{cc1.saldo:,.2f}')
    print(cc1)
    print(cp1)
    
if __name__ == '__main__':
    main()

        



        

        