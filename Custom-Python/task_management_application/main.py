import mysql.connector
import dotenv
import os
import textwrap
from datetime import datetime
from prettytable import PrettyTable

#invocando as variaveis de ambiente pelo .env
dotenv.load_dotenv(dotenv.find_dotenv())

#inicia a conexão com servidor
connection_db = mysql.connector.connect(
    host= os.getenv("HOST"),
    user= os.getenv("USER"),
    password= os.getenv("PASSWORD"),
    database= os.getenv("DATABASE"),
)

cursor = connection_db.cursor()

#classe onde funcionara as requisições
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
    def read(table, column, req):

        command = f'SELECT * FROM {table} Where {column} = "{req}"'
        cursor.execute(command)
        result = cursor.fetchall() #le o banco de dados
      
        return result

    def read_task_userId(req):

        command = f'SELECT title FROM Task WHERE userId = "{req}"'
        cursor.execute(command)
        result = cursor.fetchall() #le o banco de dados
      
        return result

    def read_task_id(title, req):

        command = f'SELECT taskId FROM Task WHERE title = "{title}" AND userId = "{req}"'
        cursor.execute(command)
        result = cursor.fetchall() #le o banco de dados
      
        return result   
        
    #UPDATE
    def update(table, column, update, validation, req):

        #define na tabela na coluna especifica e define ela com "update", depois procurar todas as linhas na tabela onde a coluna "validation" tem o valor "req".

        command = f'UPDATE {table} SET {column} = "{update}" WHERE {validation} = "{req}"'
        cursor.execute(command)
        connection_db.commit() #edita o banco de dados

    #DELETE
    def delete(table, column, req):
       
        command = f'DELETE FROM {table} WHERE {column} = "{req}" '
        cursor.execute(command)
        connection_db.commit() #edita o banco de dados 

        if table == "User":
            print("\n Usuário deletado com sucesso!!!")
        else:
            print("\n Tarefa deletada com sucesso!!!")
    
    def force_delete(user_id):
        # Apagar as tarefas relacionadas ao usuário
        cursor.execute(f'DELETE FROM task WHERE userId = "{user_id}"')
        # Apagar o usuário
        cursor.execute(f'DELETE FROM user WHERE id = "{user_id}"')

        connection_db.commit()

        print("\n Usuário deletado com sucesso!!!")



#verificando lista de titulos relacionada ao id do usuario e depois verifica se titulo solicitado para update/delete esta dentro dessa lista, se sim ele me retorna o id dessa task e true
def linked_task(req, title):    
    result_list = Crud.read_task_userId(req)
    task_verify_id_task = 0

    title_list = [list_tasks[0] for list_tasks in result_list]
    
    if title in title_list:
        result_id_task = Crud.read_task_id(title, req)

        id_task = [task[0] for task in result_id_task]
        for id in id_task:
            task_verify_id_task = id

        return task_verify_id_task, True

    else:
        return 0, False    

#função para criar usuário/tarefa antes de fazer a requisição e também faz uma pequena verfição se usuário com email ja existe antes de criar
def create(option = 0, user_id = 0, email = ""):    
    created = Crud()
    verify_email = "" 

    if option == 1:
        result = Crud.read("User", "email", email)
        users = [usuario[2] for usuario in result]

        for user in users:
            verify_email = user

        if verify_email == email:
           print("\n Operação inválida, email já cadastrado!") 
        else:
            nome = input("digite seu nome: ")
            data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            created.insert_user(nome, email, data_criacao)
            print("\n Usuário adicionado com sucesso!!!")
    else:
        title = input("digite um titulo para sua tarefa: ")
        verification_task = verify_task(title, user_id)
       
        if verification_task:
            description = input("digite uma descrição de sua tarefa: ")
            data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            idUser = user_id

            created.insert_task(title, description, data_criacao, idUser)
            print("\n Tarefa adicionada com sucesso!!!")
        else:
            print("\n Operação inválida, usuário ja tem uma tarefa com esse titulo!") 

#função para atualizar e verificar usuário/tarefa antes de fazer a requisição
def updated(option, req):
    if option == 1:
        while True:
            try:
                tributes = int(input("Deseja editar nome[1] ou email[2]: "))
                if tributes == 1:

                    update_name = input("Informe o novo nome: ")
                    #define na tabela USER o name e define ela com update_name, depois procurar todas as linhas na tabela User onde a coluna email tem o valor "req".
                    Crud.update( "User", "name", update_name, "email", req)

                    print("\n Nome do usuário atualizado com sucesso!!!")
                    break
                elif tributes == 2:
                    update_email = input("Informe o novo email: ")

                    #define na tabela USER o email e define ela com update_email, depois procurar todas as linhas na tabela User onde a coluna email tem o valor "req".
                    Crud.update("User", "email", update_email, "email", req)

                    print("\n Email do usuário atualizado com sucesso!!!")
                    break
                else:
                    print("\n Operação inválida, por favor selecione novamente a operação desejada.")
            except ValueError:
                    print("\n Operação inválida, por favor selecione novamente a operação desejada.") 
    else:

        #verificão se usuário esta atrelado a tarefa que ele solicitou atualizar
        verify_id = req

        title_search = input("Qual titulo da tarefa que você deseja editar: ")

        task_verify_id_user, validation = linked_task(verify_id, title_search)
        #-------------------------------------

        if validation:
            while True:
                try:
                    tributes = int(input("Deseja editar titulo[1] ou descrição[2]: "))
                    if tributes == 1:
                        update_title = input("Digite um novo titulo: ")

                        verification_task = verify_task(update_title, req)

                        if verification_task:
                            #define na tabela TASK o title e define ela com update_title, depois procurar todas as linhas na tabela TASK onde a coluna title tem o valor "title_search".
                            Crud.update("Task", "title", update_title, "taskId", task_verify_id_user)

                            print("\n titulo atualizado com sucesso!!!")
                            break
                        else:
                            print("\n Operação inválida, usuário ja tem uma tarefa com esse titulo!")
                            break  
                    elif tributes == 2:
                        update_description = input("Digite uma nova descrição: ")
                        #define na tabela TASK o description e define ela com update_description, depois procurar todas as linhas na tabela TASK onde a coluna title tem o valor "title_search".
                        Crud.update("Task", "description", update_description, "taskId", task_verify_id_user)

                        print("\n descrição atualizada com sucesso!!!")
                        break
                    else:
                        print("\n Operação inválida, por favor selecione novamente a operação desejada.")
                except ValueError:
                        print("\n Operação inválida, por favor selecione novamente a operação desejada.") 

        else:
            print("\n Operação inválida, usuário não está atrelado a essa tarefaaaaaaaaaa!")

#verifica se usuario nao vai criar tarefa com o mesmo titulo
def verify_task(req, id):
    verify_title = ""
    result = Crud.read("Task", "UserId", id)
    title_task = [usuario[1] for usuario in result]

    for title in title_task:
        verify_title = title

    if verify_title != req:
        return True
    else:
        return False    

#função que verifica usuário já existe antes de toda requisição
def verify_user(email, type_crud = "" ,option = 0,):
    result = Crud.read("User", "email", email)
    
    if result == []:
        return print("\n Operação inválida, usuário não existe. ")
    else:
        if option == 1: 
            id_user = [usuario[0] for usuario in result]  
            for id in id_user:
                if type_crud == "delete":
                    confirm_email = input("Confirme seu email para deletar: ")
                    if confirm_email == email: 
                        result = Crud.read("Task", "UserId", id)
                        if result == []:
                            Crud.delete("User", "email", confirm_email)
                        else:
                            table_result(result, "Task") 
                            try:
                                confirm = int(input("\n Esse usuário tem tarefas pendentes deseja prosseguir e deletar? sim[1] não[2]"))    
                                if confirm == 1:
                                    Crud.force_delete(id)
                                elif confirm == 2:
                                    print("")
                                else:
                                    print("\n Operação inválida, por favor selecione novamente a operação desejada.")   
                            except ValueError:    
                                print("\n Operação inválida, tente novamente!")
                        
                    else:
                        print("\n Operação inválida, emails diferentes! ")    
                elif type_crud == "update":
                    updated(option, email)
                elif type_crud == "read":
                    result = Crud.read("User", "email", email)
                    table_result(result) 

        else:
            id_user = [usuario[0] for usuario in result]  
            for id in id_user: 
                if type_crud == "create":
                    create(option, id)

                elif type_crud == "read":
                    result = Crud.read("Task", "UserId", id)
                    if result == []:
                        print("\n Operação inválida, esse usuário não tem nenhuma tarefa. ")
                    else:
                        table_result(result, "Task")  

                elif type_crud == "delete":
                    result = Crud.read("Task", "UserId", id)
                    
                    if result == []:
                        print("\n Operação inválida, esse usuário não tem nenhuma tarefa. ")
                    else:
                        table_result(result, "Task")  

                        #verificão se usuário esta atrelado a tarefa que ele solicitou deletar
                        verify_id = id
                        
                        title_delete = input("Digite o titulo da tarefa que deseja deletar: ")

                        task_verify_id_user, validation = linked_task(id, title_delete)
                        #----------------------------------------------------

                        if validation:
                            Crud.delete("Task", "taskId", task_verify_id_user)
                        else:
                            print("\n Operação inválida, usuário não está atrelado a essa tarefa!")   

                elif type_crud == "update":
                    result = Crud.read("Task", "UserId", id)
                    
                    if result == []:
                        print("\n Operação inválida, esse usuário não tem nenhuma tarefa. ")
                    else:
                        table_result(result, "Task")    
                        updated(option, id) 

#transforma a lista de resultados do banco de dados em um tabela usando prettyTable
def table_result(result, type = ""):
    #criar a tabela
    table = PrettyTable()

    if type == "Task":
        table.field_names = ["N°", "Titulo", "Descrição", "Data de criação"]
    else:    
        table.field_names = ["N°", "Nome", "Email", "Data de criação"]

    #adicionar linhas
    for i, row in enumerate(result, start=1):
        table.add_row([i, row[1], row[2], row[3]])

    #exibir a tabela
    print(f"\n{table}")

#menu da função main    
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

#opçoes do usuário depois de escolher uma opção do menu classificado em usuãrio/tarefa
def user_task_choose(x):
    menu = f"""\n
    ================ OPÇÕES ================
    Deseja {x} um(a):
    [1]\tUsuário
    [2]\tTarefa
    [3]\tVoltar para o menu
    => """
    return input(textwrap.dedent(menu))

def erro_message():
    print("\n Operação inválida, por favor selecione novamente a operação desejada.")
#função principal main    
def main():

    while True:
        opcao = menu()

        if opcao == "c":
            while True:
                option = (user_task_choose("criar"))

                if option == "1":
                    email = input("Digite seu email: ")
                    create(int(option), email= email)
                    break
                elif option == "2":
                    email = input("Digite seu email de usuário: ")
                    verify_user(email, "create", int(option))
                    break
                elif option == "3":
                    
                    break
                else:
                    erro_message() 

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
                    erro_message()

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
                    erro_message()
            
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
                    erro_message()  

        elif opcao == "q":
            break

        else:
            erro_message()

main()

#fecha conexão com servidor
cursor.close()
connection_db.close()