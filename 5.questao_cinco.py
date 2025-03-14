import os 
os.system ("clear")

#Faça um programa que leia um código de operação (+,-,* ou /), e também dois valores inteiros A e B. 
#O programa deve calcular o resultado da operação escolhida aplicado a A e B. Por exemplo, se operação 
# escolhida foi * e A = 1 e B = 3, o programa deve fornecer como resultado o valor de 1*3, que é 3.

import os
os.system('clear')


operacao = input("Digite o código de operação (+, -, *, /): ")

A = int(input("Digite valor de A: "))
B = int(input("Digite valor de B: "))


match operacao:
    case "+":
        resultado = A + B
        print("O resultado é: ", resultado)
    case "-":
        resultado = A - B
        print("O resultado é: ", resultado)
    case "*":
        resultado = A * B
        print("O resultado é: ", resultado)
    case "/":
        if B != 0:
            resultado = A / B
            print("O resultado é: ", resultado)
        else:
            print("Erro: Divisão por zero!")
    case _:
        print("Erro: Operação inválida!")