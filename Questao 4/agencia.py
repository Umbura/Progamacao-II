class Agencia:
    def __init__(self, numero):
        self.numero = numero
        self.lista_contas = []

    def adicionar_conta(self, conta):
        self.lista_contas.append(conta)

    def buscar_conta(self, numero_conta):
        for conta in self.lista_contas:
            if conta.numero == numero_conta:
                return conta
        return None

    @property
    def saldo_total(self):
        return sum(conta.saldo for conta in self.lista_contas)

    def __str__(self):
        return f"Agência: {self.numero}, Contas: {len(self.lista_contas)}, Saldo Total: R${self.saldo_total:.2f}"
