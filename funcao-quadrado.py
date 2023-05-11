import math
def quadrado(lado):

    area = lado * lado
    perimetro = 4 * lado
    diagona = (lado * math.sqrt(2))
    print(area)
    print(perimetro)
    print(f'diagona {diagona:.2f}')
lado = float(input('digite um valor'))
quadrado(lado)

'''import math

def quadrado(x):
  print('area do quadrado é {}'.format(x*x))
  print('perimetro do quadrado é {}'.format(4*x))
  print('tamanho da diagonal é {}'.format(x*math.sqrt(2)))

lado = float(input('digite lado do quadrado: '))

quadrado(lado)'''