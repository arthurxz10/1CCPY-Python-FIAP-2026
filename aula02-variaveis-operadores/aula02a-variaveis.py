print("ola mundo")

print(7+4)
print("7+4")
print("7" + "4")  #CONCATENAÇÃO DE STRINGS

#Comentários de 1 linha em python
'''
Comentários de 
multiplas 
linhas 
'''

#VARIÁVEIS
nome = "Arthur" # string - texto
idade = 18 # int - numero
peso = 70,5 # float - num. decimal
print(nome, idade, peso)
print(f"oiii {nome}!!!!")

# IMPUTS - SIMULAÇÃO DE FORMS NO CMD
nome = input("Digite seu nome: ")
print(nome)
idade = int(input("Digite sua idade: "))
print("oiii", nome, "!Você tem", idade, "anos")
print(f"oiii {nome}!Você tem {idade} anos")

nova_idade = idade + 1
print(nova_idade)