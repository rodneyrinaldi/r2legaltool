import os
import tkinter as tk
import configparser

# def LoadIcon(rel_path):
#     script_dir = os.path.dirname(__file__)
#     abs_file_path = os.path.join(script_dir, rel_path)
#     icon = tk.PhotoImage(file=abs_file_path)
#     return icon


def LoadIcon(rel_path):
    script_dir = os.path.dirname(__file__) 
    abs_file_path = os.path.join(script_dir, rel_path)   
    try:
        icon = tk.PhotoImage(file=abs_file_path)
        return icon
    except tk.TclError as e:        
        try:
            icon = tk.PhotoImage(file=rel_path)
            return icon
        except tk.TclError as e:
            print(f"Erro ao carregar o ícone: {e}")
            return None
        print(f"Erro ao carregar o ícone: {e}")
        return None


def GetSecretKey(section, key):
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        value = config[section][key]
        return value
    except KeyError:
        return None


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




