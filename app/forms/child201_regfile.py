import os
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import uuid

from app.utils.helpers import LoadIcon, CreateControl, JsonTuple
from app.processing.feat201_regfile import RegisterFile
from app.utils.pdf import DecreasePdf, ConvertA4Pdf, CompressPdf, LockerPdf


class RegFile:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de documentos")
        logo_icon = LoadIcon("../images/logo.png")
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

        self.button_key = ttk.Button(self.frame, width=3, text="-", command=self.set_uuid)
        self.button_key.grid(row=4, column=2, padx=5, pady=5) 

        self.button_key = ttk.Button(self.frame, width=3, text="=", command=self.set_uuid)
        self.button_key.grid(row=4, column=3, padx=5, pady=5)

        self.frame2 = ttk.Frame(self.root, padding=10)
        self.frame2.pack(padx=20, pady=5)
        
        self.checkbox_var = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.frame2, text="Numerar páginas", variable=self.checkbox_var, command=self.toggle_input)
        self.checkbox.grid(row=2, column=0, padx=5)
        
        self.checkbox_file = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.frame2, text="Gerar arquivo uui", variable=self.checkbox_file, command=self.toggle_input)
        self.checkbox.grid(row=2, column=1, padx=5)
        
        self.checkbox_decrease = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.frame2, text="Reduzir arquivo", variable=self.checkbox_decrease, command=self.toggle_input)
        self.checkbox.grid(row=2, column=2, padx=5)
        
        self.checkbox_a4format = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.frame2, text="Formatar A4 arquivo", variable=self.checkbox_a4format, command=self.toggle_input)
        self.checkbox.grid(row=3, column=0, padx=5)
        
        self.checkbox_prot = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.frame2, text="Proteger arquivo", variable=self.checkbox_prot, command=self.toggle_input)
        self.checkbox.grid(row=3, column=1, padx=5)
        
        self.checkbox_zip = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.frame2, text="Compactar arquivo", variable=self.checkbox_zip, command=self.toggle_input)
        self.checkbox.grid(row=3, column=2, padx=5)
          
        self.confirm_button = tk.Button(self.root, width=20, text="Processar", command=self.process_file)
        self.confirm_button.pack(pady=5)


    def toggle_input(self):
        if self.checkbox_var.get():
            return
        else:
            return


    def set_uuid(self):
        resposta = messagebox.askyesno("Confirmação", "Confirma nova chave de registro?")
        if resposta:
            new_uuid = str(uuid.uuid4())
            self.text_key.delete(0, tk.END)
            self.text_key.insert(0, new_uuid)
            file_path = self.text_file.get()
            CreateControl(file_path,new_uuid)
        else:
            print("Operação cancelada.")


    def select_file(self):
        file_name = filedialog.askopenfilename(title="Selecione um documento", filetypes=[("PDF files", "*.pdf")])
        if file_name:
            self.text_file.delete(0, tk.END)
            self.text_file.insert(0, file_name)
        else:
            messagebox.showwarning("Aviso", "Nenhum documento foi selecionado!")

    
    def process_file(self):
        key = self.text_key.get()
        file = self.text_file.get()
        numerator = self.checkbox_var.get()
        decrease = self.checkbox_decrease.get()
        a4format = self.checkbox_a4format.get()
        protect = self.checkbox_prot.get()
        zip = self.checkbox_zip.get()
        if not key.strip() or not file.strip(): 
            messagebox.showwarning( "Aviso", "Chave ou documento não informado!")
        else:
            RegisterFile(key,file,numerator,decrease,a4format,protect,zip)
            messagebox.showinfo("Aviso","Documento processado!")
