## Requisitos previos windows
* Tener python instalado
* Tener behave instalado
* Tener selenium instalado
* Tener instalado chrome
* Tener el chromedriver asociado a su versión de chrome instalada
* Tener la ubicación del archivo chrome.exe
* Tener la ubicación del archivo chromedriver.exe

### Instalación de selenium
* pip install selenium

### ¿Cómo saber la versión de chrome que tengo instalada?

1) Situarse en la esquina superior derecha del navegador chrome
2) Presionar los tres puntitos
3) Presionar **configuración**
4) Presionar el botón **Acerca de Chrome**

### ¿Cómo saber la ubicación del archivo chrome.exe?
1) Buscar ejecutable de Chrome en el computador
2) Click derecho
3) Abrir ubicación del archivo  

### ¿Como descargo el chromedriver.exe?

1) Buscar chrome driver <version_chrome_instalada>
2) Ingresar a la página https://chromedriver.chromium.org/downloads
3) Pinchar el enlace llamado ChromeDriver <version_chrome_instalada>
4) Descargar el archivo chromedriver_win32.zip
5) Descomprimir el archivo

### Configuraciones
* Abrir archivo login.py
* Colocar la ubicación del ejecutador de Chrome en options.binary_location
* Colocar la ubicación del chromedriver.exe en `executable_path`

### Ejecución

* Escribir `behave` en la consola.
