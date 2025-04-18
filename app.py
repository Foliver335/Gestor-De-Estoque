import tkinter as tk
from view.main_view import MainView

if __name__ == "__main__":
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()
