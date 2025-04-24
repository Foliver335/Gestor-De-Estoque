import tkinter as tk
from tkinter import messagebox
from controller.material_controller import MaterialController

class RegisterView:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastrar Material")
        self.ctrl = MaterialController()

        container = tk.Frame(master)
        container.place(relx=0.5, rely=0.5, anchor="center")
        container.pack(expand=True)   


        labels = ["Código:", "Nome:", "Quantidade:", "Unidade:", "Descrição:", "Validade (YYYY-MM-DD):"]
        for i, text in enumerate(labels):
            tk.Label(container, text=text).grid(row=i, column=0, sticky="e", pady=2)

        self.codigo    = tk.Entry(container)
        self.nome      = tk.Entry(container)
        self.quantidade= tk.Entry(container)
        self.unidade   = tk.Entry(container)
        self.descricao = tk.Entry(container)
        self.validade  = tk.Entry(container)

        entries = [self.codigo, self.nome, self.quantidade, self.unidade, self.descricao, self.validade]
        for i, w in enumerate(entries):
            w.grid(row=i, column=1, padx=10, pady=2)

        tk.Button(container, text="Cadastrar", width=20, command=self._cadastrar).grid(
            row=len(labels), column=0, columnspan=2, pady=15)

    def _cadastrar(self):
        try:
            dados = (
                self.codigo.get().strip(),
                self.nome.get().strip(),
                int(self.quantidade.get()),
                self.unidade.get().strip(),
                self.descricao.get().strip(),
                self.validade.get().strip()
            )
        except ValueError:
            return messagebox.showerror("Erro", "Quantidade deve ser um número inteiro.", parent=self.master)

        self.ctrl.cadastrar(*dados)
        messagebox.showinfo("Sucesso", "Material cadastrado com sucesso!", parent=self.master)
        self.master.destroy()
