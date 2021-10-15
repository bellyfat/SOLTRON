#!/usr/bin/env python3
from flask import Flask, render_template, request,session
import json
import requests
import os
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    userid = request.args.get('userid')
    url = "https://projects.convaiinnovations.com/interact?user={}&msg={}".format(userid, userText)
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    result = str(response.text)

    text = result
    text = text.replace('_POTENTIALLY_UNSAFE__','')
    print(text)



    return str(text)

if __name__ == "__main__":
        app.run()

