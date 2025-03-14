import os
os.system ("clear")

morango = int(input("""
  Fruta: \t\t Valor até 5 kg: \tValor acima de 5 kg:
 Morango \t\t R$ 2,50 por kg  \t 2,20 por kg
 Maçã    \t\t R$ 1,80 por kg   \t 1,50 por kg
 Digite a quantidade de morangos: """))
maca = float(input("Digite a quantidade de maçãs: "))

if morango < 5:
    preco_morangos = morango * 2.50
else:
    preco_morangos = morango * 2.20

if maca < 5:
   maca = maca * 1.80
else:
    maca = maca * 1.50

total_kg = morango + maca
total_compra = preco_morangos + maca

if total_kg > 10 or total_compra > 15.00:
    total_compra *= 0.90


print(f"O valor total a ser pago é: R$ {total_compra:.2f}")

