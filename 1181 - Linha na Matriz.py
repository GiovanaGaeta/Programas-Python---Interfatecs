def main():
    linha = int(input())
    operacao = input()
    M = montar_matriz()
    M = ler_matriz(M)
    resultado = calculo_matriz(M, linha, operacao)
    print(f"{resultado:.1f}")

def montar_matriz() -> list:
    lista = []
    for i in range(12):
        lista.append([0] * 12)
    return lista


def ler_matriz(matriz) -> list:
    for i in range(12):
        for j in range(12):
            matriz[i][j] = float(input())
    return matriz


def calculo_matriz(matriz, linha, operacao) -> float:
    soma = 0
    media = 0
    for j in range(12):
        soma += matriz[linha][j]
    if operacao == "S":
        return soma
    else:
        media = soma / 12
        return media
    

main()
