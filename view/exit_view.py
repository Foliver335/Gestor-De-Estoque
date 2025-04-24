import tkinter as tk
from tkinter import messagebox
from controller.material_controller import MaterialController
from controller.auth_controller     import AuthController
from controller.log_controller      import LogController

class ExitView:
    def __init__(self, master, user):
        self.master = master
        self.user = user                     # (id, username)
        self.mat_ctrl  = MaterialController()
        self.auth_ctrl = AuthController()
        self.log_ctrl  = LogController()

        master.title("Saída de Material")


        tk.Label(master, text="Código do Material:").pack(pady=5)
        self.codigo_entry = tk.Entry(master); self.codigo_entry.pack(pady=5)
        self.codigo_entry.focus()

        tk.Label(master, text="Quantidade:").pack(pady=5)
        self.qtd_entry = tk.Entry(master); self.qtd_entry.pack(pady=5)

        tk.Label(master, text="Senha (reconfirmação):").pack(pady=5)
        self.pwd_entry = tk.Entry(master, show="*"); self.pwd_entry.pack(pady=5)

    def registrar_saida(self):
        codigo   = self.codigo_entry.get().strip()
        pwd      = self.pwd_entry.get().strip()
        try:
            quantidade = int(self.qtd_entry.get())
        except ValueError:
            return messagebox.showerror("Erro", "Quantidade deve ser um inteiro.")

        if not self.auth_ctrl.login(self.user[1], pwd):
            return messagebox.showerror("Erro", "Senha incorreta.")

        mat = self.mat_ctrl.buscar_material(codigo)
        if not mat:
            return messagebox.showerror("Erro", "Material não encontrado.")
        if mat[3] < quantidade:
            return messagebox.showwarning("Aviso", "Estoque insuficiente.")

        self.mat_ctrl.saida_material(codigo, quantidade)
        self.log_ctrl.registrar_log_saida(mat, self.user, quantidade)

        messagebox.showinfo("Sucesso",
            f"{quantidade}x '{mat[2]}' retirado por {self.user[1]}.")
        self.master.destroy()
