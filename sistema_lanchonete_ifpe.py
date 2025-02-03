# Sistema de Autoatendimento - Lanchonete IFPE

def remover_espacos(texto):
    resultado = ""
    for char in texto:
        if char != " ":
            resultado += char
    return resultado

def separar_linha(linha, separador):
    partes = []
    parte_atual = ""
    for char in linha:
        if char == separador:
            partes.append(parte_atual)
            parte_atual = ""
        else:
            parte_atual += char
    partes.append(parte_atual)
    return partes

def juntar_lista(lista, separador):
    resultado = ""
    for i in range(len(lista)):
        resultado += lista[i]
        if i < len(lista) - 1:
            resultado += separador
    return resultado

def exibir_cardapio():   
    with open("menu_estoque.txt", 'r') as file:
        print("\n--- Cardápio ---\n")
        cardapio = file.readlines()
        if cardapio:
            for i in range(len(cardapio)):
                print(f"{i+1}. {cardapio[i]}")
        else:
            print("O cardápio está vazio!")

def fazer_pedido():
        exibir_cardapio()
        pedido = []

        while True:
            item = int(input("Digite o número do item que deseja:"))
            with open("menu_estoque.txt","r") as file:
                cardapio = file.readlines()
                num_item = []
                for i in range(len(cardapio)):
                    num_item.append(i+1) 
            if item not in num_item:
                print("Item não encontrado no cardápio. Tenta novamente.")
                continue

            quantidade = int(input("Digite a quantidade: "))
            if cardapio[item]['estoque'] < quantidade:
                print("Quantidade indisponível no estoque. Escolha uma quantidade menor.")
                continue

            pedido.append((item,quantidade))
            cardapio[item]['estoque'] -= quantidade

            maisItens = input("Deseja adiciomais mais um item ao pedido? (s/n)").strip().lower()
            if maisItens != "s":
                pedidoFinal = ", ".join([f"{quantidade}x {item}" for item, quantidade in pedido])
                print(f"Pedido de {pedidoFinal} registrado com sucesso!")
                break

        with open(pedidos_file, 'a') as file:
            linha_pedido = ",".join([f"{item},{quantidade}" for item, quantidade in pedido]) + ",pendente\n"
            file.write(linha_pedido)

        with open(menu_file, "w") as file:
            for nome_item, detalhes in cardapio.items():
                file.write(f"{nome_item},{detalhes['preco']},{detalhes['estoque']}\n")

def exibir_pedidos():
    with open("pedidos.txt", "r") as file:
        pedidos = file.readlines()
        if pedidos:
            for i in range(len(pedidos)):
                print(f"{i + 1}. {pedidos[i]}")
        else:
            print("Nenhum pedido pendente.")

def alterar_status_do_pedido():
    try:
        with open("pedidos.txt", "r") as file:
            pedidos = file.readlines()
        if not pedidos:
            print("Nenhum pedido pendente.")
            return
        for i in range(len(pedidos)):
            print(f"{i + 1}. {pedidos[i]}")
        num_pedido = int(input("Digite o número do pedido que deseja alterar o status: ")) - 1
        if 0 <= num_pedido < len(pedidos):
            dados = separar_linha(remover_espacos(pedidos[num_pedido]), ",")
            dados[-1] = "finalizado"
            pedidos[num_pedido] = juntar_lista(dados, ",") + "\n"
            with open("pedidos.txt", "w") as file:
                file.writelines(pedidos)
            print("Status do pedido atualizado com sucesso.")
        else:
            print("Número de pedido inválido.")
    except:
        print("Erro ao alterar o status do pedido.")

def adicionar_item_ao_cardapio():
    item = input("Nome do novo item: ")
    preco = input("Preço do item: ")
    quantidade = input("Quantidade disponível: ")
    try:
        with open("menu_estoque.txt", "a") as file:
            file.write(juntar_lista([item, preco, quantidade], ",") + "\n")
        print("Item adicionado com sucesso ao cardápio.")
    except:
        print("Erro ao adicionar item ao cardápio.")

def menu_cliente():
        while True:
            print("\n--- Menu Cliente ---")
            print("1. Ver cardápio")
            print("2. Fazer pedido")
            print("3. Cancelar pedido")
            print("4. Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                exibir_cardapio()
            elif opcao == '2':
                fazer_pedido()
            elif opcao == '3':
                cancelar_pedido()
            elif opcao == '4':
                break
            else:
                print("Opção inválida. Tente novamente.")

def menu_vendedor():
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
                exibir_pedidos()
            elif opcao == '2':
                alterar_status_do_pedido()
            elif opcao == '3':
                limpar_pedidos()
            elif opcao == '4':
                adicionar_item_ao_cardapio()
            elif opcao == '5':
                alterar_item_do_cardapio()
            elif opcao == '6':
                excluir_item_do_cardapio()
            elif opcao == '7':
                break
            else:
                print("Opção inválida. Tente novamente.")

def menu_principal():
    while True:
        print("\n--- Sistema de Autoatendimento - Lanchonete IFPE ---")
        print("1. Interface do Cliente")
        print("2. Interface do Vendedor")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_cliente()
        elif opcao == '2':
            menu_vendedor()
        elif opcao == '3':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()
