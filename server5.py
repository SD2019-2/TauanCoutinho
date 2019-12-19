import Pyro4

@Pyro4.expose
class Nadador(object):
    def categoria(self, idade):
        if (idade >= 5 and idade <= 7):
            return "infantil A"
        elif (idade >= 8 and idade <= 10):
            return "infantil B"
        elif (idade >= 11 and idade <= 13):
            return "juvenil A"
        elif (idade >= 14 and idade <= 17):
            return "juvenil B"
        elif (idade >= 18):
            return "adulto"
        else:
            return "idade invalida"

daemon = Pyro4.Daemon(host="tauan-Aspire-A515-51G")
ns = Pyro4.locateNS()
uri = daemon.register(Nadador)
ns.register("identificador", uri)
daemon.requestLoop()
