import os
import subprocess

# Define o diretório principal
# project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# command = f"pyinstaller --onefile --windowed {os.path.join(project_dir, 'app', 'main.py')}"

# Comando para criar o executável com PyInstaller
command = f"pyinstaller --onefile --windowed {'main.py'}"

# Executa o comando
subprocess.run(command, shell=True)
