import tkinter as tk
from tkinter import messagebox, simpledialog
from controller.auth_controller import AuthController
from view.register_user_view import RegisterUserView
from view.main_view import MainView
from config import MASTER_PASSWORD         # ← importa do arquivo separado

class LoginView:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.ctrl = AuthController()

        tk.Label(master, text="Usuário:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(master, text="Senha:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(master, text="Auth Code:").grid(row=2, column=0, padx=5, pady=5)

        self.username = tk.Entry(master)
        self.password = tk.Entry(master, show="*")
        self.code     = tk.Entry(master)
        self.username.grid(row=0, column=1, padx=5, pady=5)
        self.password.grid(row=1, column=1, padx=5, pady=5)
        self.code.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(master, text="Entrar",             width=12, command=self._try_login)   .grid(row=3, column=0, pady=10)
        tk.Button(master, text="Cadastrar Usuário",  width=12, command=self._prompt_master).grid(row=3, column=1, pady=10)

        master.bind("<Return>", lambda e: self._try_login())

    def _prompt_master(self):
        pwd = simpledialog.askstring(
            "Senha Master",
            "Digite a senha master para cadastrar usuário:",
            show="*",
            parent=self.master
        )
        if pwd == MASTER_PASSWORD:
            win = tk.Toplevel(self.master)
            RegisterUserView(win)
        else:
            messagebox.showerror("Acesso negado", "Senha master incorreta.")

    def _try_login(self):
        u = self.username.get().strip()
        p = self.password.get().strip()
        t = self.code.get().strip()
        user = self.ctrl.login(u, p, t)
        if user:
            self.master.destroy()
            root = tk.Tk()
            MainView(root, user)
            root.mainloop()
        else:
            messagebox.showerror("Falha", "Credenciais ou código inválidos.")
            self.code.delete(0, tk.END)
