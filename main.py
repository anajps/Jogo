# main.py
from Desafio_1 import executar as executar_desafio1
from Desafio_2 import executar as executar_desafio2
from Desafio_3 import executar as executar_desafio3
from Modulo2_Desafio1 import executar as executar_Modulo2_Desafio_1
from Modulo2_Desafio2 import executar as executar_Modulo2_Desafio_2

def historia():
    print("\n Página Inicial - O Início da Jornada")
    print("No pacato Reino de Lógika, onde o conhecimento reina e a sabedoria é poder, vivia a Princesa Cessia — guardiã dos Algoritmos Sagrados, fragmentos mágicos que mantêm o equilíbrio entre lógica e caos.")
    print("Mas a paz foi quebrada... Dr. Bahia, um ex-mestre corrompido pelo desejo de controle, sequestrou a princesa e espalhou os fragmentos mágicos por todo o reino.")
    print(" Surge Dudão, um jovem aprendiz com sua mochila de códigos. Cabe a você ajudá-lo a recuperar os fragmentos, dominar os algoritmos esquecidos e salvar a Princesa Cessia!")

def Desafio1():
    print("\n Desafio 1: A Busca pelo Pergaminho Vital (Busca Sequencial e Binária)")
    print("Nas planícies de Vetória, jazem os Pergaminhos Vitais — registros antigos que revelam os segredos da busca eficiente.")
    print("Dudão deve decifrar listas encantadas onde nem todos os caminhos são otimizados. Alguns são lentos e cansativos (Busca Sequencial), outros, rápidos e astutos (Busca Binária).")
    print("Somente dominando essas técnicas, ele poderá encontrar o primeiro Fragmento Sagrado.")
    executar_desafio1()

def Desafio2():
    print("\n Desafio 2: O Feitiço de Compressão (Algoritmo de Huffman)")
    print("Em meio às Torres da Memória, arquivos mágicos crescem sem controle. Para restaurar o equilíbrio entre espaço e informação, Dudão precisa invocar o Feitiço de Huffman.")
    print("Essa técnica ancestral permite comprimir símbolos, guardando mais com menos. Um desafio de sabedoria e eficiência espera por ele!")
    executar_desafio2()

def Desafio3():
    print("\n Desafio 3: A Tinta Invisível de Rabin-Karp (Busca de Padrões)")
    print("Nas Crônicas Ocultas de Cessia, palavras-chave estão escondidas em pergaminhos aparentemente comuns.")
    print("Dudão deve dominar a técnica Rabin-Karp para localizar padrões mágicos e decifrar mensagens secretas que o aproximam do paradeiro da princesa.")
    executar_desafio3()

def Modulo2_Desafio_1():
    print("\n Módulo 2 - Desafio 1: O Enigma da Compressão Sagrada")
    print("Diante da Biblioteca Sombria, Dudão encontra um portão selado por compressões enigmáticas.")
    print("Ele deverá aplicar novamente o poder do algoritmo de Huffman, mas agora com textos ainda mais densos e desafiadores.")
    executar_Modulo2_Desafio_1()

def Modulo2_Desafio_2():
    print("\n Módulo 2 - Desafio 2: A Fortaleza das Tabelas Hash")
    print("Para acessar o Cofre das Respostas, Dudão precisa dominar a arte do Hashing.")
    print("Funções como Multiplicação, Enlaçamento e Meio-Quadrado serão suas armas contra colisões e caos. Somente com eficiência e precisão, ele abrirá o caminho final.")
    executar_Modulo2_Desafio_2()

def sair():
    print("\nSaindo do programa... Que a lógica esteja com você em sua próxima jornada!")

def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Página Inicial")
        print("\n--- Módulo 1 ---")
        print("2. Desafio 1: Busca")
        print("3. Desafio 2: Compressão")
        print("4. Desafio 3: Rabin-Karp")
        print("\n--- Módulo 2 ---")
        print("5. Desafio 1: Compressão Avançada")
        print("6. Desafio 2: Hashing")
        print("0. Sair")

        escolha = input("Escolha uma opção (0-6): ")

        if escolha == "1":
            historia()
        elif escolha == "2":
            Desafio1()
        elif escolha == "3":
            Desafio2()
        elif escolha == "4":
            Desafio3()
        elif escolha == "5":
            Modulo2_Desafio_1()
        elif escolha == "6":
            Modulo2_Desafio_2()
        elif escolha == "0":
            sair()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
