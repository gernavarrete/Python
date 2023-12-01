from .read_user import read_user


def delete_user(dni:int, db_users:list = None):
    if db_users is None:
        print("DB not exist")
        return
    
    user:dict = read_user(dni, db_users)

    if len(user) == 0:
        print("user not exist!")
        return

    for index,u in enumerate(db_users):
        if u["dni"] == user["dni"]:
            db_users.pop(index)

    return