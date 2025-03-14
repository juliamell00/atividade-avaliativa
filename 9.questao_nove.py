import os 
os.system ("clear")
#Uma financeira usa o seguinte critério para conceder empréstimos: o valor total do empréstimo deve ser 
# até dez vezes o valor da renda mensal do solicitante e o valor da prestação deve ser no máximo 30% 
# da renda mensal do solicitante. Escreva um programa que leia a renda mensal de um solicitante,
#  o valor total do empréstimo solicitado e o 
# número de prestações que o solicitante deseja pagar e informe se o empréstimo pode ou não ser concedido.



renda_mensal = float(input("Digite a renda mensal: R$ "))
valor_emprestimo = float(input("Digite o valor total do empréstimo: R$ "))

numero_prestacoes = int(input("Digite o número de prestações que deseja pagar: "))

valor_prestacao = valor_emprestimo / numero_prestacoes


if valor_emprestimo < 10 * renda_mensal and valor_prestacao < 0.3 *renda_mensal:
    print("O empréstimo pode ser concedido!")

else:
    print("O empréstimo não pode ser concedido!")