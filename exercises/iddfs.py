import copy
import heapq

estado_inicial = [[1, 0, 3], [4, 5, 6], [7, 8, 2]]
estado_final =  [[1,2,3],[4,5,6],[7,8,0]]
movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]



class No:
  def __init__(self, estado_atual, acao, pai, custo_do_caminho):
      self.estado_atual = estado_atual
      self.acao = acao
      self.pai = pai
      self.custo_do_caminho = custo_do_caminho



def abrir_No(no_pai, movimentos):

  vizinhos = []

  for linha_idx, linha in enumerate(no_pai.estado_atual):
    if 0 in linha:
      coluna_idx = linha.index(0)
      posicao_x, posicao_y = linha_idx, coluna_idx
      break

  for movimento in movimentos:

    if(0 <= movimento[0] + posicao_x <= 2 and 0 <= movimento[1] + posicao_y <= 2):

      novo_estado = copy.deepcopy(no_pai.estado_atual)

      novo_x = posicao_x + movimento[0]
      novo_y = posicao_y + movimento[1]

      novo_estado[posicao_x][posicao_y], novo_estado[novo_x][novo_y] = novo_estado[novo_x][novo_y], novo_estado[posicao_x][posicao_y]

      filho = No(novo_estado, movimento, no_pai, no_pai.custo_do_caminho + 1)

      vizinhos.append(filho)

  return vizinhos



def IDDFS(tabuleiro):

  for limite in range(1, 100):

    inicio = No(tabuleiro, None, None, 0)

    explorados = {}

    fronteira = [inicio]

    while(len(fronteira) > 0):

      no_atual = fronteira.pop()

      if(no_atual.estado_atual == estado_final):

        return no_atual, explorados

      else:

        if(no_atual.custo_do_caminho < limite):

          atual = str(no_atual.estado_atual)
          if (atual not in explorados) or (no_atual.custo_do_caminho < explorados[atual]):

            explorados[atual] = no_atual.custo_do_caminho

            fronteira.extend(abrir_No(no_atual, movimentos))



vencedor, explorados = IDDFS(estado_inicial)

no = vencedor
caminho = []
direcoes = []

while (no != None):

  caminho.append(no.estado_atual)
  direcoes.append(no.acao)

  no = no.pai

passos = len(caminho) - 1

print("Passos", passos)
print("Estados Expandidos", len(explorados)-1)

for tabuleiro, direcao in zip(caminho[::-1], direcoes[::-1]):

    if direcao is not None:
        print(direcao)

    for linha in tabuleiro:
        print(linha)

    print("-" * 15)