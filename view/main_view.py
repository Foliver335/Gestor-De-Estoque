import tkinter as tk
from view.register_view import RegisterView
from view.entry_view    import EntryView
from view.exit_view     import ExitView

class MainView:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.root.title(f"Sistema de Depósito — {self.user[1]}")

        container = tk.Frame(self.root)
        container.pack(expand=True)                  
        btn_cad = tk.Button(container,
                            text="Cadastrar Material",
                            width=30,
                            command=self.abrir_cadastro)
        btn_cad.pack(pady=10)

        btn_ent = tk.Button(container,
                            text="Registrar Entrada",
                            width=30,
                            command=self.abrir_entrada)
        btn_ent.pack(pady=10)

        btn_sai = tk.Button(container,
                            text="Registrar Saída",
                            width=30,
                            command=self.abrir_saida)
        btn_sai.pack(pady=10)

    def abrir_cadastro(self):
        win = tk.Toplevel(self.root)
        RegisterView(win)

    def abrir_entrada(self):
        win = tk.Toplevel(self.root)
        EntryView(win, self.user)

    def abrir_saida(self):
        win = tk.Toplevel(self.root)
        ExitView(win, self.user)
