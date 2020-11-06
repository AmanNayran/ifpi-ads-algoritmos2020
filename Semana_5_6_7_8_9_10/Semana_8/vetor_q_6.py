print('\033[35m-=-=- Questão 6 -=-=-\033[m')
num = int(input('Digite um número na base binária:\n*OBS:Máximo de caractere é 8\n>>> '))
print()
numberEx = int ( f"{num}" , 2) 
print(f'Base binária = {num}')
print()
print(f'Base decimal = {numberEx}')

hexadecimal = hex(numberEx) [2:]
print(f'Base hexadecimal = {hexadecimal}')
