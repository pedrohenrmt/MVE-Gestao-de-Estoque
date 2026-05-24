import tkinter as tk

janela = tk.Tk()

janela.title("Sistema de Estoque")

janela.geometry("500x300")

titulo = tk.Label(
    janela,
    text="Sistema de Gestão de Estoque",
    font=("Arial", 16)
)

titulo.pack(pady=20)

janela.mainloop()
