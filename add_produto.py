import json
import os
os.system("cls")
# FILE ONDE FICA OS PRODUTOS
CARDAPIO_FILE = "cardapio.json"
# Função para carregar os produtos do JSON
def carregar_produtos():
    if os.path.exists(CARDAPIO_FILE):
        with open(CARDAPIO_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []

# Função para salvar os produtos no JSON
def salvar_produtos(produtos):
    with open(CARDAPIO_FILE, "w") as f:
        json.dump(produtos, f, indent=3)

# Função para adicionar um novo produto
def adicionar_produto(id,nome,composicao, preco):
    produtos = carregar_produtos()
    novo_produto = {"ID":id ,"nome": nome, "composicao":composicao ,"preco": preco}
    produtos.append(novo_produto)
    salvar_produtos(produtos)
    print(f"Produto {nome} adicionado com sucesso!")

# Exemplo de uso
if __name__ == "__main__":
    id = input("Digite o ID do produto: ")
    nome = input("Digite o nome do produto: ")
    composicao = input("Digite a composição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    adicionar_produto(id, nome, composicao, preco)