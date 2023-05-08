valor = int(input('quanto vc quer sacar? '))
notas100 = valor // 100
valor %= 100
notas50 = valor // 50
valor %= 50
notas20 = valor // 20
valor %= 20
notas5 = valor // 5
valor %= 5
notas1 = valor

print(f" vai ser {notas100} notas de 100, {notas50} notas 50 , {notas20} notas 20, {notas5} notas 5, {notas1} notas1")