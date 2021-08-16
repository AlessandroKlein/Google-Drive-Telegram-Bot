# Bot de Telegram Uploader de Google Drive
** Un bot de Telegram para cargar archivos desde Telegram o enlaces directos a Google Drive. **
- Encuéntrelo en Telegram como [Google Drive Uploader]

## Características
- [X] Soporte de archivos de Telegram.
- [X] Soporte de enlaces directos.
- [X] Carpeta de carga personalizada.
- [X] Soporte TeamDrive.
- [X] Clonar / Copiar archivos de Google Drive.
- [X] Eliminar archivos de Google Drive.
- [X] Vaciar la papelera de Google Drive.
- Soporte de [X] youtube-dl.

## Que hacer
- [] Maneja más excepciones.
- [] Soporte LOGGER.
- [] Soporte de cuenta de servicio.
- [] Comando de actualización.
## Deploying

### Deploy on [Heroku](https://heroku.com)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Installation
- Install required modules.
```sh
apt install -y git python3 ffmpeg
```
- Clone this git repository.
```sh 
git clone https://github.com/viperadnan-git/google-drive-telegram-bot
```
- Change Directory
```sh 
cd google-drive-telegram-bot
```
- Install requirements with pip3
```sh 
pip3 install -r requirements.txt
```

### Configuration
**There are two Ways for configuring this bot.**
1. Add values to Environment Variables. And add a `ENV` var to Anything to enable it.
2. Add values in [config.py](./bot/config.py). And make sure that no `ENV` environment variables existing.

### Configuration Values
- `BOT_TOKEN` - Get it by contacting to [BotFather](https://t.me/botfather)
- `APP_ID` - Get it by creating app on [my.telegram.org](https://my.telegram.org/apps)
- `API_HASH` - Get it by creating app on [my.telegram.org](https://my.telegram.org/apps)
- `SUDO_USERS` - List of Telegram User ID of sudo users, seperated by space.
- `SUPPORT_CHAT_LINK` - Telegram invite link of support chat.
- `DATABASE_URL` - Postgres database url.
- `DOWNLOAD_DIRECTORY` - Custom path for downloads. Must end with a forward `/` slash. (Default to `./downloads/`)

### Deploy 
```sh 
python3 -m bot
```

## Credits
- [Dan](https://github.com/delivrance) for creating [PyroGram](https://pyrogram.org)
- [Spechide](https://github.com/Spechide) for [gDriveDB.py](./bot/helpers/sql_helper/gDriveDB.py)
- [Shivam Jha](https://github.com/lzzy12) for [Clone Feature](./bot/helpers/gdrive_utils/gDrive.py) from [python-aria-mirror-bot](https://github.com/lzzy12/python-aria-mirror-bot)

## Copyright & License
- Copyright (©) 2020 by [Adnan Ahmad](https://github.com/viperadnan-git)
- Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](./LICENSE)
