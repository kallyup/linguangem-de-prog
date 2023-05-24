print("-"*60)
print('Bem Vidos a Loja da Débora Lídia Barros de Macedo'.center(60))
print("-"*60)
ru = 4303056
valor = float(input('digite o valor do produto: '))
quantidade = int(input('digite a quantidade de produtos desejada: '))
#aplicando descontos
if 10 <= quantidade <= 99:
    valordesc = valor - valor * 0.05
    print('Você recebeu 5% de desconto valor atual {}R$ {}{} '.format('\033[1;32m', valordesc*quantidade, '\033[m'))
elif 100 <= quantidade <= 999:
    valordesc = valor - valor * 0.10
    print('Você recebeu 10% de desconto valor atual {}R$ {}{} '.format('\033[1;32m', valordesc*quantidade, '\033[m'))
elif quantidade >= 1000:
    valordesc = valor - valor * 0.15
    print('Você recebeu 15% de desconto valor atual {}R$ {}{} '.format('\033[1;32m', valordesc*quantidade, '\033[m'))
else:
    print('Voce não atingiu quantidade suficiente para ganhar desconto. O valor do produto sem desconto é : {}R$ {}{}'.format('\033[1;31m', valor*quantidade, '\033[m'))
print('O valor do produto sem desconto é : {}R$ {}{}'.format('\033[1;31m', valor*quantidade, '\033[m'))
print('Meu RU é : {}{}{}'.format('\033[1;35;40m', ru, '\033[m'))
