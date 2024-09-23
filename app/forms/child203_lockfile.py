import time
from datetime import date
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog

from app.utils.helpers import LoadIcon
from app.processing.feat203_lockfile import LockerFile


class LockFile:
    def __init__(self, root):
        self.root = root
        self.root.title("Proteção de documentos")
        logo_icon = LoadIcon("app/images/logo.png")
        self.root.iconphoto(False, logo_icon)
        
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=0)

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(padx=20, pady=20)
        
        self.label = ttk.Label(self.frame, text="Documento para proteção:")
        self.label.grid(row=1, column=0, padx=10, pady=10)        
        self.text_file = ttk.Entry(self.frame,width=50)
        self.text_file.grid(row=2, column=0, sticky="ew", padx=5, pady=5)        
        self.button_file = ttk.Button(self.frame, width=3, text="...", command=self.select_file)
        self.button_file.grid(row=2, column=1, padx=5, pady=5)   
        
        self.label = ttk.Label(self.frame, text="Senha de usuário do documento:")
        self.label.grid(row=3, column=0, padx=10, pady=10)        
        self.text_upassword = ttk.Entry(self.frame,width=50)
        self.text_upassword.grid(row=4, column=0, sticky="ew", padx=5, pady=5)   
        self.checkbox_var = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.frame, text="Somente leitura", variable=self.checkbox_var, command=self.toggle_input)
        self.checkbox.grid(row=4, column=1, padx=5)
        
        self.label = ttk.Label(self.frame, text="Senha de proprietário do documento:")
        self.label.grid(row=5, column=0, padx=10, pady=10)        
        self.text_opassword = ttk.Entry(self.frame,width=50)
        self.text_opassword.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
          
        self.confirm_button = tk.Button(self.root, width=20, text="Processar", command=self.process_file)
        self.confirm_button.pack(pady=5)


    def toggle_input(self):
        if self.checkbox_var.get():
            self.text_upassword.delete(0, tk.END)
            self.text_upassword.config(state=tk.DISABLED)
        else:
            self.text_upassword.config(state=tk.NORMAL)


    def select_file(self):
        file_name = filedialog.askopenfilename(title="Selecione um documento")
        if file_name:
            self.text_file.delete(0, tk.END)
            self.text_file.insert(0, file_name)
        else:
            messagebox.showwarning("Aviso", "Nenhum documento foi selecionado!")

      
    def process_file(self):
        file = self.text_file.get()
        upass = self.text_upassword.get()
        opass = self.text_opassword.get()
        
        time.sleep(1)
        if not file.strip() or not opass.strip(): 
            messagebox.showwarning("Aviso", "Senha de usuário ou de dono ou documento não informado!")
        else:
            LockerFile(file,upass,opass)
            messagebox.showinfo("Aviso","Documento processado!")