# 3. Escreva um programa que recebe o valor de um salário e um percentual de aumento e imprime o valor do aumento e o novo salário.

salario = float( input("Salario sem percentual de aumento: ") )

aumento = salario * 0.2
novoSalario = salario + aumento

print('Salario: R$: ', salario)
print('Valor do aumento: ', aumento)
print('Novo salario: R$:' , novoSalario)
print('O valor do aumento foi 20%')