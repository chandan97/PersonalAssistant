# // Importing functionalities // #

from bing_search import bing_search
from custom_search import custom_search
from word_meaning import word_meaning
from youtube import youtube
from news import news
from fallback import fallback

actions = {
    "bing_search": bing_search,
    "custom_search": custom_search,
    "word_meaning": word_meaning,
    "youtube": youtube,
    "news": news,
    "fallback": fallback
}

def intent_solver(dialogflow_resp):
    action = dialogflow_resp['result']['action']
    speech, result = actions[action](dialogflow_resp)
    print(speech, result)
    return speech, result