import os
import time
import tkinter as tk
import pymupdf

from app.utils.helpers import CreateNewName


def RegisterFile(secure_key, input_filename, print_page_numbers=False,decrease=False,a4format=False,protect=False,zip=False):
    output_filename = CreateNewName(input_filename, "(reg)")
    input_file = pymupdf.open(input_filename)
    total_pages = len(input_file)  # Get the total number of pages

    for page_number, page in enumerate(input_file, start=1):
        left_margin = 10
        page_width = page.rect.width
        page_height = page.rect.height
        pos_x = left_margin
        pos_y = page_height / 2

        # Text to be inserted
        text_to_insert = secure_key
        if print_page_numbers:
            text_to_insert += f"    {page_number} de {total_pages}"

        page.insert_text((pos_x, pos_y), text_to_insert, fontname="helv", fontsize=8, rotate=90, color=(0.7, 0.7, 0.7))

    input_file.save(output_filename)
    input_file.close()

    return output_filename
