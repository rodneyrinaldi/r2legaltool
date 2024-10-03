import os
import json
import tkinter as tk
from tkinter import ttk, messagebox

from app.utils.helpers import LoadIcon

class Folders:
    def __init__(self, root):
        self.root = root
        self.root.title("Explorador de pasta de arquivos")
        logo_icon = LoadIcon("app/images/logo.png")
        self.root.iconphoto(False, logo_icon)
        
        # self.selected_files = []
        # self.last_folder = self.load_last_folder()

        # Barra de ferramentas
        self.toolbar = tk.Frame(self.root, bg="lightgray")
        self.toolbar.pack(side="top", fill="x")

        # # Botão para adicionar etiqueta
        # self.show_names_button = tk.Button(self.toolbar, text="Adicionar controle", command=self.show_file_names)
        # self.show_names_button.pack(side="left", padx=2, pady=2)

        # # Botão para mostrar tamanhos
        # self.show_sizes_button = tk.Button(self.toolbar, text="Selecionar controle", command=self.show_file_sizes)
        # self.show_sizes_button.pack(side="left", padx=2, pady=2)

        # # Botão para mostrar tamanhos
        # self.show_sizes_button = tk.Button(self.toolbar, text="Deselecionar controle", command=self.show_file_sizes)
        # self.show_sizes_button.pack(side="left", padx=2, pady=2)

        # Botão para alternar filtro
        self.filter_var = tk.BooleanVar(value=True)  
        self.toggle_filter_button = tk.Button(self.toolbar, text="Desativar Filtro", command=self.toggle_filter)
        self.toggle_filter_button.pack(side="left", padx=2, pady=2)

        self.tree = ttk.Treeview(self.root, selectmode="extended")
        self.tree.pack(fill=tk.BOTH, expand=True)  

        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscroll=self.scrollbar.set)

        self.tree.heading("#0", text="Explorador de Arquivos", anchor="w")
        # initial_folder = self.last_folder if self.last_folder else os.path.expanduser("~")
        # self.populate_tree(initial_folder)
        self.tree.bind("<Double-1>", self.on_double_click)


    def populate_tree(self, path, parent=''):
        try:
            for entry in os.listdir(path):
                full_path = os.path.join(path, entry)
                is_dir = os.path.isdir(full_path)

                # Aplicar filtro de arquivos
                if not is_dir and self.filter_var.get():
                    if not entry.lower().endswith(('.pdf', '.doc', '.docx')):
                        continue

                node = self.tree.insert(parent, "end", text=entry, open=False, values=[full_path])
                if is_dir:
                    self.tree.insert(node, "end")
        except PermissionError:
            pass

    def toggle_filter(self):
        if self.filter_var.get():
            self.filter_var.set(False)
            self.toggle_filter_button.config(text="Ativar Filtro")
        else:
            self.filter_var.set(True)
            self.toggle_filter_button.config(text="Desativar Filtro")
        self.refresh_tree()

    def refresh_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        # initial_folder = self.last_folder if self.last_folder else os.path.expanduser("~")
        # self.populate_tree(initial_folder)

    def on_double_click(self, event):
        item = self.tree.selection()[0]
        item_path = self.tree.item(item, "values")[0]

        if os.path.isdir(item_path):
            if self.tree.get_children(item):
                self.tree.delete(*self.tree.get_children(item)) 
            else:
                self.populate_tree(item_path, item)
            self.save_last_folder(item_path)
        else:
            if item_path in self.selected_files:
                self.selected_files.remove(item_path)
                self.tree.selection_remove(item)
            else:
                self.selected_files.append(item_path)
                messagebox.showinfo("Arquivo Selecionado", f"{os.path.basename(item_path)} foi selecionado.")
                self.root.control_name = item_path

    def show_file_names(self):
        if not self.selected_files:
            messagebox.showwarning("Nenhum arquivo", "Nenhum arquivo foi selecionado.")
            return
        file_names = [os.path.basename(file) for file in self.selected_files]
        messagebox.showinfo("Etiqueta adicionada", "\n".join(file_names))


    def show_file_sizes(self):
        if not self.selected_files:
            messagebox.showwarning("Nenhum arquivo", "Nenhum arquivo foi selecionado.")
            return
        file_sizes = [f"{os.path.basename(file)}: {os.path.getsize(file)} bytes" for file in self.selected_files]
        messagebox.showinfo("Tamanhos dos Arquivos", "\n".join(file_sizes))

    # def load_last_folder(self):
        # """Carrega o nome da última pasta explorada do arquivo config.json."""
        # if os.path.exists(self.CONFIG_FILE):
        #     with open(self.CONFIG_FILE, "r") as f:
        #         config = json.load(f)
        #         return config.get("last_folder", None)
        # return None

    # def save_last_folder(self, folder_path):
    #     with open(self.CONFIG_FILE, "w") as f:
    #         json.dump({"last_folder": folder_path}, f)











    def show_message(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_text = self.tree.item(selected_item, "text")
            messagebox.showinfo("Selected Item", item_text)
        else:
            messagebox.showwarning("Warning", "No item selected")

        
