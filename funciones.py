import sys #pipreq
import subprocess#pipreq
import pkg_resources#pipreq
from PyPDF2 import PdfFileReader, PdfFileWriter#Metadatos
import logging#general
import os #general
import requests#Webscrap
from lxml import html #webscrap
from bs4 import BeautifulSoup#webscrap
from PIL.ExifTags import TAGS, GPSTAGS #Metadatos
from PIL import Image #Metadatos  
import smtplib #envio de correos
import ssl #API
import getpass 
import pathlib #General
import socket #fqdn
from email import encoders   #envio de correos
from email.mime.base import MIMEBase #envio de correos
from email.mime.text import MIMEText #envio de correos
from email.mime.multipart import MIMEMultipart #envio de correos
import base64 #Codificacion
import subprocess #PS
from pathlib import Path #General
import uuid #identificador
import warnings #Metadatos


# Uso de pireq

def pireq():
    logging.info("Se busca si esta instalado pipreqs")
    try:
        required = {"pipreqs"}
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = required - installed
        if missing:
            python = sys.executable
            subprocess.check_call(
                [python, "-m", "pip", "install", *required],
                stdout=subprocess.DEVNULL
            )
            subprocess.check_call(
                [python, '-m', "pip", "install", "-r", "requirements.txt"]
            )
            logging.info("Se instalo pipreqs")
        else:
            print("PIPREQS INSTALADO")
            print("Modulos en requirements instalados")
            logging.info("Pipreqs ya estaba instalado")
    except:
        print("Modulo pipreqs no encontrado")
        logging.debug(
            "No se encontró pipreqs, pero ya es posible volver a correr "
            "el codigo ya que se instaló automáticamente")

# WebScrapping


class Scraping:
    def scrapingImages(self, url):
        print("\nObteniendo imagenes de la url:" + url)

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            # expresion regular para obtener imagenes
            images = parsed_body.xpath("//img/@src")

            print("Imagenes %s encontradas" % len(images))

            # create directory for save images
            os.system("mkdir images")
            logging.info("Se creó un folder para imagenes")

            for image in images:
                if image.startswith("http") is False:
                    download = url + image
                else:
                    download = image
                print(download)
                # download images in images directory
                r = requests.get(download)
                f = open("images/%s" % download.split("/")[-1], "wb")
                f.write(r.content)
                logging.info(
                    "Se descargo imagen con dirreccion al folder creado")
                f.close()

        except:
            print("Error conexion con " + url)
            logging.warning("Hubo error de conexion con la url")
            print("Ingrese un url adecuado a la próxima")
            exit()

    def scrapingPDF(self, url):
        print("\nObteniendo pdfs de la url:" + url)

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            # expresion regular para obtener pdf
            pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')

            # create directory for save pdfs
            if len(pdfs) > 0:
                os.system("mkdir pdfs")

            print("Encontrados %s pdf" % len(pdfs))
            logging.info("Se creo un folder para los pdfs")

            for pdf in pdfs:
                if pdf.startswith("http") is False:
                    download = url + pdf
                else:
                    download = pdf
                print(download)

                # descarga pdfs
                r = requests.get(download)
                f = open("pdfs/%s" % download.split("/")[-1], "wb")
                logging.info(
                    "Se descargo PDF con dirreccion al folder creado")
                f.write(r.content)
                f.close()

        except:
            print("Error conexion con " + url)
            logging.warning("Hubo error de conexion con la url")
            print("Ingrese un url adecuado a la próxima")
            exit()

# bloque de obtencion de metadata
def printMeta():
    informe = open("Reporte_Imagenes.txt", "w+")
    logging.info(
        "Se creo un informe con los metadatos obtenidos de las imagenes")
    ruta = "images"

    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            informe.write("nombre: " + (name))
            informe.write("\n")
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    informe.write("[+] %s - Value: %s " %
                                  (metadata, exif[metadata]))
                    informe.write("\n")

            except:
                import sys
                import traceback
                traceback.print_exc(file=sys.stdout)
            informe.write("\n\n")
    informe.close()
    print("La obtencion de metadatos ha sido exitosa\n")
    print("listos en su respectivo archivo(Reporte_imagenes o Reporte_PDFs)\n ")

#image_path ruta de la imagen con nombre /carpeta/imagen.jpg
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, "_getexif"):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret

# Formato a Extración de Datos
def decode_gps_info(exif):  # exif =
    gpsinfo = {}
    if "GPSInfo" in exif:
        # Parse geo references.
        Nsec = exif["GPSInfo"][2][2]
        Nmin = exif["GPSInfo"][2][1]
        Ndeg = exif["GPSInfo"][2][0]
        Wsec = exif["GPSInfo"][4][2]
        Wmin = exif["GPSInfo"][4][1]
        Wdeg = exif["GPSInfo"][4][0]
        if exif["GPSInfo"][1] == "N":
            Nmult = 1
        else:
            Nmult = -1
        if exif["GPSInfo"][1] == "E":
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec / 60.0) / 60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec / 60.0) / 60.0)
        exif["GPSInfo"] = {"Lat": Lat, "Lng": Lng}
        input()



# PENDIENTE MetadataPDF


def printPDF():
    os.chdir(pathlib.Path(__file__).parent.absolute())
    Informe = open("Reporte_PDFs.txt", "w+")
    logging.info(
        "Se creo un informe con los metadatos obtenidos de los PDF's")
    for dirpath, dirs, files in os.walk(".", topdown=False):
        for name in files:
            ext = name.lower().rsplit(".", 1)[-1]  # archivo.nombre.algo.pdf
            if ext in ["pdf"]:
                pdfFile = PdfFileReader(
                    open(dirpath + os.path.sep + name, "rb",))
                warnings.simplefilter("ignore")
                docInfo = pdfFile.documentInfo
                Informe.write("Archivo: " + name.lower())
                Informe.write("\n")
                Informe.write(
                    "[+] Cantidad de paginas: " + str(pdfFile.numPages) + "\n"
                )
                Informe.write("[+] Encriptado: " +
                              str(pdfFile.isEncrypted) + "\n")
                for metaItem in docInfo:
                    Informe.write(
                        "[+] " + str(metaItem) + ": " + str(docInfo[metaItem])
                    )
                    Informe.write("\n")
            Informe.write("\n\n")
    Informe.close()


def encode():
    print("Se codificaran los Reportes obtenidos\n")
    os.chdir(pathlib.Path(__file__).parent.absolute())
    base64.encode(
        open("Reporte_Imagenes.txt", "rb"),
        open("ReporteB64_Imagenes.txt", "wb"))
    base64.encode(open("Reporte_PDFs.txt", "rb"),
                  open("ReporteB64_PDFs.txt", "wb"))
    logging.info(
        "Se codificaron los reportes en b64")


def envioCorreos(rec):
    print("Se hará un envio de correo con la codificación de los reportes obtenidos en base 64")
    try:
        logging.info("Se enviara un correo con los reportes obtenidos")
        body = "Reportes del Web Scraping"
        # sender_email ="emailemisor" 
        sender_email =""
        receiver_email = rec

        msg = MIMEMultipart()
        msg["Subject"] = "[PIA 2021]"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        msgText = MIMEText("<b>%s</b>" % (body), "html")
        msg.attach(msgText)

        # filename = "example.txt"
        # msg.attach(MIMEText(open(filename).read()))
        adjunto = MIMEBase("application", "octect-stream")
        adjunto.set_payload(open("ReporteB64_Imagenes.txt", "rb").read())
        adjunto.add_header(
            "content-Disposition",
            'attachment; filename="Reporte_Imagenes.txt"'
        )
        msg.attach(adjunto)

        adjunto = MIMEBase("application", "octect-stream")
        adjunto.set_payload(open("ReporteB64_PDFs.txt", "rb").read())
        adjunto.add_header(
            "content-Disposition", 'attachment; filename="Reporte_PDFs.txt"'
        )
        msg.attach(adjunto)

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as smtpObj:
                smtpObj.ehlo()
                smtpObj.starttls()
                # smtpObj.login("emailemisor", "emailreceptor")
                smtpObj.login("", "")
                smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
                logging.info("Se envió el correo con los reportes obtenidos")
        except Exception as e:
            print(e)

    except FileNotFoundError:
        print("Archivo Reporte_imagenes.txt no encontrado")
        logging.warning("No se encontraron los reportes para el envío")


def APImail(email, key):
    logging.info("Se hará uso de una Api de correos")
    url = "https://mailcheck.p.rapidapi.com/"
    querystring = {"disable_test_connection": "true", "domain": email}
    headers = {
        'x-rapidapi-host': "mailcheck.p.rapidapi.com",
        'x-rapidapi-key': key
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    print(response.text)
    logging.info("Se realizó la petición a la API")


def Fdqn():
    logging.info("Se buscará el nombre de dominio completo del equipo")
    fqdn = socket.getfqdn()
    print("Fully qualified domain name of this computer is:")
    print(fqdn)
    logging.info("Se entregó fqdn perfectamente")


def ReglasPS():
    logging.info("Se verán las reglas bloqueadas del firewall")
    fpath = Path("powershellpia.ps1").absolute()
    p = subprocess.Popen(["powershell.exe", fpath], stdout=sys.stdout)
    print(fpath)
    logging.info("Se entregaron las reglas bloqueadas")
    


def identUU(arch):
    os.chdir(pathlib.Path(__file__).parent.absolute())
    logging.info("Se busca obtener un UUID para cambio de nombre del archivo")
    u=uuid.uuid4()
    print("Obteniendo UUID")
    p=str(u)
    logging.info("Nombre para cambio: " + p)
    archivo=arch
    nombre_nuevo=p
    os.rename(archivo,nombre_nuevo)
    print("Se cambió el nombre del archivo deseado")
    logging.info("Cambió de nombre el archivo: " + arch)

# Formato de loggins
log_format = (
    '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')

logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    filename=('app.log'))

