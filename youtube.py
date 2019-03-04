import requests
from get_api_keys import get_api_keys
from get_base_url import get_base_url

def youtube(dialogflow_resp):
    """This function takes a query and performs a search on youtube"""

    query = ""
    for value in dialogflow_resp['result']['parameters'].values():
        if value:
            query = query.replace(" ", "+") + " " + value
    query = query.replace(" ", "+")
    print(query)
    api_key = get_api_keys("YOUTUBE_API")
    youtube_url = get_base_url("YOUTUBE") + "/search?q={}&part=snippet&MaxResults=1&key={}".format(query, api_key)
    response = requests.get(youtube_url)
    result = []
    for i in response.json()['items']:
        result.append("https://www.youtube.com/watch?v=" + i['id']['videoId'])
    print(result)
    speech = "Here is your results for {}".format(query)
    return speech, result

# query = input('Enter : ')
# youtube({'result': {'parameters': {'video': query}}})
