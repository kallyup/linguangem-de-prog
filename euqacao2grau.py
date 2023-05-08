
x1 = float(input('digite uma valor :'))
y1 = float(input('digite uma valor :'))
x2 = float(input('digite uma valor :'))
y2 = float(input('digite uma valor :'))
x = (x1+x2) / 2
y = (y1+y2) / 2

if x >= 1 and y >= 1:
    print('primeiro quadrante ')
elif x <= 1 and y <= 1:
    print('terceiro quadrante')
elif x >= 1 >= y:
    print('quarto quadrante')
else:
    print('segundo quadrante')