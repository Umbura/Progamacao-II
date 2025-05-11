from conta import Conta

class Agencia:
    def __init__(self, numero):
        self.numero = numero
        self.lista_contas = []

    def buscar_conta(self, numero):
        for conta in self.lista_contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def cadastrar_conta(self, numero, saldo=0):
        conta = Conta(numero, saldo)
        self.lista_contas.append(conta)

    def relatorio(self):
        total_saldo = sum(conta.get_saldo() for conta in self.lista_contas)
        print(f"Agência: {self.numero}, Contas: {len(self.lista_contas)}, Saldo Total: R${total_saldo:.2f}")