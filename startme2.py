import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import tkinter as tk
    from tkinter import filedialog, ttk, messagebox
    import os

except ImportError:
    required_packages = ['tkinter', 'os']
    for package in required_packages:
        install(package)

class ServerClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Server-Client App")
        self.root.geometry("500x450")
        self.root.configure(bg="#1E1E1E")
        self.root.resizable(False, False)

        self.bg_color = "#1E1E1E"
        self.fg_color = "#FFFFFF"
        self.fg1_color = "#FF0000"
        self.entry_bg_color = "#222222"

        self.create_widgets()

    def create_widgets(self):
        self.root.config(bg=self.bg_color)

        header_label = tk.Label(
            self.root, text="Server-Client App", font=("Felix Titling", 32, "bold"), bg=self.bg_color, fg=self.fg1_color
        )
        header_label.pack(pady=65)

        server_button = ttk.Button(
            self.root, text="Start Server", command=self.start_server, style="TButton"
        )
        server_button.pack(pady=20)

        client_button = ttk.Button(
            self.root, text="Start Client", command=self.start_client, style="TButton"
        )
        client_button.pack(pady=20)

    def start_server(self):
        subprocess.Popen([sys.executable, "server2.py"], creationflags=subprocess.CREATE_NO_WINDOW)

    def start_client(self):
        subprocess.Popen([sys.executable, "client2.py"], creationflags=subprocess.CREATE_NO_WINDOW)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Server-Client App")
    icon_path = "./icon.ico"
    root.iconbitmap(icon_path)
    root.geometry("500x450")
    root.configure(bg="#1E1E1E")
    root.resizable(False, False)

    style = ttk.Style()
    style.theme_use('alt')

    style.configure("TButton", padding=(50, 15), font='Helvetica 12', background='#1E1E1E', foreground='#FF0000')

    app = ServerClientApp(root)
    
    root.mainloop()