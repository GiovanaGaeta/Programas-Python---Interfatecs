from datetime import datetime

def main():
    carteira = cadastrar_carteira()
    imprimir_carteira(carteira)


def cadastrar_carteira() -> dict:
    carteira = {}
    carteira['nome'] = input('Nome: ')
    carteira['idade'] = int(input('Ano de nascimento: '))
    carteira['ctps'] = int(input('Carteira de Trabalho (0 não tem: )'))
    if carteira['ctps'] != 0:
        carteira['contratação'] = int(input('Ano de contratação: '))
        carteira['salário'] = float(input('Salário: R$ '))
        carteira['aposentadoria'] = carteira['contratação'] - carteira['idade'] + 35
    carteira['idade'] = datetime.now().year - carteira['idade']
    return carteira


def imprimir_carteira(carteira):
    for k, v in carteira.items():
        print(f'{k} tem o valor {v}')


main()
