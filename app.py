import tkinter as tk
from view.login_view import LoginView

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda e: root.attributes('-fullscreen', False))
    LoginView(root)
    root.mainloop()
