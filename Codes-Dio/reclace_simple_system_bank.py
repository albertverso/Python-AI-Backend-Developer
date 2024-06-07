import textwrap

def menu(): #função que vai mostrar a opção do menu para o usuario
    while True:
        try:                                                            #---> usando try/except para tratar erro de valor recebido no input que so recebera do tipo int
            menu_options = int(input("""
                ESCOLHA UMA OPÇÃO DE OPERAÇÃO ABAIXO:
                -----------------------------------------------
                    1° - DEPOSITO
                    2° - SAQUE
                    3° - EXTRATO  
                    4° - NOVA CONTA
                    5° - LISTAR USUARIOS
                    6° - NOVO USÚARIO                                        
                    7° - FINALIZAR
                    
                -----------------------------------------------
            """))
            if 0 < menu_options <= 7:       #verificando a se o menu recebera numeração valida de acordo com min/max de opção
                break             #se ele atender o laço ira parar
            else:
                print("INVALIDO: Digite um numero entre 1° e 7°!") #retornando se as opções forem invalidas
        except ValueError:
            print("INVALIDO: Digite um Numero inteiro!") #retornando se as opções forem invalidas

    return menu_options # função retornara o numero escolhido no menu      

def deposito(saldo, valor, extrato):
    saldo += valor #cada vez que o usuario escolher deposito ele ira somar o valor do deposito ao saldo
    extrato += f"Deposito: R$ {valor:.2f}\n" #a cada deposito sera guardado da variavel extrato
    
    return saldo, extrato

def check_deposito(name, saldo, extrato): #função para checar o deposito se ele recebera um valor valido ou maior que zero
    while True:
        try:           #---> usando try/except para tratar erro de valor recebido no input que so recebera do tipo float
            valor = float(input(f"{name}, Quanto deseja depositar? \n"))
            if valor > 0: 
                saldo, extrato = deposito(saldo, valor, extrato)  
                break       
            else:
                print("INVALIDO: Digite um numero float e positivo!")
        except ValueError:
            print("INVALIDO: Digite um Numero do tipo float!") 

    return saldo, extrato #função retornara o valor do deposito

def saque(saldo, valor, extrato, numero_saques):
    LIMITE_SAQUES = 3

    if numero_saques < LIMITE_SAQUES: 
        saldo -= valor #cada vez que o usuario escolher deposito ele ira subtrai o valor do deposito ao saldo
        extrato += f"Saque: R$ {valor:.2f}\n" #a cada saque sera guardado da variavel extrato
        numero_saques += 1 # a cada saque o variavel numero_saques recebera +1
    else:
        print("INVALIDO: numero de saques diarios excedido!")# caso numero de saques diario seja excedido

    return saldo, extrato, numero_saques

def check_saque(name, saldo, extrato, numero_saques): #função para checar o saque se ele recebera um valor valido ou maior que zero
    while True:
        try:          #---> usando try/except para tratar erro de valor recebido no input que so recebera do tipo float
            valor = float(input(f"{name}, Quanto deseja sacar? \n"))
            if valor > 0:    #verificando se o saque recebera numero positivo
                if valor <= saldo: #verificando se o saque é maior ou igual ao saldo
                    if valor <= 500:  # verificando se o saque é menor ou igual ao limite diario de 500
                        saldo, extrato, numero_saques = saque(saldo, valor, extrato, numero_saques)
                        break
                    else:
                        print("INVALIDO: limite de R$ 500.00 excedido!") 
                else:
                    print("INVALIDO: Saldo insuficiente")                    
            else:
                print("INVALIDO: Digite um saldo valido!")
        except ValueError:
            print("INVALIDO: Digite um Numero do tipo float!")  

    return saldo, extrato, numero_saques  #retornara o valor do saque

def exibir_extrato(name, saldo, extrato):
    print("----------------EXTRATO-----------------")
    print(f"Nome: {name}\n")
    print("Sem movimentaçãoes na conta." if not extrato else extrato) #se o extrato retorna em branco ele retornara que esta movimentações 
    print(f"Saldo: R$ {saldo:.2f}")
    print("----------------------------------------")

def criar_usuario(usuarios):
    while True:
        try:
            cpf = int(input("Informe o CPF (somente numero):"))
        except ValueError:
            print("INVALIDO: Somente numeros")
        else:
            break
    
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuario com esse CPF!")

    nome = input("Infome o seu nome completo: ")
    while True:
        try:
            data_nascimento = int(input("Informe sua data ded nascimento: "))
        except ValueError:
            print("INVALIDO: Somente numeros, formato (dd-mm-aaaa)")
        else:
            break
    
    endereco = input("Informe seu endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco })
    print(" Usuario criado com sucesso!!!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(numero_conta, usuarios):
    AGENCIA = "0001"
    while True:
        try:
            cpf = int(input("Informe o CPF (somente numero):"))
        except ValueError:
            print("INVALIDO: Somente numeros")
        else:
            break  
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario nao encontrado!!!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agencia:\t{conta['agencia']}
            C/C/:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))    

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

def main():
    numero_saques = 0
    extrato = ""
    saldo = 0.0
    usuarios = []
    contas = []
    operation_finish_menu = 0

    user = str(input("Digite seu nome:")) #1 passo, pergunta o nome do usuario e guarda na variavel user

    while True: #laço while como true ate que seja atendida as condicões
        if operation_finish_menu == 2:  #a cada inicio do laço ele vai verificar a variavel que vai receber a operaçaõ final
            print("Operação finalizada!!!")
            break
        else:
            number_option_menu = menu() #variavel chamando a função menu() e guardara o numero escolhido

            while True: #laço while como true ate que seja atendida as condicões do menu entre deposito/saque/extrato/encerrar

                if number_option_menu == 1: #verifica se o numero do menu escolhido foi igual a 2, caso seja ele ira chamar a função check_deposito passando user como parametro
                    saldo, extrato = check_deposito(user, saldo, extrato)
                    break
                elif number_option_menu == 2: #verifica se o numero do menu escolhido foi igual a 1, caso seja ele vai verificar o numero de saques e depois chamar a função check_saque
                    saldo, extrato, numero_saques = check_saque(user, saldo, extrato, numero_saques)
                    break
                elif number_option_menu == 3: #verifica se o numero do menu escolhido foi igual a 3 e mostrara o extrato
                    exibir_extrato(user, saldo, extrato)
                    break
                elif number_option_menu == 4:
                    numero_conta = len(contas) +1
                    conta = criar_conta(numero_conta, usuarios)
                    break
                elif number_option_menu == 5:
                    listar_contas(contas)
                    break
                elif number_option_menu == 6:
                    criar_usuario(usuarios)
                    break
                elif number_option_menu == 7: #verifica se o numero do menu escolhido foi igual a 4 e finalizara o codigo
                    print("Operação finalizada!!!")
                    break
                else:
                    print("Invalido! escolha uma opção!")

            operation_finish_menu = finish_operation() # a cada final de laço ele ira definir a variavel chamado a função finish_operation para verificar 
                                                    # se o usuario quer finalizar ou voltar para o menu e repetir as opreções

main()




