# Criar variáveis para nome(str), idade(int), altura(float)
# e peso(int) de uma pessoa
# Criar uma variável com o ano atual(int)
# Obter o ano de nascimento da pessoa (baseado na idade e ano atual)
# Obter o IMC da pessoa com 2 casas decimais
# Exibir um texto com todos os valores na tela usando F-Strings

from datetime import datetime

nome = 'Bruno'
idade = 39
altura = 1.91
peso = 120
ano_atual = 2022

current_date = datetime.now().date()
if current_date.month < 5 or current_date.day < 30:
    ano_nascimento = ano_atual - idade - 1
    print('caiu no primeiro')
else:
    idade = idade + 1
    ano_nascimento = ano_atual - idade
    print('caiu no segundo')

imc = peso / (altura ** 2)

print(
  f"Olá {nome}. Vejo que você tem {idade} anos de idade.\n"
  f"Você mede {altura} cm e está pesando {peso} kg.\n"
  f"Você nasceu em {ano_nascimento}.\n"
  f"Seu IMC é {imc:.2f}"
)
