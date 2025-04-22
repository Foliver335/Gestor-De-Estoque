import tkinter as tk
from tkinter import messagebox
from controller.material_controller import MaterialController

class EntryView:
    def __init__(self, master):
        self.master = master
        self.master.title("Entrada de Material")
        self.controller = MaterialController()

        tk.Label(master, text="Código do Material:").pack(pady=5)
        self.codigo_entry = tk.Entry(master); self.codigo_entry.pack(pady=5)
        self.codigo_entry.focus()

        tk.Label(master, text="Quantidade:").pack(pady=5)
        self.qtd_entry = tk.Entry(master); self.qtd_entry.pack(pady=5)

        tk.Button(master, text="Registrar Entrada", command=self.registrar_entrada).pack(pady=10)
        self.codigo_entry.bind("<Return>", lambda e: self.registrar_entrada())

    def registrar_entrada(self):
        codigo = self.codigo_entry.get()
        try:
            quantidade = int(self.qtd_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser número inteiro.")
            return

        material = self.controller.buscar_material(codigo)
        if material:
            self.controller.entrada_material(codigo, quantidade)
            messagebox.showinfo("Sucesso", f"Entrada registrada: {material[2]}")
            self.master.destroy()
        else:
            messagebox.showerror("Erro", "Material não encontrado.")
