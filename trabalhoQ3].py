
print("- " *65)
print('*Bem Vindos a companhia de logistica da Débora Lídia Barros de Macedo*'.center(60))
print("- " *65)
# ru -Registro único indetificação
ru = 4303056

# função para imprimir tabela
def imprimirTabela(valor):
    for pos in range(0, len(valor)):
        if pos % 2 == 0:
            print(f'{valor[pos]:<50}', end='')
        else:
            print(f'Multi - {valor[pos]}')

# funçao para obter o volume do objeto
def dimensoesObjeto(valor):
    #cabeçalho e tabela
    print("-" * 65)
    print('TABELA VOLUME'.center(50))
    print("-" * 65)
    volume = ('volume < 1000 ', 10,
              '1000   <= volume < 10000', 20,
              '10000 <= volume < 30000', 30,
              '30000 <= volume < 100000', 50,
              'volume >= 100000', 'Não é aceito')
    imprimirTabela(volume)
#coletando os valores e passando no try except
    while True:
        try:
            altura = int(input('digite a altura do objeto (EM CM) '))
            comprimento = int(input('digite o comprimento do objeto(EM CM) '))
            largura = int(input('digite a largura do objeto (EM CM) '))
            objeto = (altura * largura * comprimento)
            #Condição de para do While
            #Ele só vai parar se os valores forem positivos, e o volume ser inferior a 100000
            if(altura>=0 and comprimento>=0 and largura>=0 and objeto<100000):
                break
            elif(objeto>=10000):
                print("Volume excedente, tente novamente:")
            else:
                print('Valor negativo não aceito, tente novamente:')
        #Em caso de digitar valor não númerico, entra no except e volta
        except:
            print('Valor não numérico, tente novamente:')
    # realizando a lógica para saber o valor a ser pago pelo volume
    if 0 <= objeto < 1000:
        valor = 10
    elif 1000 <= objeto < 10000:
        valor = 20
    elif 10000 <= objeto < 30000:
        valor = 30
    elif 30000 <= objeto < 100000:
        valor = 50
    print(f'O volume do objeto é {objeto}m3, O valor a ser pago é R${valor}')
    return valor

#funçao para saber o peso do objeto
def pesoObjeto(multi):
    # cabeçalho e tabelha
    print("-" * 65)
    print('TABELA PESO'.center(50))
    print("-" * 65)
    tabelaPeso = ('peso <= 0.1', 1,
                  '0.1 <= peso < 1', 1.5,
                  '1 <= peso < 10',	2,
                  '10  <= peso < 30', 3,
                  'peso =>   30', 'Não é aceito')
    imprimirTabela(tabelaPeso)
            
    #lógica para saber o multiplicador a ser usado e tratamento de erro no try except
    while multi == 0:
        try:
            peso = float(input('Digite o peso do objeto (EM KG) '))
            if 0 < peso <= 0.1:
                multi = 1
            elif 0.1 <= peso < 1:
                multi = 1.5
            elif 1 <= peso < 10:
                multi = 2
            elif 10 <= peso < 30:
                multi = 3
            elif peso >= 30:
                print('Peso execendete não é aceito, tente novamente:')
            elif peso < 0:
                print('Valor negativo não aceito, tente novametne:')
        except:
            print('valor não numérico')

    return multi

#funçao para saber a rota desejada e umltiplicdor usado
def rotaObjeto(multiR):
    # cabeçalho e tabela
    print("-" * 65)
    print('TABELA ROTAS'.center(50))
    print("-" * 65)
    rotas = (
        'RS - De Rio de Janeiro até São Paulo', 1,
        'SR - De São Paulo até Rio de Janeiro', 1,
        'BS - De Brasília até São Paulo', 1.2,
        'SB - De São Paulo até Brasília', 1.2,
        'BR - De Brasília até Rio de Janeiro', 1.5,
        'RB - Rio de Janeiro até Brasília', 1.5)
    imprimirTabela(rotas)
#lógica para saber o valor
    while multiR == 0:
        rota = input('Digite a Sigla da Rota Desejada: ').upper()
        if rota == 'RS':
            multiR = 1
        elif rota == 'SR':
            multiR = 1
        elif rota == 'BS':
            multiR= 1.2
        elif rota == 'SB':
            multiR = 1.2
        elif rota == 'BR':
            multiR= 1.5
        elif rota == 'RB':
            multiR = 1.5
        else:
            print('Sigla incorreta, tente novamente:')
    return multiR

#variavel para mutiplicar tudo e saber o total
total = dimensoesObjeto(0) * pesoObjeto(0) * rotaObjeto(0)
#printes finais do program com valor e ru
print('O valor total do produto é : {}R$ {}{}'.format('\033[1;31m', total, '\033[m'))
print('Meu RU é : {}{}{}'.format('\033[1;35;40m', ru, '\033[m'))