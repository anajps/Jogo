class no_atual:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.next = None

class Hashtabela:
    def __init__(self, tamanho=10, limite=3):
        self.tamanho = tamanho
        self.limite = limite
        self.tabela = [None] * tamanho
    
    def _hash_multiplicacao(self, chave):
        
        if isinstance(chave, str):
            chave_int = sum(ord(c) for c in chave)
        else:
            chave_int = int(chave)
        A = 0.6180339887  
        frac = (chave_int * A) % 1
        return int(self.tamanho * frac)
    
    def _enlacamento_limite(self, index):
        
        indice_inicial = index
        while True:
            length = 0
            no_atual = self.tabela[index]
            while no_atual:
                length += 1
                no_atual = no_atual.next
            if length < self.limite:
                return index
            else:
                index = (index + 1) % self.tamanho
            if index == indice_inicial:
                raise Exception("Tabela cheia: não é possível inserir a nova chave.")
    
    def insert(self, chave, valor):
        index = self._hash_multiplicacao(chave)
        index = self._enlacamento_limite(index)

        novo_No = no_atual(chave, valor)
        if self.tabela[index] is None:
            self.tabela[index] = novo_No
        else:
            novo_No.next = self.tabela[index]
            self.tabela[index] = novo_No
    
    def search(self, chave):
        index = self._hash_multiplicacao(chave)
        indice_inicial = index

        
        while True:
            no_atual = self.tabela[index]
            while no_atual:
                if no_atual.chave == chave:
                    return no_atual.valor
                else:
                    no_atual = no_atual.next
            index = (index + 1) % self.tamanho
            if index == indice_inicial:
                return None  
    
    def display(self):
        print("\nTabela Hash (index : [chaves]):")
        for i, no_atual in enumerate(self.tabela):
            chaves = []
            no_corrente = no_atual
            while no_corrente:
                chaves.append(f"{no_corrente.chave}:{no_corrente.valor}")
                no_corrente = no_corrente.next
            print(f"{i} : {chaves}")

def executar():
    print("=== Executando Desafio 2: Hashing com Multiplicação e Enlaçamento Limite ===")
    ht = Hashtabela(tamanho=7, limite=2)

    
    dados = [("Ana", 25), ("Bruno", 30), ("Carla", 22), ("Diego", 28), ("Eva", 35), ("Fábio", 20)]

    for nome, idade in dados:
        print(f"Inserindo {nome} -> {idade}")
        ht.insert(nome, idade)
    
    ht.display()

    
    nomes_busca = ["Ana", "Eva", "Lucas"]
    for nome in nomes_busca:
        resultado = ht.search(nome)
        if resultado is not None:
            print(f"Busca: {nome} -> Idade: {resultado}")
        else:
            print(f"Busca: {nome} não encontrado na tabela.")

if __name__ == "__main__":
    executar()
