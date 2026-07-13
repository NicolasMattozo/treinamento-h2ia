heapq = __import__('heapq')

def calcular_heuristica(matriz):
        objetivo = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
        distancia = 0

        for i in range(3):
            for j in range(3):
                if matriz[i][j] != 0:
                    objetivo_linha = (matriz[i][j] - 1) // 3
                    objetivo_coluna = (matriz[i][j] - 1) % 3
                    distancia += abs(i - objetivo_linha) + abs(j - objetivo_coluna)

        return distancia

class No:
    def __init__(self, matriz, g, h, f, pai, vazio_linha, vazio_coluna):
        self.matriz = matriz
        self.g = g
        self.h = h
        self.f = f
        self.pai = pai
        self.vazio_linha = vazio_linha
        self.vazio_coluna = vazio_coluna

    def __lt__(self, outro):
        return self.h < outro.h

    def gerar_vizinhos(self):

        vizinhos = []
        movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for movimento in movimentos:

            nova_linha = self.vazio_linha + movimento[0]
            nova_coluna = self.vazio_coluna + movimento[1]

            if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:

                matriz_aberta = [list(linha) for linha in self.matriz]

                matriz_aberta[self.vazio_linha][self.vazio_coluna], matriz_aberta[nova_linha][nova_coluna] = matriz_aberta[nova_linha][nova_coluna], matriz_aberta[self.vazio_linha][self.vazio_coluna]

                novo_tabuleiro = tuple(tuple(linha) for linha in matriz_aberta)

                novo_g = self.g + 1
                novo_h = calcular_heuristica(novo_tabuleiro)
                novo_f = novo_g + novo_h

                vizinhos.append(No(novo_tabuleiro, novo_g, novo_h, novo_f, self, nova_linha, nova_coluna))

        return vizinhos

def a_estrela(matriz):

    matriz_embaralhada = ((8,7,4),(1,0,6),(5,3,2))
    h = calcular_heuristica(matriz_embaralhada)
    f = h

    no_inicial = No(matriz_embaralhada, 0, h, f, None, 1, 1)

    lista_aberta = []
    heapq.heappush(lista_aberta, (no_inicial.f, no_inicial))
    lista_fechada = set()

    while len(lista_aberta) > 0:

        f_atual, no_atual = heapq.heappop(lista_aberta)

        if no_atual.h == 0:
            caminho = []
            while no_atual is not None:
                caminho.append(no_atual.matriz)
                no_atual = no_atual.pai
            return caminho[::-1]

        lista_fechada.add(no_atual.matriz)

        filhos = no_atual.gerar_vizinhos()
        for filho in filhos:
            if filho.matriz not in lista_fechada:
                heapq.heappush(lista_aberta, (filho.f, filho))



caminho_vitorioso = a_estrela(None)

if caminho_vitorioso is None:
    print("Este puzzle é matematicamente impossível de ser resolvido!")
else:
    print(f"Solução encontrada em {len(caminho_vitorioso) - 1} passos!\n")

    for passo_numero, tabuleiro in enumerate(caminho_vitorioso):
        print(f"PASSO {passo_numero}")
        for linha in tabuleiro:
            print(linha)
        print()