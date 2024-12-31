import yt_dlp

def descargar_video(url, ruta_destino='.'):
    try:
       
        opciones = {
            'outtmpl': f'{ruta_destino}/%(title)s.%(ext)s',  
            'format': 'best',  
        }

        # Crear el objeto y descargar
        with yt_dlp.YoutubeDL(opciones) as ydl:
            print(f"Descargando: {url}")
            ydl.download([url])
            print(f"Video descargado en: {ruta_destino}")

    except Exception as e:
        print(f"Error al descargar el video: {e}")

if __name__ == '__main__':
   
    url_video = input("Introduce la URL del video: ")
    
    ruta_destino = input("Introduce la carpeta de destino (presiona Enter para usar la carpeta actual): ")
    if not ruta_destino:
        ruta_destino = '.'
    
    descargar_video(url_video, ruta_destino)






