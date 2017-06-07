from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>gabriel ql!</h1>"

@application.route("/test")
def hola():
    return "<h1 style='color:blue'>Holi :V</h1>"

