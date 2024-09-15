import os
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from dotenv import load_dotenv

def LoadIcon(path):
    # Carrega a imagem usando tkinter
    icon = tk.PhotoImage(file=path)
    return icon


def GetSecretKey(key):
    path_env = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(path_env)
    secret_key = os.getenv(key)
    if secret_key:
        return secret_key
    else:
        raise ValueError("A chave secreta não foi encontrada no arquivo .env")


def CreateNewName(file_name,tag_name):
    file_name, extensao = os.path.splitext(file_name)
    return f"{file_name}{tag_name}{extensao}"


def DeleteFile(caminho_arquivo,message=False):
    try:
        os.remove(caminho_arquivo)
        if message: print(f"Arquivo {caminho_arquivo} apagado com sucesso.")
    except FileNotFoundError:
        if message: print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
    except PermissionError:
        if message: print(f"Erro: Sem permissão para apagar o arquivo {caminho_arquivo}.")
    except Exception as e:
        if message: print(f"Ocorreu um erro ao tentar apagar o arquivo: {e}")


def RenameFile(path_file_name, new_file_name, message=True):
    try:
        if not path_file_name or not new_file_name:
            raise ValueError("Os nomes dos arquivos não podem estar vazios.")
        os.rename(path_file_name, new_file_name)
        if message:
            print(f"Arquivo renomeado com sucesso para {new_file_name}")
    except FileNotFoundError:
        if message:
            print(f"Erro: O arquivo {path_file_name} não foi encontrado.")
    except PermissionError:
        if message:
            print(f"Erro: Sem permissão para renomear o arquivo {path_file_name}.")
    except ValueError as ve:
        if message:
            print(f"Erro: {ve}")
    except Exception as e:
        if message:
            print(f"Ocorreu um erro ao tentar renomear o arquivo: {e}")




