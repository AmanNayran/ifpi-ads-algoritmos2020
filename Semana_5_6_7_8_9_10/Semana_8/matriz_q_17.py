print('\033[35m-=-=- Questão 17 -=-=-\033[m')

n=int(input('Digite o valor de n da matriz n x n: '))
matriz=[[] for c in range(0,n)]
for l in range(0,n):
    for c in range(0,n):
        matriz[l].append(int(input(f'Digite um valor para [{l},{c}]: ')))

print('-='*20)
for l in range(0,n):
    for c in range(0,n):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
    

maior = 0
menor = matriz[l][c]

print('-='*20)
for l in range(0,n):
    for c in range(0,n):
        if maior < matriz[l][c]:
            maior = matriz[l][c]
        if matriz[l][c] < menor:
            menor = matriz[l][c]

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
