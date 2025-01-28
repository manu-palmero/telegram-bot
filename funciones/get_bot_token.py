import os

def get_bot_token():
    token = os.getenv("BOT_TOKEN")
    print(token)
    if token:
        return token
    else:
        raise Exception("BOT_TOKEN environment variable not set")