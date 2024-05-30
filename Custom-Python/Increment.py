initial_number = int(input("Digite um Número Inicial:")) #variavel numero inicial
final_number = int(input("Digite um Número Final:")) #variavel numero final

if InitialNumber < FinalNumber: #verificação_1 se o numero inicial é menor que o final
    IncrementNumber = int(input("Digite um Número para Incremento:")) #variavel de incremento
    if IncrementNumber < FinalNumber: #verificação_2 se incremento é menor ou igual ao numero final
        print("-------------------")
        print("Resultado:")
        while InitialNumber <= FinalNumber: #verifica a condição
            print(InitialNumber) #o corpo, a ação
            InitialNumber += IncrementNumber #o passo de "incremento"
        print("-------------------")
    else:
        print("O valor do incremento não pode ser maior que o número final! Tente Novamente!")#caso a verificaçao_2 desse falso ele iria parar no else e mostra esse print       
else:
    print("O número inicial não pode ser maior que o número final! Tente Novamente!")#caso a verificaçao_1 desse falso ele iria parar no else e mostra esse print    