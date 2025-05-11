class Conta: 
    def __init__ (self, numero, saldo):
        self._numero = numero
        self._saldo = saldo

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, novo_numero):
        self._numero = novo_numero
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo > 0:
            self.creditar(novo_saldo)
        elif novo_saldo < 0:
            self.debitar(abs(novo_saldo))
        else:
            pass

    def creditar (self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        return False

    def debitar (self, valor):
        if valor <= 0:
            return False
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False
    
    def relatorio(self):
        print(f"Conta: {self._numero}, Saldo: R${self._saldo:.2f}")

class Corrente(Conta):
    def __init__(self, numero, saldo, taxa=0.01):
        super().__init__(numero, saldo)
        self.taxa_operacao = taxa


    def debitar(self, valor):
       if valor <= 0:
           return False
       valor_total_debito = valor * (1 + self.taxa_operacao)

       if self._saldo >= valor_total_debito:
           self._saldo -= valor_total_debito
           return True
       else:
           return False

class Poupanca(Conta):
    def __init__(self, numero, saldo):
        super().__init__(numero, saldo)

    def render_juros(self, taxa_juros):
        if taxa_juros > 0:
            juros_calculado = self._saldo * taxa_juros
            self._saldo += juros_calculado
            return True
        return False

class Automatica(Conta):
    contador = 1  

    def __init__(self, saldo):
        super().__init__(Automatica.contador, saldo)
        Automatica.contador += 1