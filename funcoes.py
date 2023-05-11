#função maior de 3
'''def maior3(x,y,z):
    if x >= y and x >=z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

m1 = maior3(10, 20, 30)
m2 = maior3(40, 50, 60)
m3 = maior3(70, 80, 90)
resultado = maior3(m1, m2, m3)

val1 = float(input('digite um valor'))
val2 = float(input('digite um valor'))
val3 = float(input('digite um valor'))

resultado = maior3(val1, val2, val3)
print(resultado)'''
# float(inf) e float(-inf) valores mais baixos possiveis no python
val = int(input('digite um valor '))
maximo = val
while val != 0 : #digitou 0 o programa para
    if val > maximo:
        maximo = val
    val = int(input('digite o valor'))
print('valor maximo', maximo)