sexo = input('Qual o seu sexo? (m ou f)').lower()
estatura = float(input('Qual a sua estatura?'))
if sexo == 'm':
    print(f'Seu peso ideal é {(72.7*estatura)-58}')
elif sexo == 'f':
    print(f'Seu peso ideal é {(62.1*estatura)/44.7}')
else:
    print("deixa de ser burro digita m ou f")