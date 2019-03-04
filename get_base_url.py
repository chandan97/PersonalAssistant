import os
os.environ['YOUTUBE'] = "https://www.googleapis.com/youtube/v3"
os.environ['CUSTOM_SEARCH'] = "https://www.googleapis.com/customsearch/v1"
os.environ['OXFORD'] = "https://od-api.oxforddictionaries.com/api/v1"
os.environ['WEATHER'] = "https://api.openweathermap.org/data/2.5/weather"  #chandan - weathermap
os.environ['STOCK'] =  "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY"
os.environ['NEWS'] = "https://newsapi.org/v2/everything"
os.environ['TOP_NEWS'] = "https://newsapi.org/v2/top-headlines"

def get_base_url(key):
    return os.environ.get(key)