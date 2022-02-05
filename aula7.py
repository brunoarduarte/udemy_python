# Manipulando strings
nome = "Bruno"
idade = 39
altura = 1.91
peso = 100
imc = peso / (altura**2)

print(nome, "tem", idade, "anos de idade e seu IMC é ", imc)
print(f"{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}")
print("{} tem {} anos de idade e seu IMC é {:.2f}".format(nome, idade, imc))
print("{0} tem {1} anos de idade e seu IMC é {2:.2f}".format(nome, idade, imc))
print(
    "{n} tem {id} anos de idade e seu IMC é {im:.2f}".format(
        n=nome, id=idade, im=imc
    )
)
