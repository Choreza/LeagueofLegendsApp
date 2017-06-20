#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from parser import Parser
from SQLWrapper import SQLWrapper

DEBUG = False
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


@application.route("/date")
def date_page():
    return render_template("date_search.html")


@application.route("/player")
def player_page():
    return render_template("player_search.html")


@application.route("/champion")
def champion_page():
    return render_template("champion_search.html")

@application.route("/team")
def team_page():
    return render_template("team_search.html")

@application.route("/game")
def game_page():
    return render_template("game_search.html")

@application.route("/game/<team1>/<team2>/<order>/<offset>")
def game_matchs(team1=None, team2=None, order=None, offset = 1):
    order = order.upper()
    SQL.queryTeamVersus(team1, team2, order,int(offset)-1)
    data = parser.tableheader(SQL.colnames)
    data += parser.tableBody(SQL.fetch())
    return render_template("game.html", team1=team1, team2=team2, order=order, data=data, offset=offset)


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
    
    SQL.queryChampionBan(name)
    data2 = "<br>"
    data2 += "<h2>Historial de baneos</h2>"
    data2 += "<hr>"
    data2 += parser.tableheader(SQL.colnames)
    data2 += "<br>"
    data2 += parser.tableBody(SQL.fetch())
    if DEBUG:
        print data
        print str(SQL.colnames)
    # data += parser.tableBody(SQL.fetch())
    return render_template("champion.html", titulo=name, data=data, data2=data2)

@application.route("/season/<season>/<order>/<offset>")
def season_matchs(season, order, offset = 1):
    if DEBUG:
        print season + order
    SQL.queryMatchBySeason(season, order, offset)

    data = parser.tableheader(SQL.colnames)
    data += "<br>"

    data += parser.tableBody(SQL.fetch())
    return render_template("date.html", date_name=season,season = season, data=data, offset = offset)


@application.route("/date/<date>/<order>/<offset>")
def date_matchs(date, order, offset = 1):
    SQL.queryMatchByDate(date, order, offset)

    data = parser.tableheader(SQL.colnames)
    data += "<br>"
    data += parser.tableBody(SQL.fetch())
    return render_template("date.html", date_name=date,order=order, data=data, offset = offset)


@application.route("/team/<name>")
def team_matchs(name):
    SQL.queryTeamInvocadores(name)
    data = parser.tableheader(SQL.colnames)
    data += "<br>"
    data += parser.tableBody(SQL.fetch())

    SQL.queryTeamSeason(name)
    data2 = parser.tableheader(SQL.colnames)
    data2 += "<br>"
    data2 += parser.tableBody(SQL.fetch())

    SQL.queryTeamYear(name)
    data3 = parser.tableheader(SQL.colnames)
    data3 += "<br>"
    data3 += parser.tableBody(SQL.fetch())

    SQL.queryTeamChampionByYear(name)
    data4 = parser.tableheader(SQL.colnames)
    data4 += "<br>"
    data4 += parser.tableBody(SQL.fetch())

    return render_template("team.html", team_name=name, data=data, data2=data2, data3=data3, data4=data4)

@application.route("/player/<name>")
def player1_matchs(name):
    SQL.queryMatchByPlayer1(name)

    data = parser.tableheader(SQL.colnames)
    data += "<br>"
    data += parser.tableBody(SQL.fetch())

    SQL.queryMatchByPlayer2(name)
    data2 = parser.tableheader(SQL.colnames)
    data2 += "<br>"
    data2 += parser.tableBody(SQL.fetch())

    SQL.queryMatchByPlayer3(name)
    data3 = parser.tableheader(SQL.colnames)
    data3 += "<br>"
    data3 += parser.tableBody(SQL.fetch())

    return render_template("player.html",player_name = name, data = data, data2 = data2, data3 = data3)


@application.route("/handle_season", methods=['POST'])
def handle_season():
    season = str(request.form['seasonGetter'])
    order = str(request.form['orderGetter'])
    if DEBUG:
        print season
        print order
    return redirect(url_for("season_matchs", season=season, order=order, offset = 1))


@application.route("/handle_champion", methods=['POST'])
def handle_champion():
    name = str(request.form['championName']).strip().lower()
    if DEBUG:
        print name
    return redirect(url_for("champion_match", name = name))


@application.route("/handle_player1", methods=['POST'])
def handle_player1():
    name = str(request.form['playerName']).strip().lower().capitalize()
    return redirect(url_for("player1_matchs", name=name))


@application.route("/handle_date", methods=["POST"])
def handle_date():
    date = str(request.form['dateGetter'])
    order = str(request.form['orderGetter'])
    if DEBUG:
        print date
        print order
    return redirect(url_for("date_matchs", date=date, order=order, offset = 1))

@application.route("/handle_team", methods=["POST"])
def handle_team():
    name = str(request.form['teamName']).strip().upper()
    return redirect(url_for("team_matchs", name=name))

@application.route("/handle_game", methods=["POST"])
def handle_game():
    team1 = str(request.form['team1']).strip()
    team2 = str(request.form['team2']).strip()
    order = str(request.form['orderGetter'])
    return redirect(url_for("game_matchs", team1=team1, team2=team2, order=order, offset = 1 ))