import psycopg2

class SQLWrapper:

    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname='cc3201' user='public_www' host='localhost' password='hola123'")
            self.cur = self.conn.cursor()
            #nombre de columnas
            self.colnames = []
            #numero de paginas
            self.numpages = 0
        except:
            print "I am unable to connect to the database"
            raise

    def query1(self,data):
        try:
            try:
                self.cur.fetchall()
            except:
            pass
            self.cur.execute("SELECT COUNT(*) from lol.deathvalues WHERE victim LIKE (%s)",("%"+data+"%",))
            self.numpages = (self.cur.fetchone()[0])/100 + 1
            self.cur.execute("SELECT * from lol.deathvalues WHERE victim LIKE (%s)",("%"+data+"%",))
            self.colnames = [desc[0] for desc in self.cur.description]
        except:
            print "Can't execute query"

    #fetch los siguientes 100 resultados
    def fetch(self):
        return self.cur.fetchmany(100)
