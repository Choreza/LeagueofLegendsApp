
#Class que toma los datos obtenidos por las queries y retorna un string en html

class Parser:
    def __tagGenerator(self,tag):
        def func(text):
            return "<" + tag + ">" + text + "</" + tag + ">"
        return func

    def __init__(self):
        self.thead = self.__tagGenerator("thead")
        self.tbody = self.__tagGenerator("tbody")

        self.tr = self.__tagGenerator("tr")
        self.th = self.__tagGenerator("th")
        self.td = self.__tagGenerator("td")

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
