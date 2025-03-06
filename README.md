# 🛡️ PIA - Herramientas de Ciberseguridad

## 📌 Descripción  
Este proyecto agrupa diversas **herramientas de ciberseguridad** diseñadas para el análisis, monitoreo y protección de sistemas. Incluye scripts de automatización para auditorías de seguridad, análisis de tráfico, pruebas de penetración y generación de reportes. Ideal para profesionales y estudiantes en seguridad informática.

## 🚀 Características  
✔️ **Escaneo de vulnerabilidades** en sistemas y redes.  
✔️ **Automatización de auditorías de seguridad**.  
✔️ **Análisis de tráfico y detección de anomalías**.  
✔️ **Herramientas para pruebas de penetración básicas**.  
✔️ **Generación de reportes de seguridad** en PDF y CSV.  

## 🛠️ Tecnologías Utilizadas  
- **Python** 🐍 (Automatización y análisis)  
- **Bash** 🖥️ (Scripts de seguridad para Linux)  
- **Wireshark/TShark** 🕵️ (Captura de tráfico de red)  
- **Nmap** 🌐 (Escaneo de redes y puertos)  
- **Metasploit Framework** 🔥 (Pruebas de penetración)  

## 🔧 Requisitos Previos  
1️⃣ Tener **Python 3.8+** instalado.  
2️⃣ Acceso a **herramientas de análisis de seguridad** (Wireshark, Nmap, Metasploit).  
3️⃣ Sistema operativo **Linux o Windows con WSL**.  

## ⚡ Instalación  
1. **Clona el repositorio**:  
   ```bash
   git clone https://github.com/FernandoCeGa/PIA---Herramientas-de-ciberseguridad.git
   cd PIA---Herramientas-de-ciberseguridad
   ```
2. **Instala las dependencias necesarias**:  
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecuta la herramienta principal**:  
   ```bash
   python main.py
   ```

## 🎯 Modo de Uso  

### **1. Ejecución Automatizada**
Para ejecutar la herramienta en modo automatizado:
```bash
python main.py
```
Esto iniciará la secuencia automatizada de todas las funcionalidades integradas en la herramienta.

### **2. Ejecución Manual**
Para seleccionar funcionalidades específicas:
```bash
python main.py -mode Manual
```
Aparecerá un menú interactivo donde podrás elegir la herramienta deseada.

### **3. Ejecución con Parámetros Específicos**
Puedes ejecutar funcionalidades individuales con los siguientes comandos:

- **Envío de Correos**:
  ```bash
  python main.py -script Email -dest [correo1,correo2]
  ```
- **Escaneo de Puertos**:
  ```bash
  python main.py -script Ports -ip 192.168.1.1 -port 8080
  ```
- **Web Scraping de Correos**:
  ```bash
  python main.py -script WebMail
  ```
- **Análisis de Archivos con VirusTotal**:
  ```bash
  python main.py -script VirusTotal
  ```

## 🤝 Contribuciones  
¡Las contribuciones son bienvenidas! 🚀  

1. **Haz un fork del repositorio** en [GitHub](https://github.com/FernandoCeGa/PIA---Herramientas-de-ciberseguridad/fork).  
2. **Crea una nueva rama** para tu funcionalidad:  
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. **Realiza cambios y haz commit**:  
   ```bash
   git commit -m "Añadir nueva funcionalidad"
   ```
4. **Sube los cambios al repositorio**:  
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. **Abre una Pull Request** en [este enlace](https://github.com/FernandoCeGa/PIA---Herramientas-de-ciberseguridad/pulls).  

## 📜 Licencia  
Este proyecto está licenciado bajo la **GNU General Public License v3.0**. Esto significa que tienes la libertad de usar, modificar y distribuir este software, siempre que mantengas la misma licencia en versiones derivadas. Para más información, consulta el archivo [LICENSE](LICENSE) o visita la página oficial de la [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html).

## 📩 Contacto  
Desarrollado por **Fernando CeGa**.  
✉️ **Correo:** [fcerecedogi@uanl.edu.mx](mailto:fcerecedogi@uanl.edu.mx)  
🔗 **GitHub:** [github.com/FernandoCeGa](https://github.com/FernandoCeGa)  


