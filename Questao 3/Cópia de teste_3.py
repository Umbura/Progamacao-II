from banco import Banco
from agencia import Agencia
from conta import Conta

print("---  Verificação de teste do Cenário (Adaptado com Sobrecarga) ---")

# --- Parte 1: Configuração do Cenário ---

#  Criação do bando
banco = Banco(1)
print(f"\nPasso: Criado Banco {banco.numero}")

# Cadastro de agência
banco.cadastrar_agencia(101)
banco.cadastrar_agencia(102)
print("Passo: Cadastradas Agências 101 e 102")

# Verifica as agências (busca)
agencia1 = banco.buscar_agencia(101)
agencia2 = banco.buscar_agencia(102)

# Cadastra contas na agência 101
agencia1.cadastrar_conta(1001, 500)
agencia1.cadastrar_conta(1002, 300)

# Cadastra contas na agência 102
agencia2.cadastrar_conta(2001, 1000)

# --- Parte 2: Verificações básicas ---

print("\n--- Verificando os Resultados ---")

print(f"\n{banco}")  # Testa __str__ do banco
print(f"{agencia1}")  # Testa __str__ da agência
print(f"{agencia2}")  # Testa __str__ da outra agência

# Teste de sobrecarga de operadores

print("\n--- Testando sobrecarga de operadores ---")

# Soma de contas
conta1 = agencia1.buscar_conta(1001)
conta2 = agencia1.buscar_conta(1002)
soma_contas = conta1 + conta2
print(f"Soma dos saldos das contas 1001 e 1002: R${soma_contas:.2f}")

# Soma de agências
soma_agencias = agencia1 + agencia2
print(f"Soma dos saldos das agências 101 e 102: R${soma_agencias:.2f}")

# Soma entre contas de agências diferentes
conta3 = agencia2.buscar_conta(2001)
soma_mista = conta1 + conta3
print(f"Soma dos saldos das contas 1001 e 2001: R${soma_mista:.2f}")

print("\n--- Fim do Teste com Sobrecarga ---")