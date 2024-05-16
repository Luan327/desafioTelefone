def relatorio(matriz_cliente, tipo_assinatura):
    print("RELATORIO")
    for cliente in matriz_cliente:
        valor_conta = calculo_conta(cliente[2], cliente[3], tipo_assinatura)
        print(
            f"Nome: {cliente[0]}, {cliente[1]}, Tipo {cliente[2]}, Minutos: {cliente[3]}, Conta = R$ {valor_conta:.2f}"
        )
def calculo_conta(tipo_conta, minutos_utilizados, tipo_assinatura):
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
def cadastrar_clientes(quantidade_clientes):
    dados_clientes = []
    for i in range(quantidade_clientes):
        print(f"Dados do {i+1}º Cliente: ")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        tipo_conta = int(input("Tipo de conta (0,1 ou 2): "))
        
        while tipo_conta != 0 and tipo_conta != 1 and tipo_conta != 2:
            print("Tipo da conta invalido, Digite ( 0,1 ou 2: )")
            tipo_conta = input()

        minutos = int(input("Minutos: "))
        print()

        linha = [nome, telefone, tipo_conta, minutos]
        dados_clientes.append(linha)
    return dados_clientes

quantidade_cliente = int(input("Informe a quantidade de clientes: "))

tipo_assinatura = [
    [25.5, 0.10],  # TIPO 0: [TARIFA_FIXA, TARIFA_EXCESSO]
    [35.0, 0.12],  # TIPO 1: [TARIFA_FIXA, TARIFA_EXCESSO]
    [60.0, 0.15],  # TIPO 2: [TARIFA_FIXA, TARIFA_EXCESSO]
]


clientes_cadastrados = cadastrar_clientes(quantidade_cliente)
relatorio(clientes_cadastrados, tipo_assinatura)
