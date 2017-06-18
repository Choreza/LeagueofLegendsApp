from flask import Flask, render_template, request, redirect, url_for
from parser import Parser
from SQLWrapper import SQLWrapper

DEBUG = True
parser = Parser()
SQL = SQLWrapper()
application = Flask(__name__)


@application.route("/index")
def welcome_page():
    return render_template("index.html")


@application.route("/test/<name>")
def hola(name):
    name = name.capitalize()
    if DEBUG:
        print name
    SQL.queryChampionSeason(name)
    #data = parser.tableheader(SQL.colnames)
    data = parser.parseChampionQuery("Winrate por Season",SQL.colnames,SQL.fetch())
    data += "<br>"
    SQL.queryChampionYear(name)
    data += parser.parseChampionQuery("Winrate por Anho"A,SQL.colnames, SQL.fetch())
    if DEBUG:
        print data
        print str(SQL.colnames)
    #data += parser.tableBody(SQL.fetch())
    return render_template("test.html", titulo=name, data=data)


@application.route("/handle_data", methods=['POST'])
def handle_data():
    name = str(request.form['projectFilepath']).strip().lower()
    if DEBUG:
        print name
    return redirect(url_for("hola", name=name))


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
