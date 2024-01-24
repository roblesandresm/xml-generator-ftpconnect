from ftplib import FTP
import os

def subir_archivo_ftp(archivo_local, servidor_ftp, usuario_ftp, clave_ftp, directorio_remoto):
    try:
        # Conectar al servidor FTP
        ftp = FTP()
        ftp.connect(servidor_ftp, port=21)
        ftp.login(user=usuario_ftp, passwd=clave_ftp)

        # Verificar si el directorio remoto existe, si no, crearlo
        if not ftp.nlst(directorio_remoto):
            ftp.mkd(directorio_remoto)

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
        ftp.quit()

# Rutas y credenciales ftp
archivo_local = './products-list.xml'
directorio_remoto = '/'
ftp_host = 'ftp.tucanmarketingdigital.com'
ftp_user = 'u482066164.arobles'
ftp_password = 'At062415*'

# Llamar a la función para subir el archivo
subir_archivo_ftp(archivo_local, ftp_host, ftp_user, ftp_password, directorio_remoto)
