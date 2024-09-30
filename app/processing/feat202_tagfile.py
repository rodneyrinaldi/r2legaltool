import os
import time
import tkinter as Tk
from tkinter import filedialog
import pymupdf
from PyPDF2 import PdfReader, PdfWriter

from app.utils.helpers import CreateNewName,DeleteFile
from app.processing.feat201_regfile import RegisterFile


def LabelerFile(key,title,description,input_filename,gray=True):
    current_directory = os.path.dirname(os.path.abspath(__file__))

    if key:
        input_filename = RegisterFile(key,input_filename)
        time.sleep(2)
        output_filename = CreateNewName(input_filename,"(etiq)")
    else:
        output_filename = CreateNewName(input_filename,"(etiq)")

    if gray:
        label_filename =  pymupdf.open(current_directory + "\\label1.pdf")  
    else:
        label_filename =  pymupdf.open(current_directory + "\\label2.pdf")  

    output_file = pymupdf.open(label_filename)
    for pagina in output_file:
        margem_esquerda = 10  
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
    if key:
        DeleteFile(input_filename)

    return(output_filename)


