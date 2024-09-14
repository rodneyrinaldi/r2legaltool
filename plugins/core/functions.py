import tkinter as tk
import sys
import os
import pickle


class Functions:
    def close(self):
        print("Sistema fechado")
        self.quit()


    def registerdocs():
        print("Documento registrado")


    def tagdocs():
        print("Documento etiquetado")


    def sobre():
        print("Sobre o Legal Office")


    def refresh(self):
        print("Refresh pressionado")   
        
        def deletar_arquivo(caminho_arquivo):
            try:
                os.remove(caminho_arquivo)
                print(f"Arquivo {caminho_arquivo} deletado com sucesso.")
            except FileNotFoundError:
                print(f"O arquivo {caminho_arquivo} não foi encontrado.")
            except PermissionError:
                print(f"Permissão negada para deletar o arquivo {caminho_arquivo}.")
            except Exception as e:
                print(f"Ocorreu um erro ao deletar o arquivo: {e}")

        deletar_arquivo("last_folder.pkl")

    def unit(self):
        print("Unit pressionado")

        unidades = [f"{d}:\\" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
        popup = tk.Toplevel()
        popup.title("Escolher Unidade de Disco")
        
        label = tk.Label(popup, text="Escolha uma unidade de disco:")
        label.pack(pady=10)
        
        lista_unidades = tk.Listbox(popup)
        for unidade in unidades:
            lista_unidades.insert(tk.END, unidade)
        lista_unidades.pack(pady=10)
        
        def selecionar_unidade():
            unidade_selecionada = lista_unidades.get(tk.ACTIVE)
            listar_pastas(self.tree, unidade_selecionada)
            popup.destroy()        
            btn_selecionar = tk.Button(popup, text="Selecionar", command=selecionar_unidade)
            btn_selecionar.pack(pady=10)

            def listar_pastas(tree, caminho):
                for item in tree.get_children():
                    tree.delete(item)
                for pasta in os.listdir(caminho):
                    if os.path.isdir(os.path.join(caminho, pasta)):
                        tree.insert('', 'end', text=pasta, values=(pasta,))