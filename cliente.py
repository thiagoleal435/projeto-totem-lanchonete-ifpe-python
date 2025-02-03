#Responsável por:

#Exibir o cardápio
#Ralizar pedidos
#Salvar os pedido em pedidos.txt

#Entre 21/01 e 25/01 resolver:
#1- Adicionar pergunta: "Deseja pedir mais alguma coisa?"
#2- Atualizar a quantidade de estoque no arquivo menu_estoque.txt

class Cliente:
    def __init__(self, menu_file, pedidos_file):
        self.menu_file = menu_file
        self.pedidos_file = pedidos_file
        self.cardapio = self.carregar_cardapio()

    def carregar_cardapio(self):
        cardapio = {}
        with open(self.menu_file, 'r') as file:
            for linha in file:
                item, preco, estoque = linha.strip().split(',')
                cardapio[item] = {'preco': float(preco), 'estoque': int(estoque)}
        return cardapio

    def exibir_cardapio(self):
        print("\n--- Cardápio ---")
        for item, detalhes in self.cardapio.items():
            print(f"{item}: R${detalhes['preco']} (Disponível: {detalhes['estoque']})")

    def fazer_pedido(self):
        self.exibir_cardapio()
        pedido = []

        while True:
            item = input("Digite o nome do item que deseja: ")
            if item not in self.cardapio:
                print("Item não encontrado no cardápio. Tenta novamente.")
                continue

            quantidade = int(input("Digite a quantidade: "))
            if self.cardapio[item]['estoque'] < quantidade:
                print("Quantidade indisponível no estoque. Escolha uma quantidade menor.")
                continue

            pedido.append((item,quantidade))
            self.cardapio[item]['estoque'] -= quantidade

            maisItens = input("Deseja adiciomais mais um item ao pedido? (s/n)").strip().lower()
            if maisItens != "s":
                pedidoFinal = ", ".join([f"{quantidade}x {item}" for item, quantidade in pedido])
                print(f"Pedido de {pedidoFinal} registrado com sucesso!")
                break

        with open(self.pedidos_file, 'a') as file:
            linha_pedido = ",".join([f"{item},{quantidade}" for item, quantidade in pedido]) + ",pendente\n"
            file.write(linha_pedido)

        with open(self.menu_file, "w") as file:
            for nome_item, detalhes in self.cardapio.items():
                file.write(f"{nome_item},{detalhes['preco']},{detalhes['estoque']}\n")   

    def cancelar_pedido(self):
        try:
            with open(self.pedidos_file, 'r') as file:
                pedidos = file.readlines()

            if not pedidos:
                print("Nenhum pedido para cancelar.")
                return

            print("\n--- Pedidos Pendentes ---")
            pedidos_pendentes = []
            for i, pedido in enumerate(pedidos, start=1):
                if "pendente" in pedido:
                    print(f"{i}. {pedido.strip()}")
                    pedidos_pendentes.append(i - 1)  # Guarda o índice dos pedidos pendentes

            if not pedidos_pendentes:
                print("Nenhum pedido pendente pode ser cancelado.")
                return

            num_pedido = int(input("Digite o número do pedido que deseja cancelar: ")) - 1

            if num_pedido in pedidos_pendentes:
                # Recuperar os itens do pedido
                dados = pedidos[num_pedido].strip().split(",")
                itens_pedido = [(dados[i], int(dados[i + 1])) for i in range(0, len(dados) - 1, 2)]

                # Devolver os itens cancelados ao estoque
                for item, quantidade in itens_pedido:
                    if item in self.cardapio:
                        self.cardapio[item]['estoque'] += quantidade  # Retorna a quantidade cancelada

                # Remover o pedido do arquivo
                del pedidos[num_pedido]

                # Atualizar pedidos.txt (removendo o pedido cancelado)
                with open(self.pedidos_file, 'w') as file:
                    file.writelines(pedidos)

                # Atualizar menu_estoque.txt (salvar estoque atualizado)
                with open(self.menu_file, "w") as file:
                    for nome_item, detalhes in self.cardapio.items():
                        file.write(f"{nome_item},{detalhes['preco']},{detalhes['estoque']}\n")

                print("Pedido cancelado e itens devolvidos ao estoque com sucesso.")
            else:
                print("Número de pedido inválido ou já processado.")
        except FileNotFoundError:
            print("Arquivo de pedidos não encontrado.")
        except ValueError:
            print("Erro: Digite um número válido.")

    def menu_cliente(self):
        while True:
            print("\n--- Menu Cliente ---")
            print("1. Ver cardápio")
            print("2. Fazer pedido")
            print("3. Cancelar pedido")
            print("4. Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.exibir_cardapio()
            elif opcao == '2':
                self.fazer_pedido()
            elif opcao == '3':
                self.cancelar_pedido()
            elif opcao == '4':
                break
            else:
                print("Opção inválida. Tente novamente.")