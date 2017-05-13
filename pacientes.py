from Cola import Cola

class ColaDePacientes:
    def __init__(self):
        self.pacientes=Cola()
    def nuevo_paciente(self,nombre):
        self.pacientes.encolar(nombre)
    def proximo_paciente(self):
        return self.pacientes.desencolar()

class Recepcion:
    def __init__(self):
        self.doctores={}
    def nuevo_paciente(self,paciente,medico):
        self.doctores[medico]=ColaDePacientes().nuevo_paciente(paciente)
    def proximo_paciente(self,paciente):
        
        