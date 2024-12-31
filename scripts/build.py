import os
import subprocess

# Define o diretório principal
# project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# command = f"pyinstaller --onefile --windowed {os.path.join(project_dir, 'app', 'main.py')}"

# Comando para criar o executável com PyInstaller
command = f"pyinstaller --onefile --windowed --add-data {'app/images/logo.png;app/images'} --add-data {'app/resources/label1.pdf;app/resources'} --add-data {'app/resources/label2.pdf;app/resources'} {'r2legaltool.py'}"

# Executa o comando
subprocess.run(command, shell=True)


# pyinstaller --onefile 
# --add-data "images/imagem1.png;images" 
# --add-data "pdfs/arquivo1.pdf;pdfs" 
# main.py
