class Pila:
    def _init__(self):
        self.pila=[]

    def apilar(self,x):
        self.pila.append(x)
    def desapilar(self):
        if len(self.pila)==0:
            raise IndexError('La pila esta vacia')
        return self.pila.pop()
    def esta_vacia(self):
        return len(self.pila)==0