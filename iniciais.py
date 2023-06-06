
def iniciais(nome, sobrenome):
    letrasIniciais = ""
    letrasIniciais += nome[0].upper()
    letrasIniciais += ". "
    letrasIniciais += sobrenom[0].upper()
    letrasIniciais += "."
    return letrasIniciais
nome = input('digite seu nome: ')
sobrenom = input('digite seu sobrenome: ')
iniciais(nome, sobrenom)