user = "user@1203uptc.edu.co"
password = "123456789"
user_two="user@12uptc.edu.co"
password_two="987654321"
user_ingress=0
password_ingress=0
def messaje_of_welcome():
    print("Bienvenido, a continuacion debera ingresar sus datos para verificar su Identidad")


def request_usuario():
    print("ingrese el usuario")
    return str(input())


def comprobar_usuario(user,user_ingress):
    if user == user_ingress :
        print("Ingrese su contraseña")
        return str(input())
    elif user_two ==user_ingress:
        print("Ingrese su contraseña")
        return str(input())
    else:
        print("Usuario incorrecto,vuelve a intentarlo")



def comprobar_contraseña(password,password_ingress):
    if password==password_ingress:
        print("Bienvenido a tu cuenta")
    elif password_two == password_ingress:
        print("Bienvenido a tu cuenta")
        return str(input())
    else:
         print("contraseña incorrecta ,vuelve a intentarlo")

messaje_of_welcome()

user_ingress=request_usuario()

password_ingress=comprobar_usuario(user,user_ingress)

comprobar_contraseña(password,password_ingress)

print("fin")