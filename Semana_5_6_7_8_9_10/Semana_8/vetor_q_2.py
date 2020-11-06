print('\033[35m-=-=- Questão 2 -=-=-\033[m')
numero = []
while True:
    print()
    n = int(input('Digite um valor:\n>>> '))
    print()
    if n not in numero:
        numero.append(n)
        print('Valor adicionado')
        print()
    else:
        print('-='*5)
        print('Valor duplicado')
        print('-='*5)
        print()

    r = input('Desejar continuar? (S/N)\n>>> ')
    if r in 'Nn':
        break
