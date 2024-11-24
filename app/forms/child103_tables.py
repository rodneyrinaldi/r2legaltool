import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import threading

from app.utils.helpers import LoadIcon
from app.processing.feat103_oabtable import ReadOabTable

class Tables:
    def __init__(self, root):        
        self.root = root
        self.root.title("Importador de honorários advocatícios")
        logo_icon = LoadIcon("../images/logo.png")
        self.root.iconphoto(False, logo_icon)

                
        self.status_label = tk.Label(root, text="Importação da tabela de honorários da OAB SP:")
        self.status_label.pack(pady=10)
        
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)
        
        self.status_label = tk.Label(root, text="Status: Aguardando...")
        self.status_label.pack(pady=10)
        
        self.button = tk.Button(root, text="Iniciar Processamento", command=self.toggle_process)
        self.button.pack(pady=10)
        
        self.processing = False
        self.thread = None

    def toggle_process(self):
        if self.processing:
            self.processing = False
            self.button.config(text="Iniciar Processamento")
        else:
            self.processing = True
            self.button.config(text="Cancelar Processamento")
            self.thread = threading.Thread(target=self.open_pdf)
            self.thread.start()

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        if file_path:
            ReadOabTable(file_path, self.update_progress, self.check_processing, self.update_status, self.processing_complete)

    def update_progress(self, value):
        self.progress["value"] = value
        self.root.update_idletasks()

    def update_status(self, current, total):
        self.status_label.config(text=f"Processando linha {current} de {total}")
        self.root.update_idletasks()

    def processing_complete(self):
        self.processing = False
        self.button.config(text="Iniciar Processamento")
        self.progress["value"] = 0
        self.status_label.config(text="Status: Processamento concluído")
        messagebox.showinfo("Concluído", "O processamento foi concluído com sucesso!")
        self.root.config(cursor="")

    def check_processing(self):
        return self.processing
