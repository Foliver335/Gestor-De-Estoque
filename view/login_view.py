# view/login_view.py
import tkinter as tk
from tkinter import messagebox
from controller.auth_controller import AuthController
from view.main_view import MainView

class LoginView:
    def __init__(self, master):
        self.master = master; master.title("Login")
        self.ctrl = AuthController()
        # labels
        tk.Label(master,text="Usuário:").grid(row=0,column=0)
        tk.Label(master,text="Senha:").grid(row=1,column=0)
        tk.Label(master,text="Auth Code:").grid(row=2,column=0)
        # entradas
        self.user = tk.Entry(master); self.pwd = tk.Entry(master,show="*")
        self.code = tk.Entry(master)
        self.user.grid(row=0,column=1); self.pwd.grid(row=1,column=1)
        self.code.grid(row=2,column=1)
        tk.Button(master,text="Entrar",command=self._try).grid(
            row=3,column=0,columnspan=2,pady=10)
        master.bind("<Return>",lambda e: self._try())

    def _try(self):
        u = self.user.get().strip()
        p = self.pwd.get().strip()
        t = self.code.get().strip()
        user = self.ctrl.login(u,p,t)
        if user:
            self.master.destroy()
            root = tk.Tk()
            MainView(root,user)
            root.mainloop()
        else:
            messagebox.showerror("Falha","Credenciais ou código inválidos.")
            self.code.delete(0,tk.END)
