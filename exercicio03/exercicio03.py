# RESOLUÇÃO DO EXERCÍCIO 3
# Linguagem Python

import json

# Dados iniciais
valores_dados = []
soma = 0
dias = 0
dias_superior = 0

# Transforma arquivo JSON em vetor
with open('dados.json') as arquivo:
  dados = json.load(arquivo)
  
  
  for i in range(len(dados)):
    # Adiciona os valores de dados ao vetor valores_dados
    valores_dados.append(dados[i]['valor'])
    
    # Cálculo para a média
    if (dados[i]['valor'] != 0):
      soma += dados[i]['valor']
      dias += 1
    
  # Valores de centralidade
  valor_minimo = min(valores_dados)
  valor_maximo = max(valores_dados)
  valor_medio = soma / dias
  
  # Dias com faturamento acima da média
  for i in range(len(dados)):
    if (valores_dados[i] > valor_medio):
      dias_superior += 1
  
  # Impressão dos valores buscados
  print(f"Valor Mínimo: {valor_minimo}\nValor Máximo: {valor_maximo}\nNúmero de dias com faturamento superior à média: {dias_superior}")