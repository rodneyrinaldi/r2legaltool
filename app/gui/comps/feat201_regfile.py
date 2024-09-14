import os
import time
import tkinter as tk
import pymupdf

from utils.helpers import CreateNewName


def RegisterFile(secure_key,input_filename):
    output_filename = CreateNewName(input_filename,"(reg)")
    print(output_filename)
    input_file = pymupdf.open(input_filename)   
    
    for pagina in input_file:
        margem_esquerda = 10  
        largura_pagina = pagina.rect.width
        altura_pagina = pagina.rect.height
        pos_x = margem_esquerda
        pos_y = altura_pagina / 2
        pagina.insert_text((pos_x, pos_y), secure_key, fontname="helv", fontsize=8, rotate=90, color=(0.7, 0.7, 0.7))

    input_file.save(output_filename)
    input_file.close()

    return(output_filename)