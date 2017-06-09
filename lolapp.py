from flask import Flask, render_template, request, redirect, url_for
from parser import Parser
from SQLWrapper import SQLWrapper

parser = Parser()
SQL = SQLWrapper()
application = Flask(__name__)


@application.route("/")
def hello():
    return render_template("request1.html")


@application.route("/test/<name>")
def hola(name):
    SQL.query1(name)
    data = parser.tableheader(SQL.colnames)
    data += parser.tableBody(SQL.fetch())
    return render_template("test.html", data=data)


@application.route("/grupo07/handle_data", methods=['GET', 'POST'])
def handle_data():
    name = request.form['projectFilepath']
    print request.method
    if request.method == "GET":
        return render_template("request1.html")
    else:
        return "<h1>It works!</h1>"
