def WordPlay():
    print()
    menu = '\033[35m-=-=- WordPlay -=-=-\n\033[m' \
        + '\n' \
        + '1 - Palavras com mais de 20 letras\n' \
        + '2 - Palavras sem o "e"\n' \
        + '3 - Palavras proibidas\n' \
        + '0 - Sair\n' \
        + '\nDigite uma opção:\n>>> '

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            print()
            palavras_com_mais_de_20_letras()
            print()
        elif opcao == 2:
            print()
            palavras_sem_letra_e()
            print()
        elif opcao == 3:
            print()
            letras_proibidas()
            print()
        else:
            print('ERRO...Opção Inválida!')

        input('Para continuar aperte <enter> ...')
        opcao = int(input(menu))

    print('Obrigado pela atenção.')


def palavras_com_mais_de_20_letras():
    print('>>> Palavras com + de 20 letras \n')
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha
        if len(palavra) > 20:
            print(palavra)

    arquivo.close()


def palavras_sem_letra_e():
    print('>>> Palavras sem letra "e" \n')
    arquivo = open('words.txt')
    total_de_palavras = 0
    palavras_sem_e = 0

    for linha in arquivo:
        palavra = linha
        total_de_palavras += 1
        if has_no_e(palavra):
            palavras_sem_e += 1
            print(palavra)

    porcentagem = (palavras_sem_e / total_de_palavras) * 100

    print(f'Total de Palavras = {total_de_palavras}')
    print(f'Palavras sem "e" = {palavras_sem_e}')
    print(f'Porcentagem = {porcentagem:.2f} %')
    arquivo.close()


def has_no_e(palavra):
    return 'e' not in palavra


def letras_proibidas():
    print('>>> Palavras proibidas \n')
    arquivo = open('words.txt')

    l_p_1 = input('primeira letra proibida:\n>>> ')
    l_p_2 = input('segunda letra proibida:\n>>> ')
    l_p_3 = input('terceira letra proibida:\n>>> ')

    for linha in arquivo():
        palavra = linha
        if avoids(palavra, l_p_1, l_p_2, l_p_3):
            print(palavra)

    arquivo.close()


def avoids(palavra, l_p_1, l_p_2, l_p_3):
    return l_p_1, l_p_2, l_p_3 not in palavra



WordPlay()