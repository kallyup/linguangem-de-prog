listaJogos = []
# CRUD
# Create
# Read
# Update
# Delete

while True:
    print('')
    print('1-Cadastrar Jogo')
    print('2-Listar Jogos')
    print('3-Remover Jogo')
    print('4-Pesquisar Jogo')
    print('0-Sair')

    try:
        op = int(input('Digite opção: '))
    except:
        op = -9999

    if op == 1:
        # Código de adicionar
        jogo = {}
        jogo['nome'] = input('Nome Jogo:')
        jogo['desenvolvedora'] = input('Desenvolvedora:')
        jogo['ano'] = int(input('Ano: '))
        listaJogos.append(jogo.copy())

    elif op == 2:
        # Código de listar
        print('Lista de jogos: ')
        for indice, jogo in enumerate(listaJogos):
            print(indice + 1, '- Nome:', jogo['nome'], 'Desenvolvedora:', jogo['desenvolvedora'], 'Ano:', jogo['ano'])
    elif op == 3:
        print('Lista de jogos - escolha qual remover:')
        for indice, jogo in enumerate(listaJogos):
            print(indice + 1, '- Nome:', jogo['nome'], 'Desenvolvedora:', jogo['desenvolvedora'], 'Ano:', jogo['ano'])
        indice = int(input('Digite o número do jogo:')) - 1
        # listaJogos.remove() #remove por conteúdo
        del listaJogos[indice]  # remove por indice

    elif op == 4:
        # código de pesquisar
        nomePesquisado = input('Digite o nome do jogo: ')
        encontrado = False
        for jogo in listaJogos:
            if jogo['nome'] == nomePesquisado:
                print('Nome:', jogo['nome'], 'Desenvolvedora:', jogo['desenvolvedora'], 'Ano:', jogo['ano'])
                encontrado = True
        if not encontrado:
            print('Jogo não encontrado')
    elif op == 0:
        break
    else:
        print('Opção errada!')


#com função
'''listaJogos= []
#CRUD
#Create
#Read
#Update
#Delete

def menu():
  print('')
  print('1-Cadastrar Jogo')
  print('2-Listar Jogos')
  print('3-Remover Jogo')
  print('4-Pesquisar Jogo')
  print('0-Sair')

def adicionar():
    jogo={}
    jogo['nome'] =input('Nome Jogo:')
    jogo['desenvolvedora'] = input('Desenvolvedora:')
    jogo['ano'] = int(input('Ano: '))
    listaJogos.append(jogo)

while True:
  menu()
  try:
    op = int(input('Digite opção: '))
  except:
    op=-9999
  if op ==1:
    #Código de adicionar
    adicionar()
  elif op==2:
    #Código de listar
    print('Lista de jogos: ')
    for indice,jogo in enumerate(listaJogos):
      print(indice+1,'- Nome:',jogo['nome'], 'Desenvolvedora:',jogo['desenvolvedora'],'Ano:',jogo['ano'])
  elif op==3:
    print('Lista de jogos - escolha qual remover:')
    for indice,jogo in enumerate(listaJogos):
      print(indice+1,'- Nome:',jogo['nome'], 'Desenvolvedora:',jogo['desenvolvedora'],'Ano:',jogo['ano'])
    indice = int(input('Digite o número do jogo:'))-1
    #listaJogos.remove() #remove por conteúdo
    del listaJogos[indice] #remove por indice

  elif op==4:
    #código de pesquisar
    nomePesquisado = input('Digite o nome do jogo: ')
    encontrado=False
    for jogo in listaJogos:
      if jogo['nome'] == nomePesquisado:
        print('Nome:',jogo['nome'], 'Desenvolvedora:',jogo['desenvolvedora'],'Ano:',jogo['ano'])
        encontrado=True
    if not encontrado:
      print('Jogo não encontrado')
  elif op==0:
    break
  else:
    print('Opção errada!')
'''