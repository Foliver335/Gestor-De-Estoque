import tkinter as tk
from view.register_view import RegisterView

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Depósito")

        tk.Button(root, text="Cadastrar Material",    width=30, command=self.abrir_cadastro).pack(pady=10)
        tk.Button(root, text="Registrar Entrada",     width=30, command=self.abrir_entrada).pack(pady=10)
        tk.Button(root, text="Registrar Saída",       width=30, command=self.abrir_saida).pack(pady=10)

    def abrir_cadastro(self):
        janela = tk.Toplevel(self.root)
        RegisterView(janela)

    def abrir_entrada(self):
        from view.entry_view import EntryView
        janela = tk.Toplevel(self.root)
        EntryView(janela)

    def abrir_saida(self):
        from view.exit_view import ExitView
        janela = tk.Toplevel(self.root)
        ExitView(janela)
