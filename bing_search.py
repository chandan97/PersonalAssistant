import requests
import bingscraper as bs
import os

def bing_search(query):
    """This function scrapes bing search result"""

    search = str(query)
    bs.scrape(search).text() #For Text Scraping.
    # bs.scrape(search).image() #For Image Scraping.)
    search_results = []
    with open(os.path.join(query.replace(' ', '_'), query + '.txt'), 'r') as f:
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
    os.remove(os.path.join(query.replace(' ', '_'), query + '.txt'))
    os.rmdir(query.replace(' ', '_'))

query = input('Enter your query : ')
bing_search(query)