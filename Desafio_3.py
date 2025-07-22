import random

def rabin_karp(texto, padrao, base, primo):
    n = len(texto)
    ocorrencias = [] 

    for pattern in padrao:
        tamanho_padrao = len(pattern)
        if tamanho_padrao == 0: 
            continue
        if tamanho_padrao > n: 
            continue
        #operações de exponenciação
        h = pow(base, tamanho_padrao - 1, primo) 
        p_hash = 0 
        t_hash = 0 

        for i in range(tamanho_padrao):
            p_hash = (base * p_hash + ord(pattern[i])) % primo
            t_hash = (base * t_hash + ord(texto[i])) % primo

        for s in range(n - tamanho_padrao + 1):
            if p_hash == t_hash:
                match = True
                for i in range(tamanho_padrao):
                    if pattern[i] != texto[s + i]:
                        match = False
                        break
                if match:
                    ocorrencias.append((pattern, s))

            if s < n - tamanho_padrao:
                t_hash = (base * (t_hash - ord(texto[s]) * h) + ord(texto[s + tamanho_padrao])) % primo
                t_hash = (t_hash + primo) % primo
    return ocorrencias

def remover_marcas_de_corrupcao(texto, marcas_encontradas):
    texto_lista = list(texto)
    
    marcas_encontradas.sort(key=lambda x: x[1], reverse=True)

    for pattern, onde_comeca in marcas_encontradas:
        fim_index = onde_comeca + len(pattern)
        for i in range(onde_comeca, fim_index):
            texto_lista[i] = ' ' 
            
    return "".join(texto_lista)

def executar():
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

    print("Buscando marcas de corrupção no tomo...\n")
    marcas_encontradas = rabin_karp(tomo, marcas_de_corrupcao, base, primo)

    print("Marcas de corrupção encontradas:")
    for pattern, pos in marcas_encontradas:
        print(f"- '{pattern}' na posição {pos}")

    tomo_limpo = remover_marcas_de_corrupcao(tomo, marcas_encontradas)

    print("\nTomo limpo:\n")
    print(tomo_limpo)


executar()
