import time
import random

def busca_sequencial(lista, valor):
    contador = 0
    for i, elemento in enumerate(lista):
        contador += 1
        if elemento == valor:
            return i, contador
    return -1, contador

def executar():
    print("Iniciando o Desafio 1: A Busca pelo Pergaminho Vital!")

    n = 100
    fragmentos = random.sample(range(1, 101), n)
    print("Fragmentos mágicos disponíveis na mochila de Dudão:")
    print(fragmentos)

    
    id = int(input("Digite o ID do Pergaminho Vital a ser encontrado: "))
    

    inicio = time.time()
    posicao, comparacoes = busca_sequencial(fragmentos, id)
    fim = time.time()

    tempo_exec = (fim - inicio) * 1000  

    if posicao != -1:
        print(f"O Pergaminho {id} foi encontrado na posição {posicao}!")
    else:
        print(f" O Pergaminho {id} não foi encontrado!")

    print(f" Número de comparações realizadas: {comparacoes}")
    print(f" Tempo de execução: {tempo_exec:.6f} ms")
