#cabeçalho
print("-"*65)
print('*Bem Vidos a lanchonete da Débora Lídia Barros de Macedo*'.center(60))
print("-"*65)
# ru -Registro único indetificação
ru = 4303056
codigo = ('CÓDIGO', 100, 101, 102, 103, 104, 105, 200, 201)
descricao = ('DESCRIÇÃO', 'Cachorro-Quente', 'Cachorro-Quente Duplo', 'X-Egg', 'X-Salada', 'X-bacon', 'X-tudo', 'Refrigerante em Lata', 'Chá Gelado')
preco = ('VALOR(R$)', 9.00, 11.00, 12.00, 13.00, 14.00, 17.00, 5.00, 4.00)
#Mostrando o menu
print('CARDÁPIO'.center(60))
print("-"*65)
for i in range(len(codigo)):
    print(f'{codigo[i]: <15}', end=' ')
    print(f'{descricao[i]: ^30}', end=' ')
    print(f'{preco[i]:>15}')
#iniciando a interação com o usuário
total = 0
while True:
    #perguntado se quer continuar
    continuar = input('Deseja continuar? S/N').upper()
    if continuar == 'S':
        #interação sobre os produtos que deseja
        codProduto = int(input('digite o código do produto'))
        if codProduto in codigo:
            #pegar a posição na lista, onde está o código
            posicao=codigo.index(codProduto)
            print(f'Você pediu {descricao[posicao]: ^30} {preco[posicao]:>10}')
            total += preco[posicao]
            print(f'Total = R${total}')
        else:
            print('opção invalida')
            continue
    else:
        print('O valor total dos produtos é : {}R$ {}{}'.format('\033[1;31m', total, '\033[m'))
        break


print('Meu RU é : {}{}{}'.format('\033[1;35;40m', ru, '\033[m'))
#CODIGO ANTES DO REFATORAMENTO PODE CONSIDERAR O MAIS CERTO PARA O QUE FOI PEDIDO
'''if codProduto == 100:
    print(f'Você pediu {descricao[1]: ^30} {preco[1]:>10}')
    total += preco[1]
    print(f'Total = R${total}')
elif codProduto == 101:
    print(f'Você pediu {descricao[2]: ^30} {preco[2]:>10}')
    total += preco[2]
    print(f'Total = R${total}')
elif codProduto == 102:
    print(f'Você pediu {descricao[3]: ^30} {preco[3]:>10}')
    total += preco[3]
    print(f'Total = R${total}')
elif codProduto == 103:
    print(f'Você pediu {descricao[4]: ^30} {preco[4]:>10}')
    total += preco[4]
    print(f'Total = R${total}')
elif codProduto == 104:
    print(f'Você pediu {descricao[5]: ^30} {preco[5]:>10}')
    total += preco[5]
    print(f'Total = R${total}')
elif codProduto == 105:
    print(f'Você pediu {descricao[6]: ^30} {preco[6]:>10}')
    total += preco[6]
    print(f'Total = R${total}')
elif codProduto == 200:
    print(f'Você pediu {descricao[7]: ^30} {preco[7]:>10}')
    total += preco[7]
    print(f'Total = R${total}')
elif codProduto == 201:
    print(f'Você pediu {descricao[8]: ^30} {preco[8]:>10}')
    total += preco[8]
    print(f'Total = R${total}')
else:
    print('opção invalida')
    continue'''