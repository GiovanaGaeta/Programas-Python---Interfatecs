def main():
    canais = []
    qtde = int(input())
    for i in range(qtde):
        canais.append(ler_canais())
    com_bonus = float(input())
    sem_bonus = float(input())
    bonus_canais = calcular_bonus(canais, com_bonus, sem_bonus)
    imprimir_bonus(bonus_canais)


def ler_canais() -> tuple:
    nome, inscritos, monetizacao, premium = input().split(";")
    inscritos = int(inscritos)
    monetizacao = float(monetizacao)
    if premium == "sim":
        premium = True
    else:
        premium = False
    canal = nome, inscritos, monetizacao, premium
    return canal


def calcular_bonus(canais, com_bonus, sem_bonus) -> list:
    bonus_canais = []
    for canal in canais:
        nome, inscritos, monetizacao, premium = canal
        acrescimo = (inscritos // 1000)
        if premium:
            acrescimo = acrescimo * com_bonus + monetizacao
        else:
            acrescimo = acrescimo * sem_bonus + monetizacao
        bonus = nome, acrescimo
        bonus_canais.append(bonus)
        

    return bonus_canais


def imprimir_bonus(bonus_canais):
    print("-----")
    print("BÔNUS")
    print("-----")
    for canal in bonus_canais:
        nome, bonus = canal
        print(f"{nome}: R$ {bonus:.2f}")
        

main()
