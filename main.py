# Responsavel por:

#Gerencia a comunicação entre cliente e vendedor
#Exibe menu principal para escolher entre cliente e vendedor
#Carrega os dados do cardápio e pedidos
#Instanciar as classes e vendedor

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

if __name__ == "__main__":
    menuPrincipal()