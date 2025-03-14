import os 
os.system ("clear")
#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C,
#  caso contrário, imprima que a A + B é maior que C.

primeiro_valor =  float(input("Digite o primeiro valor: "))
segundo_valor =  float(input("Digite o segundo valor: "))
terceiro_valor = float(input("Digite o terceiro valor: "))

if (primeiro_valor + segundo_valor) < terceiro_valor:
    print(f"Soma: {primeiro_valor + segundo_valor}")
    print(f"A soma é menor que {terceiro_valor}")

else:
    print(f"A soma é maior que {terceiro_valor}")



    