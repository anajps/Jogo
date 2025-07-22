# main.py
from Desafio_1 import executar as executar_desafio1
from Desafio_2 import executar as executar_desafio2
from Desafio_3 import executar as executar_desafio3
from Modulo2_Desafio1 import executar as executar_Modulo2_Desafio_1
from Modulo2_Desafio2 import executar as executar_Modulo2_Desafio_2

def historia():
    print("\n Você está na Página Inicial.")
    print("Bem-vindo(a) ao mundo de Algorithmic Adventures!")

def Desafio1():
    print("\n Desafio 1: A Busca pelo Pergaminho Vital")
    executar_desafio1()

def Desafio2():
    print("\n Desafio 1: A Busca pelo Pergaminho Vital")
    executar_desafio2()

def Desafio3():
    print("\n Desafio 1: A Busca pelo Pergaminho Vital")
    executar_desafio3()

def Modulo2_Desafio_1():
    print("\n Desafio 1: A Busca pelo Pergaminho Vital")
    executar_Modulo2_Desafio_1()

def Modulo2_Desafio_2():
    print("\n Desafio 1: A Busca pelo Pergaminho Vital")
    executar_Modulo2_Desafio_2()


def sair():
    print("\nSaindo do programa... Até logo!")

def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Página Inicial")
        print("\n--- Modulo 1 ---")
        print("2. Desafio 1")
        print("3. Desafio 2")
        print("4. Desafio 3")
        print("\n--- Modulo 2 ---")
        print("5. Desafio 1")
        print("6. Desafio 2")
        print("0. Sair")

        escolha = input("Escolha uma opção (1-6): ")

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
