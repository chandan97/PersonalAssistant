import requests
from get_api_keys import get_api_keys
from get_base_url import get_base_url

def currency_converter(dialogflow_resp):

    amount = int(dialogflow_resp['result']['parameters']['amount'])
    currency_to = dialogflow_resp['result']['parameters']['currency-to']
    currency_fro = dialogflow_resp['result']['parameters']['currency-from']
    
    app_key = get_api_keys("CURRENCY_API")

    q1 = currency_fro
    q2 = currency_to
    apikey = app_key
    q = q1 + "_" + q2

    url = get_base_url("CURRENCY_CONVERT")+ "?q={}&compact=ultra&apiKey={}".format(q,apikey)
    response = requests.get(url)
    value = response.json()[q]
    total_value = amount * value
    print(total_value)
    speech = "Converted Amount is {}".format(total_value)
    result = {
        'c_amt': total_value
    }
    return speech,result 

# cur1 = str(input('Enter From Currency : '))
# cur2 = str(input('Enter To Currency : '))
# amount = int(input('Enter Amount: '))
# d_resp = {
#     "result": {
#         "parameters": {
#             "currency-fro": cur1,
#             "currency-to": cur2,
#             "amount": amount
#         }
#     }
# }
# currency_converter(d_resp)


    