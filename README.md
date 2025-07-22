# Projeto - Fase 2: Desafios Algorítmicos

## Estrutura do projeto

### desafio_1.py  
O código implementa a busca sequencial para encontrar um valor específico em uma lista de números únicos gerados aleatoriamente. Ele percorre a lista elemento a elemento, contando o número de comparações até encontrar o valor desejado ou concluir que ele não está presente. Também mede o tempo de execução da busca.  
---

### desafio_2.py  
O código implementa a busca binária para localizar todas as ocorrências de um valor em listas ordenadas. Após encontrar uma ocorrência do valor, o algoritmo verifica as posições adjacentes para identificar todas as repetições consecutivas. Além disso, conta o número de comparações realizadas e mede o tempo de execução, exibindo resultados detalhados para cada valor buscado em duas listas diferentes.  
---

### desafio_3.py  
O algoritmo rabin-karp calcula uma hash para o padrão e para janelas do texto, comparando para encontrar ocorrências. Ao detectar possível ocorrência, valida caractere a caractere para evitar falsos positivos. Este exemplo busca várias "marcas de corrupção" em um texto e as remove substituindo por espaços, simulando limpeza.  
---

### modulo2_desafio1.py  
- `tabela_frequencia_caracter`: cria tabela de frequências dos caracteres  
- `montar_arvore`: monta árvore de huffman com base nas frequências  
- `gerar_codigo`: gera os códigos binários para cada caractere  
- `conversao_texto`: codifica texto para código binário  
- `desconversao_texto`: decodifica código binário para texto original  
- `executar`: função para testar o algoritmo com entrada do usuário  
---

### modulo2_desafio2.py  
- função de hash por multiplicação (usando constante A = 0.618...)  
- tratamento de colisão com enlaçamento encadeado e limite de elementos por índice (`limite`)  
- métodos para inserção, busca e exibição dos dados  
---

### main.py  
(coordenador geral para testar os módulos)

---

## Complexidades

                    
Busca Sequencial    | O(n)                    
Busca Binária       | O(log n)                
Rabin-Karp          | O(n + m)  


Compressão Huffman	| O(n log n)	
Hashing            |	Média O(1), pior O(n)	Depende do fator de carga da tabela.
