
print("----------------------Menu-----------------------------")
print("|  21    | Napolitana | R$ 20,00    |  G R$ 26,00     |")
print("|  22    | Margherita | R$ 20,00    |  G R$ 26,00     |")
print("|  23    | Calabresa  | R$ 25,00    |  G R$ 32,50     |")
print("|  24    | Toscana    | R$ 30,00    |  G R$ 39,00     |")
print("|  25    | Portuguesa | R$ 30,00    |  G R$ 39,00     |")
print("-------------------------------------------------------")

valor_total=0


pedido=1 #Valor inicial necessário para passar no while

while pedido == 1: #loop para controle de saida do usuário
 valor_pizza_escolhida=0 
 tamanho = input('tamanho da pizza (M/G): ') #seta o tamanho da pizza digitado pelo cliente na variavel tamanho
 if tamanho != "M" and tamanho != "G":
   print(tamanho)
   print("digite uma opcao valida M ou G")
   continue
 
 
 sabor = input('Codigo do sabor desejado: ') #seta o codigo do sabor digitado pelo cliente na variavel sabor
 
 
 if sabor == "21":
    valor_pizza_escolhida += 20.00
    print("Voce pediu uma pizza Napolitana")
 
 elif sabor == "22":
    valor_pizza_escolhida += 20.00
    print("Voce pediu uma pizza Margherita")
 
 elif sabor == "23":
    valor_pizza_escolhida += 25.00
    print("Voce pediu uma pizza Calabresa")
 
 elif sabor == "24":
    valor_pizza_escolhida += 30.00
    print("Voce pediu uma pizza Toscana")
 
 elif sabor == "25":
    valor_pizza_escolhida += 30.00
    print("Voce pediu uma pizza Portuguesa")
 
 else:
    print("opcao invalida")
    continue
 
 
 if tamanho == "G":
   valor_pizza_escolhida = valor_pizza_escolhida + valor_pizza_escolhida * 0.3
 
 valor_total += valor_pizza_escolhida

 novopedido = input('Deseja pedir mais alguma coisa?   0 - Nao         1 - Sim: ')

 if novopedido == "1":
   continue
 elif novopedido == "0":
    print("O valor total do seu pedido foi de: R$", valor_total)
    break

 else:
    print("opcao Invalida")
    continue
 
 

