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
        
    def read_user(email):

        command = f'SELECT * FROM User Where email = "{email}";'
        cursor.execute(command)
        result = cursor.fetchall() #le o banco de dados

        return result
        
    def read_task(user_id, type):

        command = f'SELECT * FROM Task Where {type} = "{user_id}";'
        cursor.execute(command)
        result = cursor.fetchall() #le o banco de dados
      
        return result
    
        
    #UPDATE
    def update_user(coluna ,choosen, email):

        command = f'UPDATE User SET {coluna} = "{choosen}" WHERE email = "{email}"'
        cursor.execute(command)
        connection_db.commit() #edita o banco de dados
        
    def update_task(coluna ,choosen, title):

        command = f'UPDATE Task SET {coluna} = "{choosen}" WHERE title = "{title}"'
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


class User_linked_task:

    def linked_user(choosen):
        user_id = choosen
        result = Crud.read_task(user_id, "UserId")
        verify_id = 0

        id_user = [usuario[4] for usuario in result]
        for id_u in id_user:
            verify_id = id_u
     
        return verify_id

    def linked_task(title_search):    
        result_title = Crud.read_task(title_search, "title")
        task_verify_id_user = 0

        title_id_user = [task[4] for task in result_title]
        for task in title_id_user:
            task_verify_id_user = task  

        return task_verify_id_user

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
        tributes = int(input("Deseja editar nome[1] ou email[2]: "))
        if tributes == 1:

            update_name = input("Informe o novo nome: ")
            Crud.update_user("name", update_name, choosen)

            print("\n Nome do usuário atualizado com sucesso!!!")
        elif tributes == 2:
            update_email = input("Informe o novo email: ")
            Crud.update_user("email", update_email, choosen)

            print("\n Email do usuário atualizado com sucesso!!!")
    else:
        linked = User_linked_task

        verify_id = linked.linked_user(choosen)
        
        title_search = input("Qual titulo da tarefa vc deseja editar: ")

        task_verify_id_user = linked.linked_task(title_search)

        if task_verify_id_user == verify_id:
            while True:

                try:
                    tributes = int(input("Deseja editar titulo[1] ou descrição[2]?"))
                    if tributes == 1:
                        update_title = input("Digite um novo titulo: ")
                        Crud.update_task("title", update_title, title_search)

                        print("\n titulo atualizado com sucesso!!!")
                        break
                    elif tributes == 2:
                        update_description = input("Digite uma nova descrição: ")
                        Crud.update_task("description", update_description, title_search)

                        print("\n descrição atualizada com sucesso!!!")
                        break
                    else:
                        print("\n Operação inválida, por favor selecione novamente a operação desejada.")
                except ValueError:
                        print("\n Operação inválida, por favor selecione novamente a operação desejada.") 

        else:
            return print("\n Operação inválida, usuário não está atrelado a essa tarefa!")

def verify_user(email, type_crud = "" ,option = 0,):
    
    result = Crud.read_user(email)
    
    if result == []:
        return print("\n Operação inválida, usuário não existe. ")
    else:
        if option == 1: 
            if type_crud == "delete":
                confirm_email = input("Confirme seu email para deletar: ")
                if confirm_email == email: 
                    Crud.delete_user(confirm_email)
                else:
                    print("\n Operação inválida, emails diferentes! ")    
            elif type_crud == "update":
                updated(option, email)
            elif type_crud == "read":
                result = Crud.read_user(email)
                if result == []:
                    return print("\n Operação inválida, esse usuário não tem nenhuma tarefa. ")
                else:
                    print(f"\n{result}")

        else:
            id_user = [usuario[0] for usuario in result]  
            for id in id_user: 
                if type_crud == "create":
                    create(option, id)

                elif type_crud == "read":
                    result = Crud.read_task(id, "UserId")
                    print(f"\n{result}") 

                elif type_crud == "delete":
                    result = Crud.read_task(id, "UserId")
                    
                    if result == []:
                        return print("\n Operação inválida, esse usuário não tem nenhuma tarefa. ")
                    else:
                        print(f"\n{result}") 

                        linked = User_linked_task
                        verify_id = linked.linked_user(id)
                        
                        title_delete = input("Digite o titulo da tarefa que deseja deletar: ")

                        task_verify_id_user = linked.linked_task(title_delete)

                        if verify_id == task_verify_id_user:
                            Crud.delete_task(title_delete)
                        else:
                            print("\n Operação inválida, usuário não está atrelado a essa tarefa!")   

                elif type_crud == "update":
                    result = Crud.read_task(id, "UserId")
                    
                    if result == []:
                        return print("\n Operação inválida, esse usuário não tem nenhuma tarefa. ")
                    else:
                        print(f"\n{result}")    
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

def user_task_choose(x):
    menu = f"""\n
    ================ OPÇÕES ================
    Deseja {x} um(a):
    [1]\tUsuário
    [2]\tTarefa
    [3]\t>voltar para o menu<
    => """
    return input(textwrap.dedent(menu))
    
def main():
    erro_message = print("\n Operação inválida, por favor selecione novamente a operação desejada.") 

    while True:
        opcao = menu()

        if opcao == "c":
            while True:
                option = (user_task_choose("criar"))

                if option == "1":
                    create(int(option))
                    break
                elif option == "2":
                    email = input("Digite seu email de usuário: ")
                    verify_user(email, "create", int(option))
                    break
                elif option == "3":
                    
                    break
                else:
                    erro_message 

        elif opcao == "r":
            while True:
                option = (user_task_choose("exibir"))

                if option == "1":
                    email = input("Digite seu email de usuário: ")
                    verify_user(email, "read", int(option))
                elif option == "2":
                    email = input("Digite seu email de usuário: ")
                    verify_user(email, "read", int(option))
                elif option == "3":
                    break
                else:
                    erro_message

        elif opcao == "u":
            while True:
                option = (user_task_choose("atualizar"))

                if option == "1":
                    email = input("digite seu email: ")
                    verify_user(email, "update", int(option))
                elif option == "2":
                    email = input("digite seu email: ")
                    verify_user(email, "update", int(option))    
                elif option == "3":
                    break
                else:
                    erro_message
            
        elif opcao == "d":
            while True:
                option = (user_task_choose("deletar"))

                if option == "1":
                    delete = input("Digite seu email: ")
                    verify_user(delete, "delete", int(option))
                elif option == "2":
                    delete = input("Digite seu email: ")
                    verify_user(delete, "delete", int(option))    

                elif option == "3":
                    break

                else:
                    erro_message  

        elif opcao == "q":
            break

        else:
            erro_message

main()

cursor.close()
connection_db.close()