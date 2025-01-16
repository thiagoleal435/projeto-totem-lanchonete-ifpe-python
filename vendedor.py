#Responsável por:

#Exibe os pedidos pendentes
#Atualiza o status dos pedidos no arquivo pedidos.txt
#Gerencia o estoque e cardápio

class Vendedor:
    def __init__(self, pedidos_file):
        self.pedidos_file = pedidos_file

    def exibir_pedidos(self):
        print("\n--- Pedidos Pendentes ---")
        try:
            with open(self.pedidos_file, 'r') as file:
                pedidos = file.readlines()
                if pedidos:
                    for i, pedido in enumerate(pedidos, start=1):
                        print(f"{i}. {pedido.strip()}")
                else:
                    print("Nenhum pedido pendente.")
        except FileNotFoundError:
            print("Arquivo de pedidos não encontrado.")

    def limpar_pedidos(self):
        with open(self.pedidos_file, 'w') as file:
            pass
        print("Todos os pedidos foram processados e o arquivo está limpo.")

    def menu_vendedor(self):
        while True:
            print("\n--- Menu Vendedor ---")
            print("1. Ver pedidos pendentes")
            print("2. Limpar pedidos")
            print("3. Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.exibir_pedidos()
            elif opcao == '2':
                self.limpar_pedidos()
            elif opcao == '3':
                break
            else:
                print("Opção inválida. Tente novamente.")