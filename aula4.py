# Tipos primitivos
# str - string - "texto" 'texto'
# int - inteiro - 1234 -12 0
# float - real/ponto flutuante - 3.5 9.93129319
# bool - booleano/lógico - True/False

print('Bruno Araujo Duarte', type('Bruno Araujo Duarte'))
print(39, type(39))
print(1.91, type(1.91))


def is_majority(age):
    if age > 18:
        print('Maior de idade', type(age > 18))
    else:
        print('Menor de idade', type(age < 18))


is_majority(9)
