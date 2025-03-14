import os 
os.system('clear')

combustivel = (input("""
combustível \t\t até 25L : \t acima de 25L:
A = Àlcool \t\t desconto de 2% por litro  \t desconto de 4% por litro
G = Gasolina    \t\t desconto de 3% por litro   \t desconto de 5% por litro
 Digite o combustível: """))


def calcular_valor(litros, tipo_combustivel):
    preco_gasolina = 6.59
    preco_alcool = 3.79
    
    if tipo_combustivel == 'G':  # Gasolina
        if litros < 25:
            desconto = 0.03  # 3% de desconto
        else:
            desconto = 0.05  # 5% de desconto
        preco_por_litro = preco_gasolina
    elif tipo_combustivel == 'A':  # Álcool
        if litros < 25:
            desconto = 0.02  # 2% de desconto
        else:
            desconto = 0.04  # 4% de desconto
        preco_por_litro = preco_alcool
    else:
        return "Tipo de combustível inválido!"

    
    valor_bruto = litros * preco_por_litro
    desconto_total = valor_bruto * desconto
    valor_final = valor_bruto - desconto_total

    return round(valor_final, 2)



litros = float(input("Digite a quantidade de litros: ")) 



valor_a_pagar = calcular_valor(litros, combustivel)

print(f"O valor a ser pago pelo cliente é: R$ {valor_a_pagar}")