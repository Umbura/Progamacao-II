from banco import Banco
from agencia import Agencia
from conta import Conta, Corrente, Poupanca, Automatica

# Criar o banco
nome_banco = input("Digite o nome do banco: ")
banco = Banco(nome_banco)
print(f"Passo: Criado Banco '{nome_banco}'")

# Criar 2 agências
agencia1 = Agencia(101)
agencia2 = Agencia(102)
banco.lista_agencias.append(agencia1)
banco.lista_agencias.append(agencia2)
print("Passo: Cadastradas Agências 101 e 102")

# Função para criar as contas em uma agência
def criar_contas_padrao(agencia, prefixo):
    contas = [
        Conta(prefixo + 1),
        Corrente(prefixo + 2, 0.01),
        Poupanca(prefixo + 3),
        Poupanca(prefixo + 4),
        Automatica(prefixo + 5),
        Automatica(prefixo + 6),
        Automatica(prefixo + 7),
    ]
    for conta in contas:
        agencia.adicionar_conta(conta)
    return contas

# Criar contas nas duas agências
contas_ag1 = criar_contas_padrao(agencia1, 1000)
contas_ag2 = criar_contas_padrao(agencia2, 2000)

# Creditar e debitar em todas as contas
for conta in contas_ag1 + contas_ag2:
    conta.creditar(200.0)
    conta.debitar(100.0)
print("Passo: Créditos e Débitos aplicados")

# Render juros de 5% (onde for possível)
for agencia in [agencia1, agencia2]:
    for conta in agencia.lista_contas:
        if hasattr(conta, 'render_juros'):
            conta.render_juros(0.05)

# Relatórios iniciais
print("\n--- Relatório inicial ---")
print(agencia1)
print(agencia2)

# Remover 1 conta de cada agência
agencia1.lista_contas.pop(0)
agencia2.lista_contas.pop(0)
print("\nPasso: 1 conta removida de cada agência")

# Relatório após remoção de contas
print("\n=== Relatório Após Remoção de Contas ===")
print(agencia1)
print(agencia2)

# Remover 1 agência do banco
banco.lista_agencias.pop(0)
print("\nPasso: 1 agência removida")

# Relatório final
print("\n=== Relatório Final ===")
banco.relatorio()
