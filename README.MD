# Bot de telegram

Bot de telegram experimental enfocado en proporcionar informaci'on o
realiazar acciones en un servidor ejecut'andose en un contenedor de docker.

## Uso

### docker-compose

```yaml
---
services:
  telegram-bot:
    image: ghcr.io/manu-palmero/telegram-bot:main
    container_name: telegram-bot
    environment:
    - BOT_TOKEN = "TOKEN"
    restart: unless-stopped
```