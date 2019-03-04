# // Importing Libraries // #

from apiai import ApiAI
from flask import Flask, request, jsonify
import json
from shortid import ShortId

from get_api_keys import get_api_keys
from intent_solver import intent_solver

app = Flask(__name__)
d_flow = ApiAI(get_api_keys("CLIENT_ACCESS_TOKEN"))
sid = ShortId()

@app.route('/', methods=['GET', 'POST'])
def main():
    """This is where all the speech/text come to

    Request (PARAMS):-
    {
        "text": "Some text wrote/said by user",
        "session": "generated session value"
    }

    Response (JSON):-
    {
        TODO: Decide response structure
    }

    """
    if request.method == 'GET':
        try:
            if request.args:
                text = request.args['text']
                req = d_flow.text_request()
                req.lang = 'en'
                if not "session" in request.args:
                    req.session_id = sid.generate() 
                else:
                    req.session_id = request.args['session']
                req.query = text
                dialogflow_resp = req.getresponse().read().decode()
                print(dialogflow_resp)
                dialogflow_resp = json.loads(dialogflow_resp)

                speech, result = intent_solver(dialogflow_resp)
                return jsonify({'error': False, 'result': {'speech': speech, 'data': result}}), 200
        except Exception as e:
            print(str(e))
            return jsonify({'error': True, 'result': None}), 400
    else:
        return "POST method is not allowed at this moment", 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)


