def main():
    coluna = int(input())
    operacao = input()
    M = criar_matriz()
    M = ler_matriz(M)
    resultado = operacao_matriz(M, coluna, operacao)
    print(f"{resultado:.1f}")


def criar_matriz() -> list:
    lista = []
    for i in range(12):
        lista.append([0] * 12)
    return lista


def ler_matriz(matriz) -> list:
    for i in range(12):
        for j in range(12):
            matriz[i][j] = float(input())
    return matriz


def operacao_matriz(matriz, coluna, operacao) -> float:
    soma = 0
    media = 0
    for i in range(12):
        soma += matriz[i][coluna]
    if operacao == "S":
        return soma
    else:
        media = soma / 12
        return media

    
main()
