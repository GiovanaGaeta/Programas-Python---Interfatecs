def main():
    matriz = criar_matriz()
    operacao = input()
    matriz = ler_valores(matriz)
    resultado = calculo_matriz(matriz, operacao)
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


def calculo_matriz(matriz, operacao) -> float:
    soma = 0
    qtde = 0
    media = 0
    for i in range(12):
        for j in range(12):
            if j > i and j < 11 - i:
                soma += matriz[i][j]
                qtde += 1
    if operacao == "S":
        return soma
    else:
        media = soma / qtde
        return media


main()
