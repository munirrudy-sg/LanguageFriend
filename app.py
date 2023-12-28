import re
from datetime import datetime
from flask import Flask,render_template,request,jsonify,make_response,redirect
import json
import logging

app = Flask(__name__)
app.config['DEBUG'] = True
app.static_folder = 'static'

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host="127.0.0.1", port=5000)

# Global variables
hoursPracticed=42
wordsSpoken=62400
accuracy=72.2

uiLanguage=""
learnedLanguage=""

# Pages
@app.route("/", methods=['GET','POST'])
def login():
    responseMsg=""
    if request.method =="POST":
        reqdata=request.form
        username = "inf2002"
        password = "2002"
        if reqdata['username'] == username and reqdata['password']==password:
            return render_template("home.html")
        else:
            responseMsg="Incorrect username or password!"
            return render_template("login.html",response=responseMsg)
    return render_template("login.html",response=responseMsg)

@app.route("/home/")
def home():
    return render_template("home.html")

    
@app.route("/summary/", methods=['GET','POST'])
def summary():
        return render_template("summary.html")

@app.route("/transcript/")
def transcript():
    return render_template("transcript.html")

@app.route("/settings/", methods=['GET','POST'])
def settings():
    global uiLanguage
    global learnedLanguage
    responseMsg=""
    if request.method =="POST":
        reqdata=request.form
        uiLanguage=reqdata['ui-lang']
        learnedLanguage=reqdata["learned-lang"]
        responseMsg="Saved!"
    
    return render_template("settings.html",response=responseMsg)

@app.route("/prelesson-settings/", methods=['GET','POST'])
def prelessonSettings():
    global uiLanguage
    global learnedLanguage
    destination=""
    if request.method =="GET":
        destination=request.args.get('dest')
        return render_template("prelesson-settings.html",destURL=destination)

    return render_template("prelesson-settings.html",destURL=destination)

@app.route("/save-prelesson-settings/", methods=['GET','POST'])
def savePrelessonSettings():
    global learnedLanguage
    if request.method =="POST":
        reqdata=request.form
        learnedLanguage=reqdata["learned-lang"]
        destination=reqdata["destination"]
        return redirect(destination)
    return redirect(destination)

@app.route("/conversation-overview/")
def conversationOverview():
    return render_template("conversation-overview.html")

@app.route("/scenario-overview/")
def scenarioOverview():
    return render_template("scenario-overview.html")

@app.route("/conversation/")
def conversation():
    return render_template("conversation.html")

@app.route("/scenario/")
def scenario():
    return render_template("scenario.html")

@app.route("/pause/")
def pause():
    return render_template("pause.html")