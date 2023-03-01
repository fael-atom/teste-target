# RESOLUÇÃO DO EXERCÍCIO 02
# Linguagem Python

# Dados iniciais
sequencia = [0, 1];
elemento_sequencia = 0;

# Entrada do usuário
numero_usuario = eval(input("Insira um número: "))

# Analise se o número pertence à sequência de Fibonacci
while True:
  if numero_usuario in sequencia:
    print(f"O número {numero_usuario} pertence à sequência de Fibonacci {sequencia}.")
    break;
  elif (sequencia[-1] > numero_usuario):
      print(f"O número {numero_usuario} NÃO pertence à sequência de Fibonacci {sequencia}")
      break;
  else:
    elemento_sequencia = sequencia[-2] + sequencia[-1]
    sequencia.append(elemento_sequencia)