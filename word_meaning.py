import requests
from get_api_keys import get_api_keys
from get_base_url import get_base_url

def word_meaning(word):
    """This function takes a word and finds the meaning, synonyms/antonyms of that word"""

    app_id = get_api_keys("OXFORD_APP_ID")
    app_key = get_api_keys("OXFORD_APP_KEY")
    header = {
        "app_id": app_id,
        "app_key": app_key
    }
    url = get_base_url("OXFORD") + "/entries/{}/{}/regions=us;definitions;examples".format('en', word)
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        return "Sorry could not find a meaning of %s." % word.title()
    else:
        meaning = response.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        example = response.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]
        result = {'meaning': meaning, 'example': example['text']}
        return result

# word = input('Enter a word : ')
# word_meaning(word)
