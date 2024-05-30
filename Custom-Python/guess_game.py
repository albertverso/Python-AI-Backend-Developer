import random

# Funçao para verificar se o input so recebera numero inteiro e maior que zero e menor que dez,
# a funcao com dois parametros
def verify_input(name, description):
    while True: #O while True garante que a leitura será efetuada até que o break seja executado
            try: 
                number = int(input( name + description))
                if description == ", Digite um numero de 1 a 10:":
                    if 0 < number <= 10:  # --> verifica se rounds declarado pelo usuario é maior que zero menor que dez 
                        break             # ---> se for verdadeiro ele para o while
                    else:
                        print("INVALIDO: Digite um numero maior que zero e menor que dez!")
                else:
                    break          
            except ValueError:                                          # --> try/except captura a exceção disparada pelo int, que é um ValueError,                                                                    
                print("INVALIDO: Digite um Numero inteiro!")            #     exibindo a mensagem de erro; se a exceção não é disparada, o bloco
                                                                        #      else é executado, parando o laço
            # else:                                                       
            #     if description == ", quantas vezes você deseja jogar? \n":
            #         break                                                 

    return number #--> retorna um o numero que sera usado tanto para definir o numero de rounds como os numeros escolhidos pelo usuario de 1 a 10


#funcao para sortear um numero entre 1 e 10
def random_number():
    x = random.randint(1,10) #variavel que vai receber o modulo random com a função ranfint so numero inteiro
    return x 


description_total_rounds = ", quantas vezes você deseja jogar? \n"  # variaveis do tipo string para reaproveitar a função de verificar input
description_chosen_number = ", Digite um numero de 1 a 10:"


user = str(input("Digite seu nome? \n"))   #variavel guardando nome do usuario
total_rounds = verify_input(user, description_total_rounds)   #variavel guardando total de rounds recebendo uma funçao com 2 parametros
rounds = 1    #variavel para numero de rounds
total_points = 0    #variavel para pontualção final


while rounds <= total_rounds: #while sera executado ate round ser igual ou maior que total rounds
    chosen_number = verify_input(user, description_chosen_number) #variavel numero escolhido que recebeu um função com 3 parametros
    sorted_number = random_number() #variavel que recebeu a funçao que sorteia o numero e guarda esse valor ate o proximo loop

    if chosen_number == sorted_number: # verifica se o numero escolhido é igual ao sorteado
        print("Você acertou!!!")
        total_points += 3
    else:
        print("Você errouuuu! o numero sorteado foi:", + sorted_number)
        total_points -= 1

    rounds += 1 #a cada laço rounds recebera +1


if total_points >= 0: #verificando se o total de pontos nao saia negativo caso saia ele sera igual a zero
    print("FIM DE JOGO! sua pontuação foi:", total_points) # resultado final
else:
    print("FIM DE JOGO! sua pontuação foi: 0") # resultado final
