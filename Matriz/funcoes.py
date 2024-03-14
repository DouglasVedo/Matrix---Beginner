# Função para realizar a soma entre as metrizes

def soma(matriz_A, matriz_B):
  matriz_C = []
  for linha_a , linha_b in zip(matriz_A, matriz_B):
    linha_c = []
    for elemento_a , elemento_b in zip(linha_a, linha_b):
      elemento_c = elemento_a + elemento_b
      linha_c.append(elemento_c)
    matriz_C.append(linha_c)
  return matriz_C

# Função para realizar a multiplicação entre as metrizes

def produto(matriz_A, matriz_B):
  matriz_C=[]
  for n_linha in range(len(matriz_A)):
    linha_c = []
    for n_coluna in range(len(matriz_B[0])):
      linha = matriz_A[n_linha]
      coluna = [col[n_coluna] for col in matriz_B]
      mult_resultado = [elemento_a*elemento_b for elemento_a, elemento_b in zip (linha,coluna)]
      linha_c.append(sum(mult_resultado))
    matriz_C.append(linha_c)
  return matriz_C

# Função para realizar a transposta da matriz

def transposta(matriz_A):
  matriz_B = []
  for n_coluna in range(len(matriz_A[0])):
    linha_b = [col[n_coluna] for col in matriz_A]
    matriz_B.append(linha_b)
  return matriz_B

# Função para realizar a simetria da matriz

def simetrica(matriz_A):
  if matriz_A == transposta(matriz_A):
    return True
  return False

# Função para calcular o determinante da matriz

def determinante_2(matriz_A):
  return matriz_A[0][0] * matriz_A[1][1] - matriz_A[1][0] * matriz_A[0][1]

def determinante_3(matriz_A):

  positivo = (matriz_A[0][0] * matriz_A[1][1] * matriz_A[2][2]) + (matriz_A[0][2] * matriz_A[1][0] * matriz_A[2][1]) + (matriz_A[0][1] * matriz_A[1][2] * matriz_A[2][0])
  negativo = (matriz_A[0][2] * matriz_A[1][1] * matriz_A[2][0]) + (matriz_A[0][0] * matriz_A[1][2] * matriz_A[2][1]) + (matriz_A[0][1] * matriz_A[1][0] * matriz_A[2][2])
  return positivo - negativo

# Função para concatenar as matrizes na horizontal

def concatenar_horizontal(matriz_A, matriz_B):
  matriz_C = []
  for linha_a, linha_b in zip(matriz_A, matriz_B):
    linha_c = []
    linha_c.extend(linha_a)
    linha_c.extend(linha_b)
    matriz_C.append(linha_c)
  return matriz_C

# Função para concatenar as matrizes na vertical

def concatenar_vertical(matriz_A, matriz_B):
  matriz_C = []
  matriz_C.extend(matriz_A)
  matriz_C.extend(matriz_B)
  return matriz_C