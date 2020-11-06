import os
import json


def app():

    celulares = inicializar('celulares.bd')

    menu = interface()
    opçao = int(input(menu))

    while opçao != 0:
        if opçao == 1:
            celular = novo_celular()
            celulares.append(celular)
            print()
            print('O celular foi registrado com êxito!')
        elif opçao == 2:
            listar_celulares(celulares)
        elif opçao == 3:
            print('-=-'*10)
            print('Buscar por nome ou marca:')
            print()
            busc = input('Buscar:\n>>> ')
            print()
            celulares_encontrados = buscar(celulares, busc)
            for celular in celulares_encontrados:
                print('Nome:', celular['nome'])
                print('Marca:', celular['marca'])
                print('Valor:', celular['valor'])
                print('-=-'*10)

        input('Para continuar aperte <enter>...')
        opçao = int(input(menu))

    print('Obrigado pela atenção.')
    finalizar('celulares.bd', celulares)


def interface():
    menu = '\033[35m-=-=- App -=-=-\033[m\n'
    menu += '1 - Registrar celular\n'
    menu += '2 - Listar celular\n'
    menu += '3 - Buscar (nome ou marca)\n'
    menu += '0 - Salvar e sair\n'
    menu += '\nEscolha uma opção:\n>>> '

    return menu


def inicializar(nome_arquivo):
    celulares_carregados = []

    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        dados = arquivo.readline()
        arquivo.close()
        celulares_carregados = json.loads(dados)

    return celulares_carregados


def finalizar(nome_arquivo, celulares):
    dados = json.dumps(celulares)

    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)
    arquivo.close()


def novo_celular():
    print('-=-'*10)
    print('Registrando novo celular')
    print()

    nome = input('Nome do celular: ')
    marca = input('Marca do celular: ')
    tela = input('Qual o tamanho da tela("): ')
    valor = float(input('Quanto custa o celular(R$): '))
    cam_frontal = input('Possui câmera frontal(Sim/Não): ')
    print('-=-'*10)

    celular = {}
    celular['nome'] = nome
    celular['marca'] = marca
    celular['tela'] = tela
    celular['valor'] = valor
    celular['cam_frontal'] = cam_frontal

    return celular


def listar_celulares(celulares):
    qtd = len(celulares)
    print('-=-'*10)
    print(f'Listando {qtd} celulares')
    print()

    for celular in celulares:
        print('Nome:', celular['nome'])
        print('Marca:', celular['marca'])
        print('Valor:', celular['valor'])
        print('-=-'*10)

def buscar(celulares, chave_busca):
    resultado = []
    for celular in celulares:
        if chave_busca in celular['nome']:
            resultado.append(celular)
        else:
            print('Nenhum resultado encontrado')
            print('-=-'*10)

    return resultado

app()