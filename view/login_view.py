import tkinter as tk
from tkinter import messagebox, simpledialog
from controller.auth_controller import AuthController
from view.register_user_view import RegisterUserView
from view.main_view import MainView
from config import MASTER_PASSWORD

class LoginView:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.ctrl = AuthController()

        container = tk.Frame(master)
        container.place(relx=0.5, rely=0.5, anchor="center")
        container.pack(expand=True)   

        tk.Label(container, text="Usuário:").grid(row=0, column=0, pady=5, sticky="e")
        tk.Label(container, text="Senha:").grid(row=1, column=0, pady=5, sticky="e")
        tk.Label(container, text="Auth Code:").grid(row=2, column=0, pady=5, sticky="e")

        self.username = tk.Entry(container)
        self.password = tk.Entry(container, show="*")
        self.code     = tk.Entry(container)
        self.username.grid(row=0, column=1, padx=10)
        self.password.grid(row=1, column=1, padx=10)
        self.code.grid(row=2, column=1, padx=10)

        tk.Button(container, text="Entrar",            width=12, command=self._try_login)     .grid(row=3, column=0, pady=15)
        tk.Button(container, text="Cadastrar Usuário", width=12, command=self._prompt_master).grid(row=3, column=1, pady=15)

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
            win.transient(self.master); win.grab_set(); win.attributes('-topmost', True)
            from view.register_user_view import RegisterUserView
            RegisterUserView(win)
        else:
            messagebox.showerror("Acesso negado", "Senha master incorreta.", parent=self.master)

    def _try_login(self):
        u = self.username.get().strip()
        p = self.password.get().strip()
        t = self.code.get().strip()
        user = self.ctrl.login(u, p, t)
        if user:
            self.master.destroy()
            root = tk.Tk()
            root.attributes('-fullscreen', True)
            root.bind("<Escape>", lambda e: root.attributes('-fullscreen', False))
            from view.main_view import MainView
            MainView(root, user)
            root.mainloop()
        else:
            messagebox.showerror("Falha", "Credenciais ou código inválidos.", parent=self.master)
            self.code.delete(0, tk.END)
