from agencia import Agencia

class Banco:
    def __init__(self, numero):
        self.numero = numero
        self.lista_agencias = []

    def buscar_agencia(self, numero):
        for agencia in self.lista_agencias:
            if agencia.numero == numero:
                return agencia
        return None

    def cadastrar_agencia(self, numero):
        agencia = Agencia(numero)
        self.lista_agencias.append(agencia)

    def transferir(self, num_agencia1, num_conta1, num_agencia2, num_conta2, valor):
        agencia1 = self.buscar_agencia(num_agencia1)
        agencia2 = self.buscar_agencia(num_agencia2)
        if agencia1 and agencia2:
            conta1 = agencia1.buscar_conta(num_conta1)
            conta2 = agencia2.buscar_conta(num_conta2)
            if conta1 and conta2:
                conta1.debitar(valor)
                conta2.creditar(valor)

    def relatorio(self):
        total_saldo = sum(conta.get_saldo() for agencia in self.lista_agencias for conta in agencia.lista_contas)  
        print(f"Banco: {self.numero}, Agências: {len(self.lista_agencias)}, Saldo Total: R${total_saldo:.2f}")