def main():
    convidados = {}
    convidados_noiva = {}
    convidados_noivo = {}
    convidado = input()
    while convidado != 'ACABOU':
        convidado = convidado.split(';')
        convidados[convidado[0]] = convidado[1]
        if convidado[1] == 'noivo':
            convidados_noivo[convidado[0]] = convidado[1]
        else:
            convidados_noiva[convidado[0]] = convidado[1]
        convidado = input()
    ambos = organizar_ambos(convidados_noiva, convidados_noivo)
    apenas_noiva = organizar_apenas_noiva(convidados_noiva, ambos)
    apenas_noivo = organizar_apenas_noivo(convidados_noivo, ambos)
    imprimir_final(convidados)
    imprimir_noiva(apenas_noiva)
    imprimir_noivo(apenas_noivo)
    imprimir_ambos(ambos)
    imprimir_apenas_um(apenas_noivo, apenas_noiva)


def organizar_ambos(convidados_noiva, convidados_noivo) -> list:
    ambos = []
    for nome in convidados_noiva.keys():
        if nome in convidados_noivo.keys():
            ambos.append(nome)
    for nome in convidados_noivo.keys():
        if nome in convidados_noiva.keys() and nome not in ambos:
            ambos.append(nome)
    ambos.sort()
    return ambos

def organizar_apenas_noivo(convidados_noivo, ambos) -> list:
    apenas_noivo = []
    for nome in convidados_noivo.keys():
        if nome not in ambos:
            apenas_noivo.append(nome)
    apenas_noivo.sort()
    return apenas_noivo

def organizar_apenas_noiva(convidados_noiva, ambos) -> list:
    apenas_noiva = []
    for nome in convidados_noiva.keys():
        if nome not in ambos:
            apenas_noiva.append(nome)
    apenas_noiva.sort()
    return apenas_noiva

def imprimir_ambos(ambos):
    print('-' * 20)
    print('POR AMBOS')
    print('-' * 20)
    for i in ambos:
        print(i)
    print('*')


def imprimir_noiva(apenas_noiva):
    print('-' * 20)
    print('APENAS NOIVA')
    print('-' * 20)
    for i in apenas_noiva:
        print(i)
    print('*')


def imprimir_noivo(apenas_noivo):
    print('-' * 20)
    print('APENAS NOIVO')
    print('-' * 20)
    for i in apenas_noivo:
        print(i)
    print('*')

   
def imprimir_apenas_um(apenas_noivo, apenas_noiva):
    unico = apenas_noivo + apenas_noiva
    unico.sort()
    print('-' * 20)
    print('POR APENAS UM DELES')
    print('-' * 20)
    for i in unico:
        print(i)


def imprimir_final(convidados):
    convidados = sorted(convidados.keys())
    print('-' * 20)
    print('LISTA FINAL')
    print('-' * 20)
    for i in convidados:
        print(i)
    print('*')

   
main()
    
