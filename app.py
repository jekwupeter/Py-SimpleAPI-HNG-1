from datetime import datetime
from flask import Flask, jsonify, request

# import flask
app = Flask(__name__)

@app.route("/api", methods=["GET"])
def get_user_data():
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")
    now = datetime.now()
    day = datetime.now().strftime("%A")
    mock_model = {
        "slack_name": slack_name,
        "current_day": day,
        "utc_time": now,
        "github_repo_url": "https://github.com/jekwupeter/Py-SimpleAPI-HNG-1",
        "github_file_url": "https://github.com/jekwupeter/Py-SimpleAPI-HNG-1/app.py",
        "track": track,
        "status_code": 200
    } 
    return jsonify(mock_model)
