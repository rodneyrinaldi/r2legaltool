import time
from datetime import datetime
import pymupdf
from PyPDF2 import PdfReader, PdfWriter

from utils.helpers import CreateNewName
from gui.comps.feat201_regfile import RegisterFile
from gui.comps.feat203_lockfile import LockerFile


def SignerFile(uuid_key,input_filename):    
    upassword = ""
    opassword = "senhatemporaria"  
    register_key = "xxxxxxxx-9999-xxxx-9999-xxxxxxxxxxxxxxxx"
    print(input_filename)
    wip_filename = RegisterFile(register_key,input_filename)
    print(wip_filename)
    time.sleep(1)
    wip_filename = NotifierFile(uuid_key,wip_filename)
    print(wip_filename)
    time.sleep(1)
    wip_filename = LockerFile(wip_filename,upassword,opassword)
    print(wip_filename)



def NotifierFile(uuid_key,wip_filename):
    output_filename = CreateNewName(wip_filename,"(inf)")
    
    now = datetime.now()
    data = now.strftime("%Y/%m/%d %H:%M:%S")
    message = "Documento (protegido) produzido por Rodney Rinaldi Advogado \n\n" 
    message += "Processamento: " + data + "\n" + "Chave de segurança: " + uuid_key + "\n"
    message += "https://advogado.rodneyrinaldi.com.br/validacao?chave=" + uuid_key 

    perm = int(
        pymupdf.PDF_PERM_PRINT 
    )
    owner_pass = "owner" 
    user_pass = "" 
    encrypt_meth = pymupdf.PDF_ENCRYPT_AES_256 
    doc = pymupdf.open(wip_filename) # pdf
    n = doc.insert_page(
        -1, # default insertion point
        text = message,
        fontsize = 11,
        width = 595,
        height = 190, #height = 842,
        fontname = "Helvetica", 
        fontfile = None, 
        color = (0.7, 0.7, 0.7) 
    ) 
    doc.save(output_filename)
    doc.close()

    return(output_filename)
