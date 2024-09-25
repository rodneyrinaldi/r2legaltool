import time
from datetime import datetime
import json
import fitz 
import pymupdf
from PyPDF2 import PdfReader, PdfWriter

from app.utils.helpers import CreateNewName, DeleteFile, RenameFile, GetSecretKey
from app.utils.net import GetGeolocation,GetLocalIP,GetPublicIP
from app.utils.qrcode import CreateQrcode

from app.processing.feat201_regfile import RegisterFile
from app.processing.feat203_lockfile import LockerFile


def SignerFile(uuid_key,input_filename):    
    upassword = ""
    opassword = GetSecretKey("Signature","SignSecretKey")
    wip_filename = RegisterFile(uuid_key,input_filename)
    time.sleep(1)
    wip_filename = NotifierFile(uuid_key,wip_filename)
    time.sleep(1)
    wip_filename = LockerFile(wip_filename,upassword,opassword)
    output_filename = CreateNewName(input_filename,"(assinado)") 
    DeleteFile(output_filename) 
    RenameFile(wip_filename,output_filename)
    DeleteFile(input_filename[:-4]+"(reg).pdf")
    DeleteFile(input_filename[:-4]+"(reg)(inf).pdf")
    DeleteFile(input_filename[:-4]+"(reg)(inf).png")



def NotifierFile(uuid_key,wip_filename):
    output_filename = CreateNewName(wip_filename,"(inf)")
    
    now = datetime.now()
    data = now.strftime("%Y/%m/%d %H:%M:%S")

    local_ip = GetLocalIP()
    public_ip = GetPublicIP()
    geolocation = GetGeolocation(public_ip)
    url_check = "https://advogado.rodneyrinaldi.com.br/validacao?chave=" + uuid_key 

    message = "Documento produzido por Rodney Rinaldi Advogado \n" 
    message += "Assinado eletronicamente com r2legaltool \n\n" 
    message += "Processamento: " + data + "\n" + "Chave de segurança: " + uuid_key + "\n"
    message += "IP local: " + local_ip + "\n" + "IP publico: " + uuid_key + "\n"
    message += "Geolocalização: " + json.dumps(geolocation, indent=2) + "\n\n" + url_check

    CreateQrcode(url_check, output_filename[:-4]+".png")

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
        fontsize = 9,
        width = 595,
        height = 400, #height = 842,
        fontname = "Helvetica", 
        fontfile = None, 
        color = (0.2, 0.2, 0.2) 
    ) 
    
    image = fitz.Rect(350, 50, 450, 150)
    page = doc.load_page(-1)
    page.insert_image(image, filename=output_filename[:-4]+".png")

    doc.save(output_filename)
    doc.close()

    # InsertQrcodeIntoPDF(output_filename,output_filename[:-4]+".png")

    return(output_filename)


def InsertQrcodeIntoPDF(path_pdf, path_image):
    file = fitz.open(path_pdf)
    image = fitz.Rect(350, 50, 450, 150)
    page = file.load_page(-1)
    page.insert_image(image, filename=path_image)
    file.save(path_pdf)
    file.close()
