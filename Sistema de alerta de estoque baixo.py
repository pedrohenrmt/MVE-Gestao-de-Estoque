import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# BANCO DE DADOS

conn = sqlite3.connect("estoque.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    nome TEXT,

    categoria TEXT,

    preco REAL,

    quantidade INTEGER
)
""")

conn.commit()

# ALERTA

def alerta_estoque_baixo():

    cursor.execute("""
    SELECT nome, quantidade
    FROM produtos
    WHERE quantidade < 5
    """)

    produtos = cursor.fetchall()

    if len(produtos) > 0:

        messagebox.showwarning(
            "Alerta",
            "Existem produtos com estoque baixo"
        )

# MOSTRAR PRODUTOS

def mostrar_produtos():

    for item in tabela.get_children():

        tabela.delete(item)

    cursor.execute("""
    SELECT * FROM produtos
    """)

    produtos = cursor.fetchall()

    for produto in produtos:

        tabela.insert(
            "",
            tk.END,
            values=produto
        )

    alerta_estoque_baixo()

# CADASTRAR

def cadastrar_produto():

    nome = entry_nome.get()

    categoria = entry_categoria.get()

    preco = entry_preco.get()

    quantidade = entry_quantidade.get()

    cursor.execute("""
    INSERT INTO produtos
    (nome, categoria, preco, quantidade)

    VALUES (?, ?, ?, ?)
    """, (
        nome,
        categoria,
        preco,
        quantidade
    ))

    conn.commit()

    mostrar_produtos()

# ENTRADA

def registrar_entrada():

    produto_id = entry_id.get()

    quantidade = entry_movimentacao.get()

    cursor.execute("""
    UPDATE produtos
    SET quantidade = quantidade + ?
    WHERE id = ?
    """, (
        quantidade,
        produto_id
    ))

    conn.commit()

    mostrar_produtos()

# SAÍDA

def registrar_saida():

    produto_id = entry_id.get()

    quantidade = entry_movimentacao.get()

    cursor.execute("""
    UPDATE produtos
    SET quantidade = quantidade - ?
    WHERE id = ?
    """, (
        quantidade,
        produto_id
    ))

    conn.commit()

    mostrar_produtos()

# JANELA

janela = tk.Tk()

janela.title("Sistema de Estoque")

janela.geometry("800x700")

# TÍTULO

titulo = tk.Label(
    janela,
    text="Sistema de Gestão de Estoque",
    font=("Arial", 16)
)

titulo.pack(pady=20)

# NOME

label_nome = tk.Label(
    janela,
    text="Nome"
)

label_nome.pack()

entry_nome = tk.Entry(
    janela,
    width=30
)

entry_nome.pack()

# CATEGORIA

label_categoria = tk.Label(
    janela,
    text="Categoria"
)

label_categoria.pack()

entry_categoria = tk.Entry(
    janela,
    width=30
)

entry_categoria.pack()

# PREÇO

label_preco = tk.Label(
    janela,
    text="Preço"
)

label_preco.pack()

entry_preco = tk.Entry(
    janela,
    width=30
)

entry_preco.pack()

# QUANTIDADE

label_quantidade = tk.Label(
    janela,
    text="Quantidade"
)

label_quantidade.pack()

entry_quantidade = tk.Entry(
    janela,
    width=30
)

entry_quantidade.pack()

# BOTÃO CADASTRAR

botao = tk.Button(
    janela,
    text="Cadastrar Produto",
    command=cadastrar_produto
)

botao.pack(pady=20)

# MOVIMENTAÇÃO

label_id = tk.Label(
    janela,
    text="ID do Produto"
)

label_id.pack()

entry_id = tk.Entry(
    janela,
    width=30
)

entry_id.pack()

label_movimentacao = tk.Label(
    janela,
    text="Quantidade"
)

label_movimentacao.pack()

entry_movimentacao = tk.Entry(
    janela,
    width=30
)

entry_movimentacao.pack()

# BOTÃO ENTRADA

botao_entrada = tk.Button(
    janela,
    text="Registrar Entrada",
    command=registrar_entrada
)

botao_entrada.pack(pady=10)

# BOTÃO SAÍDA

botao_saida = tk.Button(
    janela,
    text="Registrar Saída",
    command=registrar_saida
)

botao_saida.pack(pady=10)

# TABELA

colunas = (
    "ID",
    "Nome",
    "Categoria",
    "Preço",
    "Quantidade"
)

tabela = ttk.Treeview(
    janela,
    columns=colunas,
    show="headings"
)

for coluna in colunas:

    tabela.heading(
        coluna,
        text=coluna
    )

tabela.pack(pady=20)

mostrar_produtos()

# INICIAR

janela.mainloop()