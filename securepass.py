#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import secrets
import string

VERSION = "1.0"

print(">>> SECUREPASS SE ESTÁ EJECUTANDO <<<")


class SecurePassApp:

    def __init__(self, root):
        self.root = root
        self.root.title("SecurePass 1.0")
        self.root.geometry("520x450")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        self.password_var = tk.StringVar()
        self.length_var = tk.IntVar(value=12)

        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        self.create_menu()
        self.create_widgets()

    # ==========================
    # MENÚ
    # ==========================
    def create_menu(self):

        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Guardar", command=self.save_password)
        file_menu.add_command(label="Copiar al portapapeles", command=self.copy_to_clipboard)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Ayuda", command=self.show_help)
        help_menu.add_command(label="Créditos", command=self.show_credits)

        menubar.add_cascade(label="Archivo", menu=file_menu)
        menubar.add_cascade(label="Ayuda", menu=help_menu)

        self.root.config(menu=menubar)

    # ==========================
    # INTERFAZ
    # ==========================
    def create_widgets(self):

        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Longitud de contraseña:").pack(anchor="w")

        ttk.Spinbox(frame, from_=4, to=15,
                    textvariable=self.length_var).pack(fill="x")

        ttk.Checkbutton(frame, text="Incluir Mayúsculas",
                        variable=self.use_upper).pack(anchor="w")
        ttk.Checkbutton(frame, text="Incluir Minúsculas",
                        variable=self.use_lower).pack(anchor="w")
        ttk.Checkbutton(frame, text="Incluir Números",
                        variable=self.use_numbers).pack(anchor="w")
        ttk.Checkbutton(frame, text="Incluir Símbolos",
                        variable=self.use_symbols).pack(anchor="w")

        ttk.Button(frame, text="Generar / Regenerar",
                   command=self.generate_password).pack(pady=10)

        ttk.Entry(frame, textvariable=self.password_var,
                  font=("Courier", 12)).pack(fill="x", pady=5)

        ttk.Button(frame, text="Guardar en archivo",
                   command=self.save_password).pack(pady=5)
        ttk.Button(frame, text="Cerrar aplicación",
                   command=self.root.quit).pack(pady=5)

        ttk.Label(frame, text="Fortaleza:").pack(anchor="w", pady=(15, 0))

        self.strength_bar = ttk.Progressbar(frame,
                                            length=400,
                                            maximum=100)
        self.strength_bar.pack()

        self.strength_label = ttk.Label(frame, text="")
        self.strength_label.pack()

    # ==========================
    # GENERADOR
    # ==========================
    def generate_password(self):

        length = self.length_var.get()

        if length < 4 or length > 15:
            messagebox.showerror("Error",
                                 "La longitud debe estar entre 4 y 15 caracteres.")
            return

        charset = ""

        if self.use_upper.get():
            charset += string.ascii_uppercase
        if self.use_lower.get():
            charset += string.ascii_lowercase
        if self.use_numbers.get():
            charset += string.digits
        if self.use_symbols.get():
            charset += string.punctuation

        if not charset:
            messagebox.showerror("Error",
                                 "Debe seleccionar al menos un tipo de carácter.")
            return

        password = ''.join(secrets.choice(charset) for _ in range(length))
        self.password_var.set(password)

        self.update_strength(password)

    # ==========================
    # FORTALEZA
    # ==========================
    def update_strength(self, password):

        length = len(password)
        variety = 0

        if any(c.islower() for c in password):
            variety += 1
        if any(c.isupper() for c in password):
            variety += 1
        if any(c.isdigit() for c in password):
            variety += 1
        if any(c in string.punctuation for c in password):
            variety += 1

        score = (length * 4) + (variety * 10)
        percent = min(score, 100)

        self.strength_bar["value"] = percent

        if length <= 5:
            text = "Muy débil"
            color = "#8b0000"
        elif length <= 7:
            text = "Débil"
            color = "#d90429"
        elif length <= 10:
            text = "Media"
            color = "#f77f00"
        elif length <= 13:
            text = "Fuerte"
            color = "#fcbf49"
        else:
            text = "Muy fuerte"
            color = "#2a9d8f"

        self.strength_label.config(text=text)

        style = ttk.Style()
        style.configure("Custom.Horizontal.TProgressbar",
                        troughcolor="white",
                        background=color)

        self.strength_bar.config(style="Custom.Horizontal.TProgressbar")

    # ==========================
    # UTILIDADES
    # ==========================
    def save_password(self):

        password = self.password_var.get()

        if not password:
            messagebox.showwarning("Aviso",
                                   "No hay contraseña para guardar.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt")

        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(password)

    def copy_to_clipboard(self):

        password = self.password_var.get()

        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copiado",
                                "✔ Copiado al portapapeles")

    def show_help(self):
        messagebox.showinfo("Ayuda",
                            "Seleccione opciones y genere una contraseña segura.")

    def show_credits(self):
        messagebox.showinfo("Créditos",
                            f"SecurePass {VERSION}\n"
                            "Autor: Javier Cachón Garrido\n"
                            "Licencia: GPL v3")


# ==========================
# MAIN
# ==========================
if __name__ == "__main__":
    root = tk.Tk()
    app = SecurePassApp(root)
    root.mainloop()