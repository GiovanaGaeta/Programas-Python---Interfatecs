def main():
    operacao = input()
    M = criar_matriz()
    M = ler_valores(M)
    resultado = operacao_matriz(M, operacao)
    print(f"{resultado:.1f}")


def criar_matriz() -> list:
    matriz = []
    for i in range(12):
        matriz.append([0] * 12)
    return matriz


def ler_valores(matriz) -> list:
    for i in range(12):
        for j in range(12):
            matriz[i][j] = float(input())
    return matriz


def operacao_matriz(matriz, operacao) -> float:
    soma = 0
    qtde = 0
    media = 0
    for i in range(12):
        for j in range(11, -1, -1):
            if j > 12 - (i + 1):
                soma += matriz[i][j]
                qtde += 1
    if operacao == "s":
        return soma
    else:
        media = soma / qtde
        return media


main()
