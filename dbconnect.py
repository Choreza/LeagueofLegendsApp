from parser import Parser
from SQLWrapper import SQLWrapper

parser = Parser()
SQL = SQLWrapper()

SQL.query1("Bjergsen")
print SQL.numpages
print parser.tableheader(SQL.colnames)
data = SQL.fetch()
print data
print parser.tableBody(data)