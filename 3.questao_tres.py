import os
os.system ("clear")
#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem
#  iguais deverá se somar os dois, caso contrário multiplique A por B. Ao final de qualquer 
# um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

primeiro_valor = int(input("Digite um valor: "))
segundo_valor = int(input("Digite outro valor: "))


if primeiro_valor == segundo_valor:
    resultado = primeiro_valor + segundo_valor 
   
else: 
   resultado =primeiro_valor * segundo_valor
    

print(f"Resultado: {resultado}")