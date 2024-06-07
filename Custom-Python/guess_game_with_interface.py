import customtkinter as ctk # importando o customtkinter e renomeando para ctk
import random
from PIL import Image # importaçao para conseguir aplicar imagens no codigo

rounds = 0 # #variavel para guardar os rounds ele sera atualizado em uma função toda vez que for chamada
total_points = 0 # variavel total de pontos

#funcao para sortear um número entre 1 e 10
def random_number():
    x = random.randint(1,10) #variavel que vai receber o modulo random com a função ranfint so número inteiro
    return x 

# Funçao para verificar se o input so recebera número inteiro e maior que zero e menor que dez,
# a funcao com dois parametros
def verify_input(value, range_input=bool ):
    playing.delete(0, ctk.END) # deleta o conteudo do entry playing 
    
    try:                  # --> try/except captura a exceção disparada pelo int, que é um ValueError
        value = int(value)
        if range_input == True: #caso a função verify_input receba um valor TRUE como um dos parametros ele passara para proxima verificaçao
            if 0 < value <= 10:  # --> verifica se rounds declarado pelo usuario é maior que zero menor que dez 
                playing.configure(border_color='gray') #define a bordar padrao caso a verificção do input esteja ok
                error.configure(text = "") #redefine a mensagem de erro para não aparecer
                global chosen_number #definindo a variavel como global e assim poder atualizar e ter acesso ela em qualquer local do codigo
                chosen_number = value #definindo value a variavel
                sorted() #chamando a funçao sorted
            else:
                playing.configure(border_color='red') #definindo a borda para vermelho em caso de erro no entry playing
                error.configure(text = "INVÁLIDO: Digite um número maior que 0 e menor que 10!") #definindo uma mensagem para label erro
        else: 
            global total_rounds #definindo total_rounds de forma global para ter acesso e atualizar em qualquer local do codigo
            total_rounds = value #definin
            error.configure(text = "")
            second_screen()

    except ValueError:
        playing.configure(border_color='red') #definindo a borda para vermelho em caso de erro no entry playing
        error.configure(text = "INVÁLIDO: Digite um número inteiro!") #definindo uma mensagem para label erro                                                                                                                                             

def sorted(): # função que verificar a quantidade de sorteios
    global total_points #definindo a variavel de forma global para ter acesso e atualizar em qualquer local do codigo
    global rounds  #definindo a variavel de forma global para ter acesso e atualizar em qualquer local do codigo

    sorted_number = random_number() # variavel que recebeu a funçao que sorteia o número e guarda esse valor ate o proximo loop
    if rounds < total_rounds:
        if chosen_number == sorted_number:    # verifica se o número escolhido é igual ao sorteado
            result.configure( text = "Você acertou!!!", text_color= 'green' ) # retorna uma mensagem para label result e altera para cor verde, a cada vez que acertar o número
            total_points += 3
        else:
            result.configure(text = f"Você errou!!! o número sorteado foi: {sorted_number}", text_color='red') # retorna uma mensagem para label result e altera para cor vermelha, a cada erro
            total_points -= 1                       
        rounds += 1
        if rounds == total_rounds:
            error.configure(text="Fim de jogo! Veja sua pontuação!", text_color='white')
            button.configure(text="Ver pontuação", command=final_screen, image=None) # no fim da verificação ele verifica novamente se rounds é igual a total rounds
            playing.configure(state='disable')                                       # se for ele altera o texto do botao e o comando chama a função final_screen e desabilita a imagem                      
                                                                                     # e tambem desabilita o entry playing

def update_progress(): # função para alterar o progresso do progressbar
    global progress
    if progress < 1.0: #condição para some 0.10 ate que seja menor que 1
        progress += 0.10
        progressbar.set(progress) #adiciona o progresso
        app.after(50, update_progress)  # Atualiza a cada 50 milissegundos
    else:
        first_screen() #caso o progressbar termine ele ira chamar outra tela

def first_screen(): #funçao para chamar 1 tela
    for widget in app.winfo_children():
        widget.destroy()  # Remove todos os widgets da tela de carregamento

    label = ctk.CTkLabel(app, text="JOGO DA ADIVINHAÇÃO", font=("Arial", 25)) #titulo
    label.pack(pady=30)


    label_name = ctk.CTkLabel(app, text="Digite seu nome:", font=("Arial", 16)) #label
    label_name.pack(pady=0, padx=40, anchor='w')#definindo os paddings e posiçao do label no codigo com anchor

    name = ctk.CTkEntry(app, placeholder_text="Nome") #input
    name.pack(pady=10)

    label_playing = ctk.CTkLabel(app, text="Digite a quantidade de vezes de jogos:", font=("Arial", 16)) #label
    label_playing.pack(pady=0, padx=40, anchor='w') #definindo os paddings e posiçao do label no codigo com anchor

    global playing #definindo a variavel de forma global para ter acesso e atualizar em qualquer local do codigo
    playing = ctk.CTkEntry(app, placeholder_text="Nº jogos") #input
    playing.pack(pady=10)

    global error #definindo a variavel de forma global para ter acesso e atualizar em qualquer local do codigo
    error = ctk.CTkLabel(app, text="", text_color="red") #label em caso de erro
    error.pack(pady=0)

    def event(): #funçao que sera acionada toda vez que o button for clicado
        global user #definindo a variavel de forma global para ter acesso e atualizar em qualquer local do codigo
        user = name.get() #obtendo o valor input name e guardando na variavel user
        value = playing.get() #obtendo o valor input playing e guardando na variavel value
        verify_input(value, False) #chamando a função de verificar input e passadando dois paramentros(value , FALSE)

    button = ctk.CTkButton(app, text="Confirmar", command=event, fg_color='green', font=("Arial", 16), hover_color='darkgreen')
    button.pack(pady=10) #exibindo o botao de confirmar onde ele acionara a funçao event caso clicado

def second_screen(): #funçao para chamar 2 tela
    for widget in app.winfo_children():
        widget.destroy()  # Remove todos os widgets da tela de carregamento

    label = ctk.CTkLabel(app, text="JOGO DA ADIVINHAÇÃO", font=("Arial", 25)) #label
    label.pack(pady=30)

    label_playing = ctk.CTkLabel(app, text="Digite um número de 1 a 10", font=("Arial", 16))#label
    label_playing.pack(pady=0)
    
    global playing #definindo a variavel de forma global para ter acesso e atualizar em qualquer local do codigo
    playing = ctk.CTkEntry(app, placeholder_text="Digite um número")#input
    playing.pack(pady=10)

    global error #definindo a variavel de forma global para ter acesso e atualizar em qualquer local do codigo
    error = ctk.CTkLabel(app, text="", text_color="red")#label em caso de erro
    error.pack(pady=0)

    def event(): #funçao que sera acionada toda vez que o button for clicado
        value = playing.get() #obtendo o valor input playing e guardando na variavel value
        verify_input(value, True) #chamando a função de verificar input e passadando dois paramentros(value , TRUE)

    img = Image.open("Images\dadosB.png") #importando a imagem
    img_ctk = ctk.CTkImage(img, size=(30,30)) #redimencionando imagem

    global button #definindo a variavel de forma global para ter acesso e atualizar em qualquer local do codigo
    button = ctk.CTkButton(app, text="",image=img_ctk, command=event, fg_color='green', hover_color='darkgreen', compound='right', width=60, height=40)#button
    button.pack(pady=10)

    global result #definindo a variavel de forma global para ter acesso e atualizar em qualquer local do codigo
    result = ctk.CTkLabel(app, text="", text_color="red", font=("Arial", 16))
    result.pack(pady=0)

def final_screen(): #função para chamar ultima tela
    for widget in app.winfo_children():
        widget.destroy()  # Remove todos os widgets da tela de carregamento

    label = ctk.CTkLabel(app, text="FIM DE JOGO", font=("Arial", 25))#title
    label.pack(pady=30)

    label = ctk.CTkLabel(app, text=f"{user if user != '' else 'Player'}, sua pontuação foi: {total_points if total_points >= 0 else 0}", font=("Arial", 16) )
    label.pack(pady=30) #mostrara a mensagem com nome do usuario e passando total de pontos, caso total de pontos ser menor que zero ele vai definir 0 como padrao

    def restart(): #funçao reiniciar jogo
        global rounds
        rounds = 0
        global total_points
        total_points = 0
        first_screen()

    def finish(): #funçao finalizar jogo
        app.destroy()

    button = ctk.CTkButton(app, text="Jogar Novamente", fg_color='green', command=restart, font=("Arial", 16), hover_color='darkgreen') #button
    button.pack(pady=10)

    button = ctk.CTkButton(app, text="Sair do Jogo", fg_color='red', command=finish, font=("Arial", 16), hover_color='darkred') #button
    button.pack(pady=10)

app = ctk.CTk() #criando a aplicação
app.title("JOGO DA ADIVINHAÇÃO") #titulo
app.geometry("350x400") #tamanho da aplicação
app.iconbitmap("Images\dadosB.ico") #icon da aplicaçao
ctk.set_appearance_mode("Dark") #definindo o tema do app

img = Image.open("Images\dadosV.png") #importando a imagem
img_resize = ctk.CTkImage(light_image=img, dark_image=img, size=(152,152)) #redimencionando a imagem

icon = ctk.CTkLabel(app, text="", image=img_resize) #label usado para mostrar um imagem
icon.pack(pady=40) # defino os padding dos widgets

# Barra de progresso
progress = 0
progressbar = ctk.CTkProgressBar(app, width=200) #invoca e define o tamanho
progressbar.place(relx=0.5, rely=0.5, anchor=ctk.CENTER) # centraliza
progressbar.configure(progress_color='red') # mudando a cor do progress
progressbar.set(progress) #valor do progressbar
progressbar.pack(pady=20) # defino os padding dos widgets

loading_label = ctk.CTkLabel(app, text="Carregando o Game...", font=("Arial", 24)) # label da splashscreen
loading_label.pack(pady=10) # defino os padding dos widgets

# Inicia a atualização da barra de progresso
update_progress()

app.mainloop()