from ftplib import FTP

# Configuración del servidor FTP
ftp_host = 'ftp.vinalium.com'
ftp_user = 'roblesandres@vinalium.com'
ftp_password = 'At062415*'

# Ruta local del archivo que deseas subir
archivo_local = './products-list.xml'

# Ruta remota en el servidor FTP donde deseas almacenar el archivo
archivo_remoto = '/public_html'

# Conexión al servidor FTP
with FTP() as ftp:
    try:
        ftp.connect(ftp_host)
        ftp.login(ftp_user, ftp_password)
        print("Se conecto exitosamente")
    except TypeError as err:
        print("Se conecto exitosamente", err)

    # Cambia al directorio remoto (opcional)
    #ftp.cwd('/')

    # Abre el archivo local en modo binario
    with open(archivo_local, 'rb') as file:
        # Sube el archivo al servidor FTP
        ftp.storbinary(f'STOR {archivo_remoto}', file)

print('Archivo subido exitosamente al servidor FTP.')
