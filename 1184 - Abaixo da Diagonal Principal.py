def main():
    operacao = input()
    M = criar_matriz()
    M = ler_valores(M)
    resultado = calculo_operacao(M, operacao)
    print(f"{resultado:.1f}")


def criar_matriz() -> list:
    lista = []
    for i in range(12):
        lista.append([0] * 12)
    return lista


def ler_valores(matriz) -> list:
    for i in range(12):
        for j in range(12):
            matriz[i][j] = float(input())
    return matriz


def calculo_operacao(matriz, operacao) -> float:
    soma = 0
    qtde = 0
    media = 0
    for i in range(12):
        for j in range(12):
            if j < i:
                qtde += 1
                soma += matriz[i][j]
    if operacao == "S":
        return soma
    else:
        media = soma / qtde
        return media


main()
