import mysql.connector
import dotenv
import os
from datetime import datetime
import textwrap


dotenv.load_dotenv(dotenv.find_dotenv())

connection_db = mysql.connector.connect(
    host= os.getenv("HOST"),
    user= os.getenv("USER"),
    password= os.getenv("PASSWORD"),
    database= os.getenv("DATABASE"),
)

cursor = connection_db.cursor()

class Crud:
    #CREATE
    def insert_user(self, nome, email, createdAt):
        self.nome = nome
        self.email = email
        self.createdAt = createdAt

        command = f'INSERT INTO user (name, email, createdAt) VAlUES ("{self.nome}", "{self.email}", "{self.createdAt}")'
        cursor.execute(command)
        connection_db.commit() #edita o banco de dados 

    def insert_task(self, title, description, createdAt, userId):
        self.title = title
        self.description = description
        self.createdAt = createdAt
        self.userId = userId
        
        command = f'INSERT INTO task (title, description, createdAt, userId) VAlUES ("{self.title}", "{self.description}", "{self.createdAt}", "{self.userId}")'
        cursor.execute(command)
        connection_db.commit() #edita o banco de dados 

    #READ
    def read(choosen):

        command = f'SELECT * FROM {choosen};'
        cursor.execute(command)
        result = cursor.fetchall() #le o banco de dados

        print(result)
        
    def read_user(email):

        command = f'SELECT * FROM User Where email = "{email}";'
        cursor.execute(command)
        result = cursor.fetchall() #le o banco de dados

        return result
        
    def read_task(user_id):

        command = f'SELECT * FROM Task Where userId = "{user_id}";'
        cursor.execute(command)
        result = cursor.fetchall() #le o banco de dados
      
        return result
    
        
    #UPDATE
    def update_user(coluna ,choosen, email):

        command = f'UPDATE User SET {coluna} = "{choosen}" WHERE email = "{email}"'
        cursor.execute(command)
        connection_db.commit() #edita o banco de dados
        
    def update_task(coluna ,choosen, title):

        command = f'UPDATE Task SET {coluna} = "{choosen}" WHERE userId = "{title}"'
        cursor.execute(command)
        connection_db.commit() #edita o banco de dados

    #DELETE
    def delete_user(choosen):
       
        command = f'DELETE FROM User WHERE email = "{choosen}" '
        cursor.execute(command)
        connection_db.commit() #edita o banco de dados 

        print("\n Usuário deletado com sucesso!!!")
        
    def delete_task(choosen):

        command = f'DELETE FROM Task WHERE title = "{choosen}" '
        cursor.execute(command)
        connection_db.commit() #edita o banco de dados 

        print("\n Tarefa deletada com sucesso!!!")




def create(option = 0, user_id = 0):    
    created = Crud() 

    if option == 1:
        nome = input("digite seu nome: ")
        email = input("digite seu email: ")
        data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        created.insert_user(nome, email, data_criacao)

        print("\n Usuário adicionado com sucesso!!!")
    else:
        title = input("digite um titulo para sua tarefa: ")
        description = input("digite uma descrição de sua tarefa: ")
        data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        idUser = user_id

        created.insert_task(title, description, data_criacao, idUser)

        print("\n Tarefa adicionada com sucesso!!!")

def updated(option, choosen):
    if option == 1:
        tributes = int(input("Deseja editar nome[1] ou email[2]?"))
        if tributes == 1:

            update_name = input("Para qual nome deseja mudar?")
            Crud.update_user("name", update_name, choosen)

            print("\n Nome do usuário atualizado com sucesso!!!")
        elif tributes == 2:
            update_email = input("Para qual email deseja mudar?")
            Crud.update_user("email", update_email, choosen)

            print("\n Email do usuário atualizado com sucesso!!!")
    else:
        user_id = choosen
        result = Crud.read_task(user_id)
        verify_id = 0

        id_user = [usuario[4] for usuario in result]
        for id in id_user:
            verifi_id = id
        # PAREI NA PARTE DE VERIFICAR SE USUARIO ESTA ESTRELADO AO TASK PARA PODER ATUALIZAR A TABELA DE TAREFAS

        #ja tenho a vcerificação de id de uma task que esta atrelado ao usuario
        print(verifi_id)

        #proximo passo pergunta ao usuario o titulo da task que ele quer editar e verificar se a task que ele solicitou pertence a ele


        # tributes = int(input("Deseja editar titulo[1] ou descrição[2]?"))
        # if tributes == 1:
        #     update_title = input("Digite um novo titulo: ")
        #     Crud.update_task("title", update_title, choosen)

        #     print("\n titulo atualizado com sucesso!!!")
        # elif tributes == 2:
        #     update_description = input("Digite uma nova descrição: ")
        #     Crud.update_task("description", update_description, choosen)

        #     print("\n descrição atualizada com sucesso!!!")

def verify_user(email, type_crud = "" ,option = 0,):
    
    result = Crud.read_user(email)
    
    if result == []:
        return print("\n Operação inválida, usuário não existe. ")
    else:
        if option == 1: 
            if type_crud == "delete":
                Crud.delete_user(email)
            elif type_crud == "update":
                updated(option, email)
            elif type_crud == "read":
                result = Crud.read_user(email)
                print(f"\n{result}")

        else:
            id_user = [usuario[0] for usuario in result]  
            for id in id_user: 
                if type_crud == "create":
                    create(option, id)

                elif type_crud == "read":
                    result = Crud.read_task(id)
                    print(f"\n{result}") 

                elif type_crud == "delete":
                    title = input("Digite o titulo da tarefa que deseja deletar: ")
                    Crud.delete_task(title)

                elif type_crud == "update":
                    updated(option, id)

    
   
    
def menu():
    menu = """\n
    ================ MENU ================
    [c]\tCriar Usuário ou tarefa
    [r]\tExibir usuários ou tarefas
    [u]\tAtualizar usuário ou tarefa
    [d]\tDeletar usuario ou tarefa
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))    
    
def main():
    while True:
        opcao = menu()

        if opcao == "c":
            option = int(input("Deseja criar um novo usuario [1] ou uma nova tarefa[2]?"))
            if option == 1:
                create(option)
            elif option == 2:
                email = input("Digite seu email de usuário: ")
                verify_user(email, "create", option)
            else:
                print("\n Operação inválida, por favor selecione novamente a operação desejada. ")   

        elif opcao == "r":
            option = int(input("Deseja exibir um usuario [1] ou uma tarefa[2]?"))
            if option == 1:
                email = input("Digite seu email de usuário: ")
                verify_user(email, "read", option)
            elif option == 2:
                email = input("Digite seu email de usuário: ")
                verify_user(email, "read", option)
            else:
                print("\n Operação inválida, por favor selecione novamente a operação desejada. ") 

        elif opcao == "u":
            option = int(input("Deseja atualizar um usuario [1] ou uma tarefa[2]?"))

            if option == 1 or 2:
                email = input("digite seu email: ")
                verify_user(email, "update", option)
            else:
                print("\n Operação inválida, por favor selecione novamente a operação desejada. ") 

            
        elif opcao == "d":
            option = int(input("Deseja deletar Usuário[1] ou Tarefa[2]?"))

            if option == 1:
                delete = input("Digite o email de usuário que deseja deletar: ")
                verify_user(delete, "delete", option)

            elif option == 2:
                delete = input("Digite seu email: ")
                verify_user(delete, "delete", option)

            else:
                print("\n Operação inválida, por favor selecione novamente a operação desejada. ")  
        elif opcao == "q":
            break

        else:
            print("\n Operação inválida, por favor selecione novamente a operação desejada. ")

main()

cursor.close()
connection_db.close()