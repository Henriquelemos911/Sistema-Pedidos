# -- FAZ UM PEDIDO ENTRE OS ITENS DENTRO DE CARDAPIO --
import json
import os
from InquirerPy import prompt

CARDAPIO_FILE = "cardapio.json"
TODOS_PEDIDOS = "todos_pedidos.json"
MESA = 1
valor_total = 0
pedidos_usuario = []

def salvar_produtos(pedidos):
    with open(TODOS_PEDIDOS, "w") as f:
        json.dump(pedidos, f, indent=3)

def adicionar_produto(MESA, pedido):
    if os.path.exists(TODOS_PEDIDOS):
        with open(TODOS_PEDIDOS, "r") as f:
            try:
                todos_pedidos = json.load(f)
            except json.JSONDecodeError:
                todos_pedidos = []
    else:
        todos_pedidos = []

    novo_pedido = {"MESA": MESA, "PEDIDO": pedido}
    todos_pedidos.append(novo_pedido)
    salvar_produtos(todos_pedidos)
    print(f"Seu pedido foi salvo e está a caminho!")

def carregar_produtos():
    if os.path.exists(CARDAPIO_FILE):
        with open(CARDAPIO_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []

produtos = carregar_produtos()
# MOSTRA TODAS AS OPCOES DO CARDAPIO AO USUARIO
opcoes_pedidos = [f"{produto['nome']} - R${produto['preco']}" for produto in produtos if 'nome' in produto and 'preco' in produto]
opcoes_pedidos.append("- FINALIZAR PEDIDO")

# O USUARIO ESCOLHE SEUS PEDIDOS
while True:
    os.system("cls")
    if pedidos_usuario:
        print("SEU PEDIDO INCLUI:")
        for pedido in pedidos_usuario:
            print(pedido)
        print("\n")
    
    comidas = [
        {
            "type": "list",
            "name": "pedido",
            "message": "Qual seu pedido?",
            "choices": opcoes_pedidos,
        }
    ]

    result = prompt(comidas)
    choice = result['pedido']

    # CALCULAR O VALOR TOTAL
    if choice == "- FINALIZAR PEDIDO":
        print("Seu pedido inclui:")
        for pedido in pedidos_usuario:
            print(pedido)
        print(f"Valor total: R${valor_total:.2f}")
        adicionar_produto(MESA, pedidos_usuario)
        break
    else:
        pedidos_usuario.append(choice)
        # Adiciona o preço do produto ao valor total
        for produto in produtos:
            if f"{produto['nome']} - R${produto['preco']}" == choice:
                valor_total += produto['preco']
                break