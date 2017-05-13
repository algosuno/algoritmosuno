from Cola import Cola
import random

class TorreDeControl:
    def __init__(self):
        self.aterrizar=Cola()
        self.despegar=Cola()
    def reconocimiento(self):
        for x in range(random.randrange(2)):
            self.aterrizar.encolar('avion')
        for x in range(random.randrange(2)):
            self.despegar.encolar('avion')
    def accion(self):
        if len(self.aterrizar)<len(self.despegar):
            return self.despegar.desencolar()
        else:
            return self.aterrizar.desencolar()
    def __str__(self):
        return 'Hay {} aviones esperando para aterrizar y {} para despegar'.format(len(self.aterrizar),len(self.despegar))

def ejecutar():
    t=TorreDeControl()
    while True:
        try:
            print('Reconociendo...')
            t.reconocimiento()
            print(t)
            t.accion()
            print('Despegando o aterrizando un avion')
        except ValueError:
            print('No hay mas aviones')
            break

ejecutar()