import os
import shutil
import sys
import argparse
import tkinter as tk
from tkinter import messagebox

def relocate_and_delete_self():
    # Determina o caminho da pasta de programas do sistema operacional
    if os.name == 'nt':  # Windows
        program_files = os.environ.get('ProgramFiles', 'C:\\Program Files')
    else:  # Unix/Linux/Mac
        program_files = '/usr/local/bin'

    # Cria a pasta r2legaltools
    target_dir = os.path.join(program_files, 'r2legaltools')

    # Solicita autorização ao usuário
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    if not messagebox.askyesno("Authorization Required", f"Do you allow the creation of the folder '{target_dir}'?"):
        sys.exit("Operation cancelled by the user.")

    os.makedirs(target_dir, exist_ok=True)

    # Caminho do script atual
    current_script = os.path.abspath(sys.argv[0])

    # Caminho de destino para copiar o script
    target_script = os.path.join(target_dir, os.path.basename(current_script))

    # Copia o script para a nova pasta
    shutil.copy2(current_script, target_script)

    # Apaga o script original
    os.remove(current_script)

    # Encerra a instância do script
    sys.exit()

# Chama a função
# relocate_and_delete_self()
