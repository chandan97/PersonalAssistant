from get_api_keys import get_api_keys
from get_base_url import get_base_url
import requests

def custom_search(query):
    """This function performs a google search"""

    url = get_base_url("CUSTOM_SEARCH") + "?cx=" + get_api_keys("CUSTOM_SEARCH_ID") \
        + "&q=" + query.replace(' ', '+') + "&key=" + get_api_keys("CUSTOM_SEARCH_KEY")

    response = requests.get(url)
    results = response.json()['items']
    result = {'result': results}
    print(result)
    return result

# query = input('Enter a query : ') 
# custom_search(query)