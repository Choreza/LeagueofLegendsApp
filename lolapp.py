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
    name = str(name).strip().lower().capitalize()
    print name
    SQL.queryChampion(name)
    data = parser.tableheader(SQL.colnames)
    data += parser.tableBody(SQL.fetch())
    return render_template("test.html", data=data)


@application.route("/handle_data", methods=['POST'])
def handle_data():
    return redirect(home+"/test/"+str(request.form['projectFilepath']))

@application.route("/about")
def about_page():
	return render_template("about.html")

@application.route("/contact")
def contact_page():
	return render_template("contact.html")	

@application.route("/work")
def work_page():
    return render_template("work.html")


@application.route("/work01")
def work01_page():
    return render_template("work01.html")