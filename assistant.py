import requests
import json

api_key = "AIzaSyArH_HxjcIEabfBa1FpMGFvG2NRQ13DYvE"
youtube_url = "https://www.googleapis.com/youtube/v3/search?q={}&part=snippet&MaxResults=1&key={}"

def search_video(query):
    """This function takes a query and performs a search on youtube"""

    response = requests.get(youtube_url.format(query, api_key))
    print(response.json())
    for i in response.json()['items']:
        print("https://www.youtube.com/watch?v=" + i['id']['videoId'])

query = input("Enter a string : ")
search_video(query)
