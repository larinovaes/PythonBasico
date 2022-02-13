#1. Escreva um programa que recebe uma quantidade de dias e imprime a quantidade de horas, minutos e segundos da quantidade informada.

dias =int(input("Quantidade de dias: ") )

horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

print('Quantida de dias digitados: ', dias)
print('Quantidade de horas: ', horas)
print('Quantida de minutos: ', minutos)
print('Quantidade de segundos: ', segundos)

# 2. Faça um programa que recebe o valor de um produto e um percentual de desconto e imprime a valor do desconto e o preço a pagar.

valor = float( input("Valor original: R$ ") )