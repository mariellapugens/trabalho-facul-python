def valor_total(valor, quantidade):
    total = valor * quantidade
    desconto_1 = total - total * 0.03
    desconto_2 = total - total * 0.06
    desconto_3 = total - total * 0.1

    if quantidade <= 4:
        print("Valor total sem desconto: R$", total)
    elif 5 <= quantidade <= 19:
        print("Valor total sem desconto: R$", total)
        print("Valor com 3% de desconto: R$", desconto_1)
    elif 20 <= quantidade <= 99:
        print("Valor total sem desconto: R$", total)
        print("Valor com 6% de desconto: R$", desconto_2)
    elif quantidade >= 100:
        print("Valor total sem desconto: R$", total)
        print("Valor com 10% de desconto: R$", desconto_3,)


valor_total()
