from conta import Conta, Corrente, Poupanca

class Agencia:
    def __init__(self, numero_agencia):
        self._numero = numero_agencia
        self.lista_contas = []

    @property
    def numero(self):
        return self._numero

    def buscar_conta(self, numero_conta):
        for conta in self.lista_contas:
            if conta.numero == numero_conta:
                return conta
        return None

    def cadastrar_conta(self, numero_nova_conta, saldo, tipo_conta="base"):
        if self.buscar_conta(numero_nova_conta):
            return None
        nova_conta = None
        if tipo_conta == "base":
            nova_conta = Conta(numero_nova_conta, saldo)
        elif tipo_conta == "corrente":
            taxa_padrao_corrente = 0.01
            nova_conta = Corrente(numero_nova_conta, saldo, taxa_padrao_corrente)
        elif tipo_conta == "poupanca":
            nova_conta = Poupanca(numero_nova_conta, saldo)
        else:
            return None
        
        if nova_conta:
            self.lista_contas.append(nova_conta)
            return nova_conta

    def relatorio(self):
        print(f"Agência: {self.numero}, Contas: {len(self.lista_contas)}, Saldo Total: R${self.saldo_total:.2f}")

    @property
    def saldo_total(self):
        return sum(conta.saldo for conta in self.lista_contas)
   