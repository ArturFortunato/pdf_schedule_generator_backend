import flask
import flask_cors   
import json
from main import temp_main

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "YES"

@app.route('/schedule', methods=['POST'])
def schedule():
    schedules = temp_main(flask.request.get_json()['courses'])
    return schedules

app.run(threaded=True, port=5000)