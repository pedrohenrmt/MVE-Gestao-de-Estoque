import tkinter as tk

# JANELA

janela = tk.Tk()

janela.title("Sistema de Estoque")

janela.geometry("500x400")

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
    text="Cadastrar Produto"
)

botao.pack(pady=20)

# INICIAR

janela.mainloop()