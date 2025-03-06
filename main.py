import argparse
import funciones
from funciones import Scraping

print("""
         ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄ 
        ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌
        ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌      ▀▀▀▀▀▀▀▀▀█░▌
        ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌               ▐░▌
        ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌               ▐░▌
        ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌      ▄▄▄▄▄▄▄▄▄█░▌
        ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌     ▐░░░░░░░░░░░▌
        ▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ 
        ▐░█▄▄▄▄▄▄▄▄▄  ▀▀▀▀▀▀█░█▀▀ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄▄▄ 
        ▐░░░░░░░░░░░▌        ▐░▌  ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌
         ▀▀▀▀▀▀▀▀▀▀▀          ▀    ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀
                             (Github: https://github.com/YahirH/PIA-Programacion-para-Ciberseguridad)""")

# argparser


def main():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Usamos una API para el pia')
    parser.add_argument("-op", "--option", dest="op", required=True,
                        help='Opción A =WebScrapping/Obtención de Metadatos/Envio de Correo con resultado'
                        'Opción B =API de revisión de dirección de Correo'
                        'Opción C = Ver Reglas de Bloqueo del Firewall'
                        'Opción D= Obtener el nombre de Dominio Completo de mi equipo'
                        'Opción E=Obtener un Universally Unique IDentifier(UUID) y cambiar nombre a un archivo con la misma')
    parser.add_argument("-u", "--url", dest='url',
                        help="Enter an url to webscrap")
    parser.add_argument("-rec", "--receiver", dest='rec', type=str,
                        help='Destinatario del correo de los Reportes obtenidos')
    parser.add_argument("-em", "--email", dest='email',
                        type=str, help="Enter email para analizar")
    parser.add_argument("-k", "--key", dest='key',
                        type=str, help="APIKey de tu cuenta")
    parser.add_argument("-arch", "--archivo", dest='arch',
                        type=str, help="Archivo para cambiar su nombre por un UUID")

    
    args = parser.parse_args()
    x = args.op

    funciones.pireq()
    # ejecucion de funciones
    if x == 'A' or x == 'a':
        scraping = Scraping()
        scraping.scrapingImages(args.url)
        scraping.scrapingPDF(args.url)
        funciones.printMeta()
        funciones.printPDF()
        funciones.encode()
        funciones.envioCorreos(args.rec)
    if x == 'B' or x == 'b':
        funciones.APImail(args.email, args.key)
    if x == 'C' or x == 'c':
        funciones.ReglasPS()
    if x == 'D' or x == 'd':
        funciones.Fdqn()
    if x == 'E' or x == 'e':
        funciones.identUU(args.arch)


if __name__ == "__main__":
    main()

