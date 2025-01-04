import os
import traceback
import tkinter as Tk
from tkinter import filedialog

from app.utils.helpers import CreateNewName, ControlFile, DeleteFile
from app.utils.pdf import DecreasePdf, ConvertA4Pdf, CompressPdf, LockerPdf, LabelerPdf, RegisterPdf

def LabelerFile(key, title, description, input_filename, gray, numerator=False, decrease=False, a4format=False, protect=False, zip=False):
    output_filename = CreateNewName(input_filename, "(r2)")
    output_control_filename = output_filename.replace(".pdf", ".txt")

    temp_files = []
    try:
        with open(output_control_filename, 'w', encoding='utf-8') as log_file:
            log_file.write("Início do processamento.\n")
            log_file.write(f"Arquivo de entrada: {input_filename}\n")

            # Deletar arquivos de controle e saída anteriores
            DeleteFile(output_control_filename)
            log_file.write(f"Arquivo de controle {output_control_filename} deletado.\n")
            DeleteFile(output_filename)
            log_file.write(f"Arquivo de saída {output_filename} deletado.\n")

            if a4format:
                ControlFile("arquivo repaginado", output_control_filename)
                log_file.write("Repaginando para formato A4.\n")
                temp_a4_filename = CreateNewName(input_filename, "(a4)")
                ConvertA4Pdf(input_filename, temp_a4_filename)
                input_filename = temp_a4_filename
                temp_files.append(temp_a4_filename)

            ControlFile("arquivo registrado", output_control_filename)
            log_file.write("Registrando o arquivo.\n")
            temp_registered_filename = CreateNewName(input_filename, "(registered)")
            RegisterPdf(key, input_filename, temp_registered_filename, numerator)
            input_filename = temp_registered_filename
            temp_files.append(temp_registered_filename)

            if title != None:
                ControlFile("arquivo etiquetado", output_control_filename)
                log_file.write("Etiquetando o arquivo.\n")
                temp_labeled_filename = CreateNewName(input_filename, "(labeled)")
                LabelerPdf(title, description, input_filename, temp_labeled_filename, gray)
                input_filename = temp_labeled_filename
                temp_files.append(temp_labeled_filename)

            if decrease:
                ControlFile("arquivo reduzido", output_control_filename)
                log_file.write("Reduzindo o tamanho do arquivo.\n")
                temp_decreased_filename = CreateNewName(input_filename, "(decreased)")
                DecreasePdf(input_filename, temp_decreased_filename)
                input_filename = temp_decreased_filename
                temp_files.append(temp_decreased_filename)

            if protect:
                ControlFile("arquivo protegido", output_control_filename)
                log_file.write("Protegendo o arquivo.\n")
                temp_protected_filename = CreateNewName(input_filename, "(protected)")
                LockerPdf(input_filename, temp_protected_filename, "Girafa-Nao-Tem-Asa")
                input_filename = temp_protected_filename
                temp_files.append(temp_protected_filename)

            # Renomear o arquivo final antes da compactação
            final_output_filename = output_filename
            os.rename(input_filename, final_output_filename)
            log_file.write(f"Arquivo final gerado: {final_output_filename}\n")

            if zip:
                ControlFile("arquivo compactado", output_control_filename)
                log_file.write("Compactando o arquivo.\n")
                final_zip_filename = output_filename.replace(".pdf", ".zip")
                CompressPdf(final_output_filename, final_zip_filename)
                log_file.write(f"Arquivo zip gerado: {final_zip_filename}\n")

    except Exception as e:
        with open(output_control_filename, 'a', encoding='utf-8') as log_file:
            log_file.write(f"Erro ao processar o arquivo: {e}\n")
            log_file.write(traceback.format_exc())

    finally:
        # Deletar todos os arquivos temporários
        for temp_file in temp_files:
            if os.path.exists(temp_file):
                DeleteFile(temp_file)

        with open(output_control_filename, 'a', encoding='utf-8') as log_file:
            log_file.write("Arquivos temporários deletados.\n")
            log_file.write("Processamento concluído.\n")

    return