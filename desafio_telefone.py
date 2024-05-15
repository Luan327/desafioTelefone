quantidade_cliente = int(input("Informe a quantidade de clientes: "))

dados_clientes = []

for _ in range(quantidade_cliente):
    linha = []
    nome = input("Nome: ")
    tipo_conta = int(input("Tipo: "))
    minutos = int(input("Minutos: "))
    
    
    linha.append(nome)
    linha.append(tipo_conta)
    linha.append(minutos)

    dados_clientes.append(linha)

for dados in dados_clientes:
    print(dados)

