radio=0
def messaje_of_welcome():
    print("Bienvenido ,este programa le dice el area de un circulo")
def request_radio():
    print("Escriba el radio del circulo")
    return int(input())
def area_circle(radio):
    print("El area del circulo que ingreso es:",radio*radio*3.1416)
messaje_of_welcome()
radio=request_radio()
area_circle(radio)