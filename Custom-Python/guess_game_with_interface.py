import customtkinter as ctk
import random
from PIL import Image

rounds = 0 
total_points = 0 
total_rounds = 0 
chosen_number = 0 
user = ""

#funcao para sortear um numero entre 1 e 10
def random_number():
    x = random.randint(1,2) #variavel que vai receber o modulo random com a função ranfint so numero inteiro
    return x 

# Funçao para verificar se o input so recebera numero inteiro e maior que zero e menor que dez,
# a funcao com dois parametros
def verify_input(value, range_input=bool ):
    playing.delete(0, ctk.END) 
    global total_rounds
    try: 
        value = int(value)
        if range_input == True:
            if 0 < value <= 10:  # --> verifica se rounds declarado pelo usuario é maior que zero menor que dez 
                playing.configure(border_color='gray')
                error.configure(text = "")
                global chosen_number
                chosen_number = value
                sorted()
            else:
                playing.configure(border_color='red')
                error.configure(text = "INVALIDO: Digite um numero maior que 0 e menor que 10!")
        else: 
            total_rounds = value
            error.configure(text = "")
            second_screen()

    except ValueError:
        playing.configure(border_color='red')
        error.configure(text = "INVALIDO: Digite um Numero inteiro!")      # --> try/except captura a exceção disparada pelo int, que é um ValueError,                                                                    
        print("INVALIDO: Digite um Numero inteiro!")                       #     exibindo a mensagem de erro; se a exceção não é disparada, o bloco
                                                                           #      else é executado, parando o laço           

def sorted():
    global total_points
    global rounds

    sorted_number = random_number() #variavel que recebeu a funçao que sorteia o numero e guarda esse valor ate o proximo loop
    if rounds < total_rounds:
        playing.delete(0, ctk.END)
        if chosen_number == sorted_number: # verifica se o numero escolhido é igual ao sorteado
            print("Você acertou!!!")
            result.configure( text = "Você acertou!!!", text_color= 'green' )
            total_points += 3
        else:
            print("Você errouuuu! o numero sorteado foi:", + sorted_number)
            result.configure(text = f"Você errouuuu! o numero sorteado foi: {sorted_number}", text_color='red')
            total_points -= 1                       
        rounds += 1
        print(rounds)
        if rounds == total_rounds:
            button.configure(text="Ver pontuação", command=final_screen, image=None)
            playing.configure(state='disable')


def update_progress():
    global progress
    if progress < 1.0:
        progress += 0.10
        progressbar.set(progress)
        app.after(50, update_progress)  # Atualiza a cada 50 milissegundos
    else:
        firt_screen()

def firt_screen():
    for widget in app.winfo_children():
        widget.destroy()  # Remove todos os widgets da tela de carregamento

    label = ctk.CTkLabel(app, text="JOGO DA ADIVINHAÇÃO", font=("Arial", 25))
    label.pack(pady=30)


    label_name = ctk.CTkLabel(app, text="Digite seu nome:", font=("Arial", 16))
    label_name.pack(pady=0, padx=40, anchor='w')

    name = ctk.CTkEntry(app, placeholder_text="Nome")
    name.pack(pady=10)

    label_playing = ctk.CTkLabel(app, text="Digite a quantidade de vezes de jogos:", font=("Arial", 16))
    label_playing.pack(pady=0, padx=40, anchor='w')

    global playing
    playing = ctk.CTkEntry(app, placeholder_text="Nº jogos")
    playing.pack(pady=10)

    global error
    error = ctk.CTkLabel(app, text="", text_color="red")
    error.pack(pady=0)

    def event():
        global user
        user = name.get()
        value = playing.get()
        verify_input(value, False)

    button = ctk.CTkButton(app, text="Confirmar", command=event, fg_color='green', font=("Arial", 16), hover_color='darkgreen')
    button.pack(pady=10)


def second_screen():
    for widget in app.winfo_children():
        widget.destroy()  # Remove todos os widgets da tela de carregamento

    label = ctk.CTkLabel(app, text="JOGO DA ADIVINHAÇÃO", font=("Arial", 25))
    label.pack(pady=30)

    label_playing = ctk.CTkLabel(app, text="Digite um número de 1 a 10", font=("Arial", 16))
    label_playing.pack(pady=0)
    
    global playing
    playing = ctk.CTkEntry(app, placeholder_text="Digite um número")
    playing.pack(pady=10)

    global error
    error = ctk.CTkLabel(app, text="", text_color="red")
    error.pack(pady=0)

    def event():
        value = playing.get()
        verify_input(value, True)

    img = Image.open("Images\dadosB.png")
    img_ctk = ctk.CTkImage(img, size=(30,30))

    global button
    button = ctk.CTkButton(app, text="",image=img_ctk, command=event, fg_color='green', hover_color='darkgreen', compound='right', width=60, height=40)
    button.pack(pady=10)

    global result
    result = ctk.CTkLabel(app, text="", text_color="red", font=("Arial", 16))
    result.pack(pady=0)

def final_screen():
    for widget in app.winfo_children():
        widget.destroy()  # Remove todos os widgets da tela de carregamento

    label = ctk.CTkLabel(app, text="FIM DE JOGO", font=("Arial", 25))
    label.pack(pady=30)

    global user
    label = ctk.CTkLabel(app, text=f"{user if user != '' else 'Player'}, sua pontuação foi de: {total_points if total_points >= 0 else 0}", font=("Arial", 16) )
    label.pack(pady=30)

    def reiniciar():
        firt_screen()

    def finalizar():
        app.destroy()

    button = ctk.CTkButton(app, text="Jogar Novamente", fg_color='green', command=reiniciar, font=("Arial", 16), hover_color='darkgreen')
    button.pack(pady=10)

    button = ctk.CTkButton(app, text="Sair do Jogo", fg_color='red', command=finalizar, font=("Arial", 16), hover_color='darkred')
    button.pack(pady=10)

app = ctk.CTk()
app.title("JOGO DA ADIVINHAÇÃO")
app.geometry("350x400")
app.iconbitmap("Images\dadosB.ico")
ctk.set_appearance_mode("Dark")

img = Image.open("Images\dadosV.png")
img_resize = ctk.CTkImage(light_image=img, dark_image=img, size=(152,152))

icon = ctk.CTkLabel(app, text="", image=img_resize)
icon.pack(pady=40)

# Barra de progresso
progress = 0
progressbar = ctk.CTkProgressBar(app, width=200)
progressbar.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
progressbar.configure(progress_color='red')
progressbar.set(progress)
progressbar.pack(pady=20)

loading_label = ctk.CTkLabel(app, text="Carregando o Game...", font=("Arial", 24))
loading_label.pack(pady=10)

# Inicia a atualização da barra de progresso
update_progress()

app.mainloop()