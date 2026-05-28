# Sistema de Gestão de Estoque

Projeto desenvolvido em Python para a disciplina de Análise e Desenvolvimento de Sistemas (ADS).

## Tecnologias Utilizadas

- Python
- Tkinter
- SQLite
- Pandas


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


## Relatórios Gerenciais

O sistema gera:
- Histórico de movimentações
- Relatórios utilizando Pandas


# Banco de Dados

O sistema utiliza SQLite para armazenar:
- Produtos
- Movimentações


# Interface

A interface gráfica foi desenvolvida com Tkinter.


# Como Executar

## Instalar Pandas

```bash
pip install pandas
```


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
