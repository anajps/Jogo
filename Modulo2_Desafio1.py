from queue import PriorityQueue

class No:
    def __init__(self, caractere, frequencia):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esq = None
        self.dir = None

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

def tabela_frequencia_caracter(texto):
    tabela = {}
    for caractere in texto:
        tabela[caractere] = tabela.get(caractere, 0) + 1
    return tabela

def montar_arvore(tabela):
    fila = PriorityQueue()
    for caractere, frequencia in tabela.items():
        fila.put(No(caractere, frequencia))

    while fila.qsize() > 1:
        primeiro = fila.get()
        segundo = fila.get()
        novo = No('+', primeiro.frequencia + segundo.frequencia)
        novo.esq = primeiro
        novo.dir = segundo
        fila.put(novo)

    return fila.get()

def gerar_codigo(no, codigo_atual, tabela_codigos):
    if no is None:
        return 

    if no.caractere != '+':
        tabela_codigos[no.caractere] = codigo_atual
        return

    gerar_codigo(no.esq, codigo_atual + '0', tabela_codigos)
    gerar_codigo(no.dir, codigo_atual + '1', tabela_codigos)

def conversao_texto(texto, tabela_codigos):
    codigo = ''
    for caractere in texto:
        codigo += tabela_codigos[caractere]
    return codigo

def desconversao_texto(codigo, no):
    texto = ''
    atual = no
    for bit in codigo:
        if bit == '0':
            atual = atual.esq
        else:
            atual = atual.dir

        if atual.caractere != '+':
            texto += atual.caractere
            atual = no

    return texto

def executar():
    print(" Compressão de Texto com Huffman ")
    texto = input("Digite o texto para compressão: ")
    
    tabela = tabela_frequencia_caracter(texto)
    arvore = montar_arvore(tabela)
    tabela_codigos = {}
    gerar_codigo(arvore, '', tabela_codigos)
    codigo = conversao_texto(texto, tabela_codigos)
    texto_decodificado = desconversao_texto(codigo, arvore)

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
        print("\n Erro")

def main():
    executar()

if __name__ == "__main__":
    main()
