def operacoes_vetores():

    menu = '\033[35m-=-=- Operações em Vetores -=-=-\n\033[m' \
        + '\n' \
        + '1 - Inserir Valores\n' \
        + '2 - Mostrar posição do valor\n' \
        + '3 - Mostrar todos os valores\n' \
        + '4 - Remover valor (posição)\n'  \
        + '5 - Atualizar Valor (posição)\n'  \
        + '6 - Contagem geral (par,impar,positivo,negativo)\n'  \
        + '7 - Média dos valores\n'  \
        + '0 - Sair\n' \
        + '\nDigite uma opção:\n>>> '
    

    lista = []

    opcao = int(input(menu))

    while opcao != 0:  
        if opcao == 1:
            inserir_valores(lista)
        elif opcao == 2:
            mostra_valor(lista)
        elif opcao == 3:
            mostrar_todos(lista)
        elif opcao == 4:
            remover_valor(lista)
        elif opcao == 5:
            atualizar_valor(lista)
        elif opcao == 6:
            contagem_geral(lista)
        elif opcao == 7:
            calculador_de_media(lista)
        else:
            print('Opção Inválida')

        print()
        input('Para continuar aperte <enter> ...')
        opcao = int(input(menu))

    print('Obrigado pela atenção.')


def inserir_valores(lista):
    print()
    qnt = int(input('Quantos valores desejar inserir?\n>>> '))
    print()

    for i in range(qnt):
        valor = int(input('Valor:\n>>> '))
        lista.append(valor)
    
    print()
    print('Os valores foram inseridos com sucesso!')


def mostra_valor(lista):
    print()
    posicao = int(input('Qual a posição?\n>>> '))
    print()
    print('Valor buscado:')
    print(f'Valor index[{posicao}] é {lista[posicao]}')


def mostrar_todos(colecao):
    tamanho = len(colecao)
    print()
    print(f'-=-=- Mostrando {tamanho} valores -=-=-')
    for valor in colecao:
        print(f'>> {valor}')


def remover_valor(valores):
    print()
    posicao = int(input('Qual posição vc deseja remover?\n>>> '))
    print()

    removido = valores.pop(posicao)
    print(f'O valor {removido} foi removido da posição {posicao}')


def atualizar_valor(cesta):
    print()
    pos = int(input('Qual posição? '))
    print()

    valor = cesta[pos]
    print(f'Na posição {pos} existe atualmente o valor {valor}')
    print()
    novo_valor = int(input('Qual o novo valor? '))
    cesta[pos] = novo_valor
    print()
    print('Valor atualizado com sucesso!')

def contagem_geral(lista):
    par = pares(lista)
    impar = impares(lista)
    positivo = positivos(lista)
    negativo = negativos(lista)

    print()
    print('Nesse vetor tem:')
    print(f'{par} números pares')
    print(f'{impar} números impares')
    print(f'{positivo} números positivos')
    print(f'{negativo} números negativos')
    print()

def pares(lista):
    qnt_p = 0
    for numero in lista:
        if numero % 2 == 0:
            qnt_p += 1

    return qnt_p

def impares(lista):
    qnt_i = 0
    for numero in lista:
        if numero % 2 == 1:
            qnt_i += 1

    return qnt_i

def positivos(lista):
    qnt_ps = 0
    for numero in lista:
        if numero > 0:
            qnt_ps += 1

    return qnt_ps

def negativos(lista):
    qnt_ng = 0
    for numero in lista:
        if numero < 0:
            qnt_ng += 1

    return qnt_ng

def calculador_de_media(colecao):
    somatorio = 0
    for valor in colecao:
        somatorio += valor
    media = somatorio / len(colecao)

    print()
    print(f'A média dos valores é {media:.2f}')


operacoes_vetores()