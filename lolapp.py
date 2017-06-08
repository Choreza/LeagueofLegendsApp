
from flask import Flask, render_template, request
from parser import Parser
from SQLWrapper import SQLWrapper

parser = Parser()
SQL = SQLWrapper()
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>gabriel ql!</h1>"

@application.route("/test/<name>")
def hola(name):
    SQL.query1(name)
    data = parser.tableheader(SQL.colnames)
    data += parser.tableBody(SQL.fetch())
    return render_template("test.html",data=data)

@application.route("/handle_data",methods=['POST'])
def handler():
    projectpath = request.form['projectFilepath']
    print projectpath