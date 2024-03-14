from funcoes import soma, produto, transposta, simetrica, determinante_2, determinante_3, concatenar_horizontal, concatenar_vertical
from interface import le_opcao, le_matriz, le_tamanho, salva_resultado

# Arquivo main onde chama todas as funções para realizar os calculos

while True:
  opcao = le_opcao()
  if opcao != 8: 
    print('MATRIZ A')
    tamanho_A = le_tamanho()
    if opcao == 1:  # Opção 1
      matriz_A = le_matriz(tamanho_A)
      print('MATRIZ B')
      tamanho_B = le_tamanho()
      if tamanho_A == tamanho_B:
        matriz_B = le_matriz(tamanho_B)
        resposta = soma(matriz_A, matriz_B)
        print(resposta)
      else:
        resposta = 'ERRO: Matriz não possui mesma dimenção.'
        print('ERRO: Matriz não possui mesma dimenção.')
        continue
      salva_resultado('soma', resposta, matriz_A,tamanho_A, matriz_B, tamanho_B)
    elif opcao == 2:  # Opção 2
      matriz_A = le_matriz(tamanho_A)
      print('MATRIZ B')
      tamanho_B = le_tamanho()
      if tamanho_A[1] == tamanho_B[0]:
        matriz_B = le_matriz(tamanho_B)
        resposta = produto(matriz_A, matriz_B)
        print(resposta)
      else:
        resposta = 'ERRO: Matriz A não possui o mesmo número de colunas que número de linahs de matriz B.'
        print('ERRO: Matriz A não possui o mesmo número de colunas que número de linahs de matriz B.')
        continue
      salva_resultado('produto', resposta, matriz_A,tamanho_A, matriz_B, tamanho_B)
    elif opcao == 3:  # Opção 3
      matriz_A = le_matriz(tamanho_A)
      resposta = transposta(matriz_A)
      print(resposta)
      salva_resultado('transposta', resposta, matriz_A, tamanho_A)
    elif opcao == 4:  # Opção 4
      if tamanho_A[0] == tamanho_A[1]:
        matriz_A = le_matriz(tamanho_A)
        resposta = simetrica(matriz_A)
        print(resposta)
      else:
        resposta = 'ERRO: Matriz não é quadrada.'
        print('ERRO: Matriz não é quadrada.')
        continue
      salva_resultado('simetrica', resposta, matriz_A, tamanho_A)
    elif opcao == 5:  # Opção 5
      if tamanho_A == [1,1]:
        matriz_A = le_matriz(tamanho_A)
        resposta = matriz_A[0][0]
        print(resposta)
      elif tamanho_A == [2,2]:
        matriz_A = le_matriz(tamanho_A)
        resposta = determinante_2(matriz_A)
        print(resposta)
      elif tamanho_A == [3,3]:
        matriz_A = le_matriz(tamanho_A)
        resposta = determinante_3(matriz_A)
        print(resposta)
      else:
        resposta = 'ERRO: Matriz A com dimenções inválidas.'
        print('ERRO: Matriz A com dimenções inválidas.')
        continue
      salva_resultado('simetrica', resposta, matriz_A, tamanho_A)
    elif opcao == 6:  # Opção 6
      matriz_A = le_matriz(tamanho_A)
      print('MATRIZ B')
      tamanho_B = le_tamanho()
      if tamanho_A[0] == tamanho_B[0]: 
        matriz_B = le_matriz(tamanho_B)
        resposta = concatenar_horizontal(matriz_A, matriz_B)
        print(resposta)
      else:
        resposta = 'ERRO: Matrizes não possuem os mesmo números de linhas.'
        print('ERRO: Matrizes não possuem os mesmo números de linhas.')
        continue
      salva_resultado('simetrica', resposta, matriz_A,tamanho_A, matriz_B, tamanho_B)
    elif opcao == 7:  # Opção 7
      matriz_A = le_matriz(tamanho_A)
      print('MATRIZ B')
      tamanho_B = le_tamanho()
      if tamanho_A[1] == tamanho_B[1]:
        matriz_B = le_matriz(tamanho_B) 
        resposta = concatenar_vertical(matriz_A, matriz_B)
        print(resposta)
      else:
        resposta = 'ERRO: Matrizes não possuem os mesmo números de colunas.'
        print('ERRO: Matrizes não possuem os mesmo números de colunas.')
        continue
      salva_resultado('simetrica', resposta, matriz_A,tamanho_A, matriz_B, tamanho_B)
  else:
    break