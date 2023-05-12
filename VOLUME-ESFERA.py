import math
def volumeEsfera(x):
  volume = (4*math.pi/3) * (math.pow(raio,3)) # potencia poderia ser **
  return volume

raio = float(input("Digite o raio da esfera: "))
resposta = volumeEsfera(raio)
print(f"resposta:{resposta:.2f}")