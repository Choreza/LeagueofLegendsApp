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

    def query1(self, data):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            # self.cur.execute("SELECT COUNT(*) from lol.deathvalues WHERE victim LIKE (%s)",("%"+data+"%",))
            # self.numpages = (self.cur.fetchone()[0])/100 + 1
            self.cur.execute("SELECT * from lol.deathvalues WHERE victim LIKE (%s)", ("%" + data + "%",))
            self.colnames = [desc[0] for desc in self.cur.description]
            try:
                assert isinstance(self.cur.rowcount, int)
            except:
                print "cago rowcount"
            self.numpages = self.cur.rowcount
            print "rows: " + str(self.numpages)
        except Exception, e:
            print str(e)
            print "Can't execute query"

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

    def queryMatchBySeason(self, season, order="ASC"):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            if order == "DESC":
                self.cur.execute(
                "SELECT blueteamtag AS BlueTeam, redteamtag AS RedTeam, bresult, rresult, TO_CHAR((gamelength || ' minute')::interval, 'HH24:MI') AS Duración, year AS Año, season AS Temporada FROM lol.leagueoflegends WHERE season = (%s) ORDER BY año DESC",
                (season, ))
            else:
                self.cur.execute(
                "SELECT blueteamtag AS BlueTeam, redteamtag AS RedTeam, bresult, rresult, TO_CHAR((gamelength || ' minute')::interval, 'HH24:MI') AS Duración, year AS Año, season AS Temporada FROM lol.leagueoflegends WHERE season = (%s) ORDER BY año ASC",
                (season, ))
            self.colnames = [desc[0].capitalize() for desc in self.cur.description]
        except Exception, e:
            print str(e)
            print "Can't execute query"

    def queryMatchByDate(self, date, order="ASC"):
        try:
            try:
                self.cur.fetchall()
            except:
                pass
            if order == "DESC":
                self.cur.execute(
                "SELECT blueteamtag AS BlueTeam, redteamtag AS RedTeam, bresult, rresult, TO_CHAR((gamelength || ' minute')::interval, 'HH24:MI') AS Duración, year AS Año, season AS Temporada FROM lol.leagueoflegends WHERE year = (%s) ORDER BY temporada DESC",
                (date, ))
            else:
                 self.cur.execute(
                "SELECT blueteamtag AS BlueTeam, redteamtag AS RedTeam, bresult, rresult, TO_CHAR((gamelength || ' minute')::interval, 'HH24:MI') AS Duración, year AS Año, season AS Temporada FROM lol.leagueoflegends WHERE year = (%s) ORDER BY temporada ASC",
                (date, ))
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
