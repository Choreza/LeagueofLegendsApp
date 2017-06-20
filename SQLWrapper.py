#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2


class SQLWrapper:
    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname='cc3201' user='public_www' host='localhost' password='hola123'")
            self.cur = self.conn.cursor()
            # nombre de columnas
            self.colnames = []
            # numero de paginas
            self.numpages = 0
        except:
            print "I am unable to connect to the database"
            raise



    def queryChampionSeason(self, data):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            self.cur.execute(
                "SELECT foo.season,foo.wins,bar.total, round((CAST(foo.wins AS NUMERIC )*100 / bar.total),2) AS winrate FROM (SELECT season,COUNT(season) AS wins FROM lol.leagueoflegends WHERE ((%s) IN (redtopchamp,redjunglechamp,redmiddlechamp,redadcchamp,redsupportchamp) AND rresult IS true) OR ((%s) IN (bluetopchamp,bluejunglechamp,bluemiddlechamp,blueadcchamp,bluesupportchamp) AND bresult IS true) GROUP BY season) foo, (SELECT season,COUNT(season) AS total FROM lol.leagueoflegends WHERE (%s) IN (redtopchamp,redjunglechamp,redmiddlechamp,redadcchamp,redsupportchamp,bluetopchamp,bluejunglechamp,bluemiddlechamp,blueadcchamp,bluesupportchamp) GROUP BY (season) ) bar WHERE foo.season = bar.season",
                (data, data, data))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"

    def queryMatchBySeason(self, season, order="ASC", offset = 1):
        offset = int(offset)-1
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            if order == "DESC":
                self.cur.execute(
                "SELECT blueteamtag AS BlueTeam, redteamtag AS RedTeam, bresult, rresult, TO_CHAR((gamelength || ' minute')::interval, 'HH24:MI') AS Duración, year AS Año, season AS Temporada FROM lol.leagueoflegends WHERE season = (%s) ORDER BY año DESC LIMIT 100 OFFSET (%s)",
                (season,offset*100 ))
            else:
                self.cur.execute(
                "SELECT blueteamtag AS BlueTeam, redteamtag AS RedTeam, bresult, rresult, TO_CHAR((gamelength || ' minute')::interval, 'HH24:MI') AS Duración, year AS Año, season AS Temporada FROM lol.leagueoflegends WHERE season = (%s) ORDER BY año ASC LIMIT 100 OFFSET (%s)",
                (season,offset*100 ))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"

    def queryMatchByDate(self, date, order="ASC",offset = 1):
        offset = int(offset)-1
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            if order == "DESC":
                self.cur.execute(
                "SELECT blueteamtag AS BlueTeam, redteamtag AS RedTeam, bresult, rresult, TO_CHAR((gamelength || ' minute')::interval, 'HH24:MI') AS Duración, year AS Año, season AS Temporada FROM lol.leagueoflegends WHERE year = (%s) ORDER BY temporada DESC LIMIT 100 OFFSET (%s)",
                (date, offset*100))
            else:
                 self.cur.execute(
                "SELECT blueteamtag AS BlueTeam, redteamtag AS RedTeam, bresult, rresult, TO_CHAR((gamelength || ' minute')::interval, 'HH24:MI') AS Duración, year AS Año, season AS Temporada FROM lol.leagueoflegends WHERE year = (%s) ORDER BY temporada ASC LIMIT 100 OFFSET (%s)",
                (date, offset*100))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"


    def queryMatchByPlayer1(self,data):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            self.cur.execute(
                "SELECT campeon, COUNT(campeon) AS conteo FROM lol.lolcito WHERE invocador= (%s) GROUP BY(campeon) ORDER BY conteo DESC",(data, ))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"

    def queryMatchByPlayer2(self,data):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            self.cur.execute(
                "SELECT year, COUNT(invocador) AS conteo FROM lol.lolcito WHERE invocador= (%s) GROUP BY(year) ORDER BY year DESC",(data, ))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"


    def queryMatchByPlayer3(self, data):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            self.cur.execute(
                "SELECT DISTINCT(team) FROM lol.lolcito WHERE invocador = (%s)",(data,))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"


    def queryMatchByPlayer4(self, data):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            self.cur.execute(
                "SELECT foo.year,foo.death,bar.kills, ROUND((CAST(foo.death AS numeric)/bar.kills)*100,2) as deathKillRatio from (SELECT B.year,count(A.lvictim) as death FROM lol.deathvalues A,lol.leagueoflegends B where lvictim = (%s) AND A.matchhistory = B.matchhistory GROUP BY(B.year)) foo, (SELECT B.year,count(A.lkiller) as kills FROM lol.deathvalues A,lol.leagueoflegends B where lkiller = (%s) AND A.matchhistory = B.matchhistory GROUP BY(B.year)) bar WHERE foo.year = bar.year ORDER BY foo.year",(data,data))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"


    def queryTeamYear(self, data):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            self.cur.execute("SELECT winstable.year AS year, wins, totalgames, ROUND(CAST(wins AS NUMERIC)*100/totalgames,2) AS winrate FROM (SELECT team, year, COUNT(team) AS wins FROM lol.lolcito WHERE team = (%s) AND resultado = true GROUP BY (team, year)) winstable, (SELECT team, year, COUNT(team) AS totalgames FROM lol.lolcito WHERE team = (%s) GROUP BY (team, year)) totaltable WHERE winstable.year = totaltable.year ORDER BY year ASC", (data, data))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"

    def queryTeamSeason(self, data):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            self.cur.execute("SELECT winstable.season AS season, wins, totalgames, ROUND(CAST(wins AS NUMERIC)*100/totalgames,2) AS winrate FROM (SELECT season, COUNT(*) AS wins FROM lol.leagueoflegends WHERE (blueteamtag = (%s) AND bresult = true) OR (redteamtag = (%s) AND rresult = true) GROUP BY (season)) winstable, (SELECT season, COUNT(*) AS totalgames FROM lol.leagueoflegends WHERE blueteamtag = (%s) OR redteamtag = (%s) GROUP BY (season)) totaltable WHERE winstable.season = totaltable.season ORDER BY season ASC", (data, data, data, data))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"
    
    def queryTeamInvocadores(self, data):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            self.cur.execute("SELECT invocador FROM lol.lolcito WHERE team = (%s) GROUP BY(invocador)", (data,))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"

    def queryTeamChampionByYear(self, data):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            self.cur.execute("SELECT campeon, year, COUNT(*) AS conteo FROM lol.lolcito WHERE team = (%s) GROUP BY (campeon, year)  ORDER BY year DESC, conteo DESC", (data,))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"

    def queryChampionYear(self, data):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            self.cur.execute(
                "select foo.year,foo.wins,bar.total, round((CAST(foo.wins AS NUMERIC )*100 / bar.total),2) as winrate from (select year,count(year) as wins from lol.leagueoflegends  where ((%s) in (redtopchamp,redjunglechamp,redmiddlechamp,redadcchamp,redsupportchamp) and rresult is true) or ((%s) in (bluetopchamp,bluejunglechamp,bluemiddlechamp,blueadcchamp,bluesupportchamp) and bresult is true) group by year) foo, (select year,count(year) as total from lol.leagueoflegends  where (%s) in (redtopchamp,redjunglechamp,redmiddlechamp,redadcchamp,redsupportchamp,bluetopchamp,bluejunglechamp,bluemiddlechamp,blueadcchamp,bluesupportchamp) group by (year) ) bar where foo.year = bar.year;",
                (data, data, data))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"

    def queryTeamVersus(self, team1, team2, order,offset = 0):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            if order == "DESC":
                self.cur.execute("SELECT matchHistory AS informacioncompleta, redteamtag AS equiporojo, blueteamtag AS equipoazul, rresult AS resultadoequiporojo, bresult AS resultadoequipoazul, season AS Temporada, year AS Año FROM lol.leagueoflegends WHERE (blueteamtag=(%s) AND redteamtag=(%s)) OR (blueteamtag=(%s) AND redteamtag=(%s)) ORDER BY year DESC LIMIT 100 OFFSET (%s)",(team1,team2,team2,team1,offset*100))
            else:
                self.cur.execute("SELECT matchHistory AS informacioncompleta, redteamtag AS equiporojo, blueteamtag AS equipoazul, rresult AS resultadoequiporojo, bresult AS resultadoequipoazul, season AS Temporada,year AS  Año FROM lol.leagueoflegends WHERE (blueteamtag=(%s) AND redteamtag=(%s)) OR (blueteamtag=(%s) AND redteamtag=(%s)) ORDER BY year ASC LIMIT 100 OFFSET (%s)",(team1,team2,team2,team1,offset*100))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"

    def queryChampionBan(self, name):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            self.cur.execute("SELECT season, year, COUNT(*) AS conteo FROM lol.banvalues ban, lol.leagueoflegends loldata WHERE (ban_1 = (%s) OR ban_2 = (%s) OR ban_3 = (%s) OR ban_4 = (%s) OR ban_5 = (%s)) AND ban.matchhistory = loldata.matchhistory GROUP BY (season, year) ORDER BY year DESC;", (name, name, name, name, name))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"

    # fetch los siguientes 100 resultados
    def fetch(self):
        try:
            return self.cur.fetchmany(100)
        except Exception, e:
            print str(e)
            print self.cur.query
