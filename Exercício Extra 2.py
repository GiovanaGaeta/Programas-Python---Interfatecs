from random import randint

def main():
    jogadores = criar_jogadas()
    ranking = criar_ranking(jogadores)
    imprimir_ranking(ranking)


def criar_jogadas() -> list:
    jogadores = []
    print('Valores sorteados:')
    for i in range(4):
        jogada = {}
        jogada['jogador'] = 'jogador' + str(i+1)
        jogada['numero'] = randint(1,6)
        print(f'O {jogada["jogador"]} tirou {jogada["numero"]}')
        jogadores.append(jogada)
    return jogadores


def criar_ranking(jogadores) -> list:
    ranking = jogadores[:]
    for i in range(3):
        for j in range(i+1, 4):
            if ranking[j]['numero'] > ranking[i]['numero']:
                ranking[i], ranking[j] = ranking[j], ranking[i]
    return ranking


def imprimir_ranking(ranking):
    print('Ranking:')
    for i in range(4):
        jogador, numero = ranking[i].values()
        print(f'{i+1}° lugar: {jogador} com {numero}')


main()
        
