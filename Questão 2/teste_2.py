# Teste para o cenário básico de uso do sistema bancário - Questão 2

from banco import Banco
from agencia import Agencia
from conta import Conta

print("--- Executando Teste de Cenário Básico (Manual) ---")

# --- Parte 1: Configuração do Cenário ---

# Cria um banco
banco = Banco(1)
print(f"\nPasso: Criado Banco {banco.numero}")

# Cadastra agências
banco.cadastrar_agencia(101)
print("Passo: Cadastrada Agência 101")
banco.cadastrar_agencia(102)
print("Passo: Cadastrada Agência 102")

# Obtém as agências
agencia1 = banco.buscar_agencia(101)
agencia2 = banco.buscar_agencia(102)
print("Passo: Obtidas Agências 101 e 102")

# Cadastra contas na agência 101
agencia1.cadastrar_conta(1001, 500)  # Conta 1001, saldo=500
print("Passo: Cadastrada Conta 1001 na Agência 101 com saldo 500")
agencia1.cadastrar_conta(1002, 300)  # Conta 1002, saldo=300
print("Passo: Cadastrada Conta 1002 na Agência 101 com saldo 300")

# Cadastra contas na agência 102
agencia2.cadastrar_conta(2001, 1000)  # Conta 2001, saldo=1000
print("Passo: Cadastrada Conta 2001 na Agência 102 com saldo 1000")

# --- Parte 2: Verificação dos Resultados ---

print("\n--- Verificando os Resultados ---")

# Verificação 1: Número de agências no banco
expected_agencias_banco = 2
actual_agencias_banco = len(banco.lista_agencias)
print(f"Verificação 1: Número de agências no banco. Esperado: {expected_agencias_banco}, Encontrado: {actual_agencias_banco}")
if actual_agencias_banco == expected_agencias_banco:
    print("   -> Passou!")
else:
    print("   -> FALHOU!")

# Verificação 2: Número de contas na agência 101
expected_contas_agencia1 = 2
actual_contas_agencia1 = len(agencia1.lista_contas)
print(f"Verificação 2: Número de contas na Agência 101. Esperado: {expected_contas_agencia1}, Encontrado: {actual_contas_agencia1}")
if actual_contas_agencia1 == expected_contas_agencia1:
    print("   -> Passou!")
else:
    print("   -> FALHOU!")

# Verificação 3: Saldo total na agência 101
expected_saldo_agencia1 = 800
actual_saldo_agencia1 = agencia1.saldo_total
if abs(actual_saldo_agencia1 - expected_saldo_agencia1) < 0.001:
    print(f"Verificação 3: Saldo total Agência 101. Esperado: R${expected_saldo_agencia1:.2f}, Encontrado: R${actual_saldo_agencia1:.2f} -> Passou!")
else:
     print(f"Verificação 3: Saldo total Agência 101. Esperado: R${expected_saldo_agencia1:.2f}, Encontrado: R${actual_saldo_agencia1:.2f} -> FALHOU!")


# Verificação 4: Número de contas na agência 102
expected_contas_agencia2 = 1
actual_contas_agencia2 = len(agencia2.lista_contas)
print(f"Verificação 4: Número de contas na Agência 102. Esperado: {expected_contas_agencia2}, Encontrado: {actual_contas_agencia2}")
if actual_contas_agencia2 == expected_contas_agencia2:
    print("   -> Passou!")
else:
    print("   -> FALHOU!")

# Verificação 5: Saldo total na agência 102
expected_saldo_agencia2 = 1000
actual_saldo_agencia2 = agencia2.saldo_total
if abs(actual_saldo_agencia2 - expected_saldo_agencia2) < 0.001:
    print(f"Verificação 5: Saldo total Agência 102. Esperado: R${expected_saldo_agencia2:.2f}, Encontrado: R${actual_saldo_agencia2:.2f} -> Passou!")
else:
    print(f"Verificação 5: Saldo total Agência 102. Esperado: R${expected_saldo_agencia2:.2f}, Encontrado: R${actual_saldo_agencia2:.2f} -> FALHOU!")

# Verificação 6: Saldo total no banco
expected_saldo_banco = 1800
actual_saldo_banco = banco.saldo_total
if abs(actual_saldo_banco - expected_saldo_banco) < 0.001:
    print(f"Verificação 6: Saldo total Banco. Esperado: R${expected_saldo_banco:.2f}, Encontrado: R${actual_saldo_banco:.2f} -> Passou!")
else:
    print(f"Verificação 6: Saldo total Banco. Esperado: R${expected_saldo_banco:.2f}, Encontrado: R${actual_saldo_banco:.2f} -> FALHOU!")


print("\n--- Teste de Cenário Questão 2---")