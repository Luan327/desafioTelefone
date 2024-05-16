def relatorio(matriz_cliente,tipo_assinatura):
    print("RELATORIO")
    for cliente in matriz_cliente:
        valor_conta = calculo_conta(cliente[2],cliente[3],tipo_assinatura)
        print(f"Nome: {cliente[0]}, {cliente[1]}, Tipo {cliente[2]}, Minutos: {cliente[3]}, Conta = R$ {valor_conta:.2f}")
def calculo_conta(tipo_conta,minutos_utilizados,tipo_assinatura):
    # se minutos consumidos <- 90 == preço Basico
    # se nao sera // tipo_conta + (minutos consumido - 90 * excedente) == valor da conta.
    tarifa = tipo_assinatura[tipo_conta]
    tarifa_fixa = tarifa[0]
    tarifa_excesso = tarifa[1]
    if minutos_utilizados <= 90:
        valor_conta = tarifa_fixa
    else:
        valor_conta = tarifa_fixa + (minutos_utilizados - 90) * tarifa_excesso
    return valor_conta

quantidade_cliente = int(input("Informe a quantidade de clientes: "))

dados_clientes = []
tipo_assinatura = [
    [25.5, 0.10], #TIPO 0: [TARIFA_FIXA, TARIFA_EXCESSO]
    [35.0, 0.12], #TIPO 1: [TARIFA_FIXA, TARIFA_EXCESSO]
    [60.0, 0.15]  #TIPO 2: [TARIFA_FIXA, TARIFA_EXCESSO]
]
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


relatorio(dados_clientes,tipo_assinatura)
