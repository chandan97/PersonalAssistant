import os
os.environ['YOUTUBE'] = ""  # Chandan - Google Api
os.environ['OXFORD_APP_ID'] = ""  # Devin - Oxford app id
os.environ['OXFORD_APP_KEY'] = ""  # Devin - Oxford app key
os.environ['CUSTOM_SEARCH_ID'] = ""  # Devin - Google Custom Search ID
os.environ['CUSTOM_SEARCH_KEY'] = ""  # Devin - Google Custom Search Api

def get_api_key(key):
    return os.environ.get(key)
