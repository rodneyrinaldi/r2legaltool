import tkinter as tk
from tkinter import ttk, messagebox
import json
from app.utils.helpers import LoadIcon
import re

class OabTable:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabela de honorários da OABSP")
        logo_icon = LoadIcon("../images/logo.png")
        self.root.iconphoto(False, logo_icon)
        
        self.filter_var = tk.StringVar()
        self.search_index = 0
        
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        self.filter_frame = tk.Frame(self.root)
        self.filter_frame.pack(pady=10)
        
        tk.Label(self.filter_frame, text="Argumento:").pack(side=tk.LEFT, padx=5)
        self.filter_entry = tk.Entry(self.filter_frame, textvariable=self.filter_var)
        self.filter_entry.pack(side=tk.LEFT, padx=5)
        
        self.search_button = tk.Button(self.filter_frame, text="Buscar", command=self.search_next)
        self.search_button.pack(side=tk.LEFT, padx=5)
        
        self.filter_button = tk.Button(self.filter_frame, text="Filtrar", command=self.apply_filter)
        self.filter_button.pack(side=tk.LEFT, padx=5)
        
        self.copy_button = tk.Button(self.filter_frame, text="Copiar", command=self.copy_selected)
        self.copy_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = tk.Button(self.filter_frame, text="Recarregar", command=self.clear_filter)
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(self.tree_frame, columns=("col1", "col2", "col3", "col4"), show="headings")
        self.tree.heading("col1", text="Item", anchor=tk.W)
        self.tree.heading("col2", text="Atividade", anchor=tk.W)
        self.tree.heading("col3", text="Valores", anchor=tk.CENTER)
        self.tree.heading("col4", text="Porc.", anchor=tk.CENTER)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar_y = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar_y.set)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.scrollbar_x = ttk.Scrollbar(self.root, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscroll=self.scrollbar_x.set)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree.bind("<Configure>", self.adjust_columns)

    def adjust_columns(self, event):
        tree_width = self.tree.winfo_width()
        self.tree.column("col1", width=int(tree_width * 0.1), anchor=tk.W)
        self.tree.column("col2", width=int(tree_width * 0.6), anchor=tk.W)
        self.tree.column("col3", width=int(tree_width * 0.1), anchor=tk.CENTER)
        self.tree.column("col4", width=int(tree_width * 0.1), anchor=tk.CENTER)

    def load_data(self):
        try:
            with open("oabtable.json", "r", encoding="utf-8") as json_file:
                raw_data = json.load(json_file)
                if not isinstance(raw_data, list):
                    raise ValueError("O arquivo JSON deve conter uma lista.")
                self.data = [self.flatten_item(item) for sublist in raw_data for item in sublist if isinstance(item, dict)]
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

    def flatten_item(self, item):
        flattened_item = {k: v.replace('\n', ' ') if isinstance(v, str) else v for k, v in item.items()}
        if not flattened_item.get("Atividade"):
            flattened_item["Atividade"] = flattened_item.get("Item", "")
            flattened_item["Item"] = ""
        if not flattened_item.get("Item") and re.match(r'^\d+\.?\d*', flattened_item.get("Atividade", "")):
            match = re.match(r'^(\d+\.?\d*)\s*(.*)', flattened_item["Atividade"])
            if match:
                flattened_item["Item"] = match.group(1)
                flattened_item["Atividade"] = match.group(2)
        return flattened_item

    def display_data(self, data):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for item in data:
            self.tree.insert("", tk.END, values=(
                item.get("Item", ""), 
                item.get("Atividade", ""), 
                item.get("Valor", ""), 
                item.get("%", "")
            ))

    def apply_filter(self):
        filtered_data = [item for item in self.data if self.filter_var.get().lower() in item.get("Atividade", "").lower()]
        self.display_data(filtered_data)

    def clear_filter(self):
        self.filter_var.set("")
        self.display_data(self.data)

    def copy_selected(self):
        selected_items = self.tree.selection()
        selected_data = [self.tree.item(item, "values") for item in selected_items]
        self.root.clipboard_clear()
        for item in selected_data:
            self.root.clipboard_append("\t".join(item) + "\n")

    def search_next(self):
        search_text = self.filter_var.get().lower()
        children = self.tree.get_children()
        for i in range(self.search_index, len(children)):
            item = self.tree.item(children[i])
            if search_text in item['values'][1].lower():
                self.tree.selection_set(children[i])
                self.tree.see(children[i])
                self.search_index = i + 1
                return
        messagebox.showinfo("Busca", "Nenhuma outra ocorrência encontrada.")
        self.search_index = 0
