def Vetor():
    print('\033[35m-=-=- Vetor -=-=-\033[m')
    tamanho_vetor = int(input('Quantos valores desejar inserir?\n>>> '))
    vetor = [-1] * tamanho_vetor

    for posicao in range(tamanho_vetor):
        vetor[posicao] = int(input(f'\n{posicao+1}° número:\n>>> '))

    print()
    print(f'O vetor é:\n{vetor}')

    par = pares(vetor)
    impar = impares(vetor)
    positivo = positivos(vetor)
    negativo = negativos(vetor)

    print()
    print('Nesse vetor tem:')
    print(f'{par} números pares')
    print(f'{impar} números impares')
    print(f'{positivo} números positivos')
    print(f'{negativo} números negativos')
    print()

    vetor_transformado = transformar(vetor)
    print('Vetor transformado')
    print(vetor)

    
    par = pares(vetor_transformado)
    impar = impares(vetor_transformado)
    positivo = positivos(vetor_transformado)
    negativo = negativos(vetor_transformado)

    print()
    print('Nesse vetor transformado tem:')
    print(f'{par} números pares')
    print(f'{impar} números impares')
    print(f'{positivo} números positivos')
    print(f'{negativo} números negativos')
    print()
    

    media = calculador_de_media(vetor_transformado)
    print(f'A média dos valores é {media}')



def pares(vetor):
    qnt_p = 0
    for numero in vetor:
        if numero % 2 == 0:
            qnt_p += 1

    return qnt_p

def impares(vetor):
    qnt_i = 0
    for numero in vetor:
        if numero % 2 == 1:
            qnt_i += 1

    return qnt_i

def positivos(vetor):
    qnt_ps = 0
    for numero in vetor:
        if numero > 0:
            qnt_ps += 1

    return qnt_ps

def negativos(vetor):
    qnt_ng = 0
    for numero in vetor:
        if numero < 0:
            qnt_ng += 1

    return qnt_ng

def transformar(vetor):
    for i in range(len(vetor)):
        if vetor[i] > 0:
            vetor[i] = vetor[i] * 2
        else:
            vetor[i] = vetor[i] / 2

    return vetor

def calculador_de_media(vetor):
    somatorio = 0
    for valor in vetor:
        somatorio += valor
    media = somatorio / len(vetor)

    return media

Vetor()