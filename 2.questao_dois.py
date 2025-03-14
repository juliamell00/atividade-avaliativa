import os
os.system ("clear")

#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
#Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada
#(anos). Por fim, mostre os dados do usuário.

nome = input("Digite seu nome: ")
sexo = input("""Feminino (F) \t\t Masculino (M)
 Digite seu sexo:""" )
estado = input("""Casado(a) \t Solteiro(a) \t Divórciado(a) \t Viúvo(a)

Digite seu estado civil: """)
 
if sexo == "F" and estado == "Casada":
    tempo_de_casada = int(input("Digite o tempo de casada em anos: "))
else:
    tempo_de_casada = None


print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estado}")

if tempo_de_casada is not None :
    print(f"Tempo de casada: {tempo_de_casada}")


