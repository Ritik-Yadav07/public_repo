import json
from flask import Flask, request
from flask.config import T
from flask_cors import CORS


app = Flask(__name__)

CORS(app)


@app.post('/')
def dummy_post_api():
    try:

        print('Request data (JSON):', json.dumps(request.json, indent=4))
        return 'Success'
    except Exception as e:
        print(e)
        print('Request data (text):', request.get_data())
        return 'Failed'


app.run(host="0.0.0.0", port=5000, debug=True)
