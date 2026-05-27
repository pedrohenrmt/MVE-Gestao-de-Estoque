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

    categoria TEXT
)
""")

conn.commit()

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

# CADASTRAR

def cadastrar_produto():

    nome = entry_nome.get()

    categoria = entry_categoria.get()

    if nome == "" or categoria == "":

        messagebox.showerror(
            "Erro",
            "Preencha todos os campos"
        )

    else:

        cursor.execute("""
        INSERT INTO produtos
        (nome, categoria)

        VALUES (?, ?)
        """, (
            nome,
            categoria
        ))

        conn.commit()

        mostrar_produtos()

        messagebox.showinfo(
            "Sucesso",
            "Produto cadastrado"
        )

# JANELA

janela = tk.Tk()

janela.title("Sistema de Estoque")

janela.geometry("600x500")

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
    text="Nome do Produto"
)

label_nome.pack()

entry_nome = tk.Entry(
    janela,
    width=30
)

entry_nome.pack(pady=5)

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

entry_categoria.pack(pady=5)

# BOTÃO

botao = tk.Button(
    janela,
    text="Cadastrar Produto",
    command=cadastrar_produto
)

botao.pack(pady=20)

# TABELA

colunas = (
    "ID",
    "Nome",
    "Categoria"
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
