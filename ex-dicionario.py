chaves = ['Dez', 'Vinte', 'Trinta']
valores = [10, 20, 30]
#dicionario = dict(zip(chaves,valores)) tb funciona
dicionario = {}
tam = len(chaves)
for i in range(tam):
  dicionario[chaves[i]] = valores[i]

print(dicionario)
