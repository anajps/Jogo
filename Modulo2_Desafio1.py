from queue import PriorityQueue

class No:
    def __init__(self, char, frequencia):
        self.char = char
        self.frequencia = frequencia
        self.esq = None
        self.dir = None

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

def tabela_frequencia_caracter(texto):
    tabela = {}
    for char in texto:
        tabela[char] = tabela.get(char, 0) + 1
    return tabela

def montar_arvore(tabela):
    fila_prioridade = PriorityQueue()
    for char, frequencia in tabela.items():
        fila_prioridade.put(No(char, frequencia))

    while fila_prioridade.qsize() > 1:
        primeiro = fila_prioridade.get()
        segundo = fila_prioridade.get()
        novo = No('+', primeiro.frequencia + segundo.frequencia)
        novo.esq = primeiro
        novo.dir = segundo
        fila_prioridade.put(novo)

    return fila_prioridade.get()

def gerar_codigo(raiz, codigo_atual, dic):
    if raiz is None:
        return 0

    if raiz.char != '+':
        dic[raiz.char] = codigo_atual
        return

    gerar_codigo(raiz.esq, codigo_atual + '0', dic)
    gerar_codigo(raiz.dir, codigo_atual + '1', dic)

def codificar(texto, dic):
    codigo = ''
    for char in texto:
        codigo += dic[char]
    return codigo

def decodificar(codigo, raiz):
    texto = ''
    atual = raiz
    for bit in codigo:
        if bit == '0':
            atual = atual.esq
        else:
            atual = atual.dir

        if atual.char != '+':
            texto += atual.char
            atual = raiz

    return texto

def executar():
    print("=== Compressão de Texto com Huffman ===")
    texto = input("Digite o texto para compressão: ")
    
    tabela = tabela_frequencia_caracter(texto)
    arvore = montar_arvore(tabela)
    dic = {}
    gerar_codigo(arvore, '', dic)
    codigo = codificar(texto, dic)
    texto_decodificado = decodificar(codigo, arvore)

    tamanho_original = len(texto) * 8  
    tamanho_codificado = len(codigo)
    taxa = (tamanho_codificado / tamanho_original) * 100

    print("\n=== Resultados ===")
    print(f"Tamanho original: {tamanho_original} bits")
    print(f"Tamanho comprimido: {tamanho_codificado} bits")
    print(f"Taxa de compressão: {taxa:.2f}% do original")
    
    print("\nTexto codificado:", codigo)
    print("Texto decodificado:", texto_decodificado)

    if texto == texto_decodificado:
        print("\n Compressão e descompressão bem-sucedidas!")
    else:
        print("\n Erro: o texto decodificado não corresponde ao original.")

def main():
    executar()

if __name__ == "__main__":
    main()
