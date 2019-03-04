import os
os.environ['YOUTUBE_API'] = "AIzaSyArH_HxjcIEabfBa1FpMGFvG2NRQ13DYvE"  # Chandan - Google Api
os.environ['OXFORD_APP_ID'] = "9f9aaf83"  # Devin - Oxford app id
os.environ['OXFORD_APP_KEY'] = "6aa3d20af0e17107f44d51786a73c9eb"  # Devin - Oxford app key
os.environ['CUSTOM_SEARCH_ID'] = "003395937100330916829:cwjq6rqad7i"  # Devin - Google Custom Search ID
os.environ['CUSTOM_SEARCH_KEY'] = "AIzaSyAlYdimlBv24zeCg_7VMsqrM57vTCwZebE"  # Devin - Google Custom Search Api
os.environ['CLIENT_ACCESS_TOKEN'] = "d4305116581d4ed988f6b6e652abb64c"  # Devin - Dialogflow
os.environ['NEWS_API'] = "b3581e68ed2b4024b4fc1a9e0550f900"  # Chandan - News Api

def get_api_keys(key):
    return os.environ.get(key)