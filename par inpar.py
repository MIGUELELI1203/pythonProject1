number=0
def welcome_message():
    print("Bienvenido este programa le dice si un numero es par o impar ")
def request_number():
    print("Escriba el numero que desea verificar")
    return int(input())
def verification(number):
    if number%2==0:
        print("El numero escrito es par")
    else:
        print("El numero escrito es inpar")
welcome_message()
number=request_number()
verification(number)