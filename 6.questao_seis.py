import os
os.system ("clear")

nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
 
média = (nota_um + nota_dois) /2
print(f"\nA média do aluno é:{média:.2f}")
 
if média >= 6.0:
     print("Parabéns! Você esta aprovado! ")
elif média >= 4.0:
     print("Você está de recuperação.")
else:
     print(" você está reprovado.")


