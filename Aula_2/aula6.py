# Variáveis
# Devem iniciar com letras, podem conter números
# Deve separar com _
# Letras minúsculas

nome = "Bruno"
idade = 39
altura = 1.91
peso = 100


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


def get_imc(heigth, weigth):
    imc = weigth / (heigth * heigth)
    return round(imc, 2)


# É possível multiplicar um int por float. O resultado será um float
print(idade * altura)

get_person_attributes(nome, idade, altura)
print('Seu imc é ', get_imc(altura, peso))
