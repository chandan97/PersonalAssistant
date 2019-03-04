import requests
import bingscraper as bs
import os

def bing_search(dialogflow_resp):
    """This function scrapes bing search result"""

    search_query = dialogflow_resp['result']['parameters']['q']
    bs.scrape(search_query).text() #For Text Scraping.
    # bs.scrape(search).image() #For Image Scraping.)
    search_results = []
    with open(os.path.join(search_query.replace(' ', '_'), search_query + '.txt'), 'r') as f:
        counter = 0
        current = {}
        for i in f:
            if i == '\n':
                continue
            if counter % 2 == 0:
                print(i)
                current['title'] = i
            else:
                current['link'] = i
                search_results.append(current)
                current = {}
            counter += 1
    print(search_results)
    os.remove(os.path.join(search_query.replace(' ', '_'), search_query + '.txt'))
    os.rmdir(search_query.replace(' ', '_'))
    speech = "Here are your search results for {}".format(search_query)
    return speech, search_results

# query = input('Enter your query : ')
# bing_search(query)