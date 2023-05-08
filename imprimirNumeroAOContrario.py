numero = int(input("digite um numero "))
centena = numero // 100
unidade = numero % 10
dezena = (numero//10) % 10

print(unidade*100 + dezena*10 + centena)

num = input(" digite um numero ")
num = num[::-1]
print(num)