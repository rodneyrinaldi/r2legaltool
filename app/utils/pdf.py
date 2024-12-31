import os
import zipfile
import pymupdf
import fitz  # PyMuPDF

from PyPDF2 import PdfReader, PdfWriter
from app.utils.helpers import CreateNewName, GetAppRoot, GetResourcesRoot


def DecreasePdf(input_filename, output_filename):
    try:
        document = fitz.open(input_filename)
        document.save(
            output_filename,
            garbage=4,      # Remove objetos não referenciados
            deflate=True,   # Compressão zlib sem perda de qualidade
            clean=True,     # Remove entradas de tabela xref não usadas
            incremental=False,  # Salva o documento de forma não incremental
            encryption=0        # Sem encriptação
        )
        document.close()
        return output_filename
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {input_filename}")
    except PermissionError:
        print(f"Sem permissão para ler/escrever o arquivo: {input_filename}")
    except Exception as e:
        print(f"Ocorreu um erro ao comprimir o arquivo: {e}")
    return


def ConvertA4Pdf(input_filename, output_filename):
    if not os.path.exists(input_filename):
        print(f"Arquivo não encontrado: {input_filename}")
        return None
    try:
        a4_width = 595  # Largura da página A4
        a4_height = 842  # Altura da página A4
        with fitz.open(input_filename) as document, fitz.open() as new_document:
            for page_num in range(len(document)):
                page = document.load_page(page_num)
                rect = page.rect
                # Determinar a orientação da página original
                if rect.width > rect.height:  # Página em paisagem
                    new_page_width, new_page_height = a4_height, a4_width
                else:  # Página em retrato
                    new_page_width, new_page_height = a4_width, a4_height
                # Criar uma nova página com a mesma orientação
                new_page = new_document.new_page(width=new_page_width, height=new_page_height)
                # Calcular a escala para redimensionar proporcionalmente
                scale = min(new_page_width / rect.width, new_page_height / rect.height)
                # Calcular as margens para centralizar o conteúdo
                translate_x = (new_page_width - rect.width * scale) / 2
                translate_y = (new_page_height - rect.height * scale) / 2
                # Ajustar a posição e tamanho do conteúdo original na nova página
                transformed_rect = fitz.Rect(
                    translate_x,
                    translate_y,
                    translate_x + rect.width * scale,
                    translate_y + rect.height * scale
                )
                # Copiar o conteúdo da página original para a nova página
                new_page.show_pdf_page(transformed_rect, document, page_num)
            # Salvar o documento final
            new_document.save(output_filename, garbage=4, deflate=True, clean=True)
        print(f"Arquivo convertido com sucesso: {output_filename}")
        return output_filename
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {input_filename}")
    except PermissionError:
        print(f"Sem permissão para ler/escrever o arquivo: {input_filename} ou {output_filename}")
    except Exception as e:
        print(f"Ocorreu um erro ao converter o arquivo: {e}")
    return


def CompressPdf(input_filename, output_filename):
    try:
        with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(input_filename, os.path.basename(input_filename))
        
        return output_filename
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {input_filename}")
    except PermissionError:
        print(f"Sem permissão para ler/escrever o arquivo: {input_filename}")
    except Exception as e:
        print(f"Ocorreu um erro ao compactar o arquivo: {e}")
    return None


def LockerPdf(input_filename, output_filename, o_password, u_password=""):
    permission = 4 #PRINT constant permission
    reader = PdfReader(input_filename)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    if o_password != "":
        writer.encrypt(user_password=u_password, owner_password=o_password,permissions_flag=permission)
    else:
        writer.encrypt(user_password=u_password, permissions_flag=permission)
    with open(output_filename, "wb") as output_file:
        writer.write(output_filename)
    writer.close()
    return(output_filename)


def RegisterPdf(secure_key, input_filename, output_filename, print_page_numbers=False):
    input_file = pymupdf.open(input_filename)
    total_pages = len(input_file) 
    for page_number, page in enumerate(input_file, start=1):
        left_margin = 10
        page_width = page.rect.width
        page_height = page.rect.height
        pos_x = left_margin
        pos_y = page_height / 2
        text_to_insert = secure_key
        if print_page_numbers:
            text_to_insert += f"    {page_number} de {total_pages}"
        page.insert_text((pos_x, pos_y), text_to_insert, fontname="helv", fontsize=8, rotate=90, color=(0.7, 0.7, 0.7))
    input_file.save(output_filename)
    input_file.close()
    return


def LabelerPdf(title, description, input_filename, output_filename, gray):
    if gray:
        current_directory = GetResourcesRoot() + "label1.pdf"
    else:
        current_directory = GetResourcesRoot() + "label2.pdf"
    label_file =  pymupdf.open(current_directory)  
    output_file = pymupdf.open(label_file)
    for pagina in output_file:
        largura_pagina = pagina.rect.width 
        altura_pagina = pagina.rect.height
        pos_x = (largura_pagina - 0) / 2
        pos_y = altura_pagina / 2
        font = pymupdf.Font("helv")
        largura_texto = font.text_length(title,14)
        pagina.insert_text((pos_x-(largura_texto/2), pos_y-5), title, fontname="helv", fontsize=14, color=(0, 0, 0))
        largura_texto = font.text_length(description,12)
        pagina.insert_text((pos_x-(largura_texto/2), pos_y+15), description, fontname="helv", fontsize=12, color=(0, 0, 0))
    output_file.save(output_filename)
    output_file.close()
    input_file = pymupdf.open(input_filename) 
    output_file = pymupdf.open(output_filename)  
    pdf_combined = pymupdf.open()
    for page_num in range(len(output_file)):
        pdf_combined.insert_pdf(output_file, from_page=page_num, to_page=page_num)
    for page_num in range(len(input_file)):
        pdf_combined.insert_pdf(input_file, from_page=page_num, to_page=page_num)
    input_file.close()
    output_file.close()
    pdf_combined.save(output_filename)
    pdf_combined.close()
    return




