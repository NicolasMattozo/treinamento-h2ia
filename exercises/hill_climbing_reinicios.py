import random
import pandas as pd
random.seed(2)

# Estabelece limites
LIMITE = 275

# Inicia Itens solicitado no exercicio
peso = [63, 21, 2, 32, 13, 80, 19, 37, 56, 41, 14, 8, 32, 42, 7]
valor = [13, 2, 20, 10, 7, 14, 7, 2, 2, 4, 16, 17, 17, 3, 21]

def calcula_peso(candidata):

  somar_peso = 0

  for indice, itens in enumerate(candidata):

    if(itens == 1):
     somar_peso += peso[indice]

  return somar_peso


def calcula_valor(candidata):

  somar_valor = 0

  for indice, itens in enumerate(candidata):

    if(itens == 1):
     somar_valor += valor[indice]


  return somar_valor


def viabilidade(candidata):

  return LIMITE >= calcula_peso(candidata)


def vizinhas(candidata):

  vizinhas_geradas = []

  for indice, slots in enumerate(candidata):

    vizinha = candidata.copy()

    if slots == 1:

        vizinha[indice] = 0;

    else:

        vizinha[indice] = 1;

    if(viabilidade(vizinha)):
      vizinhas_geradas.append(vizinha)


  return vizinhas_geradas


contador = 0
candidata_escolhida = [0,0,0,0,0,1,1,1,1,1,0,0,0,1,0]


def hill_climbing(candidata, log_completo):

  global contador
  contador +=1

  #expando as vizinhas
  candidatas_vizinhas = vizinhas(candidata)

  #inicio o maior valor da vizinhas como zero
  maior_valor_vizinha = 0

  #pega o valor e peso da candidata
  valor_candidata = calcula_valor(candidata)
  peso_candidata = calcula_peso(candidata)

  if log_completo:
    print(f"Nº da avaliação da função objetivo: {contador}\n")
    print(f"A candidata atual é: {candidata}\n")
    print(f"O valor da candidata é: {valor_candidata}\n")
    print(f"O peso da candidata é: {peso_candidata}\n")
    print("-" * 30)
    print("\n")

  #cria a lista pra armazenar a melhor vizinha
  melhor_vizinha = []

  #percorre todas vizinhas de candidata_vizinhas
  for vizinha in candidatas_vizinhas:

    if viabilidade(vizinha):

      contador += 1

      #pega o valor atual da vizinha
      valor_atual = calcula_valor(vizinha)
      peso_atual = calcula_peso(vizinha)

      #veriica se o valor da vizinha atual é melhor que o maior valor atual
      if maior_valor_vizinha < valor_atual:

        #se for entao o maior valor vizinha recebe o valor atual e o peso atual e a melhor vizinha recebe a vizinha
        maior_valor_vizinha = valor_atual
        maior_peso_vizinho = peso_atual

        melhor_vizinha = vizinha.copy()

      elif maior_valor_vizinha == valor_atual:

        if(peso_atual < maior_peso_vizinho):

          maior_valor_vizinha = valor_atual
          maior_peso_vizinho = peso_atual

          melhor_vizinha = vizinha.copy()


  #sai do laço e verifica se o valor da candidata atual é melhor que o valor da maior
  if valor_candidata < maior_valor_vizinha:

      #se for a candidata recebe a melhor vizinha e chama novamente o hill_climbing com a nova candidata
      candidata = melhor_vizinha.copy()
      return hill_climbing(candidata, log_completo)

  if not log_completo:

    peso_final = calcula_peso(candidata)
    valor_final = calcula_valor(candidata)

    return candidata, peso_final, valor_final, contador

  return


itens = list(range(15))
melhor_valor = 0
candidata_campea = []
historico = []
peso_campeao = 0
contador = 0

def sorteio(itens):

  mochila_vazia = [0] * 15
  vizinha_viavel = sorted(itens, key=lambda x: random.random())

  chance = [random.randint(0, 1) for _ in range(15)]

  for indice, itens_viaveis in enumerate(vizinha_viavel):

      if chance[indice] == 1:

        mochila_vazia[itens_viaveis] = 1

        if not viabilidade(mochila_vazia):

            mochila_vazia[itens_viaveis] = 0

  return mochila_vazia

for i in range(20):
  candidata, peso_final, valor_final, contador = hill_climbing(sorteio(itens), log_completo=False)

  if melhor_valor < valor_final:

    melhor_valor = valor_final
    candidata_campea = candidata
    peso_campeao = peso_final

    historico.append({
        'Iteração': i + 1,
        'Valor': valor_final,
        'Peso': peso_final,
        'Candidata': str(candidata),
        'Melhor Valor': True
    })

  else:

    historico.append({
        'Iteração': i + 1,
        'Valor': valor_final,
        'Peso': peso_final,
        'Candidata': str(candidata),
        'Melhor Valor': False
    })


print("-" * 100)
print(f"Total de avaliações da função objetivo: {contador}")
print(f"A candidata campeã: {candidata_campea}")
print(f"O melhor valor: {melhor_valor}")
print(f"O peso da melhor candidata: {peso_campeao}")
print("-" * 100)

tabela_final = pd.DataFrame(historico)

display(tabela_final)
