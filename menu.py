from IPython.display import clear_output

while True:
  clear_output() #limpeza de tela, apenas para o colab
  print('Calculadora')
  print('1-Somar:')
  print('2-Subtrair:')
  print('3-Multiplicar:')
  print('4-Dividir:')
  print('0-Sair:')

  op=int(input('Digite sua opção: '))
  print()
  if op == 1:
    val1=int(input('Digite um valor:'))
    val2=int(input('Digite outro valor:'))
    print('Resposta:',val1+val2)
  elif op == 2:
    val1=int(input('Digite um valor:'))
    val2=int(input('Digite outro valor:'))
    print('Resposta:',val1-val2)
  elif op == 3:
    val1=int(input('Digite um valor:'))
    val2=int(input('Digite outro valor:'))
    print('Resposta:',val1*val2)
  elif op == 4:
    val1=int(input('Digite um valor:'))
    val2=int(input('Digite outro valor:'))
    print('Resposta:',val1/val2)
  elif op==0:
    break
  else:
    print('Opção inválida')
    continue
