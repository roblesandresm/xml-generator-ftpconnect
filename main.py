import requests
import asyncio
import os
import pandas as pd
import xml.etree.ElementTree as ET
from ftplib import FTP
from dotenv import load_dotenv

load_dotenv()

# Rutas y credenciales ftp
ftp_host = os.getenv("FTP_HOST")
ftp_user = os.getenv("FTP_USER")
ftp_password = os.getenv("FTP_PASSWORD")
ftp_path = "public_html"

async def download_from_dropbox(url, destino):
    try:
        response = requests.get(url, allow_redirects=True)
        with open(destino, 'wb') as archivo_local:
            archivo_local.write(response.content)
        print(f"Archivo descargado con éxito en: {destino}")
    except Exception as e:
        print(f"Error al descargar el archivo: {e}")

def dataframe_to_xml(df, root_name='vivino-product-list', tags=[], row_name='product', column_names=None):
    root = ET.Element(root_name)
    for _, row in df.iterrows():
        item = ET.SubElement(root, row_name)
        for col_name, value in row.items():
            # Usa nombres de etiquetas personalizados si están proporcionados
                if col_name in tags:
                    tag_name = column_names.get(col_name, col_name) if column_names else col_name
                    child = ET.SubElement(item, tag_name)
                    child.text = str(value)
                     
    return root


def upload_ftp_file(archivo_local, servidor_ftp, usuario_ftp, clave_ftp, directorio_remoto):
    try:
        # Conectar al servidor FTP
        ftp = FTP(servidor_ftp)
        ftp.login(user=usuario_ftp, passwd=clave_ftp)

        # Cambiar al directorio remoto
        ftp.cwd(directorio_remoto)

        # Abrir el archivo local en modo binario
        with open(archivo_local, 'rb') as archivo:
            # Subir el archivo al servidor FTP
            ftp.storbinary('STOR ' + os.path.basename(archivo_local), archivo)

        print(f"Archivo '{os.path.basename(archivo_local)}' subido con éxito al directorio remoto '{directorio_remoto}'")

    except Exception as e:
        print(f"Error al subir el archivo: {e}")

    finally:
        # Cerrar la conexión FTP
        ftp.quit()


# funcion punto de entrada
async def main():
    # vamos a descargar el archivo xls desde una url dropbox
    url_dropbox = 'https://www.dropbox.com/scl/fi/r36jptr2hxmlpql9h5rgb/productos_TTV-Formato-Ideal-en-ESTOC.xlsx?rlkey=2rtukkogljaxnscnpsza90kqu&dl=0&raw=1'
    filename_local = 'products.xls'
    await download_from_dropbox(url_dropbox, filename_local)

    # ruta de archivos
    xlsx_file_path = './'+filename_local
    xml_file_path = 'products-list.xml'

    # columna que se tomaran encuenta para el formato xml
    tags = ["name", "id", "bottle_volume", "url", "weight","stock", "price", "Productos tipo"]

    # Nombres de etiquetas personalizados
    custom_column_names = {
        'name': 'product_name',
        'id': 'product_id',
        'weight': 'bottles',
        'url': 'link',
        'stock': 'inventory-count',
        'Productos tipo': 'type-product',
        # Agrega más nombres de columna según sea necesario
    }

    # Lee el archivo Excel
    df = pd.read_excel(xlsx_file_path)

    # Convierte el DataFrame a elementos XML con nombres de etiquetas personalizados
    root_element = dataframe_to_xml(df, tags=tags, column_names=custom_column_names)

    # Crea un objeto ElementTree y guarda el XML en un archivo
    tree = ET.ElementTree(root_element)
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

    print(f'Se ha creado el archivo XML en: {xml_file_path}')

    # subir el archivo al creado en local al ftp del servidor remoto
    upload_ftp_file(xml_file_path,ftp_host, ftp_user, ftp_password, ftp_path)

if __name__ == "__main__":
    asyncio.run(main())

