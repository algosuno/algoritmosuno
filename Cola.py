class _Nodo:
    def __init__(self,dato=None,prox=None):
        self.dato=dato
        self.prox=prox
    def __str__(self):
        return str(self.dato)
    
class Cola:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.len=0
    def encolar(self,x):
        nuevo= _Nodo(x)
        if self.ultimo is not None:
            self.ultimo.prox=nuevo
            self.ultimo=nuevo
        else:
            self.primero=nuevo
            self.ultimo=nuevo
        self.len+=1
    def desencolar(self):
        if self.primero is None:
            raise ValueError('La cola esta vacia')
        dato=self.primero
        self.primero=self.primero.prox
        if not self.primero:
            self.ultimo=None
        self.len-=1
        return dato
    def __len__(self):
        return self.len
    