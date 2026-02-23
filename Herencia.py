class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print('Hola, estoy hablando un poco')

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, salario, empresa):
        super().__init__(nombre, edad, nacionalidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        return(f'Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.nacionalidad}. Trabajo en {self.empresa} y gano {self.salario} pesos')

class Estudiante(Persona):
    def __init__(self,nombre, edad, nacionalidad, notas, universidad):
        Persona.__init__(self, nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

roberto = Empleado('Roberto', 43, 'argentino', 50000, 'Google')

print(roberto.presentarse())