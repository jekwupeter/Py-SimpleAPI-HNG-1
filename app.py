from datetime import datetime
from flask import Flask, jsonify

# import flask
app = Flask(__name__)

@app.route("/getdata/<slack_name>/<track>")
def get_user_data(slack_name, track):
    now = datetime.now()
    day = datetime.now().strftime("%A")
    mock_model = {
        "slack_name": slack_name,
        "current_day": day,
        "utc_time": now,
        "github_repo_url": "https://github.com/jekwupeter/SimpleAPI-HNG-1",
        "github_file_url": "",
        "track": track,
        "status_code": 200
    } 
    return jsonify(mock_model)