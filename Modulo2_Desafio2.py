class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10, chain_limit=3):
        self.size = size
        self.chain_limit = chain_limit
        self.table = [None] * size
    
    def _hash_multiplicacao(self, key):
        # Convertendo key para int (se for string, usando soma dos códigos)
        if isinstance(key, str):
            key_int = sum(ord(c) for c in key)
        else:
            key_int = int(key)
        A = 0.6180339887  # constante irracional (número áureo aproximado)
        frac = (key_int * A) % 1
        return int(self.size * frac)
    
    def _enlacamento_limite(self, index):
        # Enlaçamento limite: garante que o tamanho da cadeia não ultrapasse o limite
        # Se a lista no índice já estiver no limite, tenta próximo índice (linear)
        start_index = index
        while True:
            length = 0
            node = self.table[index]
            while node:
                length += 1
                node = node.next
            if length < self.chain_limit:
                return index
            index = (index + 1) % self.size
            if index == start_index:
                raise Exception("Tabela cheia: não é possível inserir a nova chave.")
    
    def insert(self, key, value):
        index = self._hash_multiplicacao(key)
        index = self._enlacamento_limite(index)

        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            # Encadeamento: insere no começo da lista ligada
            new_node.next = self.table[index]
            self.table[index] = new_node
    
    def search(self, key):
        index = self._hash_multiplicacao(key)
        start_index = index

        # Considerar enlaçamento limite e sondagem linear para buscar
        while True:
            node = self.table[index]
            while node:
                if node.key == key:
                    return node.value
                node = node.next
            index = (index + 1) % self.size
            if index == start_index:
                return None  # não achou
    
    def display(self):
        print("\nTabela Hash (index : [chaves]):")
        for i, node in enumerate(self.table):
            keys = []
            current = node
            while current:
                keys.append(f"{current.key}:{current.value}")
                current = current.next
            print(f"{i} : {keys}")

def executar():
    print("=== Executando Desafio 2: Hashing com Multiplicação e Enlaçamento Limite ===")
    ht = HashTable(size=7, chain_limit=2)

    # Inserindo algumas chaves para testar
    dados = [("Ana", 25), ("Bruno", 30), ("Carla", 22), ("Diego", 28), ("Eva", 35), ("Fábio", 20)]

    for nome, idade in dados:
        print(f"Inserindo {nome} -> {idade}")
        ht.insert(nome, idade)
    
    ht.display()

    # Testando buscas
    nomes_busca = ["Ana", "Eva", "Lucas"]
    for nome in nomes_busca:
        resultado = ht.search(nome)
        if resultado is not None:
            print(f"Busca: {nome} -> Idade: {resultado}")
        else:
            print(f"Busca: {nome} não encontrado na tabela.")

if __name__ == "__main__":
    executar()
