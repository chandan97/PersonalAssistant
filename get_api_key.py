import os
os.environ['YOUTUBE'] = "AIzaSyArH_HxjcIEabfBa1FpMGFvG2NRQ13DYvE"  # Chandan - Google Api
os.environ['OXFORD_APP_ID'] = "9f9aaf83"  # Devin - Oxford app id
os.environ['OXFORD_APP_KEY'] = "6aa3d20af0e17107f44d51786a73c9eb"  # Devin - Oxford app key

def get_api_key(key):
    return os.environ.get(key)