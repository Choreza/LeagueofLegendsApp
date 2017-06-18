#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


@application.route("/season")
def season_page():
    return render_template("season_search.html")


@application.route("/date")
def date_page():
    return render_template("date_search.html")


@application.route("/player")
def player_page():
    return render_template("player_search.html")


@application.route("/champion")
def champion_page():
    return render_template("champion_search.html")


@application.route("/champion/<name>")
def champion_match(name):
    name = name.capitalize()
    if DEBUG:
        print name
    SQL.queryChampionSeason(name)
    # data = parser.tableheader(SQL.colnames)
    data = parser.parseChampionQuery("Winrate por Season", SQL.colnames, SQL.fetch())
    data += "<br>"
    SQL.queryChampionYear(name)
    data += parser.parseChampionQuery("Winrate por Año", SQL.colnames, SQL.fetch())
    if DEBUG:
        print data
        print str(SQL.colnames)
    # data += parser.tableBody(SQL.fetch())
    return render_template("champion.html", titulo=name, data=data)


@application.route("/season/<season>/<order>")
def season_matchs(season, order):
    if DEBUG:
        print season + order
    SQL.queryMatchBySeason(season, order)

    data = parser.tableheader(SQL.colnames)
    data += "<br>"

    data += parser.tableBody(SQL.fetch())
    return render_template("season.html", season_name=season, data=data)


@application.route("/date/<date>/<order>")
def date_matchs(date, order):
    SQL.queryMatchByDate(date, order)

    data = parser.tableheader(SQL.colnames)
    data += "<br>"
    data += parser.tableBody(SQL.fetch())
    return render_template("date.html", date_name=date, data=data)


@application.route("/player/<name>")
def player1_matchs(name):
    SQL.queryMatchByPlayer1(name)

    data = parser.tableheader(SQL.colnames)
    data += "<br>"
    data += parser.tableBody(SQL.fetch())
    return render_template("player.html",player_name = name, data = data)


@application.route("/handle_season", methods=['POST'])
def handle_season():
    season = str(request.form['seasonGetter'])
    order = str(request.form['orderGetter'])
    if DEBUG:
        print season
        print order
    return redirect(url_for("season_matchs", season=season, order=order))


@application.route("/handle_champion", methods=['POST'])
def handle_champion():
    name = str(request.form['championName']).strip().lower()
    if DEBUG:
        print name
    return redirect(url_for("champion_match", name = name))


@application.route("/handle_player1", methods=['POST'])
def handle_player1():
    name = str(request.form['playerName'])
    return redirect(url_for("player1_matchs", name=name))


@application.route("/handle_date", methods=["POST"])
def handle_date():
    date = str(request.form['dateGetter'])
    order = str(request.form['orderGetter'])
    if DEBUG:
        print date
        print order
    return redirect(url_for("date_matchs", date=date, order=order))

