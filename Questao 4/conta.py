class Conta:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0

    def creditar(self, valor):
        self.saldo += valor

    def debitar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def __str__(self):
        return f"Conta {self.numero} | Saldo: R${self.saldo:.2f}"


class Corrente(Conta):
    def __init__(self, numero, taxa_manutencao):
        super().__init__(numero)
        self.taxa_manutencao = taxa_manutencao

    def render_juros(self, taxa):
        self.saldo += self.saldo * taxa
        self.saldo -= self.taxa_manutencao


class Poupanca(Conta):
    def __init__(self, numero):
        super().__init__(numero)

    def render_juros(self, taxa):
        self.saldo += self.saldo * taxa


class Automatica(Conta):
    def __init__(self, numero):
        super().__init__(numero)

    def render_juros(self, taxa):
        self.saldo += self.saldo * (taxa + 0.02)
