import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

from utils.helpers import LoadIcon
from gui.comps.feat202_tagfile import LabelerFile


class TagFile:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de documentos")
        logo_icon = LoadIcon("app/gui/icons/logo.png")
        self.root.iconphoto(False, logo_icon)
        
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=0)

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(padx=20, pady=20)
        
        self.label = ttk.Label(self.frame, text="Documento para etiquetar:")
        self.label.grid(row=1, column=0, padx=10, pady=10)        
        self.text_file = ttk.Entry(self.frame,width=50)
        self.text_file.grid(row=2, column=0, sticky="ew", padx=5, pady=5)        
        self.button_file = ttk.Button(self.frame, width=3, text="...", command=self.select_file)
        self.button_file.grid(row=2, column=1, padx=5, pady=5)   
        
        self.label = ttk.Label(self.frame, text="Título da etiqueta:")
        self.label.grid(row=3, column=0, padx=10, pady=10)        
        self.text_title = ttk.Entry(self.frame,width=50)
        self.text_title.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.text_title.delete(0, tk.END)
        self.text_title.insert(0, "Documento 9, Anexo 9.99.99")
        
        self.label = ttk.Label(self.frame, text="Descrição da etiqueta:")
        self.label.grid(row=5, column=0, padx=10, pady=10)        
        self.text_description = ttk.Entry(self.frame,width=50)
        self.text_description.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
        self.text_description.delete(0, tk.END)
        self.text_description.insert(0, "Cópia de ...")
          
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
        title = self.text_title.get()
        description = self.text_description.get()
        file = self.text_file.get()
        
        if not title.strip() or not description.strip() or not file.strip():
            messagebox.showwarning( "Aviso", "Título, descrição ou documento não informado!")
        else:
            LabelerFile(title,description,file)
            messagebox.showinfo("Aviso","Documento processado!")

