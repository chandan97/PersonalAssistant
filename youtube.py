import requests
from get_api_keys import get_api_keys
from get_base_url import get_base_url

def youtube(query):
    """This function takes a query and performs a search on youtube"""

    api_key = get_api_keys("YOUTUBE")
    youtube_url = get_base_url("YOUTUBE") + "/search?q={}&part=snippet&MaxResults=1&key={}"
    response = requests.get(youtube_url.format(query, api_key))
    print(response.json())
    result = []
    for i in response.json()['items']:
        result.append("https://www.youtube.com/watch?v=" + i['id']['videoId'])
    return result[0]



