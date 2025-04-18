import tkinter as tk
from tkinter import messagebox
from controller.material_controller import MaterialController

class RegisterView:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastrar Material")
        self.controller = MaterialController()

        labels = ["Código:", "Nome:", "Quantidade:", "Unidade:", "Descrição:", "Validade (AAAA-MM-DD):"]
        for idx, text in enumerate(labels):
            tk.Label(master, text=text).grid(row=idx, column=0, sticky="e", padx=5, pady=2)

        self.codigo    = tk.Entry(master); self.codigo.grid(row=0, column=1, padx=5, pady=2)
        self.nome      = tk.Entry(master); self.nome.grid(row=1, column=1, padx=5, pady=2)
        self.quantidade= tk.Entry(master); self.quantidade.grid(row=2, column=1, padx=5, pady=2)
        self.unidade   = tk.Entry(master); self.unidade.grid(row=3, column=1, padx=5, pady=2)
        self.descricao = tk.Entry(master); self.descricao.grid(row=4, column=1, padx=5, pady=2)
        self.validade  = tk.Entry(master); self.validade.grid(row=5, column=1, padx=5, pady=2)

        tk.Button(master, text="Cadastrar", command=self.cadastrar_material).grid(row=6, column=0, columnspan=2, pady=10)

    def cadastrar_material(self):
        try:
            dados = (
                self.codigo.get(),
                self.nome.get(),
                int(self.quantidade.get()),
                self.unidade.get(),
                self.descricao.get(),
                self.validade.get()
            )
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro.")
            return

        self.controller.cadastrar(*dados)
        messagebox.showinfo("Sucesso", "Material cadastrado com sucesso!")
        self.master.destroy()
