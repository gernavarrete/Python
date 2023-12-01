


def create_user(nombre:str, dni:int, edad:int, db_users:list):
    user:dict = {
         "dni" : dni,
         "nombre": nombre,
         "edad": edad   
        }
    
    if db_users is None:
        print("DB not exist")
        return
    
    db_users.append(user)

    print(db_users)

    return