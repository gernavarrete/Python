from create import user_created
from controllers.read_user import read_user
from controllers.create_user import create_user
from controllers.delete_user import delete_user
from controllers.update_user import update_user


## --- Functions ----

def greeting()->None:
    print("imprimo por pantalla")

greeting()



users = []
print(users)


## CRUD

def main():
    option:str = input(f"""
          Bienvenido
          Que operacion desea realizar?
          a - Create
          b - Read
          c - Update
          d - Delete
          """)

    if option == "a":
        nombre:str = input("Ingrese nombre\n")
        edad:int = input("Ingrese Edad\n")
        dni:int =input("Ingrese numero de DNI\n")
        create_user(nombre,dni,edad,users)
        return
    if option == "b":
        dni:int = input("Ingrese DNI\n")
        read_user(dni,users)
        return
    if option == "c":
        dni:int = input("Ingrese DNI")
        update_user(dni,users)
        return
    if option == "d":
        dni:int =  input("Ingrese DNI a borrar\n")
        delete_user(dni,users)
        return

main()