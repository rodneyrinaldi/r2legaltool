import sys
import os
import time
from datetime import datetime
import json
import tkinter as tk
import configparser
from PIL import Image, ImageTk

matriz = []
now = datetime.now()
date_sys = now.strftime("%Y/%m/%d %H:%M:%S")


def GetAppRoot():
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller cria uma pasta temporária e armazena o path em _MEIPASS
        return sys._MEIPASS
    else:
        # Quando rodando de forma interativa
        return os.path.dirname(os.path.abspath(__file__))
    

def JsonTuple(chave, valor):
    global matriz
    if chave == "" and valor == "":
        resultado_json = json.dumps(matriz)
        matriz = []
        return resultado_json
    else:
        matriz.append((chave, valor))


def LoadIcon(relative_path):
    try:
        absolute_path = os.path.join(os.path.dirname(__file__), relative_path)
        if not os.path.exists(absolute_path):
            raise FileNotFoundError(f"File not found: {absolute_path}")
        img = Image.open(absolute_path)
        return ImageTk.PhotoImage(img)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        raise
    except IOError as io_error:
        print(f"Error opening the image: {io_error}")
        raise


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


def CreateControl(file_path,new_control):
    try:
        if not file_path or not new_control:
            return None
        else:
            folder = os.path.dirname(file_path)
            new_path = os.path.join(folder, new_control)
            with open(new_path + ".json", 'w') as new_file:
                JsonTuple("Caminho",new_path)
                JsonTuple("Chave",new_control)
                JsonTuple("Data",date_sys)
                message = JsonTuple("","")
                new_file.write(message)
                print(f"Arquivo criado {new_control}!")
            new_file.close()
        return None
    except:
        return None


def ControlFile(flag, file_name):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Verifica se o arquivo existe na pasta root do programa
    if not os.path.isfile(file_name):
        # Cria o arquivo e escreve a flag
        with open(file_name, 'w') as file:
            file.write(flag + '\n')
    else:
        # Abre o arquivo existente e adiciona a flag ao final
        with open(file_name, 'a') as file:
            file.write(flag + '\n')








