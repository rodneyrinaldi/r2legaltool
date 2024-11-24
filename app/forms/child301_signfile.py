import time
from datetime import date
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import uuid

from app.utils.helpers import LoadIcon
from app.processing.feat301_signfile import SignerFile


class SignFile:
    def __init__(self, root):
        self.root = root
        self.root.title("Assinatura digital de documentos")
        logo_icon = LoadIcon("../images/logo.png")
        self.root.iconphoto(False, logo_icon)
        
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=0)

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(padx=20, pady=20)
        
        self.label = ttk.Label(self.frame, text="Documento para assinatura:")
        self.label.grid(row=1, column=0, padx=10, pady=10)        
        self.text_file = ttk.Entry(self.frame,width=50)
        self.text_file.grid(row=2, column=0, sticky="ew", padx=5, pady=5)        
        self.button_file = ttk.Button(self.frame, width=3, text="...", command=self.select_file)
        self.button_file.grid(row=2, column=1, padx=5, pady=5)   
          
        self.confirm_button = tk.Button(self.root, width=20, text="Processar", command=self.process_file)
        self.confirm_button.pack(pady=5)


    def select_file(self):
        file_name = filedialog.askopenfilename(title="Selecione um documento")
        if file_name:
            self.text_file.delete(0, tk.END)
            self.text_file.insert(0, file_name)
        else:
            messagebox.showwarning("Aviso", "Nenhum documento foi selecionado!")

      
    def process_file(self):
        new_uuid = str(uuid.uuid4())
        file = self.text_file.get()
        
        time.sleep(1)
        if not file.strip(): 
            messagebox.showwarning("Aviso", "Senha de usuário ou de dono ou documento não informado!")
        else:
            SignerFile(new_uuid,file)
            messagebox.showinfo("Aviso","Documento processado!")