texto = ("Super Mario Bros")

def contMaiMin(texto):
    mi = 0
    ma = 0
    for letra in texto:
       if letra.isupper():
           ma += 1
       elif letra.islower():
           mi += 1

       print(letra)
    print(mi)
    print(ma)
msg = ("Super Mario Bros")
contMaiMin(msg)