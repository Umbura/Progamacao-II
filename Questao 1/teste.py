from banco import Banco
from agencia import Agencia
from conta import Conta

# Cria um banco
banco = Banco(1)

# Cadastra agências
banco.cadastrar_agencia(101)
banco.cadastrar_agencia(102)

# Obtém as agências
agencia1 = banco.buscar_agencia(101)
agencia2 = banco.buscar_agencia(102)

# Cadastra contas na agência 101
agencia1.cadastrar_conta(1001, 500)  # Conta 1001, saldo=500
agencia1.cadastrar_conta(1002, 300)  # Conta 1002, saldo=300

# Cadastra contas na agência 102
agencia2.cadastrar_conta(2001, 1000)  # Conta 2001, saldo=1000

# Relatórios
agencia1.relatorio()  # Agência: 101, Contas: 2, Saldo Total: R$800.00
agencia2.relatorio()  # Agência: 102, Contas: 1, Saldo Total: R$1000.00
banco.relatorio()     # Banco: 1, Agências: 2, Saldo Total: R$1800.00