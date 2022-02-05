# Entrada de dados

# O input sempre retornará str

# name = input('Qual é o seu nome? ')

# idade = int(input('Qual é a sua idade? '))

# print(f"{name} tem {idade} anos")

# Calculadora
num_1 = input('Digite um número: ')
operator = input('Digite o tipo de Operação (+, -, *, / ou **): ')
num_2 = input('Digite outro número: ')


def calculator(num1, op, num2):
    if num1 != int or num2 != int:
        return print('Os parâmetro informados deves ser números!')
    if op == '+':
        return print(int(num1) + int(num2))
    elif op == '-':
        return print(int(num1) - int(num2))
    elif op == '*':
        return print(int(num1) * int(num2))
    elif op == '/':
        return print(int(num1) / int(num2))
    elif op == '**':
        return print(int(num1) ** int(num2))
    else:
        return print('Operador inválido')


calculator(num_1, operator, num_2)
