#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CHARS 256  // número máximo de caracteres ASCII

typedef struct No {
    char caractere;
    int frequencia;
    struct No *esq;
    struct No *dir;
} No;

typedef struct {
    No **itens;
    int tamanho;
    int capacidade;
} FilaPrioridade;

// Função para criar um novo nó
No* criar_no(char caractere, int frequencia) {
    No* novo = (No*) malloc(sizeof(No));
    novo->caractere = caractere;
    novo->frequencia = frequencia;
    novo->esq = NULL;
    novo->dir = NULL;
    return novo;
}

// Função para criar fila de prioridade
FilaPrioridade* criar_fila(int capacidade) {
    FilaPrioridade* fila = (FilaPrioridade*) malloc(sizeof(FilaPrioridade));
    fila->itens = (No**) malloc(sizeof(No*) * capacidade);
    fila->tamanho = 0;
    fila->capacidade = capacidade;
    return fila;
}

// Função para inserir nó na fila (inserção mantendo fila ordenada pelo freq)
void fila_inserir(FilaPrioridade* fila, No* no) {
    int i = fila->tamanho - 1;
    // Insere ordenando pelo menor valor de frequencia
    while (i >= 0 && fila->itens[i]->frequencia > no->frequencia) {
        fila->itens[i+1] = fila->itens[i];
        i--;
    }
    fila->itens[i+1] = no;
    fila->tamanho++;
}

// Função para remover o nó com menor frequência (o primeiro da fila)
No* fila_remover(FilaPrioridade* fila) {
    if (fila->tamanho == 0) return NULL;
    No* no = fila->itens[0];
    for (int i = 0; i < fila->tamanho - 1; i++) {
        fila->itens[i] = fila->itens[i+1];
    }
    fila->tamanho--;
    return no;
}

// Função para calcular a frequência de cada caractere no texto
void tabela_frequencia(const char* texto, int* frequencias) {
    for (int i = 0; i < MAX_CHARS; i++)
        frequencias[i] = 0;

    for (int i = 0; texto[i] != '\0'; i++) {
        frequencias[(unsigned char)texto[i]]++;
    }
}

// Função para montar a árvore de Huffman
No* montar_arvore(int* frequencias) {
    FilaPrioridade* fila = criar_fila(MAX_CHARS);

    // Criar um nó para cada caractere com freq > 0 e inserir na fila
    for (int i = 0; i < MAX_CHARS; i++) {
        if (frequencias[i] > 0) {
            fila_inserir(fila, criar_no((char)i, frequencias[i]));
        }
    }

    // Enquanto tiver mais de 1 nó na fila, remove os dois menores, junta e reinserir
    while (fila->tamanho > 1) {
        No* primeiro = fila_remover(fila);
        No* segundo = fila_remover(fila);
        No* novo = criar_no('+', primeiro->frequencia + segundo->frequencia);
        novo->esq = primeiro;
        novo->dir = segundo;
        fila_inserir(fila, novo);
    }

    No* raiz = fila_remover(fila);
    free(fila->itens);
    free(fila);
    return raiz;
}

// Função para gerar os códigos recursivamente
void gerar_codigo(No* raiz, char* codigo_atual, int topo, char codigos[MAX_CHARS][MAX_CHARS]) {
    if (raiz == NULL) return;

    // Se for folha, salva o código
    if (raiz->caractere != '+') {
        codigo_atual[topo] = '\0';
        strcpy(codigos[(unsigned char)raiz->caractere], codigo_atual);
        return;
    }

    // Caminha para esquerda adicionando '0'
    codigo_atual[topo] = '0';
    gerar_codigo(raiz->esq, codigo_atual, topo + 1, codigos);

    // Caminha para direita adicionando '1'
    codigo_atual[topo] = '1';
    gerar_codigo(raiz->dir, codigo_atual, topo + 1, codigos);
}

// Função para codificar o texto usando os códigos gerados
void codificar(const char* texto, char codigos[MAX_CHARS][MAX_CHARS], char* resultado) {
    resultado[0] = '\0';
    for (int i = 0; texto[i] != '\0'; i++) {
        strcat(resultado, codigos[(unsigned char)texto[i]]);
    }
}

// Função para decodificar o código binário em texto
void decodificar(const char* codigo, No* raiz, char* texto_decodificado) {
    int idx = 0;
    No* atual = raiz;
    for (int i = 0; codigo[i] != '\0'; i++) {
        if (codigo[i] == '0')
            atual = atual->esq;
        else
            atual = atual->dir;

        if (atual->caractere != '+') {
            texto_decodificado[idx++] = atual->caractere;
            atual = raiz;
        }
    }
    texto_decodificado[idx] = '\0';
}

// Função para liberar a memória da árvore
void liberar_arvore(No* raiz) {
    if (raiz == NULL) return;
    liberar_arvore(raiz->esq);
    liberar_arvore(raiz->dir);
    free(raiz);
}

int main() {
    printf("=== Compressão de Texto com Huffman ===\n");
    char texto[1024];
    printf("Digite o texto para compressão: ");
    fgets(texto, sizeof(texto), stdin);
    texto[strcspn(texto, "\n")] = '\0';  // Remove newline

    int frequencias[MAX_CHARS];
    tabela_frequencia(texto, frequencias);

    No* arvore = montar_arvore(frequencias);

    char codigos[MAX_CHARS][MAX_CHARS] = {{0}};
    char codigo_atual[MAX_CHARS];
    gerar_codigo(arvore, codigo_atual, 0, codigos);

    char codigo_binario[8192];
    codificar(texto, codigos, codigo_binario);

    char texto_decodificado[1024];
    decodificar(codigo_binario, arvore, texto_decodificado);

    int tamanho_original = strlen(texto) * 8;  // 8 bits por caractere
    int tamanho_codificado = strlen(codigo_binario);
    double taxa = ((double)tamanho_codificado / tamanho_original) * 100.0;

    printf("\n=== Resultados ===\n");
    printf("Tamanho original: %d bits\n", tamanho_original);
    printf("Tamanho comprimido: %d bits\n", tamanho_codificado);
    printf("Taxa de compressao: %.2f%% do original\n", taxa);

    printf("\nTexto codificado: %s\n", codigo_binario);
    printf("Texto decodificado: %s\n", texto_decodificado);

    if (strcmp(texto, texto_decodificado) == 0) {
        printf("\nCompressao e descompressao bem-sucedidas!\n");
    } else {
        printf("\nErro: o texto decodificado nao corresponde ao original.\n");
    }

    liberar_arvore(arvore);

    return 0;
}
