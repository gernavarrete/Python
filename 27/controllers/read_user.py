def read_user(dni:int, db_users:list = None)->None:
    if db_users is None:
        print("DB not exist")
        return None
    
    user_list:list = [
        user
        for user in db_users
        if user.get("dni") == dni
        ]

    if len(user_list) == 0:
        return {}

    user:dict = user_list[0]

    print(
        f""" 
        El usuario buscado es:
            {user.get("nombre")} de {user.get("edad")} anios.

    """)

    return user