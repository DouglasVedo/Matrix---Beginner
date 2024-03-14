# Dicionário que contem as opções que o usuário pode escolher e seus valores

OPCOES = {  
    '1': 'Calcular a soma de duas matrizes',
    '2': 'Calcular o produto de duas matrizes',
    '3': 'Calcular a transposta de uma matriz',
    '4': 'Identificar se uma matriz é simétrica',
    '5': 'Calcular o determinante de uma matriz',
    '6': 'Concatenar duas matrizes horizontalmente',
    '7': 'Concatenar duas matrizes verticalmente',
    '8': 'Sair \n',
}

# Função para printar as opções e pegar a escolha do usuário

def le_opcao():
  print('\n---------Calculadora de matrizes---------\n')
  for chave, valor in OPCOES.items():
    print(f'{chave} - {valor}')
  while True:
    print('-----------------------------------------')
    opcao = input('Qual operaçõa desejada: ')
    if opcao in OPCOES.keys(): 
      return int(opcao)
    print('Opção inválida')

# Função para o usuário determinar o tamanho da matriz

def le_tamanho():
  tamanho_string = input('Qual o tamanho da sua matriz sendo linha por coluna. ex:(3x3): ')
  tamanho = [int(var) for var in tamanho_string.split('x')]
  return tamanho

# Função para o usuário preencher a matriz do tamanho escolhido por ele

def le_matriz(tamanho):
  matriz = []
  for var_linha in range(tamanho[0]):
    linha = []
    for var_coluna in range(tamanho[1]):
      novo_valor = float(input(f'Digite o valor da {var_linha+1} - {var_coluna+1}: '))
      linha.append(novo_valor)
    matriz.append(linha)
  return matriz

# Função para salvar em um arquivo .txt o resultado

def salva_resultado(funcao, resultado, matriz_A=None, tamanho_A=None, matriz_B=None, tamanho_B=None):
  nome_arquivo = input('Digite o nome do arquivo de saída (não escrever .txt no final do nome!)')
  with open(f'{nome_arquivo}.txt','w') as f:
    f.write(f'função: {funcao}\n')
    if matriz_A:
      f.write(f'Matriz A: {matriz_A}\n')
      f.write(f'Tamanho A: {tamanho_A[0]} X {tamanho_A[1]}\n')
    if matriz_B:
      f.write(f'Matriz B: {matriz_B}\n')
      f.write(f'Tamanho B: {tamanho_B[0]} X {tamanho_B[1]}\n') 
    f.write(f'Resultado: {resultado}\n') 
    if type(resultado) == list:
      f.write(f'Tamanho resultado: {len(resultado)} X {len(resultado[0])} ')