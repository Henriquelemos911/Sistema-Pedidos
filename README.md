# 🍽️ Sistema de Pedidos de Restaurante

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este é um sistema simples de pedidos para restaurante desenvolvido em Python, utilizando arquivos JSON para armazenamento de dados. Inspirado em um sistema de pedidos via tablet observado em um restaurante, este projeto simula o gerenciamento de pedidos de várias mesas.

## 🚀 Funcionalidades

- Adicionar novos produtos ao cardápio.
- Fazer pedidos para mesas individuais (ex: mesa 1, mesa 2, mesa 3).
- Armazenar todos os pedidos em um arquivo JSON centralizado.
- Facilmente extensível para adicionar mais mesas ou funcionalidades.

## 🧑‍💻 Tecnologias Utilizadas

- Python 3.13
- JSON

## 📋 Como Rodar

### 🐧 No Linux:

1. Certifique-se de que o Python 3 está instalado:
   ```bash
   sudo apt update
   sudo apt install python3
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd /caminho/para/Sistema-Pedidos
   ```

3. Execute o script desejado. Por exemplo, para adicionar um produto:
   ```bash
   python3 add_produto.py
   ```

   Para fazer um pedido na mesa 1:
   ```bash
   python3 mesa01.py
   ```

### 🪟 No Windows:

1. Certifique-se de que o Python 3 está instalado. Caso não esteja, baixe e instale em: https://www.python.org/downloads/

2. Abra o Prompt de Comando e navegue até o diretório do projeto:
   ```bash
   cd C:\caminho\para\Sistema-Pedidos
   ```

3. Execute o script desejado. Por exemplo, para adicionar um produto:
   ```bash
   python add_produto.py
   ```

   Para fazer um pedido na mesa 1:
   ```bash
   python mesa01.py
   ```

## 📁 Estrutura do Projeto

```
Sistema-Pedidos/
├── add_produto.py        # Script para adicionar novos produtos ao cardápio
├── cardapio.json         # Arquivo JSON que armazena os itens do cardápio
├── mesa01.py             # Script para gerenciar pedidos da mesa 1
├── mesa02.py             # Script para gerenciar pedidos da mesa 2
├── mesa03.py             # Script para gerenciar pedidos da mesa 3
├── todos_pedidos.json    # Arquivo JSON que armazena todos os pedidos
└── README.md             # Documentação do projeto
```

## 📌 Notas

- O arquivo `cardapio.json` contém os itens do cardápio. Certifique-se de preenchê-lo antes de fazer pedidos.
- Cada script `mesaXX.py` corresponde a uma mesa específica. Você pode criar novos scripts para mais mesas, se quiser.
- Todos os pedidos são salvos no arquivo `todos_pedidos.json`.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

Sinta-se à vontade para fazer fork deste repositório e adaptá-lo às suas necessidades!
