import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import uuid

from utils.helpers import LoadIcon
from gui.comps.feat201_regfile import RegisterFile


class RegFile:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de documentos")
        logo_icon = LoadIcon("app/gui/icons/logo.png")
        self.root.iconphoto(False, logo_icon)
        
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=0)

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(padx=20, pady=20)
        
        self.label = ttk.Label(self.frame, text="Documento para registro:")
        self.label.grid(row=1, column=0, padx=10, pady=10)        
        self.text_file = ttk.Entry(self.frame,width=50)
        self.text_file.grid(row=2, column=0, sticky="ew", padx=5, pady=5)        
        self.button_file = ttk.Button(self.frame, width=3, text="...", command=self.select_file)
        self.button_file.grid(row=2, column=1, padx=5, pady=5)   
        
        self.label = ttk.Label(self.frame, text="Chave de registro:")
        self.label.grid(row=3, column=0, padx=10, pady=10)        
        self.text_key = ttk.Entry(self.frame,width=50)
        self.text_key.grid(row=4, column=0, sticky="ew", padx=5, pady=5)        
        self.button_key = ttk.Button(self.frame, width=3, text="+", command=self.set_uuid)
        self.button_key.grid(row=4, column=1, padx=5, pady=5)   
        self.button_key = ttk.Button(self.frame, width=3, text="=", command=self.set_uuid)
        self.button_key.grid(row=4, column=2, padx=5, pady=5)
          
        self.confirm_button = tk.Button(self.root, width=20, text="Processar", command=self.process_file)
        self.confirm_button.pack(pady=5)


    def set_uuid(self):
        resposta = messagebox.askyesno("Confirmação", "Confirma nova chave de registro?")
        if resposta:
            new_uuid = str(uuid.uuid4())
            self.text_key.delete(0, tk.END)
            self.text_key.insert(0, new_uuid)
        else:
            print("Operação cancelada.")


    def select_file(self):
        file_name = filedialog.askopenfilename(title="Selecione um documento")
        if file_name:
            self.text_file.delete(0, tk.END)
            self.text_file.insert(0, file_name)
        else:
            messagebox.showwarning("Aviso", "Nenhum documento foi selecionado!")

      
    def process_file(self):
        key = self.text_key.get()
        file = self.text_file.get()
        
        if not key.strip() or not file.strip(): 
            messagebox.showwarning( "Aviso", "Chave ou documento não informado!")
        else:
            RegisterFile(key,file)
            messagebox.showinfo("Aviso","Documento processado!")