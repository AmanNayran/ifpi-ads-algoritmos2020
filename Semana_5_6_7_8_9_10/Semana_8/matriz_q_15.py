print('\033[35m-=-=- Questão 15 -=-=-\033[m')
print()
l = int(input("Insira o número de linhas:\n>>> "))
c = int(input("Insira o número de colunas:\n>>> "))
print()

if l == c:
    print("A matriz é quadrada.")
    print('-='*20)

    n=int(l)
    matriz=[[] for c in range(0,n)]
    for l in range(0,n):
        for c in range(0,n):
            matriz[l].append(int(input(f'Digite um valor para [{l},{c}]: ')))

    print('-='*20)
    print('Matriz original')
    for l in range(0,n):
        for c in range(0,n):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()

    print('-='*20)
    print('Matriz transposta')
    for l in range(0,n):
        for c in range(0,n):
            print(f'[{matriz[c][l]:^5}]', end='')
        print() 

else:
    print("A matriz não é quadrada.")