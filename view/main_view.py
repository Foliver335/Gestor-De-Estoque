import tkinter as tk
from view.register_view import RegisterView
from view.entry_view import EntryView
from view.exit_view import ExitView

class MainView:
    def __init__(self, root, user):
        self.root = root
        self.user = user   # tuple (id, username)
        self.root.title(f"Sistema de Depósito — {self.user[1]}")

        tk.Button(root, text="Cadastrar Material", width=30, command=self.abrir_cadastro).pack(pady=10)
        tk.Button(root, text="Registrar Entrada",  width=30, command=self.abrir_entrada).pack(pady=10)
        tk.Button(root, text="Registrar Saída",    width=30, command=self.abrir_saida).pack(pady=10)

    def abrir_cadastro(self):
        tk.Toplevel(self.root, padx=10, pady=10, 
                    ).__class__ and RegisterView(tk.Toplevel(self.root))

    def abrir_entrada(self):
        win = tk.Toplevel(self.root)
        EntryView(win, self.user)

    def abrir_saida(self):
        win = tk.Toplevel(self.root)
        ExitView(win, self.user)
