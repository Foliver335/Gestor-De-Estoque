import tkinter as tk
from tkinter import messagebox
from controller.material_controller import MaterialController

class EntryView:
    def __init__(self, master, user):
        self.master = master
        self.user = user
        self.master.title("Entrada de Material")
        self.controller = MaterialController()

        container = tk.Frame(master)
        container.pack(expand=True)

        tk.Label(container, text="Código do Material:").pack(pady=5)
        self.codigo_entry = tk.Entry(container)
        self.codigo_entry.pack(pady=5)
        self.codigo_entry.focus()

        tk.Label(container, text="Quantidade:").pack(pady=5)
        self.qtd_entry = tk.Entry(container)
        self.qtd_entry.pack(pady=5)

        tk.Button(container, text="Registrar Entrada", command=self.registrar_entrada).pack(pady=10)

        self.codigo_entry.bind("<Return>", lambda e: self.registrar_entrada())

    def registrar_entrada(self):
        codigo = self.codigo_entry.get().strip()
        try:
            quantidade = int(self.qtd_entry.get())
        except ValueError:
            return messagebox.showerror("Erro", "Quantidade deve ser número inteiro.", parent=self.master)

        material = self.controller.buscar_material(codigo)
        if not material:
            return messagebox.showerror("Erro", "Material não encontrado.", parent=self.master)

        # registra entrada
        self.controller.entrada_material(codigo, quantidade)
        messagebox.showinfo("Sucesso",
                            f"Entrada registrada: {quantidade}x '{material[2]}'",
                            parent=self.master)
        self.master.destroy()

