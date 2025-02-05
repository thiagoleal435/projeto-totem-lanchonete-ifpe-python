#Responsável por:

#Exibe os pedidos listados em pedidos.txt
#Atualiza o status de um pedido
#Gerencia o estoque e cardápio
#Adiciona, exclui ou altera um item do cardápio

class Vendedor:
    def __init__(self, pedidos_file, menu_file):
        self.pedidos_file = pedidos_file
        self.menu_file = menu_file

    def exibir_pedidos(self):
        print("\n--- Pedidos ---")
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

    def alterar_status_do_pedido(self):
        try:
            with open(self.pedidos_file, 'r') as file:
                pedidos = file.readlines()

            if not pedidos:
                print("Nenhum pedido pendente.")
                return

            print("\n--- Pedidos ---")
            for i, pedido in enumerate(pedidos, start=1):
                print(f"{i}. {pedido.strip()}")

            num_pedido = int(input("Digite o número do pedido que deseja alterar o status: ")) - 1
            if 0 <= num_pedido < len(pedidos):
                dados = pedidos[num_pedido].strip().split(",")

                dados[-1] = "finalizado"
                pedidos[num_pedido] = ",".join(dados) + "\n"

                with open(self.pedidos_file, 'w') as file:
                    file.writelines(pedidos)

                print("Status do pedido atualizado com sucesso.")
            else:
                print("Número de pedido inválido.")
        except FileNotFoundError:
            print("Arquivo de pedidos não encontrado.")

    def adicionar_item_ao_cardapio(self):
        with open(self.menu_file, 'r') as file:
                itens = file.readlines()

        print("\n--- Cardápio Atual ---")
        if itens:
            for i, item in enumerate(itens, start=1):
                print(f"{i}. {item.strip()}")
        else:
            print("O cardápio está vazio.")

        item = input("Nome do novo item: ").strip()
        preco = input("Preço do item: ").strip()
        quantidade = input("Quantidade disponível: ").strip()

        try:
            with open(self.menu_file, 'a') as file:
                file.write(f"{item},{preco},{quantidade}\n")
            print("Item adicionado com sucesso ao cardápio.")
        except Exception as e:
            print(f"Erro ao adicionar item ao cardápio: {e}")

    def excluir_item_do_cardapio(self):
        try:
            with open(self.menu_file, 'r') as file:
                itens = file.readlines()

            if not itens:
                print("O cardápio está vazio.")
                return

            print("\n--- Cardápio Atual ---")
            for i, item in enumerate(itens, start=1):
                print(f"{i}. {item.strip()}")
            print("\n")

            num_item = int(input("Digite o número do item que deseja excluir: ")) - 1
            if 0 <= num_item < len(itens):
                dados_item = itens.pop(num_item).strip().split(',')
                nome_item = dados_item[0]

                with open(self.menu_file, 'w') as file:
                    file.writelines(itens)

                print(f"Item '{nome_item}' removido com sucesso do cardápio.")
            else:
                print("Número de item inválido.")
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar um número válido.")

    def alterar_item_do_cardapio(self):
        try:
            with open(self.menu_file, 'r') as file:
                itens = file.readlines()

            if not itens:
                print("O cardápio está vazio.")
                return

            print("\n--- Cardápio Atual ---")
            for i, item in enumerate(itens, start=1):
                print(f"{i}. {item.strip()}")
            print("\n")

            num_item = int(input("Digite o número do item que deseja alterar: ")) - 1
            if 0 <= num_item < len(itens):
                dados = itens[num_item].strip().split(",")
                print("\nO que deseja alterar?")
                print("1. Nome")
                print("2. Preço")
                opcao = input("Escolha uma opção: ")

                if opcao == '1':
                    novo_nome = input("Digite o novo nome do item: ").strip()
                    dados[0] = novo_nome
                elif opcao == '2':
                    novo_preco = input("Digite o novo preço do item: ").strip()
                    dados[1] = novo_preco
                else:
                    print("Opção inválida.")
                    return

                itens[num_item] = ",".join(dados) + "\n"

                with open(self.menu_file, 'w') as file:
                    file.writelines(itens)

                print("Item atualizado com sucesso.")
            else:
                print("Número de item inválido.")
        except FileNotFoundError:
            print("Arquivo de cardápio não encontrado.")

    def menu_vendedor(self):
        while True:
            print("\n--- Menu Vendedor ---")
            print("1. Ver pedidos")
            print("2. Alterar status de um pedido")
            print("3. Limpar pedidos")
            print("4. Adicionar item ao cardápio")
            print("5. Alterar item do cardápio")
            print("6. Excluir item do cardápio")
            print("7. Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.exibir_pedidos()
            elif opcao == '2':
                self.alterar_status_do_pedido()
            elif opcao == '3':
                self.limpar_pedidos()
            elif opcao == '4':
                self.adicionar_item_ao_cardapio()
            elif opcao == '5':
                self.alterar_item_do_cardapio()
            elif opcao == '6':
                self.excluir_item_do_cardapio()
            elif opcao == '7':
                break
            else:
                print("Opção inválida. Tente novamente.")