import copy
import heapq

estado_inicial = [[1, 0, 3], [4, 5, 6], [7, 8, 2]]
estado_final = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
explorados = set()


def calcular_heuristica(tabuleiro):
    distancia = 0
    for i in range(3):
        for j in range(3):
            valor = tabuleiro[i][j]
            if valor != 0:
                linha_objetivo = (valor - 1) // 3
                coluna_objetivo = (valor - 1) % 3
                distancia += abs(i - linha_objetivo) + abs(j - coluna_objetivo)
    return distancia


class No:
    def __init__(self, estado_atual, acao, pai, g, h, f):
        self.estado_atual = estado_atual
        self.acao = acao
        self.pai = pai
        self.g = g
        self.h = h
        self.f = f


def abrir_No(no_pai, movimentos):
    vizinhos = []

    for linha_idx, linha in enumerate(no_pai.estado_atual):
        if 0 in linha:
            coluna_idx = linha.index(0)
            posicao_x, posicao_y = linha_idx, coluna_idx
            break

    for movimento in movimentos:
        if 0 <= movimento[0] + posicao_x <= 2 and 0 <= movimento[1] + posicao_y <= 2:
            novo_estado = copy.deepcopy(no_pai.estado_atual)

            novo_x = posicao_x + movimento[0]
            novo_y = posicao_y + movimento[1]

            novo_estado[posicao_x][posicao_y], novo_estado[novo_x][novo_y] = (
                novo_estado[novo_x][novo_y],
                novo_estado[posicao_x][posicao_y],
            )

            novo_g = no_pai.g + 1
            novo_h = calcular_heuristica(novo_estado)
            novo_f = novo_g + novo_h

            filho = No(novo_estado, movimento, no_pai, novo_g, novo_h, novo_f)
            vizinhos.append(filho)

    return vizinhos


def A_estrela(tabuleiro):
    global explorados
    explorados = set()

    h_inicial = calcular_heuristica(tabuleiro)
    f_inicial = h_inicial
    inicio = No(tabuleiro, None, None, 0, h_inicial, f_inicial)

    fronteira = []
    contador = 0
    heapq.heappush(fronteira, (inicio.f, inicio.h, contador, inicio))

    menor_g = {str(tabuleiro): 0}
    estados_expandidos = 0

    while len(fronteira) > 0:
        f_atual, h_atual, _, no_atual = heapq.heappop(fronteira)
        chave_atual = str(no_atual.estado_atual)

        if chave_atual in explorados:
            continue

        if no_atual.estado_atual == estado_final:
            return no_atual, estados_expandidos

        explorados.add(chave_atual)
        estados_expandidos += 1

        for filho in abrir_No(no_atual, movimentos):
            chave_filho = str(filho.estado_atual)

            if chave_filho not in menor_g or filho.g < menor_g[chave_filho]:
                menor_g[chave_filho] = filho.g
                contador += 1
                heapq.heappush(fronteira, (filho.f, filho.h, contador, filho))

    return None, estados_expandidos


vencedor, estados_expandidos = A_estrela(estado_inicial)

no = vencedor
caminho = []
direcoes = []

while no is not None:
    caminho.append(no.estado_atual)
    direcoes.append(no.acao)
    no = no.pai

passos = len(caminho) - 1

print(passos)
print(estados_expandidos)

for tabuleiro, direcao in zip(caminho[::-1], direcoes[::-1]):
    if direcao is not None:
        print(direcao)

    for linha in tabuleiro:
        print(linha)

    print("-" * 15)