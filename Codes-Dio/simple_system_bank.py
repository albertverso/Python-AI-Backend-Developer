def menu(): #função que vai mostrar a opção do menu para o usuario
    while True:
        try:                                                            #---> usando try/except para tratar erro de valor recebido no input que so recebera do tipo int
            menu_options = int(input("""
                ESCOLHA UMA OPÇÃO DE OPERAÇÃO ABAIXO:
                -----------------------------------------------
                    1° - DEPOSITO
                    2° - SAQUE
                    3° - EXTRATO                                          
                    4° - FINALIZAR
                -----------------------------------------------
            """))
            if 0 < menu_options <= 4:       #verificando a se o menu recebera numeração valida de acordo com min/max de opção
                break             #se ele atender o laço ira parar
            else:
                print("INVALIDO: Digite um numero entre 1° e 4°!") #retornando se as opções forem invalidas
        except ValueError:
            print("INVALIDO: Digite um Numero inteiro!") #retornando se as opções forem invalidas

    return menu_options # função retornara o numero escolhido no menu      

def check_deposito(name): #função para checar o deposito se ele recebera um valor valido ou maior que zero
    while True:
        try:           #---> usando try/except para tratar erro de valor recebido no input que so recebera do tipo float
            valor = float(input(f"{name}, Quanto deseja depositar? \n"))
            if valor > 0: 
                break             
            else:
                print("INVALIDO: Digite um numero float e positivo!")
        except ValueError:
            print("INVALIDO: Digite um Numero do tipo float!")  

    return valor #função retornara o valor do deposito

def check_saque(name, saldo_check): #função para checar o saque se ele recebera um valor valido ou maior que zero
    while True:
        try:          #---> usando try/except para tratar erro de valor recebido no input que so recebera do tipo float
            saque_check = float(input(f"{name}, Quanto deseja sacar? \n"))
            if saque_check > 0:    #verificando se o saque recebera numero positivo
                if saque_check <= saldo_check: #verificando se o saque é maior ou igual ao saldo
                    if saque_check <= 500:  # verificando se o saque é menor ou igual ao limite diario de 500
                        break
                    else:
                        print("INVALIDO: limite de R$ 500.00 excedido!") 
                else:
                    print("INVALIDO: Saldo insuficiente")                    
            else:
                print("INVALIDO: Digite um saldo valido!")
        except ValueError:
            print("INVALIDO: Digite um Numero do tipo float!")  

    return saque_check  #retornara o valor do saque

def finish_operation():  #função de finalizar cada operação
    while True:
        try:  #---> usando try/except para tratar erro de valor recebido no input que so recebera do tipo int
            finish = int(input("""
                ESCOLHA UMA OPÇÃO DE OPERAÇÃO ABAIXO:
                -----------------------------------------------
                    1° - VOLTA PARA O MENU
                    2° - FINALIZAR
                -----------------------------------------------
            """))
            if 0 < finish <= 2:  #verificando a se o menu recebera numeração valida de acordo com min/max de opção
                break     
            else:
                print("INVALIDO: Digite um numero entre 1° e 2°!")
        except ValueError:
            print("INVALIDO: Digite um Numero inteiro!")

    return finish #retornara o numero da opçao escolhida pelo usuario


deposito = 0.0
saque = 0.0
extrato = ""
saldo = 0.0
operation_finish_menu = 0
numero_saques = 0
LIMITE_SAQUES = 3

user = str(input("Digite seu nome:")) #1 passo, pergunta o nome do usuario e guarda na variavel user

while True: #laço while como true ate que seja atendida as condicões
    if operation_finish_menu == 2:  #a cada inicio do laço ele vai verificar a variavel que vai receber a operaçaõ final
        print("Operação finalizada!!!")
        break
    else:
        number_option_menu = menu() #variavel chamando a função menu() e guardara o numero escolhido

        while True: #laço while como true ate que seja atendida as condicões do menu entre deposito/saque/extrato/encerrar

            if number_option_menu == 1: #verifica se o numero do menu escolhido foi igual a 2, caso seja ele ira chamar a função check_deposito passando user como parametro
                deposito = check_deposito(user)
                saldo += deposito #cada vez que o usuario escolher deposito ele ira somar o valor do deposito ao saldo
                extrato += f"Deposito: R$ {deposito:.2f}\n" #a cada deposito sera guardado da variavel extrato
                break

            elif number_option_menu == 2: #verifica se o numero do menu escolhido foi igual a 1, caso seja ele vai verificar o numero de saques e depois chamar a função check_saque
                if numero_saques < LIMITE_SAQUES: 
                    saque = check_saque(user, saldo) #variavel vai guardar o valor de saque retornado da função passando user/saldo, saldo para verificação se o saque nao vai ser maior que o saldo
                    saldo -= saque #cada vez que o usuario escolher deposito ele ira subtrai o valor do deposito ao saldo
                    extrato += f"Saque: R$ {saque:.2f}\n" #a cada saque sera guardado da variavel extrato
                    numero_saques += 1 # a cada saque o variavel numero_saques recebera +1
                    break
                else:
                    print("INVALIDO: numero de saques diarios excedido!")# caso numero de saques diario seja excedido
                    break

            elif number_option_menu == 3: #verifica se o numero do menu escolhido foi igual a 3 e mostrara o extrato
                print("----------------EXTRATO-----------------")
                print(f"Nome: {user}\n")
                print("Sem movimentaçãoes na conta." if not extrato else extrato)
                print(f"Saldo: R$ {saldo:.2f}")
                print("----------------------------------------")
               
                break

            elif number_option_menu == 4: #verifica se o numero do menu escolhido foi igual a 4 e finalizara o codigo
                print("Operação finalizada!!!")
                break

            else:
                print("Invalido! escolha uma opção!")

        operation_finish_menu = finish_operation() # a cada final de laço ele ira definir a variavel chamado a função finish_operation para verificar 
                                                   # se o usuario quer finalizar ou voltar para o menu e repetir as opreções




