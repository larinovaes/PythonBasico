# 2. Faça um programa que recebe o valor de um produto e um percentual de desconto e imprime a valor do desconto e o preço a pagar.

valor = float( input("Valor original: R$ ") )
desconto = float( input("Quanto deseja de desconto?"))

total = valor * desconto
comDesconto = total - desconto
valorTotal = valor - comDesconto

print('Valor sem desconto:     R$', valor)
print('Desconto ganho:     R$',total)
print('Valor com desconto: R$', valorTotal)