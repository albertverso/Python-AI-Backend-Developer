import requests
import smtplib
from email.message import EmailMessage 
from emailandsenha import senha, email

class GetUsers: #classe que iria instanciar funçoes dentro dela.

    def get_users(self): #função que ira pegar a lista de usuarios na api.

        response = requests.get('https://reqres.in/api/users') #chamada get na api.
        if response.status_code == 200: #se status da solicitação for 200 passa para o proximo passo.
            data = response.json() #variavel data recevera esse valor.
            return data #retorna data
        else:
            return print('ERRO: erro de requisição!')#se der algum status diferente de 200 vai aparecer mensagem de erro.

    def extract_users(self):#função para extrair usuarios em um lista mais organizada.
        data = self.get_users()#pegando retorno na funçao get_users e salvando na variavel data.
        if data:#se existir algo dentro de data ele segue com a condição.
            users = data.get('data', []) #dentro de data users ira pegar somente o objeto 'data' dentro do que foi retornado.
            format_users = [] #vairavel que recebera uma lista
            for user in users:
                format_user = {
                    'id': user['id'],                       #
                    'email': user['email'],                 #
                    'first_name': user['first_name'],       # --> percorrendo cada variavel do objeto 'data' e salvando na lista format_users.
                    'last_name': user['last_name'],         #   
                    'avatar': user['avatar']                #
                }
                format_users.append(format_user)
            return format_users
        else:
            return [] #caso data nao retorna nada ele retornara uma lista vazia.

    def save_list_users(self): #função para salvar a lista em um arquivo tipo txt.  
        users = self.extract_users()#variavel salvando o valor retornado na função extract_users
        list_users = []
        number = 1

        for user in users:                                      #
            list_users.append(f"USUARIO {number}: {user}\n")    #  --> percorrendo cada usuario e adicionando em list_users
            number += 1                                         #

        with open("lista_usuários.txt", "w") as arquivo:    #  --> abrindo e salvando a lista em um arquivo chamado lista_usuarios.
            arquivo.write(str(list_users))                  #

def email_automation(destinatario): #função para automatizar enviar da lista por email
        try:
            # Criando a mensagem
            msg = EmailMessage()
            msg['Subject'] = 'Lista de usuários' #titulo do email
            msg['From'] = email #email do remetente
            msg['To'] = destinatario#email do destinatario

            # Adicionando o anexo
            with open('lista_usuários.txt', 'rb') as arquivo:
                file_data = arquivo.read()
                file_name = arquivo.name

            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name) #guardando o anexo na variavel msg

            # Enviando o email
            with smtplib.SMTP("smtp-mail.outlook.com", 587) as smtp: #servidor smtp do outlook e porta
                smtp.starttls()
                smtp.login(email, senha) #email e senha do remetente
                smtp.send_message(msg) #mensagem onde foi guardado o anexo

            print('Email enviado com sucesso!')
        except Exception as e:
            print(f"ERRO: Erro ao enviar email! {e}")
 
def main():

    get_list_user = GetUsers()          # -->primeiro solicitando para salvar a lista localmente.
    get_list_user.save_list_users()     #

    destinatario = input("Digite o email do destinatario: \n") #segundo pedindo o usuario o email de destino.

    email_automation(destinatario) #terceiro chamando a função de automatização de passadando o email de destino como paremetro.

main() #chamando a função main().




    


