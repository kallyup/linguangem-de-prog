#{'cidade':'curitiba','latitude':-25.2548,'longitude':-49.1615}

listaCidades=[]
cidade = {}

def funcLatitude(dicionarioCidade):
  return dicionarioCidade['latitude']

def funcLongitude(dicionarioCidade):
  return dicionarioCidade['longitude']


#leitura das cidades, nome vazio encerra
nome = input('Digite o nome da cidade: ')
while nome != '':
  cidade['nome']=nome
  cidade['latitude']=float(input('Latitude: '))
  cidade['longitude']=float(input('Longitude: '))
  listaCidades.append(cidade.copy())
  nome = input('Digite o nome da cidade: ')

print(listaCidades)
#colocando em ordem crescente por latitude e longitude
listaNomes=["Mario","Luigi","Yoshi"]
sorted(listaNomes)
#sorted = função que ordena a lista
#lambda = cria uma função de uma linha no forma ENTRADA : SAIDA
listaSulNorte = sorted(listaCidades,key=funcLatitude)
listaOesteLeste = sorted(listaCidades,key=funcLongitude)
'''ou desse modo com lambda listaSulNorte = sorted(listaCidades,key=lambda dicionario : dicionario['latitude'])
listaOesteLeste = sorted(listaCidades,key=lambda dicionario : dicionario['longitude'])'''
norte = listaSulNorte[-1]['nome']
sul = listaSulNorte[0]['nome']
leste =listaOesteLeste[-1]['nome']
oeste = listaOesteLeste[0]['nome']


print('norte:',norte)
print('sul:',sul)
print('leste:',leste)
print('oeste:',oeste)
