class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print('Estudiando...')

nombre = input('Ingresa tu nombre:')
edad = input('Ingresa tu edad: ')
grado = input('Por ultimo, su grado: ')

estudiante = Estudiante(nombre, edad, grado)
print(f'''
        DATOS DEL ESTUDIANTE: \n\n
        Nombre: {estudiante.nombre} \n
        Edad: {estudiante.edad} \n
        Grado: {estudiante.grado}

        ''')

while True:
    estudiar = input()
    if (estudiar.lower() == 'estudiar'):
        estudiante.estudiar()