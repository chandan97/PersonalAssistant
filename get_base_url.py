import os
os.environ['YOUTUBE'] = "https://www.googleapis.com/youtube/v3"
os.environ['OXFORD'] = "https://od-api.oxforddictionaries.com/api/v1"

def get_base_url(key):
    return os.environ.get(key)