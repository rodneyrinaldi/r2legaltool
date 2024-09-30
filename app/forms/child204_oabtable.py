import tkinter as tk
from tkinter import ttk, messagebox
import json

from app.utils.helpers import LoadIcon

class OabTable:
    def __init__(self, root):
        self.root = root
        self.root.title("Assinatura digital de documentos")
        logo_icon = LoadIcon("app/images/logo.png")
        self.root.iconphoto(False, logo_icon)
        
        self.filter_var = tk.StringVar()
        
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        self.filter_frame = tk.Frame(self.root)
        self.filter_frame.pack(pady=10)
        
        tk.Label(self.filter_frame, text="Filtro:").pack(side=tk.LEFT, padx=5)
        self.filter_entry = tk.Entry(self.filter_frame, textvariable=self.filter_var)
        self.filter_entry.pack(side=tk.LEFT, padx=5)
        
        self.filter_button = tk.Button(self.filter_frame, text="Filtrar", command=self.apply_filter)
        self.filter_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = tk.Button(self.filter_frame, text="Limpar Filtro", command=self.clear_filter)
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.copy_button = tk.Button(self.filter_frame, text="Copiar Selecionados", command=self.copy_selected)
        self.copy_button.pack(side=tk.LEFT, padx=5)
        
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(self.tree_frame, columns=("col1", "col2", "col3", "col4"), show="headings")
        self.tree.heading("col1", text="Coluna 1")
        self.tree.heading("col2", text="Coluna 2")
        self.tree.heading("col3", text="Coluna 3")
        self.tree.heading("col4", text="Coluna 4")
        
        self.tree.column("col1", width=100)  # Largura da coluna 1
        self.tree.column("col2", width=100)  # Largura da coluna 2
        self.tree.column("col3", width=5)  # Largura da coluna 3
        self.tree.column("col4", width=5)  # Largura da coluna 4
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar_y = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar_y.set)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.scrollbar_x = ttk.Scrollbar(self.root, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscroll=self.scrollbar_x.set)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    def load_data(self):
        try:
            with open("oabtable.json", "r", encoding="utf-8") as json_file:
                raw_data = json.load(json_file)
                if not isinstance(raw_data, list):
                    raise ValueError("O arquivo JSON deve conter uma lista.")
                # Desaninhando listas internas
                self.data = [item for sublist in raw_data for item in sublist if isinstance(item, dict)]
                if not self.data:
                    raise ValueError("Nenhum item válido encontrado no arquivo JSON.")
            self.display_data(self.data)
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo oabtable.json não encontrado.")
            self.data = []
        except json.JSONDecodeError:
            messagebox.showerror("Erro", "Erro ao decodificar o arquivo JSON.")
            self.data = []
        except ValueError as e:
            messagebox.showerror("Erro", f"Erro no formato dos dados: {e}")
            self.data = []
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")
            self.data = []

    def display_data(self, data):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for item in data:
            self.tree.insert("", tk.END, values=(
                item.get("1 ATIVIDADES AVULSAS OU EXTRAJUDICIAIS", "N/A"), 
                item.get("Unnamed: 0", "N/A"), 
                item.get("Valores mínimos", "N/A"), 
                item.get("Percentuais", "N/A")
            ))

    def apply_filter(self):
        filter_text = self.filter_var.get().lower()
        if not filter_text:
            self.display_data(self.data)
        else:
            filtered_data = [
                item for item in self.data 
                if any(filter_text in str(value).lower() for value in item.values() if value)
            ]
            self.display_data(filtered_data)
            if not filtered_data:
                messagebox.showinfo("Informação", "Nenhum resultado encontrado para o filtro aplicado.")

    def clear_filter(self):
        self.filter_var.set("")
        self.display_data(self.data)

    def copy_selected(self):
        selected_items = self.tree.selection()
        selected_data = [self.tree.item(item, "values") for item in selected_items]
        self.root.clipboard_clear()
        for item in selected_data:
            self.root.clipboard_append("\t".join(item) + "\n")
        messagebox.showinfo("Copiado", "Conteúdo copiado para a área de transferência")
