#Esse código é a interface principal do Sistema de Autoatendimento para a lanchonete do Campus.
#Ele usa modularização para melhorar a organização e importa apenas as classes presentes nos scripts cliente.py e vendedor.py 

from cliente import Cliente
from vendedor import Vendedor

def menuPrincipal():
    while True:
        print("\n--- Sistema de Autoatendimento - Lanchonete IFPE ---")
        print("1. Interface do Cliente")
        print("2. Interface do Vendedor")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cliente = Cliente('menu_estoque.txt', 'pedidos.txt')
            cliente.menu_cliente()
        elif opcao == '2':
            vendedor = Vendedor('pedidos.txt', 'menu_estoque.txt')
            vendedor.menu_vendedor()
        elif opcao == '3':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menuPrincipal()