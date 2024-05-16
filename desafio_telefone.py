def relatorio(matriz_cliente):
    print("RELATORIO")
    for cliente in matriz_cliente:
        print(f"Nome: {cliente[0]},{cliente[1]},Tipo {cliente[2]}, Minutos: {cliente[3]}, Conta = R$ {0}")



quantidade_cliente = int(input("Informe a quantidade de clientes: "))

dados_clientes = []

for _ in range(quantidade_cliente):
    linha = []
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    tipo_conta = int(input("Tipo: "))
    minutos = int(input("Minutos: "))

    linha.append(nome)
    linha.append(telefone)
    linha.append(tipo_conta)
    linha.append(minutos)

    dados_clientes.append(linha)

relatorio(dados_clientes)

