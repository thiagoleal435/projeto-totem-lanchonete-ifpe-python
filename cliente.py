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
        item = input("Digite o nome do item que deseja: ")
        quantidade = int(input("Digite a quantidade: "))

        if item in self.cardapio and self.cardapio[item]['estoque'] >= quantidade:
            self.cardapio[item]['estoque'] -= quantidade
            with open(self.pedidos_file, 'a') as file:
                file.write(f"{item},{quantidade}\n")
            print(f"Pedido de {quantidade}x {item} registrado com sucesso!")
        else:
            print("Item indisponível ou quantidade insuficiente.")

    def menu_cliente(self):
        while True:
            print("\n--- Menu Cliente ---")
            print("1. Ver cardápio")
            print("2. Fazer pedido")
            print("3. Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.exibir_cardapio()
            elif opcao == '2':
                self.fazer_pedido()
            elif opcao == '3':
                break
            else:
                print("Opção inválida. Tente novamente.")