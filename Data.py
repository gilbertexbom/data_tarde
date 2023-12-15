# Classe Data

class Data(object):
    # Método construtor
    def __init__(self, dia, mes, ano):
        self.setMes(mes)
        self.setDia(dia)
        # self.dia = dia obsoleta
        # self.mes = mes obsoleta
        self.ano = ano

    # Encapsulamento
    def getDia(self):
        return self.dia

    def setDia(self, dia):
        if dia >= 1 and dia <= 31:
            if self.getMes() in (4, 6, 9, 11):
                if dia <= 30:
                    self.dia = dia
                else:
                    self.dia = 1
            elif self.getMes() == 2:
                if dia <= 29:
                    self.dia = dia
                else:
                    self.dia = 1
            else:
                self.dia = dia
        else:
            self.dia = 1

    def getMes(self):
        return self.mes

    def setMes(self, mes):
        if mes >= 1 and mes <= 12:
            self.mes = mes
        else:
            self.mes = 1

    def getAno(self):
        return self.ano

    def setAno(self, ano):
        self.ano = ano

    # Método string
    def __str__(self):
        return(
                str(self.getDia()) + '/' +
                str(self.getMes()) + '/' +
                str(self.getAno())
        )
