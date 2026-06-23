def main():
    jogador = cadastrar_jogador()
    print()
    imprimir_jogador(jogador)
    print()
    analisar_jogadas(jogador)


def cadastrar_jogador() -> dict:
    jogador = {}
    jogador['nome'] = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    for i in range(partidas):
        gol = int(input(f'Gols na partida{i}? '))
        gols.append(gol)
    jogador['gols'] = gols
    jogador['total'] = sum(jogador['gols'])
    return jogador


def imprimir_jogador(jogador):
    for k,v in jogador.items():
        print(f'O campo {k} tem o valor {v}.')


def analisar_jogadas(jogador):
    print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
    for i in range(len(jogador['gols'])):
        print(f'Na partida {i}, fez {jogador["gols"][i]} gols.')
    print(f'Foi um total de {jogador["total"]} gols.')
    
    
main()
