from .read_user import read_user
from .create_user import create_user

def update_user(dni:int,db_users:list = None)->None:
    user = read_user(dni, db_users)

    if user == None:
        return

    if len(user) == 0:
        print("user not exist, proceed to create")
        nombre:str = input("Ingrese el nombre\n")
        edad:int = input("Ingrese la edad\n")
        create_user(nombre,dni,edad, db_users)
        return
    
    key = input("What value do you want to modify?\n Value: nombre or edad")
    value = input("Input new value:\n")

    user[key] = value

    for index, user in enumerate(db_users):
        if user["dni"] == dni:
            db_users[index] = user

    print("User has been update!")