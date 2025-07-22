import random

def rabin_karp(texto, padroes, base, primo):
    tamanho = len(texto)
    ocorrencias_encontradas = []

    for padrao in padroes:
        tamanho_padrao = len(padrao)
        if tamanho_padrao == 0 or tamanho_padrao > tamanho:
            continue

        hash_base = pow(base, tamanho_padrao - 1, primo)
        hash_padrao = 0
        hash_texto = 0

        for i in range(tamanho_padrao):
            hash_padrao = (base * hash_padrao + ord(padrao[i])) % primo
            hash_texto = (base * hash_texto + ord(texto[i])) % primo

        for i in range(tamanho - tamanho_padrao + 1):
            if hash_padrao == hash_texto:
                correspondente = True
                for j in range(tamanho_padrao):
                    if padrao[j] != texto[i + j]:
                        correspondente = False
                        break
                if correspondente:
                    ocorrencias_encontradas.append((padrao, i))

            if i < tamanho - tamanho_padrao:
                hash_texto = (base * (hash_texto - ord(texto[i]) * hash_base) + ord(texto[i + tamanho_padrao])) % primo
                hash_texto = (hash_texto + primo) % primo 
    return ocorrencias_encontradas

def remover_marcas_de_corrupcao(texto, ocorrencias):
    texto_como_lista = list(texto)
    ocorrencias.sort(key=lambda x: x[1], reverse=True)

    for padrao, inicio in ocorrencias:
        fim = inicio + len(padrao)
        for i in range(inicio, fim):
            texto_como_lista[i] = ' '

    return "".join(texto_como_lista)

def executar():
    print("\n Desafio 3: A Purificação do Tomo Corrompido\n")

    tomo = """Há muito tempo, no Reino Binário, onde códigos fluem como rios de lógica, 
vivia a sábia e corajosa Princesa Cessia, guardiã dos Segredos Algorítmicos. 
Seu conhecimento mantinha o equilíbrio entre os mundos da Computação. 
Mas a paz foi quebrada quando o traiçoeiro Dr. Bahia, mestre das Estruturas Corrompidas, 
lançou sua sombra sobre o reino e raptou a princesa, escondendo-a nas profundezas 
de uma fortaleza repleta de armadilhas lógicas e desafios computacionais.

Em meio ao caos, surge um herói improvável: Dudão, um programador destemido e curioso, 
convocado pelo Conselho de Bytes para embarcar numa missão de resgate. 
Mas essa não é uma aventura comum. Dudão precisa atravessar os mundos fragmentados do Reino Binário, 
cada um representando um tema crucial da disciplina de Estruturas de Dados e Algoritmos II."""

    marcas_de_corrupcao = [
        "Dr. Bahia",
        "dados corrompidos", 
        "fortaleza",
        "Computação",
        "algoritmos corretos", 
        "árvores binárias", 
        "listas encadeadas"
    ]

    base = 256
    primo = 101

    print(" Buscando marcas de corrupção no tomo...\n")
    ocorrencias = rabin_karp(tomo, marcas_de_corrupcao, base, primo)

    if ocorrencias:
        print("Marcas de corrupção encontradas:")
        for padrao, posicao in ocorrencias:
            print(f" - '{padrao}' na posição {posicao}")
    else:
        print("Nenhuma marca de corrupção encontrada.")

    tomo_purificado = remover_marcas_de_corrupcao(tomo, ocorrencias)

    print("\n Tomo purificado:\n")
    print(tomo_purificado)
