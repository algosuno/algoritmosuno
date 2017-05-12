class Colectivo:
    def __init__(self):
        self.estado={}

    def subir(self, destino, persona):
        self.estado[destino]=self.estado.get(destino,[])
        self.estado[destino].append(persona)

    def bajar(self, destino):
        return self.estado[destino]

    