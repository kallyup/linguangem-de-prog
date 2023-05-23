'''jogo = {'Nome':'Super Mario',
        'Desenvolvedora':'Nintendo',
        'Ano':1990}

jogo['Genero']='Aventura'
print(jogo)

jogo.keys() #Devolve as chaves do dicionário
jogo.values() #Devolve os valores apenas
jogo.items() #Devolve uma lista com tuplas(chave,valor)
'''
listaJogos = []

jogo1 = {'Nome': 'Super Mario', 'videogame': 'SNES', 'Ano': 1990}
jogo2 = {'Nome': 'Mario Kart 64', 'videogame': 'N64', 'Ano': 1998}
jogo3 = {'Nome': 'Pokemon Yellow', 'videogame': 'GameBoy', 'Ano': 1999}

listaJogos = [jogo1,jogo2,jogo3]

jogo = {'Nome':'Super Mario',
        'Desenvolvedora':'Nintendo',
        'Ano':1990}

jogo.update({'Ano':1991,'Genero':'Plataforma'}) # update altera o dicionário

print(jogo)


print(listaJogos)
#Vai acessar a informação MArio Kart 64
#print(listaJogos[1]['Nome'])