# Bot de telegram

Bot de telegram experimental enfocado en proporcionar información o
realiazar acciones en un servidor ejecutándose en un contenedor de docker.

## Implementación

### docker-compose

```yaml
---
services:
  telegram-bot:
    image: ghcr.io/manu-palmero/telegram-bot:main
    container_name: telegram-bot
    environment:
    - BOT_TOKEN=TOKEN # Sin comillas
    restart: unless-stopped
```