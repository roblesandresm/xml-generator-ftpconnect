import requests

# descargar archivo desde dropbox
def download_from_dropbox(url, destino):
    try:
        response = requests.get(url, allow_redirects=True)
        with open(destino, 'wb') as archivo_local:
            archivo_local.write(response.content)
        print(f"Archivo descargado con éxito en: {destino}")
    except Exception as e:
        print(f"Error al descargar el archivo: {e}")

# Sustituye la URL con el enlace compartido de tu archivo y el nombre del archivo local deseado
# url_dropbox = 'https://www.dropbox.com/s/tu-codigo-de-enlace-compartido/tu-archivo.xls?dl=1'
url_dropbox = 'https://www.dropbox.com/scl/fi/r36jptr2hxmlpql9h5rgb/productos_TTV-Formato-Ideal-en-ESTOC.xlsx?rlkey=2rtukkogljaxnscnpsza90kqu&dl=0&raw=1'
nombre_archivo_local = 'products.xls'

download_from_dropbox(url_dropbox, nombre_archivo_local)