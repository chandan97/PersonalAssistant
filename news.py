import requests
from get_api_keys import get_api_keys
from get_base_url import get_base_url
from datetime import datetime

# link = "https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-23&sortBy=publishedAt&apiKey="

def current_date():
  now = datetime.now()
  now = datetime.strftime(now, '%Y-%m-%d')
  return now

def news(topic):
  
  date = current_date()
  url = get_base_url("NEWS") + "?q={}&from={}&sortBy=publishedAt&apiKey={}".format(topic, date, get_api_keys("NEWS_API"))
  print(url)
  response = requests.get(url)
  #print(response.json())
  articles = response.json()['articles']
  results = []
  for i in articles[:1]:
    data = {
      'title': i['title'],
      'description': i['description'],
      'image': i['urlToImage'],
      'publishedAt': i['publishedAt'],
      'content': i['content'],
      'url': i['url']
    }
    print(response.text)
    results.append(data)
topic = input('Enter Topic : ')
news(topic)
  

     