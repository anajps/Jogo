# Projeto - Fase 2: Desafios Algorítmicos


 Estrutura do Projeto
 
 Desafio_1.py   
 Este código implementa a busca sequencial para encontrar um valor específico em uma lista de números únicos gerados aleatoriamente. Ele  percorre a lista elemento a elemento, contando o número de comparações até encontrar o valor desejado ou concluir que ele não está presente. Também mede o tempo de execução da busca
 ----------------------------------------------------------------------
 Desafio_2.py  
Código implementa a busca binária para localizar todas as ocorrências de um valor em listas ordenadas. Após encontrar uma ocorrência do valor, o algoritmo verifica as posições adjacentes para identificar todas as repetições consecutivas. Além disso, conta o número de comparações realizadas e mede o tempo de execução, exibindo resultados detalhados para cada valor buscado em duas listas diferentes.
 -------------------------------------------------------------------------
 Desafio_3.py              
 O algoritmo Rabin-Karp calcula uma hash para o padrão e para janelas do texto, 
 comparando para encontrar ocorrências. Ao detectar possível ocorrência, 
 valida caractere a caractere para evitar falsos positivos.
 Este exemplo busca várias "marcas de corrupção" em um texto e as remove substituindo por espaços, simulando limpeza.            
-----------------------------------------------------------------------
 Modulo2_Desafio1.py 
- tabela_frequencia_caracter: cria tabela de frequências dos caracteres
- montar_arvore: monta árvore de Huffman com base nas frequências
- gerar_codigo: gera os códigos binários para cada caractere
- conversao_texto: codifica texto para código binário
- desconversao_texto: decodifica código binário para texto original
- executar: função para testar o algoritmo com entrada do usuário
 -------------------------------------------------------------------------
 Modulo2_Desafio2.py
- Função de hash por multiplicação (usando constante A = 0.618...)
- Tratamento de colisão com enlaçamento encadeado e limite de elementos por índice (`limite`).
- Métodos para inserção, busca e exibição dos dados.

 main.py    


Complexidades

                    
Busca Sequencial    | O(n)                    
Busca Binária       | O(log n)                
Rabin-Karp          | O(n + m)  


Compressão Huffman	| O(n log n)	
Hashing            |	Média O(1), pior O(n)	Depende do fator de carga da tabela.

