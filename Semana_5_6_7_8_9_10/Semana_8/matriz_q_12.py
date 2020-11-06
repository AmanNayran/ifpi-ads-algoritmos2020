print('\033[35m-=-=- Questão 12 -=-=-\033[m')

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

print('-='*20)
print('-='*8,'Soma1', '-='*8)
soma_diagonal_principal = 0
for l in range(0,n):
    for c in range(0,n):
        if l == c:
            soma_diagonal_principal += matriz[l][c]
            print(f'[{matriz[l][c]:^5}]', end= '')


print(f' = {soma_diagonal_principal}')

print('-='*20)
print('-='*8, 'Soma2', '-='*8)
soma_diagonal_secundaria = 0
for l in range(0,n):
    for c in range(0,n):
        if l == n - c - 1:
            soma_diagonal_secundaria += matriz[c][n - c - 1]
            print(f'[{matriz[c][n - c - 1]:^5}]', end= '')

print(f' = {soma_diagonal_secundaria}')

print('-='*20)
print('-='*6,'Soma outros', '-='*6)
soma_total = 0
for l in range(0,n):
    for c in range(0,n):
        soma_total += matriz[l][c]

outros = soma_total - (soma_diagonal_principal + soma_diagonal_secundaria)
print(f'A soma dos outros elementos é {outros}')
print('-='*20)