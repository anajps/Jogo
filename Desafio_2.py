import random
import time

def busca_binaria(lista, valor):
    comparacoes = 0
    ocorrencias = []
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        comparacoes += 1  
        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            ocorrencias.append(meio)
            
            
            tempo_meio = meio - 1
            while tempo_meio >= 0 and lista[tempo_meio] == valor:
                ocorrencias.append(tempo_meio)
                comparacoes += 1 
                tempo_meio -= 1

            
            tempo_meio = meio + 1
            while tempo_meio < len(lista) and lista[tempo_meio] == valor:
                ocorrencias.append(tempo_meio)
                comparacoes += 1 
                tempo_meio += 1

            return sorted(list(set(ocorrencias))), comparacoes 
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return [], comparacoes 

def executar():
    print("\nDesafio 2: A Lupa do Guardião Binário")

    tamanho_lista = 100
    lista1 = sorted([random.randint(0, 100) for _ in range(tamanho_lista)])
    lista2 = sorted([random.randint(0, 100) for _ in range(tamanho_lista)])

    print(" Lista 1:", lista1)
    print(" Lista 2:", lista2)

   
    num_ids = int(input("\nQuantos IDs serão procurados? "))
    

    for i in range(num_ids):
        try:
            a = int(input(f"\nDigite o ID do Pergaminho {i+1} a ser encontrado: "))
        except ValueError:
            print("Entrada inválida. Usando ID 0 por padrão.")
            a = 0

        total_comparacoes = 0
        tempo = time.time() 

       
        InicioTempo_1 = time.time()
        ocorrencias_l1, comp_1 = busca_binaria(lista1, a)
        FimTempo_1 = time.time()
        tempo_l1 = (FimTempo_1 - InicioTempo_1) * 1000
        total_comparacoes += comp_1

       
        InicioTempo_2 = time.time()
        ocorrencias_l2, comp_2 = busca_binaria(lista2, a)
        FimTempo_2 = time.time()
        tempo_l2 = (FimTempo_2 - InicioTempo_2) * 1000
        total_comparacoes += comp_2

        tempo_total_por_id = (FimTempo_2 - tempo) * 1000

        
        print(f"\n---  Resultados para o ID {a} ---")
        if ocorrencias_l1:
            print(f" Lista 1: O elemento {a} foi encontrado nas posições {ocorrencias_l1}.")
        else:
            print(f"Lista 1: O elemento {a} não foi encontrado.")
        print(f"   Comparações na Lista 1: {comp_1}")
        print(f"   Tempo de execução na Lista 1: {tempo_l1:.6f} ms")

        if ocorrencias_l2:
            print(f" Lista 2: O elemento {a} foi encontrado nas posições {ocorrencias_l2}.")
        else:
            print(f" Lista 2: O elemento {a} não foi encontrado.")
        print(f"  Comparações na Lista 2: {comp_2}")
        print(f"  Tempo de execução na Lista 2: {tempo_l2:.6f} ms")

        print(f" Total de comparações para o ID {a}: {total_comparacoes}")
        print(f" Tempo total de execução: {tempo_total_por_id:.6f} ms")
