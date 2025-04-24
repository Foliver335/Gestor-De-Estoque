import tkinter as tk
from tkinter import messagebox
from controller.auth_controller import AuthController
import pyotp, qrcode
from PIL import Image, ImageTk

class RegisterUserView:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastrar Usuário")
        self.ctrl = AuthController()

        container = tk.Frame(master)
        container.place(relx=0.5, rely=0.5, anchor="center")
        container.pack(expand=True)   

        labels = ["Usuário:","Senha:","Nome:","Sobrenome:","Matrícula:","CPF:","Patente:"]
        for i, text in enumerate(labels):
            tk.Label(container, text=text).grid(row=i, column=0, sticky="e", pady=2)

        self.username = tk.Entry(container)
        self.password = tk.Entry(container, show="*")
        self.first    = tk.Entry(container)
        self.last     = tk.Entry(container)
        self.matric   = tk.Entry(container)
        self.cpf      = tk.Entry(container)
        self.patente  = tk.Entry(container)

        entries = [
            self.username, self.password, self.first,
            self.last, self.matric, self.cpf, self.patente
        ]
        for i, w in enumerate(entries):
            w.grid(row=i, column=1, padx=10, pady=2)

        tk.Button(container, text="Cadastrar", width=20, command=self._cadastrar)\
          .grid(row=len(labels), column=0, columnspan=2, pady=15)

    def _cadastrar(self):
        dados = (
            self.username.get().strip(),
            self.password.get().strip(),
            self.first.get().strip(),
            self.last.get().strip(),
            self.matric.get().strip(),
            self.cpf.get().strip(),
            self.patente.get().strip()
        )
        if any(not v for v in dados):
            return messagebox.showerror("Erro", "Todos os campos são obrigatórios.", parent=self.master)

        if self.ctrl.user_exists(dados[0], dados[5]):
            return messagebox.showerror("Erro", "Usuário já cadastrado.", parent=self.master)

        secret = self.ctrl.create_user(*dados)
        uri    = pyotp.TOTP(secret).provisioning_uri(name=dados[0], issuer_name="SistemaDepósito")
        img    = qrcode.make(uri).resize((200,200))

        top = tk.Toplevel(self.master)
        top.title("Configurar Google Authenticator")
        top.transient(self.master); top.grab_set(); top.attributes('-topmost', True); top.focus_force()

        tk.Label(top, text="Escaneie este QR no Authenticator").pack(pady=5)
        self.tkimg = ImageTk.PhotoImage(img)
        tk.Label(top, image=self.tkimg).pack(pady=5)

        tk.Label(top, text="Digite o código de 6 dígitos:").pack(pady=(10,2))
        code_entry = tk.Entry(top); code_entry.pack(pady=5); code_entry.focus()

        def verify_and_close():
            token = code_entry.get().strip()
            if pyotp.TOTP(secret).verify(token, valid_window=1):
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!", parent=top)
                top.destroy(); self.master.destroy()
            else:
                messagebox.showerror("Erro", "Código inválido, tente novamente.", parent=top)
                code_entry.delete(0, tk.END)

        tk.Button(top, text="Verificar Código", command=verify_and_close).pack(pady=10)
