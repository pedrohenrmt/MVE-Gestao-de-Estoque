# Sistema de Gestão de Estoque

Sistema desktop desenvolvido em Python com interface gráfica, voltado para o controle de estoque de produtos, permitindo cadastro, movimentação e geração de relatórios.
Projeto acadêmico desenvolvido para a disciplina de Análise e Desenvolvimento de Sistemas (ADS).

## Tecnologias Utilizadas

- Python
- Tkinter
- SQLite

# Objetivo

O sistema tem como objetivo facilitar o gerenciamento de estoque, permitindo o controle eficiente de entrada e saída de produtos, além de fornecer informações úteis para tomada de decisão.
Sistemas desse tipo são fundamentais para organizar mercadorias e automatizar processos dentro de empresas.

# Funcionalidades

## Cadastro de Produtos

O sistema permite cadastrar:
- Nome
- Categoria
- Preço
- Quantidade


## Movimentações de Estoque

O sistema registra:
- Entradas de produtos
- Saídas de produtos


## Consulta de Estoque

O usuário consegue visualizar:
- Produtos cadastrados
- Quantidade disponível
- Preço
- Categoria


## Alertas Inteligentes

O sistema mostra alertas automáticos quando:
- A quantidade do produto é menor que 5


# Banco de Dados

O sistema utiliza SQLite para armazenar:
- Produtos
- Movimentações


# Interface

A interface gráfica foi desenvolvida com Tkinter.


#Como Executar o Projeto
# Clone o repositório
git clone https://github.com/pedrohenrmt/MVE-Gestao-de-Estoque

- Acesse a pasta do projeto
cd MVE-Gestao-de-Estoque/src

- Execute o sistema
python main.py


# Estrutura do Projeto

```text
MVE-Gestao-de-Estoque
│
├── src
│   └── main.py
│
├── estoque.db
│
└── README.md
```
