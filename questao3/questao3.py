# 3. Escreva um programa que recebe o valor de um salário e um percentual de aumento e imprime o valor do aumento e o novo salário.

salario = float( input("Salario sem percentual de aumento: ") )

aumento = float( input("Aumento: ") )

valor= salario * aumento
novoSalario = salario + valor

print('Salario: R$: ', salario)
print('Valor do aumento: ', valor)
print('Novo salario: R$:' , novoSalario)
print('O valor do aumento foi 20%')