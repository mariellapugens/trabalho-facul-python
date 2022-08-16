

def volumeFeijoada():

  pedido=1
 
  while pedido == 1:
    try:
        mls = float(input("Digite o volume da feijoada em mls: "))
        msgValorErrado = "O valor minimo e comercializado de feijoada e de 300ml e o maximo de 5000ml."
        if mls < 300:
            print(msgValorErrado)
            continue
        elif mls > 5000:
            print(msgValorErrado)
            continue
        elif mls >= 300 and mls <= 5000:
            valorFeijoada = mls * 0.08
            result = {"mls": mls, "valorFeijoada": valorFeijoada}
            return result
    except ValueError:        
        print("Valor invalido, digite um valor numerico.")
        continue
        

def opcaoFeijoada(quantidadeDeFeijoada, valorFeijoada):
    try:
        # TODO quadro de opções de feijoada bonitinho
        opcoes = "Quadro de tipos de Feijoada"

        print(opcoes)
        entrandaDoUsuario = input(
            "Digite a opcao de feijoada de sua preferencia: b - (Basica) | p - (Premium) | s - (Suprema): ")

        if entrandaDoUsuario == "b":
            print("Feijoada Basica selecionada")
            valorFinalFeijoadaEscolhida = valorFeijoada
            print("O valor cobrado por {str1}mls de feijoada Basica e de R${str2}"
                  .format(str1=quantidadeDeFeijoada, str2=valorFinalFeijoadaEscolhida))
            print(float(valorFinalFeijoadaEscolhida)) 

        elif entrandaDoUsuario == "p":
            print("Feijoada Premium selecionada")
            valorFinalFeijoadaEscolhida = valorFeijoada * 1.25
            print("O valor cobrado por {str1}mls de feijoada Premium e de R${str2}"
                  .format(str1=quantidadeDeFeijoada, str2=valorFinalFeijoadaEscolhida))
            print(float(valorFinalFeijoadaEscolhida)) 

        elif entrandaDoUsuario == "s":
            print("Feijoada Suprema selecionada")
            valorFinalFeijoadaEscolhida = valorFeijoada * 1.5
            print("O valor cobrado por {str1}mls de feijoada Suprema e de R${str2}"
                  .format(str1=quantidadeDeFeijoada, str2=valorFinalFeijoadaEscolhida))
            print(float(valorFinalFeijoadaEscolhida)) 
    except ValueError:
        print("As opcoes de feijoada sao 'b', 'p' ou 's'.")

def acompanhamentoFeijoada():
    try:
        valorTotalAcompanhamentos = 0.0
        controle = input(
            "Voce deseja algum acompanhamento ? (s - sim | n - nao): ")
        try:

                # TODO quadro de opções de acompanhamentos bonitinho

                opcoes = "Quadro de tipos de Acompanhamento"
                print(opcoes)
                entrandaDoUsuario = input(
                    "Digite a opcao do acompanhamento que voce quer adicionar no pedido: ")

                if entrandaDoUsuario == "0":
                    print("Nao adicionar mais acompanhamentos")
                    controle = 'n'

                elif entrandaDoUsuario == "1":
                    print("Adicionado 200g de arroz ao pedido")
                    valorTotalAcompanhamentos += 5.0

                elif entrandaDoUsuario == "2":
                    print("Adicionado 150g de farofa especial ao pedido")
                    valorTotalAcompanhamentos += 6.0

                elif entrandaDoUsuario == "3":
                    print("Adicionado 100g de couve cozida ao pedido")
                    valorTotalAcompanhamentos += 7.0

                elif entrandaDoUsuario == "4":
                    print("Adicionado 1 laranja descascada ao pedido")
                    valorTotalAcompanhamentos += 3.0

        except:
            return "As opcoes de acompanhamentos sao '0', '1', '2', '3' ou '4'."

        return float(valorTotalAcompanhamentos)

    except:
        return "As opcoes sao 's' ou 'n'."





def fazerPedido():

    feijoada = volumeFeijoada()
    quantidadeDeFeijoada = feijoada["mls"]
    valorFeijoada = feijoada["valorFeijoada"]

    valorTotalDoPedido = float(opcaoFeijoada(
        quantidadeDeFeijoada, valorFeijoada) + acompanhamentoFeijoada())

    return print("O valor total do pedido e de R${str1}"
                 .format(str1=valorTotalDoPedido))


fazerPedido()
