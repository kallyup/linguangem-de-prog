'''for i in range (100, 1000, 10):
   print(i)'''
#A errado
'''i = 100
while (i <= 1000):
   print(i)
   i += 10'''
#B certo
'''i = 100
while (i <= 999):
   print(i)
   i += 10'''
#C errado
'''i = 99
while (i <= 1000):
   print(i)
   i += 10'''

'''x = 5
while x <= 25:
   print(x)
   x += 5'''
'''i = 88
while (i >=0):
    print(i)
    i-=4'''
'''for i in range(88,-1,-4):
    print(i)'''

'''x = int(input('-100 ate 100'))
while(x<100 and x>-100):
    x = int(input('-100 ate 100'))
    print(x)'''
'''for i in range(10,20):
    for j in range(10,20,2):
        print('{}+{}={}'.format(i,j,i+j))'''
cont = 5
soma = 0
while cont<=25:
    soma = soma +cont
    cont = cont +5
    print(soma)
print(soma)