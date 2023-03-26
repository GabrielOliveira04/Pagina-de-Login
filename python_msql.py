
from flask import flak,request
import mysql.connector

app = flask(__name__)

@app.rout('/login', methods=['POST'])

def login():

    #Obtenha osdados do formulario de login

    username= request.form['username']
    password= requesst.form['password']

    #Conecte-se ao banco de dados MYSQL

    db=mysql.connector.connect(
        host ='localhost',
        user ='root',
        password ='sua_senha_do_mysql'
        database- 'seu_banco_de_dados'

    )
    #EXECUTE uma consulta sql para verificar se o usuario e a senha estão corretos
    cursor = db.cursor()
    query = "SELECT * FROM usuarios where username=% AND password=%"
    cursor.execute(query,(username, password))

    #verifique se o usuário e a senha estão corretos

    if cursor.fetchone():

        return 'Bem vindo'

    else:

        return 'Usuário ou senha incorretos'

if __name__ == '__main__' :
    
        app.run() 