print('\033[35m-=-=- Questão 8 -=-=-\033[m')
lista = []
qnt_numeros = int(input('Digite a quantidade de números:\n>>> '))
print()

maior = 0
menor = 0

for i in range(0, qnt_numeros):
    lista.append(int(input(f'Digite um número para a posição {i}:\n>>> ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor[i] = lista[i]

print()
print(f'lista:\n{lista}')
print()
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
print()