emprestimo = float(input('digite um valor '))
dias = int(input('digite os dias em atraso '))
multaDiaria = emprestimo * 0.02
total = emprestimo + dias * multaDiaria
print(total)