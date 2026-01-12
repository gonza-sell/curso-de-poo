class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print('Hola, estoy hablando un poco')

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        print(f'Mi habilidad es: {self.habilidad}')

class EmpleadoArtista(Persona, Artista):
    def __init__(self,nombre, edad, nacionalidad,habilidad, salario, empresa):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario    

class Estudiante(Persona):
    def __init__(self,nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

roberto = Empleado('Roberto', 43, 'argentino', 'apicultor', 50000)

roberto.hablar()