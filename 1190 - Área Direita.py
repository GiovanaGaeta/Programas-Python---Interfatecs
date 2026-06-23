def main():
    M = criar_matriz()
    operacao = input()
    M = ler_matriz(M)
    resultado = calculo_matriz(M, operacao)
    print(f"{resultado:.1f}")


def criar_matriz() -> list:
    matriz = []
    for i in range(12):
        matriz.append([0] * 12)
    return matriz


def ler_matriz(matriz) -> list:
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
            if j > i and j > 11 - i:
                soma += matriz[i][j]
                qtde += 1
    if operacao == "S":
        return soma
    else:
        media = soma / qtde
        return media


main()
    



    
