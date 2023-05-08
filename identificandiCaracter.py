ascii = ord(input("digite qualquer coisa: "))
if 57 >= ascii >= 48:
    print('é um numero')
elif 90 > ascii >= 65:
    print('é uma letra maiuscula')
elif ascii <= 122 and ascii>=97:
    print('é letra minuscula')
else:
    print('é um simbolu')
print(ascii)
