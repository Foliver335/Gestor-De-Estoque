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
        labels = ["Usuário:","Senha:","Nome:","Sobrenome:","Matrícula:","CPF:","Patente:"]
        for i,t in enumerate(labels):
            tk.Label(master,text=t).grid(row=i,column=0,sticky="e")
        self.username = tk.Entry(master); self.password = tk.Entry(master,show="*")
        self.first    = tk.Entry(master); self.last     = tk.Entry(master)
        self.matric   = tk.Entry(master); self.cpf      = tk.Entry(master)
        self.patente  = tk.Entry(master)
        entries = [self.username,self.password,self.first,
                   self.last,self.matric,self.cpf,self.patente]
        for i,w in enumerate(entries):
            w.grid(row=i,column=1,padx=5,pady=2)
        tk.Button(master,text="Cadastrar",command=self._cadastrar).grid(
            row=len(labels),column=0,columnspan=2,pady=10)

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
            return messagebox.showerror("Erro","Todos os campos são obrigatórios.")
        secret = self.ctrl.create_user(*dados)
        # gera URI e QR
        uri = pyotp.totp.TOTP(secret).provisioning_uri(
            name=self.username.get(), issuer_name="SistemaDepósito")
        img = qrcode.make(uri)
        top = tk.Toplevel(self.master)
        top.title("Configure seu Authenticator")
        tk.Label(top,text="Escaneie este QR no Google Authenticator").pack(pady=5)
        img = img.resize((200,200))
        self.tkimg = ImageTk.PhotoImage(img)
        tk.Label(top,image=self.tkimg).pack(pady=5)
        tk.Button(top,text="OK",command=top.destroy).pack(pady=10)
        messagebox.showinfo("Sucesso","Usuário cadastrado com sucesso!")
        self.master.destroy()
