class Conta: 
    def __init__ (self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    def creditar (self, valor):
        self.saldo += valor

    def debitar (self, valor):
        if self.saldo >= valor:
            self.saldo -=valor

    def get_numero (self):
        return self.numero

    def get_saldo (self):
        return self.saldo
    
    def relatorio(self):
        print(f"Conta: {self.numero}, Saldo: R${self.saldo:.2f}")

class Corrente(Conta):
    def __init__(self, numero, saldo=0, taxa=0.01):
        super().__init__(numero, saldo)
        self.taxa = taxa

    def debitar(self, valor):
        total = valor + (valor * self.taxa)
        if self.saldo >= total:
            self.saldo -= total

class Poupanca(Conta):
    def render_juros(self, taxa):
        self.saldo += self.saldo * taxa

class Automatica(Conta):
    contador = 1  

    def __init__(self, saldo=0):
        super().__init__(Automatica.contador, saldo)
        Automatica.contador += 1