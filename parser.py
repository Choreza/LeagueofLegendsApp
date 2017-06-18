
#Class que toma los datos obtenidos por las queries y retorna un string en html

class Parser:
    def __tagGenerator(self,tag):
        def func(text):
            return "<" + tag + ">" + text + "</" + tag + ">"
        return func

    def __init__(self):
        self.thead = self.__tagGenerator("thead")
        self.tbody = self.__tagGenerator("tbody")
        self.h2 = self.__tagGenerator("h2")

        self.tr = self.__tagGenerator("tr")
        self.th = self.__tagGenerator("th")
        self.td = self.__tagGenerator("td")

        self.li = self.__tagGenerator("li")
        self.ul = self.__tagGenerator("ul")
        self.b = self.__tagGenerator("b")

    def tableheader(self,header):
        h = ""
        for el in header:
            h += "\n" + self.th(el) + "\n"
        return self.thead("\n" + self.tr(h) + "\n")

    def tableBody(self,rows):
        h = ""
        for row in rows:
            d = ""
            for el in row:
                d += "\n" + self.td(str(el)) + "\n"
            h += "\n" + self.tr(d) + "\n"
        return self.tbody("\n" + h + "\n")

    def parseChampionQuery(self,title,colnames,rows):
        data = self.h2(title)
        data += "<hr>"
        table = ""
        for row in rows:
            nametime = str(row[0])
            lista = ""
            for i in range(1,len(row)):
                items=self.b(colnames[i]+": ") + str(row[i])
                lista+=self.li(items)
            lista = self.li(nametime + self.ul(lista) )
            table += lista
        table = self.ul(table)
        data += table
        return data