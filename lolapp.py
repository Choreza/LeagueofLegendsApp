from flask import Flask, render_template, request, redirect, url_for
from parser import Parser
from SQLWrapper import SQLWrapper

parser = Parser()
SQL = SQLWrapper()
application = Flask(__name__)
home = "http://cc3201.dcc.uchile.cl/grupo07"

@application.route("/")
def hello():
    return render_template("index.html")


@application.route("/test/<name>")
def hola(name):
    SQL.query1(name)
    data = parser.tableheader(SQL.colnames)
    data += parser.tableBody(SQL.fetch())
    return render_template("test.html", data=data)


@application.route("/handle_data", methods=['POST'])
def handle_data():
    return redirect(home+"/test/"+str(request.form['projectFilepath']))
