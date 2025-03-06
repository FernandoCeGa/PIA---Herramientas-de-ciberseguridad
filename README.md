=======================================
PIA - PROGRAMACIÓN PARA CIBERSEGURIDAD
=======================================
DESCRIPCIÓN DEL PROGRAMA:
-Serie de scripts para uso de WebScrapping, Obtención de Metadatos, Envió de Correos, Verificación de Correos, Ver reglas de Firewall bloqueadas, Validar un e-mail mediante uso de API.
-Uso Automatizado sin Intervención entre Procesos.
=======================================
MODO DE USO:
-Inicie CMD con dirección el directorio en el que esta el proyecto.
-NOTA: (Puede Utilizar main.py -h o main.py --help para ver los parametros a utilizar).     
-Escoja una opción disponible y agregue los parametros necesarios para su funcionamiento.

-IMPORTANTE:Si hace uso de la opcion de Api de verificación de correos es necesario registrarse en el siguiente url:
     |----------------> https://rapidapi.com/Top-Rated/api/e-mail-check-invalid-or-disposable-domain/pricing
     Despues de registrarse seleccionar el plan GRATUITO y listo puede usar sin obstáculos nuestra herramienta.
     
 En nuestra herramienta, otorgamos las siguientes opciones:
 
   -op A     En esta opcion se hace WebScrap a una url dada, se obtienen imágenes, Pdfs, se descargan en su debido 
               folder, se obtienen sus metadatos, después los metadatos se codifican en base64 y se manda un correo     
               con éstos reportes obtenidos hacia un correo dado.
               
               En esta opción hacemos uso de los argumentos -u -rec
               enseguida vemos un ejemplo de lo que puede recibir.
              
                    Ejemplo de uso
                              main.py -op A  -u https://www.facebook.com/ -rec example@outlook.com
                              
                    Advertencia: Si no se ingresa el url completo no será posible avanzar con el proceso.
                    
   -op B     En esta opcion se hace una peticion a una API llamada E-mail Check Invalid or Disposable Domain API 
               Documentation, donde es necesario el registro mencionado con anterioridad para obtener su APIKEY
               y poder dar uso a esta API, además de un email dado que pueda verficar.
               
               
              En esta opción hacemos uso de los argumentos -em -k
               enseguida vemos un ejemplo de lo que puede recibir.
               
                    Ejemplo de uso
                              main.py -em Example@gmail.com  -k XZXZXZXZXZXZXZXZXZXZ
                    
   -op C     En esta opcion lo que se hace es enlazar Python con PowerShell, para poder ver las reglas de Bloqueo 
                  del Firewall
                  
                  En esta opcion no es necesario el uso de argumentos por lo tanto
                  puedes accesar solo con
                  
                              main.py -op C
     
   -op D     En esta opcion solo se obtiene el FQDN un nombre de dominio completo que incluye el nombre de la 
               computadora y el nombre de dominio  asociado a ese equipo. 
               
                    En esta opcion no es necesario el uso de argumentos por lo tanto
                    puedes accesar solo con
                  
                              main.py -op D

   -op E     En esta última opcion lo que se hace es obtener un Universally Unique IDentifier y
                  con esta misma cambiar de nombre un archivo. -conocer mas 
                    sobre uuid en : https://www.significados.com/uuid/
               
                    En esta opcion no es necesario el uso de argumentos por lo tanto
                    puedes accesar solo con
                  
                              main.py -op E  -arch Reporte_Imagenes.txt
   


-Verifique si los parametros son correctos, ya que si estos no lo son el Programa puede Interrumpirse (Se añadira Logs de Errores, Interrupciones, etc en una archivo txt)
-En el archivo app.log puede encontrar todo lo que esta pasando internamente, desde ver que se esta descargando, el codigo de aceptación de la pagina, la creación de folders,etc..
-NOTA: Puede copiar y pegar datos como Direcciónes de directorios o cadenas de texto sin problema alguno con el funcionamiento del script.
-De ENTER y automaticamente hará los procesos de la opción utilizada
=======================================
