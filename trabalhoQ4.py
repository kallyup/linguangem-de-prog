print("- " *65)
print('*Bem Vidos ao Estoque da Bicicletaria da Débora Lídia Barros de Macedo*'.center(60))
print("- " *65)
# ru -Registro único indetificação
ru = 4303056

listaPecas = [{'codigo': 997, 'nome': 'bola', 'fabricante': 'nike', 'valor': '465'},
 {'codigo': 998, 'nome': 'bota', 'fabricante': 'nike', 'valor': '654'}, 
 {'codigo': 999, 'nome': 'sapato', 'fabricante': 'adidas', 'valor': '564'}]

#contador do código iniciado em 1000
codigo = 1000
opcao = 0

#imprimir lista de peças
def imprimirPeca(pecasParaImprimir):
    print('\nCodigo:', pecasParaImprimir['codigo'], 
    '\nNome:', pecasParaImprimir['nome'], 
    '\nFabricante:', pecasParaImprimir['fabricante'],
    '\nValor:', pecasParaImprimir['valor'])

#cadastrar peças
def cadastrarCodigo(codigo):
    continuar = ('s')
    while continuar != 'N':
        pecas = {}
        pecas['codigo'] = codigo
        codigo+=1
        pecas['nome'] = input("digite o nome da peça")
        pecas['fabricante'] =input("digite o fabricante da peça")
        pecas['valor'] = input('digite o valor da peça')
        listaPecas.append(pecas.copy())
        continuar = input('Deseja continuar cadastrando? S/N ').upper()
    print('lista de Peças:')
    for pecas in listaPecas:
        imprimirPeca(pecas)
#consultar peças
def consultarPeca():
    print('Você escolheu consultar Peças')
    print('1-Consultar todas as Peças')
    print('2-Consultar Peças por código')
    print('3-Consultar Peças por fabricante')
    print('4-Retornar')
    consulta = int(input("Digite Uma opção"))
    if consulta == 1:
        for pecas in listaPecas:
            imprimirPeca(pecas)
    elif consulta == 2:
        codigoPesquisado = int(input('Digite o código do produto: '))
        for pecas in listaPecas:
            if pecas['codigo'] == codigoPesquisado:
                imprimirPeca(pecas)
    elif consulta == 3:
        fabricantePesquisado = input('Digite o nome do fabricante')
        for pecas in listaPecas:
            if pecas['fabricante'] == fabricantePesquisado:
                imprimirPeca(pecas)
#remove peças adicionadas
def removerPecas():
    print('Você selecionou a opção de Remover Peças')
    remover = int(input('Digite o Código da Peça que  deseja remover: '))
    for pecas in listaPecas:
        if pecas['codigo'] == remover:
            listaPecas.remove(pecas)
            imprimirPeca(pecas)
#printando as opçoes
#chamando as funções
voltar = False
while voltar == False:
    print('1-Cadastrar Peças')
    print('2-Consultar Peças')
    print('3-Remover Peças')
    print('4-Sair')
    opcao = int(input('Digite Uma opção'))
    if opcao == 1:
        #cadastrar peças
        cadastrarCodigo(codigo)
    elif opcao == 2:
        #consultando peças
        consultarPeca()
    elif opcao == 3:
        #remover as peças
        removerPecas()
    elif opcao == 4:
        break
    else:
        print('\033[1;31mEscolha Inválida \033[m')

print('Meu RU é : {}{}{}'.format('\033[1;35;40m', ru, '\033[m'))