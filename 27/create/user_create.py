import random


def user_created(amount:int)->list:
    users:list = []
    for _ in range(amount):
        nombre = random.choice(["Lore", "Eva", "Oliver", "German"])
        apellido = random.choice(["Navarrete", "Vardaro"])
        users.append({
            "nombre": nombre,
            "apellido":apellido
        })
    
    return users