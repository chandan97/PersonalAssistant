import bingscraper as bs
import os

def fallback(dialogflow_resp):
    """This function handles fallback intent"""

    search_query = dialogflow_resp['result']['resolvedQuery']
    print(search_query)
    bs.scrape(search_query).text()
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
    if len(search_results) == 0:
        speech = dialogflow_resp['result']['fulfillment']['speech']
    else:
        speech = "Here are your search results for {}".format(search_query)
    return speech, search_results