import json

def load_config():
    with open("config.conf") as f:
        config = json.load(f)
        if config['jellyfin_url'][-1] != '/':
            config['jellyfin_url'] += '/'
        return config

config = load_config()
