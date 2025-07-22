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
Este código realiza a compressão de texto utilizando o algoritmo de Huffman. Ele começa calculando a frequência de cada caractere no texto digitado pelo usuário e, com essas frequências, constrói uma árvore binária onde os caracteres mais frequentes ficam mais próximos da raiz. Em seguida, gera códigos binários únicos para cada caractere e codifica o texto original com esses códigos, reduzindo seu tamanho total. O texto codificado é então decodificado com base na árvore gerada, garantindo que o resultado final seja igual ao texto original. Por fim, o programa exibe o tamanho do texto original, o tamanho comprimido, a taxa de compressão e verifica se a compressão e a descompressão foram bem-sucedidas. 
---

### modulo2_desafio2.py  
Este código implementa uma tabela hash com a função de espalhamento por multiplicação e tratamento de colisões utilizando o método de enlaçamento com limite de elementos por índice. Os dados são armazenados em uma estrutura encadeada dentro de cada posição da tabela, e cada posição aceita até um número máximo de elementos definidos pelo limite. Caso uma posição atinja esse limite, a inserção continua em posições seguintes da tabela, de forma circular, até encontrar espaço disponível
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
