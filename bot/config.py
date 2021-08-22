class config:
    BOT_TOKEN = "1925950412:AAFqFBejQcFDSHxbq6ZjVnGsm8hygBAN1OI"
    APP_ID = "7218170"
    API_HASH = "f303a5116fa885043cce5478a8fa919e"
    DATABASE_URL = "ANYTHING"
    SUDO_USERS = "1062776854" # Sepearted by space.
    SUPPORT_CHAT_LINK = "https://viperadnan-git.github.io"
    DOWNLOAD_DIRECTORY = "./downloads/"
    G_DRIVE_CLIENT_ID = "127957818724-alkoquolo79d86nh1ppmrmh90nvjglt0.apps.googleusercontent.com"
    G_DRIVE_CLIENT_SECRET = "hZBgX0Kc3Q8_SH98KYOd16C2"


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class Messages:
    START_MSG = "**Hola {}.**\n__Soy Google Drive Uploader Bot. Puedes usarme para cargar cualquier archivo / video a Google Drive desde un enlace directo o archivos de Telegram..__\n__Puedes saber más de /help.__"

    HELP_MSG = [
        ".",
        "**Cargador de Google Drive**\n__Puedo cargar archivos desde un enlace directo o archivos de Telegram a su Google Drive. Todo lo que necesito es autenticarme en su cuenta de Google Drive y enviar un enlace de descarga directa o un archivo de Telegram.__\n\nITengo más funciones ...! ¿Quieres saberlo? Simplemente recorra este tutorial y lea los mensajes con atención.",
        
        "**Autenticar Google Drive**\n__Envía el /auth comando y recibirá una URL, visite URL y siga los pasos y envíe el código recibido aquí. Utilizar /revoke para revocar su cuenta de Google Drive actualmente registrada.__",
        
        "**Enlaces directos**\n__Envíeme un enlace de descarga directa para un archivo, lo descargaré en mi servidor y lo subiré a su cuenta de Google Drive. Puede cambiar el nombre de los archivos antes de cargarlos en la cuenta de GDrive. Solo envíeme la URL y el nuevo nombre de archivo separados por ' | '.__\n\n**__Ejemplos de:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | Nuevo Nombre del archivo.mkv```",
        
        "**Archivos de Telegram**\n__Para cargar archivos de telegram en su cuenta de Google Drive, simplemente envíeme el archivo y lo descargaré y lo subiré a su cuenta de Google Drive. Nota: La descarga de archivos de Telegram es lenta. puede llevar más tiempo para archivos grandes.__",
        
        "**Carpeta personalizada para subir**\n__Quiere cargar en una carpeta personalizada o en__ **TeamDrive** __ ?\nUtiliza /setfolder {Folder ID / TeamDrive ID / Folder UrL} para configurar una carpeta de carga personalizada.\nTodos los archivos se cargan en la carpeta personalizada que proporcionas..__",
        
        "**Copiar archivos de Google Drive**\n__Sí, clonar o copiar archivos de Google Drive.\nUtiliza /copy {File id / Folder id or URL} para copiar archivos de Google Drive en su cuenta de Google Drive.__",
        
        "**Reglas y precauciones**\n__1. No copie GRANDES archivos / carpetas de Google Drive. Puede colgar el bot y sus archivos pueden dañarse.\n2. Envíe una solicitud a la vez a menos que el bot detenga todos los procesos.\n3. No envíe enlaces lentos @transfiéralo primero.\n4. No utilice mal, sobrecargue ni abUtiliza de este servicio gratuito.__",
        
        "**Desarrollado por @**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Excede el límite de velocidad.**\n__Se superó el límite de frecuencia de usuario. Intente después de 24 horas..__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **Archivo / carpeta no encontrado.**\n__ID de archivo - {} Extraviado. Asegúrese de que exista y que la cuenta registrada pueda acceder a ella.__"
    
    INVALID_GDRIVE_URL = "❗ **URL de Google Drive no válido**\nAsegúrese de que la URL de Google Drive tenga un formato válido."
    
    COPIED_SUCCESSFULLY = "✅ **Copiado exitosamente.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **No me has autenticado para subir a ninguna cuenta.**\n__Enviar /{BotCommands.Authorize[0]} autenticar.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Subiendo archivo...**\n**Nombre del archivo:** ```{}```\n**Tamaño:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Subido con éxito.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Downloader Failed**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Descargando archivo...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Ya autorizó su cuenta de Google Drive.**\n__Utiliza /revoke para revocar la cuenta corriente.__\n__Envíeme un enlace directo o un archivo para cargar en Google Drive__"
    
    FLOW_IS_NONE = f"❗ **Codigo invalido**\n__Correr {BotCommands.Authorize[0]} primero.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Cuenta de Google Drive autorizada correctamente.**'
    
    INVALID_AUTH_CODE = '❗ **Codigo invalido**\n__El código que ha enviado no es válido o ya se ha utilizado antes. Genere uno nuevo por la URL de autorización__'
    
    AUTH_TEXT = "⛓️ **Para autorizar su cuenta de Google Drive, visite este [URL]({}) y envía el código generado aquí.**\n__Visite la URL> Permitir permisos> obtendrá un código> cópielo> Envíelo aquí__"
    
    DOWNLOAD_TG_FILE = "📥 **Descargando archivo...**\n**Nombre del archivo:** ```{}```\n**Tamaño:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **El enlace de la carpeta personalizada se estableció correctamente.**\n__Su ID de carpeta personalizada - {}\nUtiliza__ ```/{} clear``` __para limpiarlo.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **La carpeta personalizada se borró correctamente.**\n__Utiliza__ ```/{BotCommands.SetFolder[0]} (Enlace de carpeta)``` __para retrasarlo__.'
    
    CURRENT_PARENT = "🆔 **Su ID de carpeta personalizada actual - {}**\n__Utiliza__ ```/{} (Enlace de carpeta)``` __para cambiarlo.__"
    
    REVOKED = f"🔓 **Cuenta registrada actual revocada con éxito.**\n__Utiliza /{BotCommands.Authorize[0]} para autenticarse nuevamente y utilizar este bot.__"
    
    NOT_FOLDER_LINK = "❗ **Enlace de carpeta no válido.**\n__El enlace que envías no pertenece a una carpeta..__"
    
    CLONING = "🗂️ **Clonación en Google Drive...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Proporcione una URL válida de Google Drive junto con el comando.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **No tienes permisos suficientes para este archivo.**\n__ID de archivo - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **Archivo eliminado correctamente.**\n__Archivo eliminado de forma permanente !\nID de archivo- {}__"
    
    WENT_WRONG = "⁉️ **ERROR: ALGO SALIÓ MAL**\n__Por favor, inténtelo de nuevo más tarde.__"
    
    EMPTY_TRASH = "🗑️🚮**Basura vaciada con éxito !**"
    
    PROVIDE_YTDL_LINK = "❗**Proporcione un enlace válido compatible con YouTube-DL.**"
