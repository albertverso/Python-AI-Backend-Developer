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
    def insert_user(self, nome, email, creatAt):
        self.nome = nome
        self.email = email
        self.createdAt = creatAt

        command = f'INSERT INTO user (name, email, createdAt) VAlUES ("{self.nome}", "{self.email}", "{self.createdAt}")'
        cursor.execute(command)
        connection_db.commit() #edita o banco de dados 

    def insert_task(self, title, description, creatAt, completedAt, userId):
        self.title = title
        self.description = description
        self.createdAt = creatAt
        self.userId = userId
        
        command = f'INSERT INTO task (title, description, creatAt, userId) VAlUES ("{self.title}", "{self.description}", "{self.createdAt}", "{self.userId}")'
        cursor.execute(command)
        connection_db.commit() #edita o banco de dados 

    #READ
    def read():

        command = f'SELECT * FROM User;'
        cursor.execute(command)
        result = cursor.fetchall() #le o banco de dados

        print(result)
        
    #UPDATE
    def update():

        nome = "carlos"
        email = "zezeinho@gmail.com"

        command = f'UPDATE User SET email = "{email}" WHERE name = "{nome}"'
        cursor.execute(command)
        connection_db.commit() #edita o banco de dados

    #DELETE
    def delete():
        nome = "carlos"

        command = f'DELETE FROM User WHERE name = "{nome}" '
        cursor.execute(command)
        connection_db.commit() #edita o banco de dados 


def create(option = 1, user_id = 0):    
    created = Crud() 

    if option == 1:
        nome = input("digite seu nome: ")
        email = input("digite seu email: ")
        data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        created.insert_user(nome, email, data_criacao)

        print("Usuário adicionado com sucesso!!!")
    else:
        title = input("digite seu nome: ")
        description = input("digite seu email: ")
        data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        idUser = 2

        created.insert_task(title, description, data_criacao, data_final, idUser)

        print("Usuário adicionado com sucesso!!!")

def verify():
    Crud.read() ## PAREI PARA VERIFICAR SE EXISTE USUARIO PARA CASDASTRA UMA TAREFA
    
   
    
def menu():
    menu = """\n
    ================ MENU ================
    [c]\tCriar Usuário ou tarefa
    [r]\tExibir usuário ou tarefa
    [u]\tAtualizar usuário ou tarefa
    [d]\Deletar usuario ou tarefa
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))    
    
def main():
    while True:
        opcao = menu()

        if opcao == "c":
            option = int(input("Deseja criar um novo usuario [1] ou uma nova terefa[2]?"))
            if option == 1:
                create()
            elif option == 2:
                verify()
                #create(option)
            else:
                print("\n Operação inválida, por favor selecione novamente a operação desejada. ")      
        elif opcao == "r":
            sd

        elif opcao == "u":
            sdf

        elif opcao == "d":
            fsd

        elif opcao == "q":
            break

        else:
            print("\n Operação inválida, por favor selecione novamente a operação desejada. ")

main()

cursor.close()
connection_db.close()