print("-"*60)
print('Bem Vidos a Loja da Débora Lídia Barros de Macedo'.center(60))
print("-"*60)
# ru -Registro único indetificação
ru = 4303056
valor = float(input('digite o valor do produto: '))
quantidade = int(input('digite a quantidade de produtos desejada: '))

#aplicando descontos
#Se o cliente comprar entre 10 e 99 unidades ganha 5% de desconto
if 10 <= quantidade <= 99:
    valordesc = valor * 0.95
    print('Você recebeu 5% de desconto valor atual {}R$ {}{} '.format('\033[1;32m', valordesc*quantidade, '\033[m'))
#Se o cliente comprar entre 100 e 999 unidades ganha 10% de desconto
elif 100 <= quantidade <= 999:
    valordesc = valor * 0.90
    print('Você recebeu 10% de desconto valor atual {}R$ {}{} '.format('\033[1;32m', valordesc*quantidade, '\033[m'))
#Se o cliente comprar apartir de 1000 unidades ganha 15% de desconto
elif quantidade >= 1000:
    valordesc = valor * 0.85
    print('Você recebeu 15% de desconto valor atual {}R$ {}{} '.format('\033[1;32m', valordesc*quantidade, '\033[m'))
#Se o cliente comprar menos que 10 unidades não ganha desconto
else:
    print('Voce não atingiu quantidade suficiente para ganhar desconto. O valor do produto sem desconto é : {}R$ {}{}'.format('\033[1;31m', valor*quantidade, '\033[m'))

print('O valor do produto sem desconto é : {}R$ {}{}'.format('\033[1;31m', valor*quantidade, '\033[m'))
print('Meu RU é : {}{}{}'.format('\033[1;35;40m', ru, '\033[m'))
