
import csv
import itertools
import re
class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir(self, nombre, apellidos, celular, edad, correo):
        contacto = Contacto(nombre, apellidos, celular,edad,correo)
        self.contactos.append(contacto)

    def mostrarTodos(self):
        self.submenuOrden()
        for contacto in self.contactos:
            self.imprimeContacto(contacto)
        opcion=str(input(""))

    def buscar(self, textoBuscar):
        encontrado = 0
        for contacto in self.contactos:
            if (re.findall(textoBuscar, contacto.nombre)) or (re.findall(textoBuscar, contacto.apellidos)):
                self.imprimeContacto(contacto)
                encontrado = encontrado + 1
                self.submenuBuscar(contacto.codigo)
        if encontrado == 0:
            self.noEncontrado()

    def borrar(self, codigo):
        for contacto in self.contactos:
            if contacto.codigo == codigo:

                print('\nQuieres borrarlo?\nPresiona 1 para eliminar el contacto:\n')
                opcion = str(input(""))
                if opcion == '1':
                    print('contacto eliminado')
                    del self.contactos[codigo]
                elif opcion != "1":
                    break

    def modificar(self, codigo):
        for contacto in self.contactos:
            if contacto.codigo == codigo:
                del self.contactos[codigo]
                nombre = str(input('Escribe el nombre: '))
                apellidos = str(input('Escribe los apellidos: '))
                celular = str(input('Escribe el numero celular: '))
                edad = str(input('Escribe la edad del contacto: '))
                correo = str(input('Escribe el correo: '))
                contacto = Contacto(nombre.capitalize(), apellidos.capitalize(), celular.capitalize(), edad.capitalize(), correo.capitalize())
                self.contactos.append(contacto)
                break

    def submenuBuscar (self, codigo):

        print('\nQuieres modificarlo:presiona 1\nQuieres borrarlo:presiona 2?\n ')

        opcion = str(input(""))
        if opcion == '1' :
            self.modificar(codigo)
        elif opcion == '2':
            self.borrar(codigo)
        else:
            print('Continuamos sin realizar modificacion alguna')

    def ordenarNombre(self):
        self.contactos.sort(key=lambda contacto: contacto.nombre)

    def ordenarApellidos(self):
        self.contactos.sort(key=lambda contacto: contacto.apellidos)

    def submenuOrden(self):

        print('\n¿Quieres ordenar por la lista por nombre presiona 1?')
        print('\n¿Quieres ordenar por la lista por apellido presiona 2')
        opcion = str(input(""))
        if opcion == '1':
            self.ordenarNombre()
        elif opcion == '2':
            self.ordenarApellidos()

    def grabar(self):
        with open('agenda.csv', 'w') as fichero:
            escribir = csv.writer(fichero)
            escribir.writerow(('codigo', 'nombre', 'apellidos', 'celular', 'edad', 'correo'))
            for contacto in self.contactos:
                escribir.writerow(( contacto.codigo, contacto.nombre, contacto.apellidos, contacto.celular, contacto.edad,contacto.correo))

    def imprimeContacto(self, contacto):
        print('\n\n')

        print('Codigo: {}'.format(contacto.codigo))
        print('Nombre: {}'.format(contacto.nombre))
        print('Apellidos: {}'.format(contacto.apellidos))
        print('Celular: {}'.format(contacto.celular))
        print('Edad: {}'.format(contacto.edad))
        print('Correo: {}'.format(contacto.correo))
        print('\n\n')


    def noEncontrado(self):
        print('\n\n')

        print('Contacto no encontrado')

        print('\n\n')


def ejecutar():
    agenda = Agenda()
    try:
        with open('agenda.csv', 'r') as fichero:
            lector = csv.DictReader(fichero, delimiter=',')
            for fila in lector:
                agenda.añadir(fila['nombre'].capitalize(), fila['apellidos'].capitalize(), fila['celular'].capitalize(),
                              fila['edad'].capitalize(), fila['correo'].capitalize())
    except:
        print('Error al abrir fichero o que no existe aun')
    while True:
        menu = str(input("""
        \nSelecciona una opcion\n
        1:Mostrar lista de contactos
        2:Buscar contacto
        3:Añadir contacto
        0:Salir \n\n               
        """))
        if menu == '1':
            agenda.mostrarTodos()
        elif menu == '2':
            texto = str(input('Escribe el texto a buscar en contactos: '))
            agenda.buscar(texto.capitalize())
            agenda.grabar()
        elif menu == '3':
            nombre = str(input('Escribe el nombre: '))
            apellidos = str(input('Escribe los apellidos: '))
            celular = str(input('Escribe el numero celular: '))
            edad = str(input('Escribe la edad: '))
            correo = str(input('Escribe el correo: '))
            agenda.añadir(nombre.capitalize(), apellidos.capitalize(), celular.capitalize(), edad, correo)
            agenda.grabar()

        elif menu == '0':
            print('Hasta pronto!!!')
            agenda.grabar()
            break
        else:
            print('Opcion no valida!!!')

class Contacto:
    nuevoId = itertools.count()

    def __init__(self, nombre, apellidos, celular, edad, correo):
        self.codigo = next(self.nuevoId)
        self.nombre = nombre
        self.apellidos = apellidos
        self.celular = celular
        self.edad = edad
        self.correo = correo


if __name__ == '__main__':
    ejecutar()
