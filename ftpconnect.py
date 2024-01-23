from ftplib import FTP

# Configuración del servidor FTP
ftp_host = 'tu_servidor_ftp.com'
ftp_user = 'tu_usuario_ftp'
ftp_password = 'tu_contraseña_ftp'

# Ruta local del archivo que deseas subir
archivo_local = 'ruta/del/archivo/local/archivo.txt'

# Ruta remota en el servidor FTP donde deseas almacenar el archivo
archivo_remoto = '/ruta/en/el/servidor/archivo.txt'

# Conexión al servidor FTP
with FTP() as ftp:
    ftp.connect(ftp_host)
    ftp.login(ftp_user, ftp_password)

    # Cambia al directorio remoto (opcional)
    ftp.cwd('/directorio/remoto')

    # Abre el archivo local en modo binario
    with open(archivo_local, 'rb') as file:
        # Sube el archivo al servidor FTP
        ftp.storbinary(f'STOR {archivo_remoto}', file)

print('Archivo subido exitosamente al servidor FTP.')
