import os
os.system ("clear")

#Em uma loja de CD´s existem apenas quatro tipos de preços que estão associados a cores. 
# Assim os CD´s que ficam na loja não são marcados por preços e sim por cores. 
# Desenvolva o algoritmo que a partir da entrada da cor o software mostre o preço.
#  A loja está atualmente com a seguinte tabela de preços.

opcao = int(input(""""
Código:  Cor: \t\t Valor:
 1 \t Verde   \t R$ 10,00
 2 \t Azul    \t R$ 20,00
 3 \t Amarelo \t R$ 30,00
 4 \t Vermelho\t R$ 40,00


Digite a opção do CD desejado: """))

match opcao:
    case 1:
     print("Valor: 10,00")
    case 2:
     print("Valor: 20,00")
    case 3:
     print("Valor: 30,00")
    case 4:
     print("Valor: 40,00")


