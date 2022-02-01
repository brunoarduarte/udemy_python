# Variáveis
# Devem iniciar com letras, podem conter números
# Deve separar com _
# Letras minúsculas

nome = "Bruno"
idade = 39
altura = 1.91


def get_person_attributes(name, age, heigth):
    message = ''
    majority = ''
    if age > 18:
        message = f"Hi {name}. You are {age} years old and {heigth} meters."
        majority = "You are of legal age."
    else:
        message = f"Hi {name}. You are {age} years old and {heigth} meters."
        majority = "You are not of age."

    return print(message + " " + majority)


get_person_attributes("Bruno", 9, 1.91)
