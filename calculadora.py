result=0
option=0
numberone=0
numberotwo=0
def messaje_of_welcome():
    print("Bienvenido, aca podra hacer las operaciones matematicas basicas")

def menu():
    print("escriba el respectivo numero segun la operacion que desee realizar")
    print("1.suma")
    print("2.resta")
    print("3.multiplicacion")
    print("4.division")
    print("5.teminar la calculadora")
    return int(input())
def request_numberone():
    print("escriba el primer numero a operar")
    return int(input())
def request_numbertwo():
    print("escriba el segundo numero a operar")
    return int(input())
def suma(numberone,numbertwo):
    print("la suma entre los numeros que ingreso es: ",numberone+numbertwo)

def resta(numberone,numbertwo):
    print("la resta entre los numeros que ingreso es: ",numberone-numbertwo)

def multiplicacion(numberone,numbertwo):
    print("la multiplicacion entre los numeros que ingreso es: ",numberone*numbertwo)

def division(numberone,numbertwo):
    if numbertwo==0:
        print("no se puede dividir entre cero")
    else:
     print("la division entre los numeros que ingreso es: ",numberone/numbertwo)

messaje_of_welcome()

while option != 5:
    option = menu()


    if option == 1:
        numberone = request_numberone()
        numbertwo = request_numbertwo()
        suma(numberone, numbertwo)

    elif option == 2:
        numberone = request_numberone()
        numbertwo = request_numbertwo()
        resta(numberone, numbertwo)

    elif option == 3:
        numberone = request_numberone()
        numbertwo = request_numbertwo()
        multiplicacion(numberone, numbertwo)
    elif option == 4:
        numberone = request_numberone()
        numbertwo = request_numbertwo()
        division(numberone, numbertwo)
    elif option == 5:
        print("Hasta pronto")
    else:
        print("el valor ingresado no es ninguna de las opciones ,vuelve a intentarlo")



